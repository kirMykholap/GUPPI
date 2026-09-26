---
type: decision
case: "437"
status: current
update: ["[[rule-spec-write]]", "[[estimate-spec-write-copies-the-ratified-case]]", "[[rule-case-protocol]]"]
origin: raw/2026-09-26/1337/ledger.md#case-437
sprint: migration
created: 2026-09-26
tags: [hooks, harness, workflow, session, ledger]
---

## Context

The hook `guppi ratified` on `Stop` writes a ratified Case into the plan file and into the ratified copy `<plan>.ratified.md`. It takes the text from the last earlier reply of the main agent that shows the Case whole. Apart from that, `guppi casecheck --subagent` stores each Case `case-guppi` answered with in `<plan>.checked.json`. For each id it keeps the text in the chat form and the findings. The comparison of `guppi casecheck` on `Stop` compares the showing with that text. On the re-fire (`stop_hook_active`) it exits 0. So a second showing that the agent retyped with a difference is not refused. Then the wrong text goes into both the plan and the copy. `guppi/ratified.py` and `guppi/prespec.py` do not open `.checked.json`, and nothing finds the difference.

The person asked whether the copy is needed at all. The ratified Case can be found mechanically: it is the last answer of `case-guppi` for that id at the time of ratification. But the store itself cannot replace the copy. The store holds the last answer for each id, ratified or not. When a ratified Case changes and `case-guppi` builds it again, the new answer replaces the old one before the new ratification. The copy holds what the person signed, already in the Spec form. `guppi ratified --edit` on each Edit or Write of the plan file, `guppi prespec --check` and the function `differences` compare the plan with it byte for byte. Without the copy, the store would need a mark of which version is ratified, and that mark is the copy. So the copy stays, and the source of the write changes. The stored answer writes the plan and the copy, and the showing is only compared with it. The comparison is the same one as on `Stop`: it moves into one function in `guppi/casecheck.py`, and `guppi/ratified.py` imports it inside a function. `casecheck` already imports `ratified`, as `prespec` does. A refused Case is not written. The ledger hook still writes its decision lines at the same `Stop`. The main agent shows the answer unchanged, and the person ratifies again. The ledger hook does not write a line twice. Until then pre-spec names a line with no item in the plan.

What stays as it is. A deferred decision in the short form is the agent's own text, with no `case-guppi` and no store. The hook still writes it from the reply that carries it, and the copy does not get it. When the last showing of a Case is a fence `DIFF` with a change of prose only, the hook writes nothing, as before. The translation of prose at pre-spec goes into the plan, and prose is not compared. Case 435 promises that a refused showing is followed by a reply of the agent that shows the Case unchanged. This Case adds a refusal at the write: it catches a retyping the re-fire let pass. The Criterion of 435 does not become false by this, and the strictness of the refusal belongs to the Estimate of the write.

What `case-guppi` found in the frame. How it works in `rule-spec-write` says that the hook writes the Case from the showing. The Render of `rule-case-protocol` (`vault/wiki/case-schema.md`) says: "it copies the Case from the reply that showed it". Both sentences become false, and the Case changes them. The Criterion of `estimate-spec-write-copies-the-ratified-case` speaks of the same source, so the Case replaces it whole. Case 436.1 of this session already replaced this Criterion. `generate` applies the items in the order of the Cases, and the Criterion of the last Case stays, so the new Criterion carries the lines of 436.1: all of them word for word but two — "as they stand in the chat" becomes "as the answer holds them", the point of this Case, and the line "`recommend` and `ratification` are not written" is folded into the first line. Case 436.1 does not change. `estimate-spec-write-checks-the-written-case` speaks only of a Case already written, and a refused Case is not written. `estimate-spec-write-writes-a-defer`, `estimate-spec-reconcile-shows-a-changed-case` and `estimate-prespec-checks-the-ratified-copy` speak of the deferred Case and of the copy, and those do not change. `estimate-case-check-shows-only-the-checked-case` is not touched: the comparison on `Stop` moves into one function, and its behaviour stays. How it works in `rule-case-check` does not say who reads the store and stays true. On `Stop` in `.claude/settings.json`, `guppi ledger`, `guppi casecheck` and `guppi context` stand beside it. There are no new hooks. The Case has no `create`, so no vault query is needed. The Criterion changes in this session, so its reading waits for the next one.

## Problem

The plan and the ratified copy take the text from the showing, not from the answer of `case-guppi`. A second showing that differs is not refused, and nothing compares it. So a text nobody built or checked can enter the Spec. The decision is where the write hook takes the Case from, and whether the copy is needed when the store exists.

## Given

`rule-spec-write` — the rule of the Spec hook; its How it works changes
**＋** `estimate-spec-write-copies-the-ratified-case` — the promise of the write
**＋** `guppi/ratified.py` and `tests/test_ratified.py` — the Spec hook and its tests
**＋** `guppi/casecheck.py` — the store `<plan>.checked.json` and the comparison of a showing with it, one function for both hooks
**＋** `guppi/materialize.py` and `guppi/generate.py` — `item_keys`, the one judgment of the keys of an item, and the script that applies by it (case 436.1)
**＋** `rule-case-check` — the check that fills the store and the comparison on `Stop`
**＋** `rule-case-protocol` and its Render `vault/wiki/case-schema.md` — the sentence on where the Spec hook takes the Case
**＋** `rule-one-judgment-one-implementation` — one comparison, imported, never copied

## History

- 2026-09-26 created · raw/2026-09-26/1337/ledger.md#case-437
