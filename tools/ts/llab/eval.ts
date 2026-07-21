/**
 * Minimal eval runner (TS mirror of llab.eval).
 *
 * Dataset: JSONL of { prompt, expected?, judge?, scorer? }.
 * Scorers: exact_match (default), regex (expected is a regex), llm_judge.
 */

import { readFile, mkdir, writeFile } from "node:fs/promises";
import { existsSync } from "node:fs";
import { dirname, basename, extname, join } from "node:path";

import { generate, defaultModel, defaultJudgeModel, type GenerateParams } from "./client.js";

export interface Example {
  prompt: string;
  expected?: string | null;
  judge?: string | null;
  meta: Record<string, unknown>;
}

export interface ScoredExample {
  example: Example;
  output: string;
  score: number;
  scorer: string;
  detail?: string;
}

export async function loadDataset(path: string): Promise<Example[]> {
  const text = await readFile(path, "utf8");
  const examples: Example[] = [];
  for (const line of text.split("\n")) {
    const trimmed = line.trim();
    if (!trimmed) continue;
    const obj = JSON.parse(trimmed) as Record<string, unknown>;
    examples.push({
      prompt: obj.prompt as string,
      expected: (obj.expected as string) ?? null,
      judge: (obj.judge as string) ?? null,
      meta: Object.fromEntries(
        Object.entries(obj).filter(([k]) => !["prompt", "expected", "judge"].includes(k)),
      ),
    });
  }
  return examples;
}

function scoreExactMatch(output: string, expected: string): number {
  return output.trim() === expected.trim() ? 1 : 0;
}

function scoreRegex(output: string, expected: string): number {
  return new RegExp(expected).test(output) ? 1 : 0;
}

async function scoreLlmJudge(
  output: string,
  judgePrompt: string,
  judgeModel: string,
): Promise<{ score: number; detail: string }> {
  const full =
    `${judgePrompt}\n\n--- Output to judge ---\n${output}\n--- End output ---\n\n` +
    "Respond with a single number between 0.0 and 1.0 only.";
  const res = await generate(judgeModel, full, { params: { temperature: 0 } });
  const m = res.text.match(/\d+(\.\d+)?/);
  const score = m ? Math.max(0, Math.min(1, parseFloat(m[0]))) : 0;
  return { score, detail: res.text };
}

export async function scoreOne(
  ex: Example,
  output: string,
  judgeModel: string | null,
): Promise<ScoredExample> {
  if (ex.expected != null && ex.meta.scorer === "regex") {
    return { example: ex, output, score: scoreRegex(output, ex.expected), scorer: "regex" };
  }
  if (ex.expected != null) {
    return { example: ex, output, score: scoreExactMatch(output, ex.expected), scorer: "exact_match" };
  }
  if (ex.judge != null && judgeModel != null) {
    const { score, detail } = await scoreLlmJudge(output, ex.judge, judgeModel);
    return { example: ex, output, score, scorer: "llm_judge", detail };
  }
  return { example: ex, output, score: 0, scorer: "none" };
}

export async function runEval(opts: {
  datasetPath: string;
  model?: string | null;
  judgeModel?: string | null;
  params?: GenerateParams;
  resultsDir?: string;
}): Promise<ScoredExample[]> {
  const model = opts.model ?? (await defaultModel());
  const judgeModel = opts.judgeModel ?? (await defaultJudgeModel());
  const params = opts.params ?? { temperature: 0 };
  const resultsDir = opts.resultsDir ?? "tools/python/llab/results";

  const examples = await loadDataset(opts.datasetPath);
  const scored: ScoredExample[] = [];
  console.log(`Eval: ${examples.length} examples | model=${model} | judge=${judgeModel}`);
  console.log("-".repeat(60));
  for (let i = 0; i < examples.length; i++) {
    const ex = examples[i]!;
    const res = await generate(model, ex.prompt, { params });
    const s = await scoreOne(ex, res.text, judgeModel);
    scored.push(s);
    const flag = s.score >= 0.999 ? "OK " : "XX ";
    console.log(`${flag}[${String(i + 1).padStart(2)}/${examples.length}] score=${s.score.toFixed(2)} (${s.scorer}) :: ${JSON.stringify(res.text.slice(0, 60))}`);
  }
  console.log("-".repeat(60));
  const mean = scored.reduce((a, s) => a + s.score, 0) / Math.max(1, scored.length);
  console.log(`mean score: ${mean.toFixed(3)} over ${scored.length} examples`);

  if (!existsSync(resultsDir)) await mkdir(resultsDir, { recursive: true });
  const stem = basename(opts.datasetPath, extname(opts.datasetPath));
  const ts = new Date().toISOString().replace(/[:.]/g, "-").slice(0, 19);
  const outPath = join(resultsDir, `${stem}-${ts}.jsonl`);
  const lines = scored.map((s) =>
    JSON.stringify({
      prompt: s.example.prompt,
      expected: s.example.expected,
      output: s.output,
      score: s.score,
      scorer: s.scorer,
      detail: s.detail,
      model,
    }),
  );
  await writeFile(outPath, lines.join("\n") + "\n");
  console.log(`results: ${outPath}`);
  return scored;
}
