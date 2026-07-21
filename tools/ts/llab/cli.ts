#!/usr/bin/env tsx
/**
 * Command-line entry point for the TS llab harness.
 *
 *   pnpm eval --dataset tools/python/llab/sample.jsonl
 *   tsx tools/ts/llab/cli.ts eval --dataset tools/python/llab/sample.jsonl
 */

import { runEval } from "./eval.js";
import type { GenerateParams } from "./client.js";

async function main(): Promise<number> {
  const args = process.argv.slice(2);
  const cmd = args[0];
  const rest = args.slice(1);

  function flag(name: string): string | undefined {
    const i = rest.indexOf(`--${name}`);
    return i >= 0 ? rest[i + 1] : undefined;
  }
  function numFlag(name: string): number | undefined {
    const v = flag(name);
    return v == null ? undefined : Number(v);
  }

  if (cmd === "eval") {
    const dataset = flag("dataset");
    if (!dataset) {
      console.error("usage: llab eval --dataset <path>");
      return 1;
    }
    const params: GenerateParams = {
      temperature: numFlag("temperature") ?? 0,
      topP: numFlag("top-p") ?? 1,
      numPredict: numFlag("num-predict"),
      seed: numFlag("seed"),
    };
    await runEval({
      datasetPath: dataset,
      model: flag("model"),
      judgeModel: flag("judge"),
      params,
      resultsDir: flag("results-dir") ?? "tools/python/llab/results",
    });
    return 0;
  }

  console.error("usage: llab <command> [args...]");
  console.error("commands: eval");
  return 1;
}

main().then((c) => process.exit(c));
