# Handoff — 2026-10-03, the answer of case-guppi and the number of a Case built again

## Notes from memory

- The person took the recommendation on every question of every round. On the second round of the Case on `insight-spec-write-parent-body-kept-on-re-ratification` the person asked for a plainer text; the main agent re-pitched it by `wait-what`, with the ledger lines of session 2300 as the real example, and the person then agreed.
- The person asked why `estimate-skill-grill-me-asks-in-rounds` and `estimate-orchestration-shows-the-built-case` stood `failed`. The first was read in Plan Mode, once the rounds of this session stood; the second waited for the close by its `method`.
- The person judged the unticked box `read estimate-prespec-onward-reads-the-decisions-of-the-stretch` of the archived Spec of session 2049 harmless and left it unticked; its Frontier line closed as work with no Case.
- The close of the sprint (Slice 5) was left on the sprint page again: the person said "let's go to work" with only that line open.
- At `/pre-spec` the Case first ratified as 608 needed a second promise, gained sub-cases, and was built again by its own rule under the new number 610, with `{supersedes:case 608}`. The person kept the defer of `rule-ledger-line-withdrawn-on-re-ratification` (option a of the pre-spec question).
- The person asked why one question was shown twice: the main agent had put a status line before a round in the loop after `/pre-spec`, and the `Stop` check refused the reply.

## Direct instructions to the librarian

- Case 608 is superseded by Case 610: its four decision lines are not applied, and its Decision page, if created, is marked superseded. Case 610.1 carries the `create` of `estimate-case-check-sends-back-a-ratified-case-in-another-shape` and the three updates 608 held.
- Cases 607 and 609 were ratified again after `/pre-spec` with unchanged decision lines; the ledger holds each of their lines once, and the stored answers of `cases/case-607.md` and `cases/case-609.md` are the second build.
- Case 610.1 retires two defers: `{supersedes:case 475}` on the line of `rule-spec-write` and `{supersedes:case 585}` on the line of the Insight, which goes `actioned` with `addressed_by` `decision-case-610.1`. Check that `backlog.md` drops the Insight, and drops `rule-spec-write` if no other Decision defers it.
- The `update` of `rule-case-protocol` is a `replace` in its splitting part; render `vault/wiki/case-schema.md` after it.
- The two lessons on the main agent's own text in a showing — one before a round, one between a heading and its list — may share a root cause with each other and with archived lessons on text before a round.

## What actually got done

- Cases ratified: 607 (607.1, 607.2), 609, 610 (610.1, 610.2).
- Code: `guppi/casecheck.py` — `is_fact`, the one test of a Fact answer that `is_round` and `answer_of` share; `answer_of` stops at the newest Case, round or Fact answer; `new_number`, `shape_findings`, `clashes`, `ledger_records`, `key_case`, `in_family`; `check_answer` takes the store; `subagent` stores `agent_id` and keeps an answer under a number another agent holds apart, under `<case>@<agent_id>`; the module docstring on the answer, the round form, the shape and the clash. Tests: `tests/test_casecheck.py`, 15 new (named `subagent`, `round_form`, `shape`, `clash`), the helper `answer` takes `now`.
- `make test`: 1117 passed, 6 skipped. `make style`: clean.
- Readings: ledger lines 7, 15, 16, 17 (`passed`) and 18 (`failed`). Lessons: ledger lines 9, 19, 20.

## Debt

- None.
- Boxes that wait for the librarian: 9.
- `read` lines whose slug this session creates or updates: `estimate-case-check-sends-back-a-faulty-case`, `estimate-case-check-sends-back-a-faulty-round`, `estimate-orchestration-defers-in-one-reply`, `estimate-case-check-sends-back-a-ratified-case-in-another-shape`, `estimate-case-check-sends-back-a-case-number-held-by-another-agent`.

## Observations

- Red before the work: `make lint` exit 2, 45 lines of `guppi lint` (5 `deferred`, 38 `unread: pending`, 2 `unread: failed`), in the Baseline of `work.md`. No expected red.
- The check of a clash (610.2) reads `agent_id` from the `SubagentStop` payload. No live payload of this session was read for that field: every answer of `case-guppi` here was checked by the code before the change, so the store holds no `agent_id` yet. The first live answer after this commit shows whether the field comes.
- `generate` does not read `vault/archive/`, so a `read` box of an archived Spec is never ticked; the boxes of the archived Specs of sessions 1202, 1834 and 2049 that the brief lists under Work stay unticked whatever readings are taken.
- Readings not taken at this session's Work readings or Retro, their moment not come: `estimate-case-build-writes-the-case` (no `create` without a `ref` this session), `estimate-case-check-requires-each-question-of-the-rounds`, `estimate-synthesis-clusters`, `estimate-retro-runs-on-to-the-handoff`, `estimate-where-to-stop-stops-only-on-its-conditions`, `estimate-end-of-work-order`, `estimate-handoff-dispatches`, `estimate-handoff-holds-each-fact-once`, `estimate-plan-mode-verified`, `estimate-event-log-records` and the other pending readings of the brief.

## For the next session

- The close of the sprint (Slice 5).
- Whether the showing of a Case may carry a note under the heading of the top-level Case, or whether the `Stop` check of `rule-case-check` should refuse text between that heading and its list, as it refuses text before a round.

## Ask the person

- none
