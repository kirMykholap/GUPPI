---
type: decision
case: "414.1"
status: current
create: ["[[estimate-spec-write-checks-the-written-case]]"]
update: ["[[rule-spec-write]]"]
supersedes: ["[[decision-case-412]]"]
origin: raw/2026-09-25/0051/ledger.md#case-414.1
sprint: migration
created: 2026-09-25
tags: [hooks, harness, workflow, session]
---

## Context

Today the plan is checked once, at `/pre-spec`. The findings pile up until the end of Plan Mode, and a Case written with a fault is found late. Case 407 proposed to check each Case right after it is written and to close the plan to the agent's edits by a guard and a fragment. The pre-spec of session 2214 found contradictions in it, and Case 412 deferred it together with the question of Case 410. This Case takes 412 up and keeps of 407 only the check at once: the `Stop` hook of `rule-spec-write` writes a Case, runs the checks of `prespec --check` on it and gives the findings back to the agent. The guard, the fragment and the comparison without `given` are withdrawn; most findings fell on them. `ratified --edit` on `PostToolUse` still guards the plan.

The other findings are answered so:
- **The grammar of the ledger lines.** The check of one Case does not read it. A finding on a line that does not parse names no Case, and `/pre-spec` keeps it.
- **The order of the hooks.** The Claude Code hooks documentation says: "All matching hooks run in parallel". So the hook takes the decision lines from the reply itself and does not wait for `ledger.md`.
- **Exit 2 after the acknowledging reply.** The agent goes on after its `LEDGER` block. Sub-case 414.2 says that this is a reply of its own.

There is no separate option `prespec --check --case N`: the hook imports the checks, and with the option the Criterion of the Estimates of `prespec --check` that promise to read the Frontier, the ratified copy and the grammar of the window would have to change.

This Case does not decide the question of Case 410, when the prose of a Case is translated. But `{supersedes:case 412}` also lifts the defer of `rule-spec-reconcile`, so the question stays a Frontier item, and a new defer is due at the close of Plan Mode if this session does not decide it.

`frame-guppi` found:
- the option `--case` contradicted the Estimates of `prespec --check`, so the option is dropped;
- the sentence on the answer after a refusal was wider than the truth when the ledger hook itself refuses, so it is narrowed to another `Stop` hook;
- it took the order of the hooks for sequential, which the documentation refutes.

`estimate-spec-write-copies-the-ratified-case` is not touched: its list of refusals is not closed, and the new refusal does not contradict it. Every `create` here is an Estimate with a `ref`, so no vault query is needed.

## Problem

The agent learns of a fault in a written Case only at `/pre-spec`, when the Cases are already many. Each Case should be checked right after it is written, by the same checks as at pre-spec, and the result should not depend on the order of the hooks on one `Stop`.

## Given

`rule-spec-write` — the `Stop` hook that writes a ratified Case into the plan; its `How it works`.
**＋** `estimate-spec-write-checks-the-written-case` — the new promise.
**＋** `rule-prespec` — the checks of `prespec --check`, which the hook runs.
**＋** `guppi/ratified.py` — `stop`, which writes the Cases of a reply.
**＋** `guppi/prespec.py` — the checks, run for one Case.
**＋** `tests/test_ratified.py` — fixes the check after the write.
**＋** `raw/<hi date>/<hi HHMM>/frontier.md` — the Frontier, which the check after the write skips.

## History

- 2026-09-25 created · raw/2026-09-25/0051/ledger.md#case-414.1
