# Brief — 2026-09-30, the conserved Spec of session 2024 built

## Where things stand

- Built: the conserved Spec of session 2024 (commit 734d216), its `carry.md` deleted. Ratified and applied: 526, 527.1, 527.2, 528.1, 528.2, 528.3, 528.5, 529, 530.1, 530.2, 531.1–531.15, 532, and the defer 533 of session 0138.
- Code: `guppi/materialize.py`, `guppi/ratified.py`, `guppi/bashguard.py`, `guppi/onward.py` (new), `guppi/cli.py`, `guppi/prespec.py`, `guppi/gate.py`; tests `test_ratified`, `test_bashguard`, `test_onward` (new), `test_prespec`, `test_gate`. The remote `origin` removed by the person.
- Not done (handoff): `make lint` red before the work; the auto mode classifier refused `git remote remove origin` twice (lesson L7); U+FFFD in `guppi context --prompt` on `UserPromptSubmit`, not investigated; `/work` has no words for taking up a conserved Spec; after the render the text of `rule-carry-over` still holds the defect of lesson L1 and defer 533 (Case 531.10).
- Yaml: `raw/2026-09-29/2024/materialize.yaml` 62 entries, 60 applied, 2 superseded by 531.11 (lines 19–20, Case 528.4); `raw/2026-09-30/0138/materialize.yaml` 7 entries and 2 of the synthesis, 9 applied. Both ledgers (62 and 7 lines) are held whole by their yaml.
- Pages: decisions 28 created, 17 updated, 6 archived (220, 243, 505, 509, 525, and 528.4 created and archived as superseded); rules 2 created (`rule-where-to-stop`, `rule-retro-onward`), 21 updated, 1 archived (`rule-github-issues`, deleted by 528.2); estimates 2 created, 1 renamed (`estimate-retro-report-holds-each-fact-once` → `estimate-retro-runs-on-to-the-handoff`), 23 updated, 1 archived (`estimate-github-issues-listed`); entities 2 updated (`entity-glossary`, `entity-sprint-migration`); lessons 2 created, 1 archived (`lesson-generate-replaced-a-ratified-criterion-on-a-field-update`); insights 2 updated.
- Synthesis: `lesson-carry-short-brief-drops-the-work-list` joined `insight-session-vault-knowledge-not-loaded` (child added, status `actioned` → `open`, severity 1, `addressed_by` 377.1 kept). `lesson-permissions-auto-mode-refuses-a-remote-change-despite-the-chat` stays `new`.
- Render wrote: `.claude/agents/librarian-guppi.md`, `.claude/settings.json`, the skills `handoff`, `hi`, `pre-spec`, `retro`, `work`, `vault/wiki/case-schema.md`, `vault/wiki/where-to-stop.md` (new). `sprint.md`, `backlog.md` (26 items) and `glossary.md` rewritten. `generate` ticked 78 boxes of `raw/2026-09-29/2024/spec.md` and 4 of `raw/2026-09-29/1753/spec.md`.
- Archive: `guppi archive` moved `raw/2026-09-29/0137`, `1134`, `1432`, `1753` and `2024` to `archive/migration/2026-09-29/<HHMM>/raw`; `raw/2026-09-30/0138`, the session of this run, stays.

## Readings due

No Estimate is `failed`. 46 are `pending`; each target stands `draft`.

