# Brief — 2026-09-30, session 0248: UTF-8 for Python, glossary rows, case-guppi quotes, the /carry brief, the sprint move removed

## Where things stand

- Ratified and applied (handoff): 534.1, 534.2, 535, 536, 537, 538.1, 538.2, 539.1, 539.2, 539.3, 539.4; deferred: 540 (`rule-work-mode`). 538.1 supersedes the defer 533 of session 0138.
- Code (handoff): `guppi/casecheck.py` (the language finding on each answer of case-guppi), `guppi/generate.py` (the move and the drop of the sprint removed), `guppi/backlog.py` (docstrings); tests `tests/test_casecheck.py`, `tests/test_generate.py`. `make test` 935 passed, 2 skipped; `make style` clean.
- Yaml: `raw/2026-09-30/0248/materialize.yaml` 42 entries and 4 of the synthesis, 46 applied, none `failed`, none `incomplete`, `unparsed` empty; its ledger (42 lines) is held whole by the yaml. `raw/2026-09-30/0138/materialize.yaml` extended with 0 entries; its ledger (7 lines) is held whole.
- Pages: decisions 12 created (534.1, 534.2, 535, 536, 537, 538.1, 538.2, 539.1, 539.2, 539.3, 539.4, 540), 1 archived (533, superseded by 538.1); rules 1 created (`rule-python-utf8`), 12 updates on 10 pages (`rule-settings`, `rule-hook-registry`, `rule-case-build`, `rule-case-check`, `rule-carry-over`, `rule-brief` ×2, `rule-sprint` ×2, `rule-page-generation`, `rule-backlog`, `rule-skill-hi`), 1 defer (`rule-work-mode`); estimates 2 created (`estimate-python-utf8-output-intact`, `estimate-case-check-refuses-a-letter-outside-the-script`), 13 readings (10 passed, 3 failed), 5 updated (`estimate-settings`, `estimate-carry-over-writes`, `estimate-brief-written`, `estimate-backlog-renders`, and `estimate-sprint-moves-a-passed-over-item` renamed to `estimate-sprint-items-move-only-by-a-case`), 1 deleted and archived (`estimate-sprint-drops-an-emptied-milestone`); entities 2 updated (`entity-glossary`, `entity-sprint-migration`); insights 3 updated; lessons 4 created, 2 updated by the synthesis, 2 archived.
- `insight-case-form-chat-form-read-by-no-script` set `actioned` by case 537; the cascade archived its two clustered lessons, `lesson-case-build-quotes-the-person-in-the-chat-language` and `lesson-case-build-rebuild-quotes-the-relayed-words`.
- Synthesis: `lesson-case-build-built-case-departs-from-the-chosen-option` joined `insight-case-build-promise-lines-compared-by-no-check` (open, severity 1, `addressed_by` 472.3 kept); `lesson-case-build-frame-count-claimed-over-a-partial-search` joined `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it` (open, severity 1, `addressed_by` 388 kept). `lesson-bash-tool-python-cp1252-dash-shown-as-u-fffd` (`addressed_by: decision-case-534.1`) and `lesson-prespec-report-decisions-off-the-question-shape` stay `new`.
- Cascade: `rule-agent-writing`, `rule-bash-guard`, `rule-git-context`, `rule-prespec`, `rule-skill-wait-what` draft → built; `rule-backlog`, `rule-carry-over`, `rule-settings`, `rule-sprint` built → draft.
- Render wrote: `.claude/settings.json` (the `env` block, `PYTHONUTF8`), `.claude/agents/case-guppi.md`, `.claude/agents/librarian-guppi.md`, `.claude/skills/carry/SKILL.md`, `.claude/skills/hi/SKILL.md`. `sprint.md`, `backlog.md` (22 items, was 26) and `glossary.md` rewritten. `generate` ticked 32 boxes of `raw/2026-09-30/0248/spec.md`.
- Archive: `guppi archive` exit 0, no stdout and no stderr; `raw/2026-09-30/0138` and `raw/2026-09-30/0248` stay under `raw/`.

## Readings due

3 Estimates are `failed`, 40 `pending`; each target stands `draft`.

