/**
 * Minimal tool-use agent loop (skeleton).
 *
 * Use this in lab/06-agents to study agent failure modes (loops, hallucinated
 * tools, lost-in-the-middle). The loop is intentionally tiny so you can
 * instrument it: every step is recorded as an AgentStep.
 *
 * Wire `generate` to a provider SDK or the Cursor SDK when you need richer
 * tool-use; the structure stays the same.
 */

import { generate, type GenerateParams } from "./client.js";

export interface Tool {
  name: string;
  description: string;
  /** JSON schema for the tool's arguments, or a free-form description. */
  inputs: Record<string, unknown> | string;
  run: (args: Record<string, unknown>) => Promise<string>;
}

export interface AgentStep {
  turn: number;
  thought: string;
  tool?: { name: string; args: Record<string, unknown> };
  observation?: string;
  raw: string;
}

export interface AgentRun {
  steps: AgentStep[];
  finalAnswer: string;
  turns: number;
}

const MAX_TURNS = 8;

function buildToolPrompt(tools: Tool[], task: string): string {
  const toolList = tools
    .map((t) => `- ${t.name}: ${t.description}\n  inputs: ${JSON.stringify(t.inputs)}`)
    .join("\n");
  return [
    "You are a tool-using agent. You have these tools:",
    toolList,
    "",
    `Task: ${task}`,
    "",
    "On each turn, either:",
    '  (a) call a tool with: TOOL: <name> {"arg": "value", ...}',
    "  (b) finish with:    FINAL: <your answer>",
    "",
    "Think one step at a time.",
  ].join("\n");
}

function parseToolCall(text: string): { name: string; args: Record<string, unknown> } | null {
  const m = text.match(/TOOL:\s*(\S+)\s*(\{.*\})/s);
  if (!m) return null;
  try {
    const args = JSON.parse(m[2] as string) as Record<string, unknown>;
    return { name: m[1] as string, args };
  } catch {
    return null;
  }
}

function parseFinal(text: string): string | null {
  const m = text.match(/FINAL:\s*([\s\S]*)/);
  return m ? (m[1] as string).trim() : null;
}

export async function runAgentLoop(opts: {
  task: string;
  tools: Tool[];
  model?: string | null;
  params?: GenerateParams;
  maxTurns?: number;
}): Promise<AgentRun> {
  const model = opts.model ?? null;
  const params = opts.params ?? { temperature: 0 };
  const maxTurns = opts.maxTurns ?? MAX_TURNS;
  const steps: AgentStep[] = [];
  let transcript = buildToolPrompt(opts.tools, opts.task);

  for (let turn = 1; turn <= maxTurns; turn++) {
    const res = await generate(model, transcript, { params });
    const raw = res.text;
    const toolCall = parseToolCall(raw);
    const final = parseFinal(raw);

    if (final) {
      steps.push({ turn, thought: raw, raw });
      return { steps, finalAnswer: final, turns: turn };
    }

    if (toolCall) {
      const tool = opts.tools.find((t) => t.name === toolCall.name);
      let observation: string;
      if (!tool) {
        observation = `ERROR: unknown tool ${toolCall.name}`;
      } else {
        try {
          observation = await tool.run(toolCall.args);
        } catch (e) {
          observation = `ERROR: ${(e as Error).message}`;
        }
      }
      steps.push({ turn, thought: raw, tool: toolCall, observation, raw });
      transcript += `\n\nTurn ${turn}:\n${raw}\nOBSERVATION: ${observation}`;
      continue;
    }

    steps.push({ turn, thought: raw, raw });
    transcript += `\n\nTurn ${turn}:\n${raw}\n(no tool call or final answer — retrying)`;
  }

  return { steps, finalAnswer: "(no final answer within max turns)", turns: maxTurns };
}
