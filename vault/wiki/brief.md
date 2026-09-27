# Brief — 2026-09-27, the librarian's run over session 2050 of 2026-09-27

## Where things stand

- Session 2050 ratified Cases 464, 465, 466.1, 466.2, 467.1, 467.2, 467.3, 468.1, 468.2 and 469 (a short defer of `rule-page-generation`, written at Retro). Frontier C1 and C2 (Slice 3g) `[-] · sprint · defer` again (handoff).
- Code, commit 31d86d5: `guppi/generate.py` (`clear_deferred_by` clears only the pages the superseding Case names; docstring), `guppi/prespec.py` (`deferred_pages`, `decided_on_its_page`, `check_backlog_line`, called from `check_frontier`), `guppi/casecheck.py` (`open_backlog_lines`, `check_backlog`, called from `check_answer` with the session's `frontier.md`); tests in `test_generate`, `test_prespec`, `test_casecheck`. The session's `make test` gave 844 passed, 2 skipped; `make style` clean (handoff).
- Readings of the session: 17, 16 `passed` and 1 `failed` (`estimate-documentation-completes`). One lesson, `lesson-test-an-absence-assert-writes-the-banned-phrase-into-the-tree` (handoff).
- Not done in the session: the re-supersede of an archived Decision brings it back from the archive, deferred as Case 469. Readings that were not readable in the session: six need a live case or a transcript, two wait for their occasion, three wait for the close of the sprint, and three are read by their method in the next session (handoff).
- The walk named `raw/2026-09-27/1255/` and `raw/2026-09-27/1819/` (each extended with 0 entries; `generate` 0 pages each), and `raw/2026-09-27/2050/` (written with 36 entries from the 36 lines of its ledger).
- Yaml of 2050: 36 entries: 14 `update` (lines 1–8, 10, 12–15, 17), 3 `create` (lines 9, 11, 16, all Estimates), 17 `estimate`, 1 `defer` (line 32, `exists`), 1 `lesson` (line 33). All 36 are `applied`. The librarian added no entry. No `near`, no `merged`, no `failed`, no `incomplete`, `unparsed: []`.
- Pages (`generate`: 52 pages written or changed; `cleanup`: 0 pages moved):
  - decisions: 10 created (464, 465, 466.1, 466.2, 467.1, 467.2, 467.3, 468.1, 468.2, 469).
  - estimates: 3 created, `pending`: `estimate-prespec-requires-a-backlog-item-decided-on-its-page` (467.1), `estimate-case-check-requires-a-backlog-item-decided-on-its-page` (467.2), `estimate-handoff-holds-each-fact-once` (468.2). 6 updated by Cases, all `pending`: `estimate-sprint-migration-file-route-gone` (464), `estimate-carry-over-writes` (465), `estimate-case-build-writes-the-case` (466.1), `estimate-case-protocol-shows-the-built-case` (466.2), `estimate-generate-writes-the-decision-page` (467.3), `estimate-retro-report-holds-each-fact-once` (468.1). 17 updated by readings: 16 `passed`, 1 `failed`.
  - rules: 7 updated by Cases: `rule-case-build` (466.1), `rule-case-protocol` (466.2, 467.1), `rule-prespec` (467.1), `rule-case-check` (467.2), `rule-backlog` (467.3), `rule-retro` (468.1), `rule-handoff` (468.2). `rule-page-generation` deferred by 469 (`deferred_by: [[decision-case-469]]`). Cascade draft → built: `rule-brief`, `rule-harness`, `rule-ledger-write`, `rule-lint`, `rule-materialize`, `rule-sprint`, `rule-synthesis`. Cascade built → draft: `rule-handoff`.
  - lessons: 1 created, `new`: `lesson-test-an-absence-assert-writes-the-banned-phrase-into-the-tree`.
  - insights: none created or updated.
- Governed files `render` rewrote: `.claude/agents/case-guppi.md`, `.claude/skills/handoff/SKILL.md`, `.claude/skills/pre-spec/SKILL.md`, `.claude/skills/retro/SKILL.md`, `vault/wiki/case-schema.md`. `guppi sprint` rewrote `vault/wiki/sprint.md` with two changes. "No Rule-class file at the close of Slice 3f" went `pending` → `passed`. "The file route is out of the scripts" went `passed` → `pending`, because 464 replaced its Criterion. `guppi backlog` rewrote `vault/wiki/backlog.md`: 16 → 17 items (`rule-page-generation` added, put off in 0 sessions). `guppi glossary` left `vault/wiki/glossary.md` unchanged.
- `generate` ticked 24 lines of `raw/2026-09-27/2050/spec.md`, 7 of `raw/2026-09-27/1819/spec.md` and 5 of `raw/2026-09-27/1255/spec.md`.

## Readings due

24 Estimates stand `pending` or `failed` after `generate`: 1 `failed`, 23 `pending`. Every rule or entity they read stands `draft`.

- `estimate-documentation-completes` — `failed` — `rule-documentation` draft — `make test-documentation`; the live reading by hand (method). Result: the librarian's run over 1819 grepped `vault/archive/` and read a file under `~/.claude/projects/` (handoff).
- `estimate-sprint-migration-file-route-gone` — `entity-sprint-migration` draft — `raw/2026-09-27/2050/spec.md` line 53.
- `estimate-case-build-writes-the-case` — `rule-case-build` draft — `raw/2026-09-27/2050/spec.md` line 154.
- `estimate-case-protocol-shows-the-built-case` — `rule-case-protocol` draft — `raw/2026-09-27/2050/spec.md` line 201.
- `estimate-prespec-requires-a-backlog-item-decided-on-its-page` — `rule-prespec` draft — `raw/2026-09-27/2050/spec.md` line 281.
- `estimate-case-check-requires-a-backlog-item-decided-on-its-page` — `rule-case-check` draft — `raw/2026-09-27/2050/spec.md` line 329.
- `estimate-generate-writes-the-decision-page` — `rule-page-generation` draft — `raw/2026-09-27/2050/spec.md` line 382.
- `estimate-retro-report-holds-each-fact-once` — `rule-retro` draft — `raw/2026-09-27/2050/spec.md` line 440.
- `estimate-handoff-holds-each-fact-once` — `rule-handoff` draft — `raw/2026-09-27/2050/spec.md` line 490.
- `estimate-agent-writing-followed` — `rule-agent-writing` draft — by hand in a later session, the person's messages of one session read for a complaint about the agent's text (method).
- `estimate-carry-over-writes` — `rule-carry-over` draft — `uv run guppi render --check`; by hand, the first `/carry` after the fork of ExitPlanMode (method).
- `estimate-case-check-sends-back-a-faulty-case` — `rule-case-check` draft — `uv run pytest tests/test_casecheck.py -k subagent`, then by hand (method).
- `estimate-case-check-shows-only-the-checked-case` — `rule-case-check` draft — `uv run pytest tests/test_casecheck.py -k stop`, then by hand (method).
- `estimate-case-protocol-defers-in-one-reply` — `rule-case-protocol` draft — by hand, the first defer the person asks for after the render (method).
- `estimate-case-protocol-ledger-line-form` — `rule-case-protocol` draft — by hand, the ledger and the preview of the first session where a lesson and the Case that closes its cause stand together (method).
- `estimate-context-size-warns-past-the-limit` — `rule-context-size` draft — `uv run pytest tests/test_context.py -k limit`; by hand at the first prompt past 400 000 tokens (method).
- `estimate-event-log-records` — `rule-event-log` draft — pytest in `tests/test_event.py` and `tests/test_gate.py`; readings by hand (method).
- `estimate-language-followed` — `rule-language` draft — by hand in the next session (method).
- `estimate-session-phases-in-order` — `rule-session` draft — by hand at the close of a session, the day's records in order (method).
- `estimate-skill-grill-me-asks-in-rounds` — `rule-skill-grill-me` draft — `uv run guppi render --check`; by hand, one `/grill-me` of the person after the render (method).
- `estimate-spec-write-reaches-the-approved-spec` — `rule-spec-write` draft — `uv run pytest tests/test_ratified.py -k approved_spec`; by hand, the first Case ratified in Work Mode after the change (method).
- `estimate-sprint-migration-leftovers-gone` — `entity-sprint-migration` draft — by hand, the tree at the close of the sprint (method).
- `estimate-sprint-migration-lint-clean` — `entity-sprint-migration` draft — `make lint` exit 0, or only unread lines on the Estimates of the sprint (method).
- `estimate-sprint-migration-merges` — `entity-sprint-migration` draft — `make test` on the last commit of migration, then `git log` of main after the merge (method).

## Flags

- `incomplete`, `failed`, `near`, `merged`, `unparsed`: none in the yamls of 1255, 1819 and 2050.
- `exists`: line 32 (Case 469, `defer` of `rule-page-generation`); the page stood, no page written; the defer applied.
- Synthesis: `lesson-test-an-absence-assert-writes-the-banned-phrase-into-the-tree` has no pair among the lessons and the Insights and stays `new`.
- Failed Estimates: 1, listed first under Readings due.
- Handoff: Case 467 took seven rounds. The person twice asked to have the gaps explained ("не понял, объясни"). The handoff reads this as a complaint about the clarity of case-guppi's round, relevant to `estimate-agent-writing-followed` and to Case 466.
- Handoff: the rounds of case-guppi strayed from the grill-me text twice. In 465, Q2 and Q3 assumed the answer to Q1. The fourth round of 467 opened with a Q1 marked "No answer needed".
- Handoff: 467.3 has no decision line on `rule-page-generation`. Its mechanism lives in the docstring of `guppi/generate.py`, and the person accepted this.
- Handoff: the ledger holds each decision line of 466–468 once although they were ratified twice (after pre-spec).
- Handoff: `rule-case-protocol` is updated by 466.2 and 467.1, each `replace` anchor in a different paragraph; both applied.
- Contradictions: none found in this run. The contradiction on `estimate-sprint-migration-file-route-gone` in the previous brief was the subject of Case 464, which replaced the Criterion whole.
- MOC candidates: none named by lint.
- Stale defers, from lint: `rule-work-mode` deferred 32 times since case 29; `rule-subagent-guppi` 31 times since case 29; `rule-morph` once since case 239; `rule-orchestration` once since case 424.
- Backlog moves by `generate`: none printed. Milestones dropped: none printed.
- `materialize`, `generate`, `cleanup`, `render`, `sprint`, `backlog`, `glossary`: no stderr lines.
- `archive` (run after the brief): exit 0, no stdout and no stderr line; it moved no unit. `raw/2026-09-27/1255/`, `1819/` and `2050/` are dated the day of the run, and `archive` looks only at units dated before it; 2050 is the session of the run.
- `make lint`, after the render: exit 2, 94 findings.
  - `decisions/decision-case-N: schema: missing section ## Context` and `## Problem` on 31 pages (cases 1–28). That is 62 findings.
  - `rules/rule-spec-box: schema: missing field kind`, `missing field estimates`, and `orphan: no other live page names it in its frontmatter`.
  - `rules/rule-morph: deferred: 1 time since case 239`; `rules/rule-orchestration: deferred: 1 time since case 424`; `rules/rule-subagent-guppi: deferred: 31 times since case 29`; `rules/rule-work-mode: deferred: 32 times since case 29`.
  - `unread: pending` on 23 Estimates and `unread: failed` on 1. These are the 24 Estimates of Readings due.
  - `estimates: unmigrated: 19 pages in the shape before case 193`.

## Next session

Cases:
- `estimate-documentation-completes` failed: the librarian's run over 1819 grepped `vault/archive/` and read a file under `~/.claude/projects/`. The handoff calls it a defect of the librarian run, for the next session (handoff).
- `estimate-skill-grill-me-asks-in-rounds` is read only on the person's own `/grill-me`, and case-guppi's rounds do not count, so its reading may never come. The handoff raises this as a question for a later Plan Mode (handoff).

Work:
- `estimate-sprint-migration-file-route-gone`
- `estimate-case-build-writes-the-case`
- `estimate-case-protocol-shows-the-built-case`
- `estimate-prespec-requires-a-backlog-item-decided-on-its-page`
- `estimate-case-check-requires-a-backlog-item-decided-on-its-page`
- `estimate-generate-writes-the-decision-page`
- `estimate-retro-report-holds-each-fact-once`
- `estimate-handoff-holds-each-fact-once`
- `estimate-agent-writing-followed`
- `estimate-carry-over-writes`
- `estimate-case-check-sends-back-a-faulty-case`
- `estimate-case-check-shows-only-the-checked-case`
- `estimate-case-protocol-defers-in-one-reply`
- `estimate-case-protocol-ledger-line-form`
- `estimate-context-size-warns-past-the-limit`
- `estimate-event-log-records`
- `estimate-language-followed`
- `estimate-session-phases-in-order`
- `estimate-skill-grill-me-asks-in-rounds`
- `estimate-spec-write-reaches-the-approved-spec`
- `estimate-sprint-migration-leftovers-gone`
- `estimate-sprint-migration-lint-clean`
- `estimate-sprint-migration-merges`
- The unticked boxes of the Specs, all `read` lines: `raw/2026-09-27/2050/spec.md` lines 53, 154, 201, 281, 329, 382, 440, 490; `raw/2026-09-27/1819/spec.md` lines 104, 396; `raw/2026-09-27/1255/spec.md` lines 110, 595, 895, 944, 1065, 1117.
- Ledger lines not applied: none; each of the 36 lines of `raw/2026-09-27/2050/ledger.md` has an applied entry.
- Dirty tree: none after the librarian's commit.

## Readings at the close

- `make test`: 844 passed, 2 skipped.
- `make lint`: exit 2, 94 findings (listed under Flags).
- Pages in `vault/wiki/`: decisions 676, estimates 145, rules 68, lessons 62, insights 25, entities 4.