- `estimate-glossary-terms-defined` — `entity-glossary` — failed: three rows contradicted their page (Decision page, Main agent, Plan Mode); method: one reading of the table by hand after the librarian's run, plus `make lint`. This run: case 535 applied to `entity-glossary`; `guppi glossary` exit 0, no stderr; the diff of `glossary.md` rewrites five rows — Types, Main agent/Subagent, Plan Mode, `CLAUDE.md`/`case-schema.md`, Decision page; `make lint` prints no line on `entity-glossary`
- `estimate-case-build-writes-a-plain-round` — `rule-case-build` — failed: the first round on Case 534 ended with a "Files checked:" list of transcript names; method: by hand in a session after the render, one first round and one later round of case-guppi read in the chat
- `estimate-skill-grill-me-asks-in-rounds` — `rule-skill-grill-me` — failed: the label `**Options:**` stood indented by four spaces under the Now block in most rounds; method: `uv run guppi render --check`; by hand, one round read in the chat in a session after the render
- `estimate-ask-finds` — `rule-ask` — method: by hand in a later session, three dispatches of ask-guppi read against the event log
- `estimate-backlog-renders` — `rule-backlog` — spec 0248: `uv run pytest tests/test_backlog.py`, and `vault/wiki/backlog.md` after the librarian's run, in a later session. This run: `guppi backlog` exit 0, no stderr; `backlog.md` holds "22 items" (was 26); its diff removes the lines of `rule-carry-over`, `insight-case-form-chat-form-read-by-no-script`, `estimate-sprint-migration-lint-clean` and `estimate-sprint-migration-merges`, and keeps `rule-work-mode` "put off in 30 sessions"
- `estimate-brief-written` — `rule-brief` — spec 0248: at the librarian's run after the render. This run: this brief was written under the frame loaded at the start of the run; the render of this run rewrote `.claude/agents/librarian-guppi.md` (6 lines, cases 538.2 and 539.2)
- `estimate-carry-over-writes` — `rule-carry-over` — spec 0248: at the first `/carry` after the render, and at the `/hi` after it
- `estimate-case-build-writes-the-case` — `rule-case-build` — method: by hand, live dispatches in a session after the render
- `estimate-case-check-refuses-a-letter-outside-the-script` — `rule-case-check` — spec 0248: at a later session; method `uv run pytest tests/test_casecheck.py -k script`
- `estimate-case-check-sends-back-a-faulty-case` — `rule-case-check` — method: `uv run pytest tests/test_casecheck.py -k subagent`, then by hand the first answer the hook sends back
- `estimate-case-check-shows-only-the-checked-case` — `rule-case-check` — method: `uv run pytest tests/test_casecheck.py -k stop`, then by hand the first reply the hook refuses
- `estimate-case-protocol-ledger-line-form` — `rule-case-protocol` — method: by hand, the ledger and preview of the first session where a lesson and the Case that closes its cause stand together, and of the first Case that takes up a decision with more than one Case in its `deferred_by`
- `estimate-case-protocol-shows-the-built-case` — `rule-case-protocol` — method: by hand, the Cases of a session at its close against the transcript
- `estimate-compact-recall-reloads` — `rule-compact-recall` — method: `pytest tests/test_recall.py`; live, the first compaction of a working session
- `estimate-documentation-completes` — `rule-documentation` — method: `make test-documentation`; the live reading by hand
- `estimate-end-of-work-order` — `rule-end-of-work` — method: `make test-end-of-work`, then by hand at the close of a later session
- `estimate-event-log-records` — `rule-event-log` — method: pytest in `tests/test_event.py` and `tests/test_gate.py`; by hand, one `/hi` outside plan mode and one in it
- `estimate-generate-rewords` — `rule-page-generation` — method: `pytest tests/test_generate.py`; the live reading, the librarian's run that applies the first reword. This run: no entry of either yaml carries `reword`
- `estimate-generate-writes` — `rule-page-generation` — method: pytest in `tests/test_generate.py`; the live reading once by hand
- `estimate-governed-files-hook-refuses` — `rule-governed-files-hook` — method: `pytest tests/test_guard.py`, then by hand one refused Edit of a governed file
- `estimate-handoff-dispatches` — `rule-handoff` — method: by hand at the `/handoff` of a later session
- `estimate-handoff-holds-each-fact-once` — `rule-handoff` — method: by hand at the first `/handoff` after the render, against the close of its Retro
- `estimate-hi-takes-its-readings` — `rule-skill-hi` — method: by hand at the first `/hi` after the render
- `estimate-permissions` — `rule-permissions` — method: the allow list of `.claude/settings.json` and `tests/test_render.py`; the live probe is the person's word on the client's prompt at a Write of `work.md`
- `estimate-plan-mode-verified` — `rule-plan-mode` — method: `make test-plan-mode`; one live reading by hand
- `estimate-python-utf8-output-intact` — `rule-python-utf8` — spec 0248: at a later session start; method `uv run guppi render --check` and `json.load` of `.claude/settings.json`, then a Python script through the Bash tool
- `estimate-retro-commit-gates` — `rule-retro-commit` — method: pytest in `tests/test_gate.py`; the live reading once by hand
- `estimate-retro-loads` — `rule-retro` — method: by hand at the first `/retro`
- `estimate-retro-onward-sends-the-agent-to-the-handoff` — `rule-retro-onward` — method: `uv run pytest tests/test_onward.py`; by hand at the first run from `/work` to the librarian after the render
- `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note` — `rule-retro` — method: by hand at the first `/retro` after the render whose `work.md` names a check under Expected red
- `estimate-retro-red-in-the-baseline-is-not-charged` — `rule-retro` — method: by hand at the first `/retro` after the render whose `work.md` Baseline holds a failing test or a lint finding line
- `estimate-retro-runs-on-to-the-handoff` — `rule-retro` — method: by hand at the first run from `/work` to the librarian after the render
- `estimate-session-phases-in-order` — `rule-session` — method: by hand at the close of a session, the marks of each phase read in order
- `estimate-session-start-context` — `rule-session-start` — method: `make test-session-start`; by hand, one session opened without `/hi`
- `estimate-settings` — `rule-settings` — spec 0248: at a later session start; method `make test-harness`, `json.load`, `guppi render --check`, the session-start line of the event log
- `estimate-spec-write-reaches-the-approved-spec` — `rule-spec-write` — method: `uv run pytest tests/test_ratified.py -k approved_spec`; by hand, the first Case ratified in Work Mode after the change
- `estimate-sprint-items-move-only-by-a-case` — `rule-sprint` — spec 0248: in a later session, after the librarian's run; method `uv run pytest tests/test_generate.py -k moves_no_line`, then the History of `entity-sprint-<id>`. This run: `generate` printed two lines, one count per yaml, and no move line; the History of `entity-sprint-migration` gained one line, the update of case 539.3
- `estimate-sprint-migration-leftovers-gone` — `entity-sprint-migration` — method: by hand on the tree at the close of the sprint
- `estimate-sprint-migration-lint-clean` — `entity-sprint-migration` — method: `make lint`, exit 0, or only unread lines on the Estimates of `entity-sprint-migration`
- `estimate-sprint-migration-merges` — `entity-sprint-migration` — method: `make test` on the last commit of `migration`, then git log of `main` after the merge
- `estimate-where-to-stop-stops-only-on-its-conditions` — `rule-where-to-stop` — method: by hand at the first run from `/work` to the librarian after the render
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — `rule-work-mode` — method: `uv run guppi render --check`; by hand, the first `/work` the agent calls at the fork and the first `/work` the person types
- `estimate-work-mode-takes-the-work-readings` — `rule-work-mode` — method: by hand at the first `/work` after the render