- `estimate-agent-writing-followed` — `rule-agent-writing` — method: by hand in a later session, the person's messages of one session read for a complaint about the agent's text
- `estimate-ask-finds` — `rule-ask` — method: by hand in a later session, three dispatches of ask-guppi read against the event log
- `estimate-bash-guard` — `rule-bash-guard` — spec 2024: `uv run pytest tests/test_bashguard.py`, then the first refusal of a later session, its message read on stderr
- `estimate-brief-written` — `rule-brief` — spec 2024: by hand after the first librarian run on the new frame. This run: this brief was written under the frame loaded at the start of the run, Next session in two lists; the frame and `rule-brief` rendered in this run (case 531.10) name three lists; `generate` printed four Backlog moves and no dropped milestone, named in Flags; `handoff.md` of 0138 has no `## Ask the person` and no `## For the next session`
- `estimate-case-build-writes-a-plain-round` — `rule-case-build` — method: by hand in a session after the render, one first round and one later round of case-guppi read in the chat
- `estimate-case-build-writes-the-case` — `rule-case-build` — method: by hand, live dispatches in a session after the render
- `estimate-case-check-sends-back-a-faulty-case` — `rule-case-check` — method: `uv run pytest tests/test_casecheck.py -k subagent`, then by hand the first answer the hook sends back
- `estimate-case-check-shows-only-the-checked-case` — `rule-case-check` — method: `uv run pytest tests/test_casecheck.py -k stop`, then by hand the first reply the hook refuses
- `estimate-case-protocol-defers-in-one-reply` — `rule-case-protocol` — spec 2024: by hand, the first defer the person asks for after the render that leaves no line under `## Cases` of `frontier.md` open
- `estimate-case-protocol-ledger-line-form` — `rule-case-protocol` — method: by hand, the ledger and preview of the first session where a lesson and the Case that closes its cause stand together
- `estimate-case-protocol-shows-the-built-case` — `rule-case-protocol` — method: by hand, the Cases of a session at its close against the transcript
- `estimate-compact-recall-reloads` — `rule-compact-recall` — method: `pytest tests/test_recall.py`; live, the first compaction of a working session
- `estimate-documentation-completes` — `rule-documentation` — spec 2024: `make test-documentation`, then by hand on the librarian's run of a later session, from its transcript and `event_log.md`
- `estimate-end-of-work-order` — `rule-end-of-work` — method: `make test-end-of-work`, then by hand at the close of a later session
- `estimate-event-log-records` — `rule-event-log` — method: pytest in `tests/test_event.py` and `tests/test_gate.py`; by hand, one `/hi` outside plan mode and one in it
- `estimate-generate-renames` — `rule-page-generation` — method: pytest in `tests/test_generate.py`; the live reading by hand, the librarian's run on a real rename. This run: the entry of line 30 of `raw/2026-09-29/2024/materialize.yaml` (case 531.1) carries `rename: estimate-retro-runs-on-to-the-handoff` and was applied at 02:36:00; `estimates/estimate-retro-report-holds-each-fact-once.md` is gone from the live tree; the new page holds "renamed from `estimate-retro-report-holds-each-fact-once` · [[decision-case-531.1]]" in History; `rule-retro` holds "ref `estimate-retro-report-holds-each-fact-once` → `estimate-retro-runs-on-to-the-handoff` · [[decision-case-531.1]]"; outside `decisions/`, the old slug stands in `vault/wiki/` only in History lines of those two pages and in `log.md`
- `estimate-generate-rewords` — `rule-page-generation` — method: `pytest tests/test_generate.py`; the live reading, the librarian's run that applies the first reword. This run: no entry of either yaml carries `reword`
- `estimate-generate-writes` — `rule-page-generation` — method: pytest in `tests/test_generate.py`; the live reading once by hand
- `estimate-git-context-current` — `rule-git-context` — spec 2024: by hand at the /hi of a session after the render
- `estimate-glossary-terms-defined` — `entity-glossary` — spec 2024: by hand in a later session after the librarian's run, the table of `vault/wiki/glossary.md` against each `where` page, and `make lint`. This run: `guppi glossary` exit 0, no stderr; `glossary.md` holds 56 rows; its diff rewrites the rows Harness, `/hi` Frontier and Retro and removes the section `[[rule-skill-hi]]` with its row Issue; `make lint` prints no line on `entity-glossary`
- `estimate-governed-files-hook-refuses` — `rule-governed-files-hook` — method: `pytest tests/test_guard.py`, then by hand one refused Edit of a governed file
- `estimate-handoff-dispatches` — `rule-handoff` — spec 2024: by hand at the first run from `/work` to the librarian after the render
- `estimate-handoff-holds-each-fact-once` — `rule-handoff` — spec 2024: by hand at the first `/handoff` after the render
- `estimate-hi-no-read-calls` — `rule-skill-hi` — spec 2024: by hand at the /hi of a session after the render
- `estimate-hi-takes-its-readings` — `rule-skill-hi` — spec 2024: by hand at the first `/hi` after the render whose brief holds an Ask the person line
- `estimate-hi-writes-frontier` — `rule-skill-hi` — spec 2024: by hand at the `/hi` of a session after the render, and the frontier findings of `guppi prespec --check` in `tests/test_prespec.py`
- `estimate-permissions` — `rule-permissions` — method: the allow list of `.claude/settings.json` and `tests/test_render.py`; the live probe is the person's word on the client's prompt
- `estimate-plan-mode-verified` — `rule-plan-mode` — method: `make test-plan-mode`; one live reading by hand
- `estimate-prespec-checks-the-frontier` — `rule-prespec` — spec 2024: `uv run pytest tests/test_prespec.py`, in a session after this one
- `estimate-retro-commit-gates` — `rule-retro-commit` — spec 2024: `uv run pytest tests/test_gate.py`, in a session after this one
- `estimate-retro-loads` — `rule-retro` — spec 2024: by hand at the first run from `/work` to the librarian after the render
- `estimate-retro-onward-sends-the-agent-to-the-handoff` — `rule-retro-onward` — spec 2024: `uv run pytest tests/test_onward.py`, and by hand at the first run from `/work` to the librarian after the render
- `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note` — `rule-retro` — spec 2024: by hand at the first run after the render whose `work.md` names a check under `## Expected red`
- `estimate-retro-red-in-the-baseline-is-not-charged` — `rule-retro` — spec 2024: by hand at the first run after the render whose `work.md` Baseline holds a failing test or a lint finding line
- `estimate-retro-runs-on-to-the-handoff` — `rule-retro` — spec 2024: by hand at the first run from `/work` to the librarian after the render
- `estimate-session-phases-in-order` — `rule-session` — method: by hand at the close of a session, the marks of each phase read in order
- `estimate-session-start-context` — `rule-session-start` — method: `make test-session-start`; by hand, one session opened without `/hi`
- `estimate-skill-grill-me-asks-in-rounds` — `rule-skill-grill-me` — method: `uv run guppi render --check`; by hand, one round read in the chat in a session after the render
- `estimate-skill-wait-what-re-pitches` — `rule-skill-wait-what` — method: `uv run guppi render --check`; by hand, one run of the skill read in the chat
- `estimate-spec-write-reaches-the-approved-spec` — `rule-spec-write` — method: `uv run pytest tests/test_ratified.py -k approved_spec`; by hand, the first Case ratified in Work Mode after the change
- `estimate-sprint-migration-leftovers-gone` — `entity-sprint-migration` — spec 2024: by hand on the tree at the close of the sprint
- `estimate-sprint-migration-lint-clean` — `entity-sprint-migration` — method: `make lint`, exit 0, or only unread lines on the Estimates of `entity-sprint-migration`
- `estimate-sprint-migration-merges` — `entity-sprint-migration` — method: `make test` on the last commit of `migration`, then git log of `main` after the merge
- `estimate-where-to-stop-stops-only-on-its-conditions` — `rule-where-to-stop` — spec 2024: by hand at the first run from `/work` to the librarian after the render
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — `rule-work-mode` — method: `uv run guppi render --check`; by hand, the first `/work` after the render at the fork and the first the person types
- `estimate-work-mode-takes-the-work-readings` — `rule-work-mode` — spec 2024: by hand at the first run from `/work` to the librarian after the render

