---
type: estimate
kind: QA
status: passed
target: "[[rule-spec-write]]"
purpose: Each Case the Stop hook writes into the plan is checked at once, and a finding comes back to the agent
method: uv run --project .guppi pytest .guppi/tests/test_ratified.py -k checks_the_written; by hand, a ratification of a session
checked: 2026-10-05
origin: raw/2026-09-25/0051/ledger.md#case-414.1
sprint: migration
created: 2026-09-25
tags: [hooks, harness, workflow]
---

## Criterion

When:
The `Stop` hook `uv run --project .guppi guppi ratified` has written Case N into the plan file after a reply whose `LEDGER` block holds the decision lines of Case N.

Then:
The hook runs the checks of `prespec --check` on each Case it wrote in this run and its sub-cases, with the decision lines of the reply added to those of the session's ledger, each line once.
**＋** The `replace` and `reword` pairs of every Case of the plan are applied in entry order, and only an anchor of a Case written in this run that misses or hits more than once is a finding.
**＋** On a finding: exit 2, the findings on stderr after `ratified:`, each naming its Case; the written Case stays in the plan file.
**＋** A finding of a Case not written in this run is not reported.
**＋** With `stop_hook_active` set, the hook checks as without it, as `estimate-spec-write-answers-a-refusal` sets it, and a finding it already gave in the stretch is not given again, as `estimate-spec-write-tells-each-reason-once` sets it.
**－** A Case not written in this run, and a defer-only Case, which the hook writes under `## Deferred`, are not checked.
**－** The Frontier is not read, and a name, `context` or `problem` that holds a Cyrillic letter is no finding.
**－** A ledger line of the window that does not parse is no finding of this check.
**－** The plan is compared with no other file, and no ratified copy `<plan>.ratified.md` is written.

## Result

2026-10-05, by hand at the Work readings of session 1343: uv run pytest -q tests/test_ratified.py -k checks_the_written 5 passed; the ratifications of 650–656, first and again: `uv run guppi ratified` ran with no error after each; `uv run guppi prespec --check` over the plan they wrote printed notes only, exit 0; after the re-ratification at 15:48:36 the check printed three findings, all on 653.1 and 653.2, Cases not written in that run, and the hook reported none of them; not exercised: a finding of a Case written in the run, a missed or doubled anchor, the Cyrillic and unparsed-line clauses

## History

- 2026-09-25 created · [[decision-case-414.1]]
- 2026-09-25 updated: the Criterion replaced whole — a defer-only Case is written by the hook and not checked (case 421.1) · [[decision-case-421.1]]
- 2026-09-25 status: pending → passed · raw/2026-09-25/1654/ledger.md#L30
- 2026-09-26 updated: the Criterion replaced whole — a DIFF showing is no longer named (case 441.9) · [[decision-case-441.9]]
- 2026-09-27 updated: the Criterion replaced whole — the Case is written into the plan file alone, no ratified copy (case 445.2) · [[decision-case-445.2]]
- 2026-09-27 status: pending → passed · raw/2026-09-27/1819/ledger.md#L31
- 2026-10-03 updated: method names the kind of its moment (case 613.3) · [[decision-case-613.3]]
- 2026-10-05 updated: the Criterion replaced whole — with stop_hook_active set the hook checks as without it, each finding once a stretch (case 644.3) · [[decision-case-644.3]]
- 2026-10-05 status: pending → passed · raw/2026-10-05/1343/ledger.md#L33
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `uv run pytest` → `uv run --project .guppi pytest` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
