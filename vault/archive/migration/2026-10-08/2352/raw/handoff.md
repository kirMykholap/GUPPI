# Handoff — 2026-10-08, the turn of a sprint and the After line of grill-me

## Notes from memory

- The person wanted all of `raw/` to go to the archive at the close; the round showed three things that must stay (the session of the run, an unfinished unit, a conserved Spec), and the person agreed to the sweep of what is done.
- On the Backlog of a closed sprint the person went against the recommendation: the opening of a sprint only says how many items `backlog.md` holds and asks whether to take any, with no walk through every line.
- The person first chose a `sprint` key in `guppi.toml` (asking for it in `pyproject.toml`, which holds no such settings), then replaced it with the closed mark in `sprint.md`, once `case-guppi` showed that a key rendered from the sprint page would break the promise that a rendered file is the text of its page.
- The person asked for two skills, `/sprint-close` and `/sprint-open`, instead of one, and for a hook on `/hi` instead of a step of `/hi`; the person asked twice how `/sprint-close` starts and what happens to the rest of the Frontier before agreeing.
- Case 744 came from the person as a cosmetic change; it grew into a change of the round check, since the check required the dash.
- At `/pre-spec` the person chose that the merge of `migration` into `main` moves into the closing Case of `/sprint-close`. One finding was closed differently from the fix proposed: `estimate-sprint-migration-leftovers-gone` and `estimate-sprint-migration-merges` keep a reason the change makes out of date, since their Criteria can change only in the session that reads them.
- Since this session ratified Cases not about the close, it could not close `migration`; the close was put off again, and `rule-morph` was deferred again by Case 745.

## Direct instructions to the librarian

- Check first the four `create` entries of `rule-skill-sprint-open` and `rule-skill-sprint-close` (ledger lines 15, 19, 27, 28): the preview of `guppi materialize --show` marks each `incomplete: [type]`, since the `then` items of 743.6 and 743.8 hold no `type: rule`. Lines 15 and 19 also carry `{ref:rule-session}`, the ref the rebuild at `/pre-spec` replaced by `rule-session-start` and `rule-plan-mode` on lines 27 and 28; a backlink by lines 15 and 19 would make the two rules children of `rule-session` and break `estimate-session-phases-in-order`.
- The `create` of `estimate-skill-sprint-open-asks-the-opening-questions`, `estimate-skill-sprint-open-starts-at-hi` and `estimate-skill-sprint-close-leads-the-closing-session` names a target that is not created while the two rule creates stay incomplete; expect a missing backlink.
- The `update` of `rule-orchestration` by 743.8 removes the paragraph on the closing session and points to `/sprint-close`. While `rule-skill-sprint-close` is not created, the rendered `orchestration.md` holds the steps of the closing session nowhere; flag it in the brief.
- `vault/wiki/backlog.md` was written in Work Mode by `uv run guppi backlog` (its task line of 743.4), with the code of 743.4; your run writes it again.
- The `defer` of `rule-morph` (line 26) shows `exists` in the preview, as a defer of a live page.

## What actually got done

- Cases ratified: 743 (743.1–743.9), 744 (744.1, 744.2), and the short-form defer 745. Case 743 was ratified, then built again on the findings of `/pre-spec` and ratified again.
- Code: `guppi/archive.py` (`sweep`, `unit_sprint`: the walk shared by `guppi archive` and the close, the sprint of a unit from its own yaml, a carried-over unit kept at the close); `guppi/sprint_close.py` (`empty_raw`, `old_logs`, `move_logs`, `remove_empty_dates`: after the tick, the sweep of `raw/` and the old event logs, and the preview of both); `guppi/sprint.py` (`item_statuses`, `is_done`, `closed_heading`, `closed_form`, `closed_id`, `hi_hook`, the `--hi` flag, the closed form of `run` and `--check`, an error on two sprint pages); `guppi/backlog.py` (`item_bodies`, `taken_by`, `finished`: a line of a closed sprint left out once taken or finished, by `item_statuses` and `is_done` of `guppi/sprint.py`); `guppi/casecheck.py` (`AFTER_LINE`, `AFTER_LINES`: the After line with or without the dash); `.gitignore` (`vault/archive/*/*/event_log.md`).
- Tests: `tests/test_archive.py`, `tests/test_sprint_close.py`, `tests/test_sprint.py`, `tests/test_backlog.py`, `tests/test_casecheck.py`; the old test that no sprint page is an error gave way to the tests of the closed form.
- `make test`: 1466 passed, 6 skipped. `make style`: clean.
- Readings: L29–L36 `passed` (`estimate-sprint-close-sweeps-raw`, `estimate-raw-archive-files-a-session-by-its-sprint`, `estimate-sprint-close-moves-old-event-logs`, `estimate-backlog-renders`, `estimate-sprint-marks-a-closed-sprint`, `estimate-sprint-checks-the-file`, `estimate-skill-sprint-open-starts-at-hi`, `estimate-skill-grill-me-asks-in-rounds`); L37–L39 `failed`, Retro, not read (`estimate-skill-sprint-open-asks-the-opening-questions`, `estimate-skill-sprint-close-leads-the-closing-session`, `estimate-case-check-sends-back-a-faulty-round`).
- Lessons: L40 `lesson-case-build-rule-create-without-type`, L41 `lesson-ledger-rebuilt-create-keeps-the-stale-ref`.

