# Handoff — 2026-10-03, the showing of a Case, the close of a sprint, the moment of a reading

## Notes from memory

- Before the second Case the person said the harness looks like an endless loop of fixes: readings hang session after session, the backlog only grows, native Claude features may already do what GUPPI builds, and a plugin that circles the same problems would serve no one. The person chose to go on: build the Case of the showing, close the readings honestly, and give the close of a sprint a cleaning role.
- The person asked whether all pending readings could be closed `passed` at once. The agent answered that a `passed` line with no reading behind it is a false record; the person moved the question into Case 613 instead of a bulk close.
- Case 612: the person said the close of a sprint is more than a Case — a skill, an agent or a mode of work of its own — and left where it runs open. The person chose that this sprint closes with a clean `make lint`: no Estimate is carried forward at the close of migration.
- Case 613.3 rewrites the `method` of 37 Estimates and lists none of its own Estimate; its check is the Estimate of 613.1 (`make lint` with no `moment` finding), which its context names.

## Direct instructions to the librarian

- Case 613.3 is 37 `update` items that change only `method`: the Criterion and the status of each page stand. The 20 of them that `make lint` reports under the class `moment` (with `estimate-hi-takes-its-readings` of 613.2, 21 in all) go clean only when these pages are written.
- Case 612.1 creates `rule-sprint-close` with no `enforcement` and no code, `applies_to: [entity-sprint]`; the cascade adds it to the `rules` of `entity-sprint`. It also replaces the note of Slice 5 on `entity-sprint-migration` by the item `[[rule-sprint-close]]` and a plain note that where the close runs is not decided; `guppi sprint` renders it.
- Case 611 sets `insight-case-form-chat-form-read-by-no-script` `actioned` with `addressed_by` `decision-case-611`; its two live lessons stand `clustered` and the cascade archives them.
- The two lessons of this Retro: `lesson-estimates-reading-tied-to-a-one-off-moment` carries `addressed_by: case 613.2`; `lesson-case-build-a-count-in-context-not-from-a-run` may sit near `insight-workflow-case-schema-silent-on-what-the-scripts-accept` (a fact the scripts do not check) — judge it at synthesis.

## What actually got done

- Ratified: 611; 612 (612.1–612.4); 613 (613.1–613.3). All three were built again after the findings of `/pre-spec` and ratified again with unchanged decision lines.
- Code: `guppi/casecheck.py` — `outside_the_list` and `showing_layout`, the `Stop` run refuses a showing with text before the first Case heading, under a heading outside the list and the `ratification` blockquote, a section other than `ratification`, or text before the last tool call (by the existing `texts_before_last_call`). `guppi/lint.py` — `tied_to_a_one_off_moment` and the class `moment`; `guppi/prespec.py` imports it in `check_form` for a `create` and a `set` of `method`. Docstrings updated.
- Tests: `tests/test_casecheck.py` — 7 tests of the layout; 9 showings that put sections under the heading now assert the layout reason alone (`compared_alike`), and `SHORT_SHOWING` and the showing of a note use the list. `tests/test_lint.py` — 3 tests `moment`; `tests/test_prespec.py` — 2 tests `moment`.
- `make test`: 1129 passed, 6 skipped. `make style`: clean.
- Readings: ledger line 1 (`estimate-synthesis-clusters`, at `/hi`), lines 52 and 53 (`estimate-case-build-writes-the-case`, `estimate-end-of-work-order`, Work readings). Lessons: lines 54 and 55.

## Debt

- None: every box of code and tests of the Spec is ticked.
- Boxes that wait for the librarian: 53 (page lines, the `guppi render` lines and the `guppi sprint` line).
- `read` lines whose slug this session creates or updates: `estimate-case-check-refuses-text-outside-the-list`, `estimate-sprint-close-archives-the-decisions`, `estimate-sprint-close-archives-done-insights-and-lone-lessons`, `estimate-sprint-close-archives-the-sprint-page-and-keeps-the-rest`, `estimate-sprint-close-settles-unread-estimates`, `estimate-lint-reports-a-method-tied-to-a-one-off-moment`, `estimate-hi-takes-its-readings`; besides them the 37 Estimates whose `method` 613.3 rewrites wait for a later session.

## Observations

- Expected red: `make lint`, the class `moment` of `guppi lint`, 21 findings on the Estimates whose `method` 613.2 and 613.3 rewrite; red until the librarian writes those pages.
- Red before the work (`## Baseline`): `make lint` exit 2 — 5 `deferred`, 37 `unread: pending`, 1 `unread: failed` (`estimate-orchestration-shows-the-built-case`).
- The `read` line of `estimate-orchestration-shows-the-built-case` in the Spec stays open: Case 611 has it read again in a later session, once the check of the layout is live; this session's showings were made before that check was built.
- The new `Stop` check of the layout is live from this commit on: a showing in a later session that keeps a note under the heading, or text before the last tool call, is refused.
- The 8 Estimates that keep a method with no one-off moment (`estimate-end-of-work-order`, `estimate-event-log-records`, `estimate-ask-finds`, `estimate-plan-mode-verified`, `estimate-case-build-writes-the-case`, `estimate-session-start-context`, `estimate-orchestration-shows-the-built-case`, `estimate-synthesis-clusters`) and the three Estimates of `entity-sprint-migration` were not rewritten.
- `estimate-plan-mode-verified` was not read: its flagging part needs a `create` whose purpose an index line already carries, which this session did not meet.

## For the next session

- Where the close of a sprint runs — a session offered by `/hi`, a command run by an agent of its own, or another place — not decided; it stands as a note on the sprint page. The Case that decides it gives `rule-sprint-close` its guard and changes `rule-insights-schema`, `rule-lessons-schema`, `rule-decisions-schema`, `rule-synthesis`, `estimate-synthesis-clusters` and `estimate-synthesis-keeps-actioned-by-the-mark`.
- The four Estimates of 612 are read "after the first close of a sprint"; the close of migration needs every Estimate read or archived (`estimate-sprint-migration-lint-clean` kept as it stands), so the readings of the next session's `/hi` (by 613.2, from the transcripts of earlier sessions) decide how much stays for the close.
- The person's question whether GUPPI should go on as it is, shrink to a core, or give way to native Claude features stands open; it shapes the plugin question too.

## Ask the person