## Flags

- `near`: `lesson-bash-tool-python-cp1252-dash-shown-as-u-fffd` near `lesson-bash-tool-heredoc-escapes-interpreted` (both name console output outside UTF-8 on Windows; different triggers); `lesson-case-build-frame-count-claimed-over-a-partial-search` near `lesson-case-build-writes-a-count-no-command-printed`.
- No entry `incomplete`, `failed` or `unparsed`.
- Failed Estimates: `estimate-glossary-terms-defined`, `estimate-case-build-writes-a-plain-round`, `estimate-skill-grill-me-asks-in-rounds`.
- MOC candidates: none. Contradictions: none found.
- Handoff observation: the `!` commands of `/work` and `/retro` reached the agent as instructions to run them, not as their output; the agent ran them itself.
- Handoff observation: `work.md` was written through Bash, so the live probe of `estimate-permissions` at its Write did not occur.
- Handoff observation: a scratchpad Python script of Work Mode stopped at the print of a Cyrillic string until it ran with `PYTHONUTF8=1`; the render of this run wrote the `env` block.
- `make lint`: exit 2, 84 finding lines — `rule-spec-box` schema: missing field `kind`, missing field `estimates`, and orphan; 31 Decision pages of Cases 1–28 missing `## Problem`; `decision-case-13` fence open at the end of `## When`; deferred: `rule-case-build-checks-its-sub-cases` 1 time since case 480, `rule-complaint-becomes-a-lesson` 1 since 504, `rule-morph` 1 since 239, `rule-orchestration` 1 since 424, `rule-prespec-script-skips-code-spans` 1 since 481, `rule-subagent-guppi` 31 times since case 29; unread: 40 `pending` and 3 `failed`, the Estimates of Readings due. Handoff: 88 lines before and after the work.