## Debt

- No box of code, a test or a command is left unticked; no test was reverted.
- 43 boxes wait for the librarian: the page lines, the render lines, the `guppi sprint` line and the `read` lines.
- `estimate-hi-takes-a-conserved-spec` — waits for a session that takes a conserved Spec and the `/hi` of the session after the close of a sprint.
- `estimate-brief-written` — waits for the `/hi` after the librarian's run of the session that closes a sprint.
- `estimate-sprint-close-runs-in-the-librarian-run` — waits for the librarian's run of the session that closes a sprint.
- `estimate-sprint-close-next-session-opens-the-sprint` — waits for the librarian's run of the session after the close.
- `estimate-sprint-close-takes-the-readings-in-groups` — waits for the Work Mode of the session that closes a sprint.
- `estimate-sprint-migration-leftovers-gone`, `estimate-sprint-migration-lint-clean`, `estimate-sprint-migration-merges` — wait for the Work Mode of the session that closes `migration`.

## Observations

- Red before the work, by `## Baseline` of `work.md`: `make lint` exit 2, 12 finding lines. The line `backlog: vault/wiki/backlog.md differs from its sources` is gone after `uv run guppi backlog` in Work Mode; `rules/rule-morph: deferred` and the ten `unread: pending` lines stay. No expected red.
- The method `-k hi` of `estimate-skill-sprint-open-starts-at-hi` selects 7 tests of `tests/test_sprint.py`, of which two are the tests of the hook: the substring `hi` stands in other test names too.
- The hook `guppi sprint --hi` runs only once the librarian's render writes the `UserPromptSubmit` registration of `rule-hook-registry` into `.claude/settings.json`.
- In the close, the tick of the close line runs before the sweep of `raw/`, so the Spec that holds the line is ticked while it is still in `raw/`; the session of the run never moves.
- `guppi sprint` now refuses two live sprint pages with its own line, where before it reported them as no sprint page.

## For the next session

- 743.6 and 743.8 need to be built again with `type: rule` on the `create` items of `rule-skill-sprint-open` and `rule-skill-sprint-close`, and with marks that retire ledger lines 15 and 19, whose `{ref:rule-session}` is stale; `estimate-skill-sprint-open-asks-the-opening-questions` and `estimate-skill-sprint-close-leads-the-closing-session` are `failed` until then.
- `estimate-case-check-sends-back-a-faulty-round` is `failed`: its method asks for a round the hook sends back live, which did not occur after the change.
- `lesson-case-build-rule-create-without-type`: no check before the Spec judges the fields `materialize` requires of a `create` item.
- `lesson-ledger-rebuilt-create-keeps-the-stale-ref`: a rebuilt Case that changes the `ref` of a `create` line leaves the first line, with its stale ref, as an entry of the yaml.
- The close of `migration` and its session of its own stay open.

## Ask the person

- `estimate-hi-writes-frontier` — needs the person — at the `/hi` of the session after the close of a sprint: did the Frontier come out as the Criterion says, an item closed `defer` or `kept` with no short Case but the short Case of a take-back, and no second line for a brief line that repeats a milestone item?
