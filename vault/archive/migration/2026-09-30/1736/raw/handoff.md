# Handoff — 2026-09-30, the Frontier after a closed line, the ledger hook that swallowed a parse error, readings taken

## Notes from memory

- The person wants the pending readings taken wherever the method allows, so they stop piling up; asked whether this needs a Case of its own, they said no — readings are taken as their moments come.
- On Case 549 the person turned the round: one condition written in several places is several implementations of one judgment, so the condition stands on `rule-case-protocol` alone and every other text points to it. They also took in the main agent's two remarks (the row `ref`, `slug`, `supersedes` becomes a pointer too; the other full copies checked).
- On Case 550 the person declined the schema sentence on old sub-case pages: Decision pages go to the archive in time, and the sentence would stay behind describing pages already archived.
- The person chose, when the ledger hook stopped writing, to leave plan mode and build the code of 552.1 before `/pre-spec`, then return to Plan Mode.
- The person put off C1 (the close of a sprint) and asked to defer the gap between `ask-guppi` and `case-guppi` on Decision pages rather than fix it now.

## Direct instructions to the librarian

- Ledger lines 29 and 30 hold one reading of `estimate-spec-write-copies-the-ratified-case` twice: line 29 has a space between its brackets and now parses (case 552.1). Expect two `estimate` entries with the same status and result.
- `rule-ledger-write` takes two `replace` pairs, from 552.2 and 552.4, on different anchors; check both applied.
- The renders owed: `vault/wiki/case-schema.md` (547), `vault/wiki/rules/schema.yaml`, `vault/wiki/entities/schema.yaml`, `vault/wiki/insights/schema.yaml`, `.claude/skills/pre-spec/SKILL.md` (549), and `guppi glossary` (549).
- Case 550 is three `update` items with `change` alone on `decision-case-534`, `-538` and `-539`: one History line each, nothing else changes.
- Case 548 sets the `method` of `estimate-decisions-schema-checked` alone; its Criterion and `pending` stand.

## What actually got done

- Cases ratified: 547, 548, 549, 550, 552.1 to 552.4; defers 551 (`rule-case-build`) and 553 (`rule-ask`). 547, 548 and 552 were built again after pre-spec and ratified again.
- Code: `guppi/materialize.py` (`parse_line` reads a space between brackets and gives None for a line it cannot read; the module docstring points to `rule-case-protocol` on `deferred_by`), `guppi/ledger.py` (a line it cannot read is refused; exit 2 on its own error after the payload is read, exit 0 on a payload it cannot read).
- Tests: `tests/test_materialize.py`, `tests/test_ledger.py`, `tests/test_schemas.py` (the three skips became asserts; the Decision test without Context adds its own Problem).
- `make test`: 984 passed, 2 skipped. `make style`: clean.
- Readings and lessons: ledger lines 1 to 4 (at `/hi`), 18 to 30 (in Plan Mode), 38 to 44 (Work readings, Retro readings and two lessons).

## Debt

- No box of code, test or command is left unticked.
- 24 boxes wait for the librarian: the page, render and glossary lines.
- Readings of Estimates this session creates or updates, for a later session: `estimate-case-protocol-shows-the-frontier-after-a-closed-line`, `estimate-decisions-schema-checked`, `estimate-ledger-write-refuses-a-line-it-cannot-read`, `estimate-ledger-write-lifts`, `estimate-ledger-write-exits-2-on-an-error`.

## Observations

- Red before the work: `make lint` exit 2 with 61 finding lines in the Baseline, the same 61 after the work (`rule-spec-box` schema and orphan, the open fence of `decision-case-13`, the deferred and unread lines). The failing test of the Baseline was the one Case 548 fixed.
- The code of 552.1 was built before the Spec and before the Baseline, by the person's choice, to unblock the ledger hook; `/work` checked it and ticked its boxes.
- `guppi ratified`, `guppi casecheck`, `guppi context` and `guppi onward` still catch their own errors and exit 0; `guppi ratified` lost the first showing of Case 551 that way.
- The method of `estimate-estimates-schema-checked` runs `-k estimates`, which does not select the test of `method` on an Estimate page.
- Readings whose moment is this Retro and its handoff, to read from this file and transcript: `estimate-retro-red-in-the-baseline-is-not-charged`, `estimate-retro-loads`, `estimate-retro-runs-on-to-the-handoff`, `estimate-handoff-holds-each-fact-once`, `estimate-where-to-stop-stops-only-on-its-conditions`. Not taken, the moment not come: `estimate-case-check-requires-each-question-of-the-rounds`, `estimate-case-check-sends-back-a-faulty-case`, `estimate-case-check-shows-only-the-checked-case` (no send-back or refusal seen in the chat), `estimate-plan-mode-verified` (no `create` without a `ref`), `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` (no `/work` typed by the person), `estimate-event-log-records` (no `/hi` outside plan mode).

## For the next session

- The other `Stop` hooks swallow their errors with exit 0, as the ledger hook did: give them the exit 2 of case 552.4, or keep them as they are?
- `estimate-estimates-schema-checked`: its method selects no test of `method`; set it to a command that runs that test.
- The Work readings failed this session need their fixes decided: `estimate-case-build-checks-the-finished-case` (a frame hit found by meaning missed, Grep claims misreported), `estimate-case-protocol-shows-the-built-case` (own text before a round), `estimate-case-build-records-the-rounds-in-recommend` (an item keeps a replaced recommendation), `estimate-documentation-completes` (the librarian read beyond its list), `estimate-spec-write-writes-a-defer` (the hook swallowed an error).

## Ask the person
