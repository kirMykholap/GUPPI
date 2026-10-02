# Handoff — 2026-10-01, the Stop hooks after a refusal, the later Frontier, related Cases in the dispatch, the waiting line of pre-spec

## Notes from memory

- On C2 the person kept the rule of one or two sentences for the `Changes:` paragraph and judged the length point of `estimate-case-protocol-acknowledging-reply` passed ("we do not count sentences anyway"). No reading was written, since 578.2 updates that Estimate in this session; the person does not want the length counted as a failure at its next reading.
- On C3 the person held that folding the open `W` lines is the norm and the Estimate was wrong, not the agent.
- On C6 the person rejected the recommended option: `case-guppi` must not read the Cases of the session; the main agent names the related ones in its prompt.
- C1 and C9 were put off with no Case. C9 is the line of the 1237 handoff that the person had put the sprint item off; it names no page of its own, so it was closed `[-] … · sprint · defer` like C1, although its source is the brief.
- The person asked to take as many Work readings as this session allows.

## Direct instructions to the librarian

- Case 580 was ratified, then ratified again as 580.1 and 580.2, then built again as 581.1 and 581.2, whose lines carry `{supersedes:case 580}`, `{supersedes:case 580.1}` and `{supersedes:case 580.2}`. The ledger keeps the lines of 580, 580.1 and 580.2; only 581 stands in `spec.md`. No Decision page of 580 should carry live content.
- Cases 577, 578 and 579 were ratified again after `/pre-spec`; the ledger holds each of their decision lines once.
- The line of 579.2 on `estimate-case-build-checks-the-finished-case` carries `{supersedes:case 571}`; an Estimate carries no `deferred_by`, so only the Decision page of 571 is superseded.
- Cases 578.2 and 579.1 both change the Render of `rule-case-protocol`, in different paragraphs; apply both pairs.

## What actually got done

- Ratified: 577.1 to 577.8, 578.1, 578.2, 579.1, 579.2, 581.1, 581.2.
- Code: `guppi/ledger.py` — `own_refusals`, the one judgment of the stretch and of a hook's own refusals, `silenced` and `untold`; the hook writes whatever `stop_hook_active` says and tells each refused line once a stretch. `guppi/onward.py` — the run without `--plan` judges its own refusal through `own_refusals` and `silenced`; `--plan` keeps the flag. `guppi/casecheck.py` — the docstrings give the true reason for the exemption after `/pre-spec`.
- Tests: `tests/test_ledger.py`, `tests/test_onward.py`. `make test` 1050 passed, 2 skipped; `make style` clean.
- Readings: ledger line 13 (`estimate-case-build-writes-a-plain-round`, passed), line 21 (`estimate-spec-write-writes-a-defer`, passed), and the Retro lines after line 32: `estimate-ask-finds` failed, `estimate-case-build-records-the-rounds-in-recommend`, `estimate-case-protocol-asks-in-the-grill-me-shape` and `estimate-governed-files-hook-refuses` passed.
- Lesson: ledger line 32, `lesson-spec-write-keeps-the-body-of-a-case-that-gains-sub-cases`.

## Debt

- None.
- 27 boxes of `spec.md` wait for the librarian: the page lines and the `guppi render` lines.
- Read lines whose slug this session updates or creates: `estimate-retro-onward-sends-the-agent-to-the-handoff`, `estimate-retro-onward-exits-2-on-an-error`, `estimate-ledger-write-lifts`, `estimate-ledger-write-exits-2-on-an-error`, `estimate-ledger-write-refuses-a-line-it-cannot-read`, `estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session`, `estimate-ledger-write-refuses-a-lesson-without-its-prefix`, `estimate-ledger-write-refuses-a-mark-with-no-decision-line`, `estimate-case-protocol-shows-the-frontier-after-a-closed-line`, `estimate-case-protocol-acknowledging-reply`, `estimate-case-protocol-names-related-cases-in-the-dispatch`, `estimate-case-build-checks-the-finished-case`, `estimate-prespec-gathers-the-answers-after-findings`, `estimate-case-check-refuses-text-before-a-round`.

## Observations

- Red before the work: the Baseline `make lint` exit 2 — `rules/rule-spec-box` schema (missing `kind`, missing `estimates`) and orphan, the open fence of `decisions/decision-case-13`, 6 deferred lines, 34 unread lines. No expected red.
- The module docstring of `guppi/casecheck.py` still says that a refusal of a `Stop` hook adds no `user` record (measured 2026-09-27); the transcripts of sessions 1237 and 1441 show it adds one, marked `isMeta`. Its judgment skips such records, so its behaviour is right.
- The changed `guppi onward` refused the reply that ended Retro, as it should; but no other hook had refused earlier in that stretch, so this was not yet the long stretch the fix is for.
- `estimate-estimates-schema-checked` was not read: its Criterion promises a finding for a conditional not met, and the only conditional of the Estimates schema is the `## Result` section on `passed` and `failed`; `tests/test_schemas.py` tests a conditional on a field only and skips the Estimates, so no test covers that Result conditional. The live `make lint` shows no schema finding on `wiki/estimates/`.
- `estimate-case-build-writes-the-case` and `estimate-plan-mode-verified` were not read: no Case of this session proposed a `create` without a `ref`.
- Not read, their moment not yet come: `estimate-brief-written`, `estimate-documentation-completes`, `estimate-generate-rewords`, `estimate-synthesis-clusters` (a later librarian's run); `estimate-carry-over-writes` (a `/carry`); `estimate-case-check-requires-each-question-of-the-rounds`, `estimate-case-check-shows-only-the-checked-case` (no refusal of the hook); `estimate-case-protocol-ledger-line-form`; `estimate-compact-recall-reloads` (no compaction); `estimate-end-of-work-order`, `estimate-handoff-dispatches`, `estimate-handoff-holds-each-fact-once`, `estimate-retro-runs-on-to-the-handoff`, `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note` (the close of this run, after Retro); `estimate-event-log-records` (a `/hi` outside plan mode); `estimate-session-start-context`; `estimate-spec-write-reaches-the-approved-spec` (no Case ratified in Work Mode); `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` (no `/work` typed by the person); `estimate-sprint-migration-leftovers-gone`, `estimate-sprint-migration-lint-clean`, `estimate-sprint-migration-merges` (the close of the sprint).

## For the next session

- The Spec hook of `rule-spec-write` keeps the body a Case held when it stood alone once it is ratified again with sub-cases, so the content is signed twice; this session worked around it with a new id. Whether the hook should replace the whole Case on re-ratification needs a decision.
- `estimate-ask-finds` failed: two of three answers of `ask-guppi` add a list of file paths after the five lines. Decide whether the frame of `ask-guppi` forbids that list or the Criterion allows it.
- The test of a conditional section of the Estimates schema: write it, or change the Criterion of `estimate-estimates-schema-checked`; the defer of case 576 still stands.
- The close of the sprint (Slice 5) stays put off.

## Ask the person

- none