## Flags

- incomplete: `rule-where-to-stop` (line 39 of the 2024 yaml, case 531.7) written without `parent`.
- incomplete: `estimate-hi-writes-frontier` (line 20 of the 2024 yaml, case 528.4) lacks `criterion`; the entry is superseded by 531.11 and not applied.
- near: `lesson-carry-short-brief-drops-the-work-list` near `lesson-defer-to-a-milestone-leaves-the-sprint-page-silent`.
- near: `lesson-permissions-auto-mode-refuses-a-remote-change-despite-the-chat` near `lesson-plan-mode-agent-and-sendmessage-pass-the-auto-mode-classifier`.
- failed, unparsed: none. Failed Estimates: none.
- Moved to the Backlog by `generate`, from the milestone Slice 5 — closing of `entity-sprint-migration`, each passed over in 3 sessions in a row, 0138, 2024 and 1753: `estimate-sprint-migration-lint-clean`, `estimate-sprint-migration-merges`, `rule-spec-box`, `rule-morph`. No milestone dropped.
- `handoff.md` says the Slice 5 items stay on the sprint page; `generate` moved the four above to the Backlog in this run.
- Stale defers (lint): `rule-subagent-guppi` deferred 31 times since case 29; `rule-case-build-checks-its-sub-cases` (480), `rule-complaint-becomes-a-lesson` (504), `rule-morph` (239), `rule-orchestration` (424), `rule-prespec-script-skips-code-spans` (481) once each.
- Contradiction: this brief follows the frame loaded at the start of the run, Next session in two lists; the frame, `rule-brief` and `estimate-brief-written` as this run rendered and wrote them name three lists, with `Ask the person` (case 531.10).
- `make lint`: 87 finding lines, make exit 2 —
  - `rules/rule-spec-box`: schema: missing field kind; schema: missing field estimates; orphan: no other live page names it in its frontmatter
  - `decisions/decision-case-1` … `decision-case-28`: schema: missing section ## Problem, 31 pages
  - `decisions/decision-case-13`: fence: ## When: a code fence open at the end of the section
  - deferred: the six lines above
  - unread: pending, 46 lines, one per `pending` Estimate of Readings due

## Next session

Cases
- The `/carry` of session 2024 dropped the Work list; the person wants the loss kept in view: defer 533 on `rule-carry-over`, and Case 531.10 keeps the short brief without Next session (handoff, lesson L1).
- `/work` names only the session's own `spec.md` and has no words for taking up a conserved Spec (handoff, What is not done).
- `guppi context --prompt` on `UserPromptSubmit` delivers U+FFFD in place of the dash after "400 000", its `Stop` line keeps it; a deferred bug, not investigated (handoff; reading L4).
- The sprint: the handoff keeps the Slice 5 items on the sprint page; `generate` moved `estimate-sprint-migration-lint-clean`, `estimate-sprint-migration-merges`, `rule-spec-box` and `rule-morph` to the Backlog (Flags).
- The brief of this run holds two lists in Next session; the rendered frame and `rule-brief` hold three (Flags).

Work
- The 46 `pending` readings of Readings due, by slug; the 21 unticked read boxes of the spec of 2024 and the unticked read boxes of the specs of 1753 (4), 1432 (3), 1134 (1) and 0137 (6), now under `archive/migration/2026-09-29/`, name Estimates of that list.
- Ledger lines 19–20 of the ledger of 2024 (case 528.4): not applied, superseded by 531.11.

## Readings at the close

- `make test`: 934 passed, 2 skipped.
- `make lint`: 87 finding lines, exit 2.
- Pages: rules 74, entities 4, estimates 160, decisions 823, lessons 69, insights 26.
