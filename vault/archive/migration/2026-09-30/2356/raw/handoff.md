# Handoff — 2026-09-30, the orchestration of the main agent

## Notes from memory

- The person folded the Frontier items C2 and C3 into one Case, 561, and decided its design in six rounds. They doubted the first answer on where the shared text goes ("is this not duplication, why would case-guppi read the orchestration text?"). The question was asked again with a third small file, and they agreed to that.
- The move of the main agent's rules into files of their own (a file of `rule-orchestration` loaded by `/hi`, a small shared file, `case-schema.md` for `case-guppi` alone) was ratified as a design and put off to a later session. It is recorded in the new `purpose` of `rule-orchestration` (561.13). That page keeps its defer of case 424 on purpose, so that the move stays in the backlog.
- The person asked for a plain discussion, not a Case, about the cost of this session. The main agent spent about 40 000 tokens to join two Cases, and the `case-guppi` of Case 561 reached about 500 000 tokens by its usage line, because Case 561 was written and returned whole at every rebuild. The person deferred the item to the next session as case 566, `rule-case-rebuild-cost`.
- The person put off the remaining items to go to work: C1 (the close of a sprint, a sprint item left for later), and C4, C6, C7 as cases 563, 564, 565.

## Direct instructions to the librarian

- Case 561 was ratified, then rebuilt and ratified again twice: once for 561.9 (its defer of 560 retired, the refused round shown again), and once after pre-spec for 561.1, 561.3, 561.4 and 561.13. Case 562 was ratified twice in the same way. The ledger holds each decision line once; the plan holds the last text of each.
- Three defers are retired: 503 on `rule-prespec` (561.1), 546 on `rule-orchestration` (561.13), and 560 on `estimate-case-protocol-shows-the-built-case` (561.9). The Estimate carries no `deferred_by`, so only its Decision page is superseded.
- 561.1 writes the Render of `rule-prespec` whole, and points the Purpose of `rule-prespec-hook` to the module docstring of `guppi/prespec.py`. The docstring already holds what the check compares.
- 561.5 creates `rule-prespec-onward` and registers `uv run guppi onward --plan` on `Stop` in `rule-hook-registry`. The hook acts only after `.claude/settings.json` is rendered.
- `backlog.md`: the defer of case 565 adds a session to `rule-spec-box`; the defer of case 566 makes a placeholder `rule-case-rebuild-cost`; 563 and 564 defer Estimates, which carry no `deferred_by`.

## What actually got done

- Cases ratified: 561.1 to 561.14, 562, and the defers 563, 564, 565, 566.
- Code: `guppi/prespec.py` (`plan_findings` shared by `--check` and the `ExitPlanMode` hook; `check_same_target`; `open_case_items`; the docstring holds what the check compares), `guppi/onward.py` (the `--plan` run), `guppi/cli.py` (the docstring), `guppi/casecheck.py` (`list_showing`, `showings`, the round check `round_opening`), `guppi/ratified.py` (`find_showing` by `showings`).
- Tests: `tests/test_prespec.py`, `tests/test_onward.py`, `tests/test_casecheck.py`, `tests/test_ratified.py`. `make test` 1034 passed, 2 skipped; `make style` clean.
- The by-hand measurement of case 562: the answer to an `Agent` call stands in the `tool_result` of the call; the answer to a `SendMessage` comes back as a later `user` record with `origin.kind` `task-notification`, the answer between `<result>` and `</result>`. The docstring of `guppi/casecheck.py` names it.
- Readings: ledger lines 40 to 45 — four passed (`estimate-case-check-exits-2-on-an-error`, `estimate-context-size-shows-its-error`, `estimate-retro-onward-exits-2-on-an-error`, `estimate-spec-write-exits-2-on-an-error`), two failed (`estimate-case-build-checks-the-finished-case`, `estimate-case-build-records-the-rounds-in-recommend`). Lesson: ledger line 46, `lesson-sendmessage-answers-open-a-turn-of-their-own`.