## Next session

Cases
- `estimate-case-build-writes-a-plain-round` failed: a round of case-guppi ended with a list of the files it checked, session ids in their names (handoff, For the next session)
- `estimate-skill-grill-me-asks-in-rounds` failed: case-guppi indents the label `**Options:**` by four spaces under the Now block in most rounds (handoff, For the next session)
- No rule gives the question shape of grill-me to a question the main agent asks the person itself, as in a pre-spec report (handoff, For the next session; `lesson-prespec-report-decisions-off-the-question-shape`)
- case-guppi can build a Case that departs from the option the person chose, and can sign a count over the frame from a partial search; both found only at pre-spec (handoff, For the next session)
- `estimate-glossary-terms-defined` failed on three rows; case 535 of this run rewrote five rows (Readings due)

Work
- `estimate-ask-finds`
- `estimate-backlog-renders` (spec 0248, unticked `read` box)
- `estimate-brief-written` (spec 0248, unticked `read` box)
- `estimate-carry-over-writes` (spec 0248, unticked `read` box)
- `estimate-case-build-writes-the-case`
- `estimate-case-check-refuses-a-letter-outside-the-script` (spec 0248, unticked `read` box)
- `estimate-case-check-sends-back-a-faulty-case`
- `estimate-case-check-shows-only-the-checked-case`
- `estimate-case-protocol-ledger-line-form`
- `estimate-case-protocol-shows-the-built-case`
- `estimate-compact-recall-reloads`
- `estimate-documentation-completes`
- `estimate-end-of-work-order`
- `estimate-event-log-records`
- `estimate-generate-rewords`
- `estimate-generate-writes`
- `estimate-governed-files-hook-refuses`
- `estimate-handoff-dispatches`
- `estimate-handoff-holds-each-fact-once`
- `estimate-hi-takes-its-readings`
- `estimate-permissions`
- `estimate-plan-mode-verified`
- `estimate-python-utf8-output-intact` (spec 0248, unticked `read` box)
- `estimate-retro-commit-gates`
- `estimate-retro-loads`
- `estimate-retro-onward-sends-the-agent-to-the-handoff`
- `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note`
- `estimate-retro-red-in-the-baseline-is-not-charged`
- `estimate-retro-runs-on-to-the-handoff`
- `estimate-session-phases-in-order`
- `estimate-session-start-context`
- `estimate-settings` (spec 0248, unticked `read` box)
- `estimate-spec-write-reaches-the-approved-spec`
- `estimate-sprint-items-move-only-by-a-case` (spec 0248, unticked `read` box)
- `estimate-sprint-migration-leftovers-gone`
- `estimate-sprint-migration-lint-clean`
- `estimate-sprint-migration-merges`
- `estimate-where-to-stop-stops-only-on-its-conditions`
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`
- `estimate-work-mode-takes-the-work-readings`

Ask the person
- none

## Readings at the close

- `make test`: 935 passed, 2 skipped.
- `make lint`: exit 2, 84 finding lines (Flags).
- Pages in `vault/wiki/`: rules 75, estimates 161, lessons 71, insights 26, entities 4, decisions 834.
