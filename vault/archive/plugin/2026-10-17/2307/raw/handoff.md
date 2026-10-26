# Handoff — 2026-10-17, the sprint plugin: neutral shipped texts, the window of a session, a retired Case

## Notes from memory

- The session ran over nine days: `/hi` on 2026-10-17 23:07, a pause of a week, a resume on 2026-10-24, work on 2026-10-25 and 2026-10-26. The person removed by hand, three times, lines of the event logs that cut the window of the session: the `resume` start line of 2026-10-24, and on 2026-10-25 the tool lines whose text held the stamp, a space and the word of the start. Each time the run went on only after that edit.
- The person asked for a plain explanation of the eight Estimates of Case 882 before answering; after it, all recommendations stood.
- The person chose that Case 884 grows to the stop on a tool line (the second form of the cut), and that the sprint close goes to a Case of its own (886), not into 884.
- At /pre-spec the person ratified 882, 883, 884 and 886 first and 881 after, since the check of rule-case-check refused 881.24 while 883 stood in the plan in its old text. The person asked that this, and the rule that a batch is ratified whole, be taken up in the next session (put off by Case 887).
- The person said of Case 884 that the fix must hold "always, so the error does not repeat".

## Direct instructions to the librarian

- Cases 882, 883, 884 and 886 were ratified twice: their first lines and the rebuilt ones. The ledger holds the rebuilt 882 and 883 lines only once, since their text did not change; 884 has a second `update` of `rule-ledger-write` with a second `{addresses:...}` mark and new lines on `rule-orchestration`; Case 881 has its 25 first lines and a new line for 881.26. Take each Case from the Spec as it stands now, the rebuilt one.
- Case 882.3 supersedes `decision-case-880.21` and puts `rule-clean-branch` off again; Case 884 supersedes `decision-case-876` and carries its put-off of `rule-orchestration` over by a `defer` and an `update` with only a `change`. Check that `rule-orchestration` keeps a live `deferred_by` (884 and 887) and that `rule-ledger-write` loses `decision-case-876`.
- Case 883 changes `guppi generate`: from this run on, a record with `superseded_by` carries out none of its `supersedes`. No record of this session carries `superseded_by`, so the run should act as before on 882.3 and 884.
- Cases 881, 883 change the same three pages, `rule-page-generation`, `rule-decisions-schema` and `entity-glossary`, on different sentences; a `replace` absent or not unique there is the first thing to look at.
- `rule-orchestration` gets two `defer` lines from two Cases (884, 887) and one `update`: two `## Deferred` Decision pages name it.

## What actually got done

- Cases ratified: 881 (881.1–881.26), 882 (882.1–882.3), 883, 884, 886; short-form defers 885 and 887.
- Code: `.guppi/guppi/ledger.py` (`parse_event`, `event_of`, `hi_stamps`, `opens_session`, `NEW_SESSION`; `session_event_logs` ends only at a `startup` or `fork` start line read by its form; `hi_moment` reads through `event_of`), `.guppi/guppi/generate.py` (`Vault.decision` returns before the `supersedes` walk for a record with `superseded_by`; docstring), `.guppi/guppi/materialize.py` (docstring), `.guppi/guppi/sprint_close.py` (`old_logs` asks the window of the hooks and returns the reason when it cannot tell the session; `move_logs` prints `archive: event logs kept: <reason>`; docstring).
- Tests: `.guppi/tests/test_ledger.py` (six `later_date` tests), `.guppi/tests/test_generate.py` (two tests of case 883), `.guppi/tests/test_sprint_close.py` (the event-log tests rewritten with start and `hi` lines, three new).
- `uv run --project .guppi guppi test`: 1768 passed, 6 skipped, 1 deselected. `uv run --project .guppi guppi style`: clean.
- Readings: L50–L54 passed (`estimate-glossary-checks-the-file`, `estimate-orchestration-asks-in-the-grill-me-shape`, `estimate-generate-writes-the-decision-page`, `estimate-ledger-write-keeps-the-window-past-a-later-resume`, `estimate-sprint-close-moves-old-event-logs`).
- Lessons: L26 `lesson-session-window-cut-by-a-resume-on-a-later-date` and L40 `lesson-session-window-cut-by-a-tool-line-that-names-the-start` (both addressed by Case 884), L48 `lesson-casecheck-reads-a-sibling-from-the-plan-as-last-ratified`, L55 `lesson-prespec-loop-stalls-when-one-case-waits-after-a-partial-ratification`.

## Debt

- No box of code, a test, a command or a migration is left unticked.
- The other unticked boxes of the Spec wait for the librarian: the page lines, the `guppi render` lines, the `guppi glossary` lines and the `read` lines of the readings above.
- `estimate-clean-branch-ships-neutral-texts` — waits for the librarian's run of this session; its next reading still fails on the `.gitignore` method of `estimate-sprint-close-moves-old-event-logs`.
- `estimate-generate-writes-rules-from-applies-to` and `estimate-spec-capture-appends` — only their `method` changed (881.11, 881.25); not read, status kept.

## Observations

- `uv run --project .guppi guppi check` was red before the work with 15 lines (Baseline of `work.md`); no new red was seen, and Retro did not run it.
- The check of rule-case-check reads another Case of the session from the plan as last ratified, but looks for its text in that Case's current file (L48); it refused the showing of Case 881 three times until 883 was ratified again.
- After the ratification of 882, 883, 884 and 886, no hook sent the run on to send 881 back; the person asked what was next (L55).
- `guppi caseid` printed no id while the window was cut, and so did the ledger hook; after each hand edit of the event log they worked again.
- The page-read hook adds a `limit` to a whole Read of a page, so a Read never returns the History of a page; the case-guppi of 881 noted it while the check asked for a whole read.

## For the next session

- The two items put off by Case 887 (`rule-case-check`: the part of a sibling read from the plan as last ratified; `rule-orchestration`: a batch ratified whole, and whether Cases with no finding are ratified first).
- L55: the loop after the findings of /pre-spec has no turn for the Cases left after a partial ratification.
- Case 883 left a known gap: the tags that a retired Case writes in `materialize.yaml` are not taken back, so an earlier Case whose entries are not yet applied would still be skipped.

## Ask the person

- `estimate-guppi-package-is-ready-after-the-install` — needs the person — In an empty project on a machine with `uv`, after the librarian's render, does `/guppi:install` run `uv --version`, ask nothing about `uv`, build `.guppi/.venv/` by `uv sync` after the copy before it sends you to `/hi`, and do the hooks find that environment at the first `/hi`?