## Debt

- None: every box of code, test and by-hand check is ticked.
- 45 boxes wait for the librarian: page, render and sprint lines.
- `read` lines of Estimates this session creates or updates: `estimate-prespec-reconciles`, `estimate-prespec-gathers-the-answers-after-findings`, `estimate-prespec-hook-gates`, `estimate-prespec-catches-two-cases-on-one-target`, `estimate-prespec-onward-sends-the-agent-on`, `estimate-case-protocol-shows-the-frontier-after-a-closed-line`, `estimate-case-protocol-defers-in-one-reply`, `estimate-case-protocol-acknowledging-reply`, `estimate-case-protocol-shows-the-built-case`, `estimate-case-check-shows-only-the-checked-case`, `estimate-case-build-answers-what-done-means`, `estimate-case-protocol-forwards-a-discussion-question`, `estimate-case-protocol-asks-in-the-grill-me-shape`, `estimate-case-protocol-puts-the-harness-before-plan-mode`, `estimate-case-check-refuses-text-before-a-round`. The deferred `estimate-case-build-writes-a-plain-round` and `estimate-spec-write-writes-a-defer` are not read here either.

## Observations

- Red before the work, from the Baseline of `work.md`: `make lint` stopped at `guppi backlog --check` (the count of `rule-spec-box` grows with the defer of 565 in the ledger until the librarian's run), and `guppi lint` printed the three findings on `rule-spec-box`, the open fence of `decision-case-13`, five `deferred` lines and 42 `unread` lines. Nothing was fixed for them.
- `guppi onward --plan` finds a Case still out by the time of its file against its last decision line in `ledger.md`. A Case built again and ratified with decision lines the ledger already holds adds no new line, so the hook stays silent after it until a later decision line of that Case. The run then falls back to the old behaviour: the agent asks.
- The round check of 562 refuses a reply in a notification turn that does not show the round, for example a short note while another `case-guppi` is still out. On the re-fire it passes. Each such wait costs one refusal.
- `estimate-estimates-schema-checked` was not read: `uv run pytest tests/test_schemas.py -k estimate` gave 5 passed and 1 skipped ("no conditional on a field"), and the Criterion names a section required on `passed` and `failed`. Whether the skip leaves that conditional untested was not settled.
- The readings of `estimate-retro-onward-sends-the-agent-to-the-handoff`, `estimate-retro-runs-on-to-the-handoff`, `estimate-where-to-stop-stops-only-on-its-conditions` and `estimate-retro-red-in-the-baseline-is-not-charged` have their moment in this run, from `/work` to the librarian's report. They wait for a reading of this session's transcript, `work.md` and this file. In this run no stop condition arose, `/retro` ran from `/work` in one turn, and the hook of `rule-retro-onward` sent the agent to `/handoff` once.
- A syntax error in `guppi/casecheck.py` stood for one tool call while the round check was written. The live `Stop` hook would have exited 2 on its own error, but no reply ended in that time.

## For the next session

- `rule-case-rebuild-cost` (case 566): rebuild only the changed sub-case, return a short answer to the main agent, keep the `context` short. Both failed readings of `rule-case-build` point the same way: Cases written whole are long, and a fault inside them goes unseen.
- The two failed readings: `estimate-case-build-checks-the-finished-case` (two pages made false and not named, a clash with another Case at one moment) and `estimate-case-build-records-the-rounds-in-recommend` (an item kept on the parent though its answer changed one sub-case).
- The move of the main agent's rules into three files, held by `rule-orchestration`.
- Whether `guppi onward --plan` should judge a Case still out by something other than the ledger's last line, since a re-ratification with unchanged lines adds none.

## Ask the person

- `estimate-context-size-shown-after-each-reply` — needs the person: after the replies of this session in the VS Code chat, did the context size line stand under each reply?
