/**
 * @ai-lab/llab — shared TypeScript harness for ai-lab.
 *
 * Mirrors the Python `llab` package for agent / Cursor SDK experiments.
 *
 * - client.ts  — unified generate() routing to Ollama (and later OpenAI/Anthropic).
 * - eval.ts    — minimal eval runner.
 * - agent.ts   — thin tool-use loop for agent experiments.
 * - cli.ts     — command-line entry point.
 */

export { generate, generateMany, defaultModel, defaultJudgeModel, splitBackend } from "./client.js";
export type { GenerateResult, GenerateParams } from "./client.js";
export { runEval, loadDataset } from "./eval.js";
export type { Example, ScoredExample } from "./eval.js";
export { runAgentLoop } from "./agent.js";
export type { Tool, AgentStep } from "./agent.js";
