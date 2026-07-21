/**
 * Unified generation client (TS mirror of llab.client).
 *
 * Routes by model prefix:
 * - `ollama/<name>`    → local Ollama (default, implemented)
 * - `openai/<name>`    → OpenAI API (skeleton)
 * - `anthropic/<name>` → Anthropic API (skeleton)
 */

import { readFile } from "node:fs/promises";
import { existsSync } from "node:fs";

export interface GenerateParams {
  temperature?: number;
  topP?: number;
  topK?: number | null;
  minP?: number | null;
  numPredict?: number | null;
  stop?: string[] | null;
  seed?: number | null;
  extra?: Record<string, unknown>;
}

export interface GenerateResult {
  text: string;
  usage: Record<string, number>;
  logprobs: unknown[] | null;
  raw: Record<string, unknown>;
  model: string;
  backend: string;
}

const DEFAULT_MODEL = "ollama/qwen2.5:7b-instruct";
const DEFAULT_JUDGE_MODEL = "ollama/qwen2.5:14b-instruct";

async function loadEnvFile(path: string): Promise<Record<string, string>> {
  if (!existsSync(path)) return {};
  const text = await readFile(path, "utf8");
  const env: Record<string, string> = {};
  for (const line of text.split("\n")) {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith("#") || !trimmed.includes("=")) continue;
    const [k, ...rest] = trimmed.split("=");
    env[k!.trim()] = rest.join("=").trim();
  }
  return env;
}

let envCache: Record<string, string> | null = null;
async function env(key: string, fallback?: string): Promise<string | undefined> {
  if (process.env[key]) return process.env[key];
  if (!envCache) {
    envCache = {
      ...(await loadEnvFile(".env")),
      ...(await loadEnvFile(`${process.env.HOME}/.ai-lab.env`)),
    };
  }
  return envCache[key] ?? fallback;
}

export async function defaultModel(): Promise<string> {
  return (await env("LAB_MODEL", DEFAULT_MODEL)) ?? DEFAULT_MODEL;
}

export async function defaultJudgeModel(): Promise<string> {
  return (await env("LAB_JUDGE_MODEL", DEFAULT_JUDGE_MODEL)) ?? DEFAULT_JUDGE_MODEL;
}

export function splitBackend(model: string): { backend: string; name: string } {
  if (model.includes("/")) {
    const idx = model.indexOf("/");
    const backend = model.slice(0, idx);
    const name = model.slice(idx + 1);
    return { backend, name };
  }
  return { backend: "ollama", name: model };
}

export async function generate(
  model: string | null,
  prompt: string,
  opts?: { system?: string | null; params?: GenerateParams },
): Promise<GenerateResult> {
  const m = model ?? (await defaultModel());
  const params = opts?.params ?? {};
  const { backend, name } = splitBackend(m);
  const fullPrompt = opts?.system ? `${opts.system}\n\n${prompt}` : prompt;

  if (backend === "ollama") return generateOllama(name, fullPrompt, params, m);
  if (backend === "openai") throw new Error("openai backend — wire up when needed");
  if (backend === "anthropic") throw new Error("anthropic backend — wire up when needed");
  throw new Error(`unknown backend: ${backend}`);
}

async function generateOllama(
  name: string,
  prompt: string,
  params: GenerateParams,
  model: string,
): Promise<GenerateResult> {
  const baseUrl = (await env("OLLAMA_BASE_URL", "http://localhost:11434")) ?? "http://localhost:11434";
  const url = `${baseUrl.replace(/\/$/, "")}/api/generate`;
  const options: Record<string, unknown> = {
    temperature: params.temperature ?? 0,
    top_p: params.topP ?? 1,
  };
  if (params.topK != null) options.top_k = params.topK;
  if (params.minP != null) options.min_p = params.minP;
  if (params.numPredict != null) options.num_predict = params.numPredict;
  if (params.stop) options.stop = params.stop;
  if (params.seed != null) options.seed = params.seed;
  if (params.extra) Object.assign(options, params.extra);

  const res = await fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ model: name, prompt, stream: false, options }),
  });
  if (!res.ok) throw new Error(`ollama ${res.status}: ${await res.text()}`);
  const data = (await res.json()) as Record<string, unknown>;
  return {
    text: (data.response as string) ?? "",
    usage: {
      prompt_eval_count: (data.prompt_eval_count as number) ?? 0,
      eval_count: (data.eval_count as number) ?? 0,
    },
    logprobs: null,
    raw: data,
    model,
    backend: "ollama",
  };
}

export async function generateMany(
  model: string | null,
  prompts: string[],
  params?: GenerateParams,
): Promise<GenerateResult[]> {
  const out: GenerateResult[] = [];
  for (const p of prompts) out.push(await generate(model, p, { params }));
  return out;
}
