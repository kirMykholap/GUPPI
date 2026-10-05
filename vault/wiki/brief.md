# Brief — 2026-10-05, after the librarian run of session 2103

## Where things stand

- Session 2103 ratified Cases 672, 673 and 674 (674.1, 674.2, 674.3); all three were built again on the findings of pre-spec and ratified again with the same ledger lines.
- Code: `guppi/generate.py` (`closes_by_decision`, used by `Vault.tick`; the docstrings of the module, `Vault.tick` and `tick_read`). Tests: `tests/test_generate.py`, 8 new. Handoff: `make test` 1266 passed, 6 skipped; `make style` clean.
- By hand in Work Mode (case 672): the eleven open `read` lines of the Estimates that 669.1–669.15 set `passed` were ticked in the 0311 Spec (5) and the 1616 Spec (6).
- Readings: L1–L7 at `/hi`, L20–L22 at Retro, all 10 passed. Lesson: L23.
- The yaml: 23 entries from the ledger (L1–L23) and 2 added by the synthesis; all 25 carry `applied`; 0 `failed`, 0 `incomplete`, 0 `near`, 0 `merged`; 1 `exists` (L19, the `defer` of `rule-prespec-judges-the-spec-whole`, page on disk); `unparsed: []`.
- Pages created: decisions 6 (672, 673, 674, 674.1, 674.2, 674.3); lessons 1 (`lesson-orchestration-a-ratified-render-change-claimed-live-before-the-render`, then set `clustered` by the synthesis).
- Pages updated: estimates 11 (10 readings set `passed`: L1–L7, L20–L22; Criteria replaced by 672 on `estimate-generate-ticks-the-spec`, by 674.1 on `estimate-prespec-reconciles`, by 674.2 on `estimate-orchestration-shows-the-built-case`; the method of `estimate-case-build-checks-the-finished-case` by 674.1); rules 10 (5 by decisions: `rule-page-generation`, `rule-orchestration` (672, 673, 674.2, in ledger order), `rule-prespec`, `rule-ask`, `rule-prespec-judges-the-spec-whole`; 5 by the cascade alone, `draft → built`: `rule-case-check`, `rule-handoff`, `rule-ledger-write`, `rule-prespec-hook`, `rule-retro`); insights 1 (`insight-workflow-fact-signed-from-a-check-that-does-not-cover-it`, a child added, severity 1 → 2); decisions 1 (`decision-case-643` set superseded by 674.3, then archived).
- `rule-prespec-judges-the-spec-whole`: `deferred_by` now `[[decision-case-674.3]]` (was 643), purpose rewritten; it stays in `backlog.md` with its new purpose.
- `generate` wrote `superseded_by: '674.3'` into the 0109 yaml. The scripts ticked 15 boxes of the 2103 Spec by `generate` and 5 render boxes by `render` (the 20 the handoff counted), and 6 `read` lines of the 1831 Spec.
- The render wrote `.claude/skills/pre-spec/SKILL.md`, `.claude/agents/ask-guppi.md` and `vault/wiki/orchestration.md`. `guppi sprint` and `guppi glossary` left `sprint.md` and `glossary.md` unchanged; `guppi backlog` rewrote 2 lines of `backlog.md` (23 items). `cleanup: 1 page(s) moved` (`decision-case-643`, to `vault/archive/migration/2026-10-05/2103/decisions/`). No script printed a line on stderr.
- `guppi archive` exit 0, printed nothing on stdout or stderr and moved no unit; the six units with a ledger (0109, 0311, 1343, 1616, 1831, 2103) are dated 2026-10-05, the day of the run.

Synthesis. `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 80 lines; `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 32 lines.
- `lesson-orchestration-a-ratified-render-change-claimed-live-before-the-render` — joined `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it` (open, `addressed_by: decision-case-636` kept): the agent stated the harness behaviour from the Case text while the skill file it would run was one read away.

## Readings due

