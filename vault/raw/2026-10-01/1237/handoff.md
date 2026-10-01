# Handoff — 2026-10-01, the readings of session 2356 and three failed Estimates

## Notes from memory

- On Case 567 the person first did not see who would name the fields of the brief. The main agent explained it by `wait-what`. The person then asked whether the rule to name and flag every read of the librarian is too strict, since what happened can be checked afterwards. They named `log.md`; the reads of the librarian stand in `event_log.md`, which git does not track, and `case-guppi` said so in its round. Their choice: flag only the reads the frame says the job does not need, and name in the report only the pages behind a judgment.
- On Case 568 the person answered outside the options: simply allow a `recommend` item on the parent. Asked whether that is a must or a may, they chose may: no fixed place and no script check.
- On Case 569 the person chose that `work.md` the agent wrote itself in the same turn counts as read "while one agent does the work and the report". Once the work and the report are split between agents, reading the file becomes required. No Case takes that split up.
- The main agent's reading of `estimate-documentation-completes` as failed was judged a misjudgment by the person (567.1, Q1): opening a page to learn its field names served the statuses of Readings due.
- The person put the remaining items off to go to work: the close of a sprint, a sprint item left for later, and the cases 570 to 576.

## Direct instructions to the librarian

- Cases 567 and 569 were ratified, then built again on the findings of `/pre-spec` and ratified again. The ledger holds each decision line once; the plan holds the last text of each.
- 567.1 and 567.2 both change `rule-brief`, in different sentences. 569.1 and 569.2 both change `rule-retro`, in different paragraphs.
- The defers 571, 572, 573 and 576 target Estimates, which carry no `deferred_by`. The defers 570, 574 and 575 target live rules: `rule-case-rebuild-cost`, `rule-orchestration` and `rule-prespec-onward`.
- The readings of ledger lines 2 and 5 were taken at `/hi` on the old Criteria of `estimate-documentation-completes` and `estimate-retro-runs-on-to-the-handoff`, and line 1 on `estimate-brief-written`. Decision lines of this session later replace those Criteria, so each Estimate ends `pending`.

## What actually got done

- Cases ratified: 567.1, 567.2, 568, 569.1, 569.2, and the defers 570 to 576.
- Code and tests: none changed. `make test` 1034 passed, 2 skipped; `make style` clean.
- Readings at `/hi`: ledger lines 1 to 8 — `estimate-brief-written`, `estimate-retro-onward-sends-the-agent-to-the-handoff`, `estimate-retro-red-in-the-baseline-is-not-charged`, `estimate-where-to-stop-stops-only-on-its-conditions`, `estimate-session-phases-in-order` and `estimate-context-size-shown-after-each-reply` passed; `estimate-documentation-completes` and `estimate-retro-runs-on-to-the-handoff` failed.
- Readings of Work Mode: ledger lines 28 to 41 — eleven passed; three failed: `estimate-case-protocol-acknowledging-reply`, `estimate-case-protocol-shows-the-frontier-after-a-closed-line`, `estimate-prespec-gathers-the-answers-after-findings`.
- No lesson.

## Debt

- None: the Spec holds no box of code, test or by-hand check.
- 18 boxes wait for the librarian: page and render lines.
- `read` lines of Estimates this session updates: `estimate-documentation-completes`, `estimate-brief-written`, `estimate-case-build-records-the-rounds-in-recommend`, `estimate-retro-runs-on-to-the-handoff`, `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note`.

## Observations

- Red before the work, from the Baseline of `work.md`: `make lint` stopped at `guppi backlog --check`, and `guppi lint` printed the three findings on `rule-spec-box`, the open fence of `decision-case-13`, six `deferred` lines and 50 `unread` lines. Nothing was fixed for them.
- At the `Stop` after the reply that ended Retro, all six `Stop` hooks ran for about half a second each with no output: the ledger hook wrote none of the fourteen readings, `guppi context` printed no line, and `guppi onward` did not send the agent to `/handoff`. The person had to ask what comes next. At the next `Stop` the ledger hook wrote the fourteen lines from the transcript and `guppi onward` refused as designed. The cause is not known.
- `guppi onward --plan` fired after the re-ratification of 567 and 569, whose decision lines the ledger already held, because the reply's `LEDGER` block carried them after the Case files were written. Session 2356 had seen it stay silent in that case.
- The two failed readings of the Frontier's form share one cause: the main agent folds the open `W` lines into one line, as `/hi` sets for the Work list, while the schema wants one line per open item in every later Frontier. With 38 open readings, one line per item makes each reply long.
- `estimate-prespec-gathers-the-answers-after-findings` fails on the silence clause by the mechanism of `lesson-sendmessage-answers-open-a-turn-of-their-own`: each answer of a `case-guppi` opens a turn, and that turn ends with a reply.
- `estimate-case-protocol-asks-in-the-grill-me-shape` and `estimate-case-check-shows-only-the-checked-case` were not read: the main agent asked no question of its own in that shape, and the hook refused no showing.

## For the next session

- `estimate-case-protocol-acknowledging-reply` failed: the Changes paragraph held three or four sentences against one or two, and the Frontier folded the open `W` lines into one line.
- `estimate-case-protocol-shows-the-frontier-after-a-closed-line` failed: the open `W` lines were folded into one line. Whether a later Frontier may fold the open `W` lines as the first reply of `/hi` does.
- `estimate-prespec-gathers-the-answers-after-findings` failed: the main agent wrote in the chat twice while an answer of a `case-guppi` was out. Whether the clause should allow one short line per notification turn.
- The silent `Stop` after the reply that ended Retro: whether it needs a check or a fallback.

## Ask the person