Pending:
- `estimate-hi-writes-frontier` — pending — `rule-skill-hi` stands `draft` — read: by hand at the `/hi` of the session after the close of a sprint; unit: the frontier findings of `guppi prespec --check` in `tests/test_prespec.py` (method).
- `estimate-hi-takes-a-conserved-spec` — pending — `rule-skill-hi` stands `draft` — read: `uv run guppi render --check`; by hand, a session that takes a conserved Spec, and the `/hi` of the session after the close of a sprint (method).
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — pending — `rule-work-mode` stands `draft` — read: `uv run guppi render --check`; by hand, a `/work` at the fork, one that `/box` calls and the `/work` of a session that closes a sprint (method).
- `estimate-brief-written` — pending — `rule-brief` stands `draft` — read: by hand at the `/hi` after the librarian's run of the session that closes a sprint (method). This run: no unticked line of the 2103 Spec holds `guppi sprint-close`; none ran.
- `estimate-backlog-renders` — pending — `rule-backlog` stands `draft` — read: `uv run pytest tests/test_backlog.py`, plus `vault/wiki/backlog.md` after the librarian's run of the session that closes a sprint (method). This run: `guppi backlog` exit 0, no stderr, `backlog.md` rewritten (2 lines), 23 items; no sprint closed.
- `estimate-sprint-close-runs-in-the-librarian-run` — pending — `rule-sprint-close` stands `draft` — read: pytest `tests/test_sprint_close.py -k tick`; by hand after the librarian's run of the session that closes a sprint (method). This run: no `guppi sprint-close` line in the 2103 Spec, none run; `vault/archive/` received 1 page from `cleanup` under `migration/2026-10-05/2103/`.
- `estimate-sprint-close-next-session-opens-the-sprint` — pending — `rule-sprint-close` stands `draft` — read: pytest `tests/test_ledger.py -k sprint` and `tests/test_materialize.py -k sprint`; by hand at the librarian's run of the session after the close of a sprint (method). This run: the yaml's `sprint` is `migration`; `guppi sprint` exit 0, no stderr, `sprint.md` unchanged.
- `estimate-sprint-close-takes-the-readings-in-groups` — pending — `rule-sprint-close` stands `draft` — read: by hand after the Work Mode of the session that closes a sprint (method).
- `estimate-sprint-migration-leftovers-gone` — pending — `entity-sprint-migration` stands `draft` — read: by hand in the Work Mode of the session that closes the sprint, before the librarian's run (method).
- `estimate-sprint-migration-lint-clean` — pending — `entity-sprint-migration` stands `draft` — read: `make lint` in the Work Mode of the session that closes the sprint, before the librarian's run (method). This run: `make lint` 15 lines — 4 `deferred`, 11 `unread`.
- `estimate-sprint-migration-merges` — pending — `entity-sprint-migration` stands `draft` — read: `make test` on the last commit of migration, in the Work Mode of the session that closes it (method). This run: `make test` 1266 passed, 6 skipped, on the working tree of this run.

No Estimate stands `failed`.

## Flags

- No entry marked `incomplete`, `failed`, `near` or `unparsed`.
- Failed Estimates: none.
- Handoff, Notes: at pre-spec the person left a finding on Case 672 as it stands — Retro counts as debt a `read` line of an earlier Case of the session that a later `update` closes by decision, and the librarian's run then ticks it; the same gap stands for a `delete`.
- Handoff, Observations: the `/pre-spec` of session 2103 still sent one `ask-guppi` per top-level Case, three runs; the skill and the agent file of 674.1 were rendered only by this run.
- Handoff, Observations: `make lint` was red before the work, exit 2, 4 `deferred` and 18 `unread` lines.
- One `- [ ] read` box stays open in the 1831 Spec: `estimate-hi-writes-frontier` (line 1004), pending.
- Stale defers, from the lint: `rule-subagent-guppi` deferred 31 times since case 29; `rule-prespec-judges-the-spec-whole` 2 times since case 643; `rule-complaint-becomes-a-lesson` (since case 504) and `rule-morph` (since case 239) 1 time each.
- MOC candidates: none found. Contradictions: none found.
- The lint: 15 lines — 4 `deferred`, 11 `unread` (11 pending); no other finding; `make lint` exits red (exit 2).
- Reads beyond the frame: none.

## Next session

Cases:
- `rule-sprint-close` and the close of migration stay for the session that closes the sprint; every pending Estimate left waits for that session or the one after it (handoff, For the next session).
- Whether the one `ask-guppi` run at pre-spec needs help on a large Spec, and whether it asks what the Cases leave open together, stands in `rule-prespec-judges-the-spec-whole`; measuring the cost of a run is one way to decide it (handoff, For the next session).

Work:
- `estimate-hi-writes-frontier` (its `- [ ] read` box in the 1831 Spec)
- `estimate-hi-takes-a-conserved-spec`
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`
- `estimate-brief-written`
- `estimate-backlog-renders`
- `estimate-sprint-close-runs-in-the-librarian-run`
- `estimate-sprint-close-next-session-opens-the-sprint`
- `estimate-sprint-close-takes-the-readings-in-groups`
- `estimate-sprint-migration-leftovers-gone`
- `estimate-sprint-migration-lint-clean`
- `estimate-sprint-migration-merges`
- Ledger lines this run did not apply: none; the ledger holds 23 lines and the yaml an entry for each.

Ask the person:
- none

## Readings at the close

- `make test`: 1266 passed, 6 skipped.
- `make lint`: 15 lines — 4 `deferred`, 11 `unread`; red.
- Pages: decisions 1169, estimates 223, rules 78, lessons 81, insights 31, entities 4; `vault/archive/` 864 pages.
