# Brief — 2026-10-04, session 2041: Slice 5 — the findings on Cases 627–629, the answer of ask-guppi, and how /pre-spec checks a Spec

## Where things stand

- Cases ratified in session 2041: 632 (632.1–632.10), 633 (633.1, 633.2), 634 (634.1–634.3). Cases 632 and 634 were built again on the findings of `/pre-spec` and ratified again; the Spec holds the second answer.
- Code: the docstring of `guppi/cleanup.py` (632.1). No test changed. `make test` at the close of the work: 1166 passed, 6 skipped; `make style` clean (handoff).
- Readings at `/hi`: L1–L6 passed (`estimate-sprint-close-archives-the-decisions`, `estimate-sprint-close-archives-done-insights-and-lone-lessons`, `estimate-sprint-close-archives-the-sprint-page-and-keeps-the-rest`, `estimate-sprint-close-settles-unread-estimates`, `estimate-sprint-ticks-the-spec`, `estimate-generate-writes`); L7 failed (`estimate-handoff-holds-each-fact-once`). Work reading L37 passed (`estimate-case-check-sends-back-a-faulty-round`). One lesson, L38.
- This librarian run, one yaml applied: `vault/raw/2026-10-04/2041/materialize.yaml`, 38 entries from 38 ledger lines, 2 synthesis entries, 18 decision blocks; 58 marked `applied`, none `failed`, `exists`, `incomplete`. `guppi generate`: 53 pages written or changed for 2041; 0 for 0004, 0112, 1439, 1934 (applied earlier).
  - decisions: 18 created (632, 632.1–632.10, 633, 633.1, 633.2, 634, 634.1–634.3).
  - rules: 10 changed — 8 by 14 entries (`rule-ask` 4, `rule-orchestration` 3, `rule-prespec` 2, `rule-sprint-close`, `rule-cleanup`, `rule-documentation`, `rule-sprint`, `rule-skill-hi` 1 each; `rule-ask` and `rule-prespec` also took an `estimates` link each from the 2 creates); `rule-insights-schema` and `rule-page-generation` by the cascade alone. Cascade: `rule-insights-schema`, `rule-orchestration`, `rule-prespec` to `draft`; `rule-page-generation`, `rule-sprint` to `built`.
  - estimates: 2 created (`estimate-ask-searches-at-prespec`, `estimate-prespec-confirms-the-findings-once`); 19 updated — 8 readings applied (7 passed, 1 failed), 11 by decision entries.
  - entities: 2 updated (`entity-sprint`, `entity-sprint-migration`, 632.3).
  - lessons: 1 created, then clustered. insights: 1 updated (synthesis).
- Spec ticks: this run ticked 41 lines of `vault/raw/2026-10-04/2041/spec.md` (11 `- [ ] read` lines stay open), 1 `read` line of `vault/raw/2026-10-04/0112/spec.md` and 6 `read` lines of `vault/raw/2026-10-04/1439/spec.md`.
- Renders: `.claude/agents/ask-guppi.md`, `.claude/agents/librarian-guppi.md`, `.claude/skills/hi/SKILL.md`, `.claude/skills/pre-spec/SKILL.md`, `vault/wiki/orchestration.md`; `vault/wiki/sprint.md` and `vault/wiki/backlog.md` (20 items) rewritten.
- Synthesis: the Grep `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 77 lines; the Grep `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 31 lines.
  - `lesson-case-build-a-grep-cited-for-files-it-did-not-print` joined `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it` (open, `addressed_by` decision-case-544.1 kept); its 11th child.
- Index check: the yaml holds no `create` outside estimates; the lesson entry was compared by the two Greps above. No entry merged, none `near`.
- No `guppi sprint-close` line in the session's `spec.md`; no sprint closed. `entity-sprint-migration` stays live.

## Readings due

- `estimate-handoff-holds-each-fact-once` — failed — `rule-handoff` (draft) — at the `/hi` of a later session, a `handoff.md` written by the rendered skill read against the close of its Retro. Result: the 1934 handoff holds the heading and seven sections in order, but Debt gives 30 Estimates in two lines grouped by moment, not one line per Estimate.
- `estimate-sprint-migration-lint-clean` — pending — `entity-sprint-migration` (draft) — spec.md L274; method: `make lint` in the Work Mode of the session that closes the sprint, before the librarian's run. This run: `make lint` printed 35 finding lines, 4 `deferred` and 31 `unread`, exit 2.
- `estimate-sprint-close-next-session-opens-the-sprint` — pending — `rule-sprint-close` (draft) — spec.md L313; method: pytest `-k sprint` of `tests/test_ledger.py` and `tests/test_materialize.py`; by hand at the librarian's run of the session after the close of a sprint. This run: the yaml carries `sprint: migration`; `guppi sprint` exit 0, no stderr; `entity-sprint-migration` live.
- `estimate-hi-writes-frontier` — pending — `rule-skill-hi` (draft) — spec.md L357; method: by hand at the `/hi` of the session after the close of a sprint.
- `estimate-hi-takes-a-conserved-spec` — pending — `rule-skill-hi` (draft) — spec.md L397; method: `uv run guppi render --check`; a session that takes a conserved Spec, and the `/hi` of the session after the close of a sprint.
- `estimate-insights-schema-checked` — pending — `rule-insights-schema` (draft) — spec.md L458; method: `pytest tests/test_schemas.py -k insights`; the live reading `make lint`.
- `estimate-orchestration-asks-in-the-grill-me-shape` — pending — `rule-orchestration` (draft) — spec.md L505; method: by hand at the close of a later session, each question of the main agent's own.
- `estimate-ask-finds` — pending — `rule-ask` (draft) — spec.md L593; method: by hand at the `/hi` of a later session, the answer of ask-guppi at a `/pre-spec` after the render by case 633.1.
- `estimate-ask-searches-at-prespec` — pending — `rule-ask` (draft) — spec.md L640; method: by hand at the `/hi` of a later session, the calls of ask-guppi at a `/pre-spec` after the render by case 633.2.
- `estimate-prespec-reconciles` — pending — `rule-prespec` (draft) — spec.md L778; method: one reading by hand of a `/pre-spec`.
- `estimate-prespec-confirms-the-findings-once` — pending — `rule-prespec` (draft) — spec.md L847; method: by hand at the `/pre-spec` of a later session whose findings send a Case back, after the render by case 634.2.
- `estimate-orchestration-shows-the-built-case` — pending — `rule-orchestration` (draft) — spec.md L895; method: by hand, the Cases of a session at its close against the transcript.
- `estimate-ask-query-before-a-create` — pending — `rule-ask` (draft) — method: by hand at the `/hi` of a later session, a case-guppi that built a Case with a `create` without a `ref`.
- `estimate-backlog-renders` — pending — `rule-backlog` (draft) — method: `uv run pytest tests/test_backlog.py`, and `vault/wiki/backlog.md` after the librarian's run of the session that closes a sprint. This run: `guppi backlog` exit 0, no stderr; `backlog.md` heads `20 items`.
- `estimate-brief-written` — pending — `rule-brief` (draft) — method: by hand at the `/hi` after the librarian's run of the session that closes a sprint.
- `estimate-case-build-checks-the-finished-case` — pending — `rule-case-build` (draft) — method: by hand at `/pre-spec` of a later session after the render, the answers of the ask-guppi runs, one per top-level Case.
- `estimate-case-build-writes-the-case` — pending — `rule-case-build` (draft) — method: by hand, live dispatches after the render — a fork, a `create` without a `ref`, a change of a hook, a change on one sub-case.
- `estimate-case-check-judges-a-lone-sub-case-with-its-stored-parent` — pending — `rule-case-check` (draft) — method: `pytest tests/test_casecheck.py -k lone`; by hand a live answer of sub-cases alone.
- `estimate-case-check-requires-each-question-of-the-rounds` — pending — `rule-case-check` (draft) — method: `pytest tests/test_casecheck.py -k rounds`; by hand a Case the hook sends back for a missing title.
- `estimate-case-check-sends-back-a-case-number-held-by-another-agent` — pending — `rule-case-check` (draft) — method: `uv run pytest tests/test_casecheck.py -k subagent_clash`; by hand a send-back for this reason.
- `estimate-case-check-sends-back-a-clash-with-another-case` — pending — `rule-case-check` (draft) — method: `pytest tests/test_casecheck.py -k session_clash`; by hand a live send-back for a clash with another Case.
- `estimate-case-check-sends-back-a-ratified-case-in-another-shape` — pending — `rule-case-check` (draft) — method: `pytest tests/test_casecheck.py -k shape`; by hand a send-back for this reason.
- `estimate-lint-runs-every-step` — pending — `rule-lint` (draft) — method: by hand, the `make lint` of the Baseline of a later `/work` whose backlog step is red.
- `estimate-session-start-context` — pending — `rule-session-start` (draft) — method: `make test-session-start`; by hand a session opened without `/hi` whose reply carries a LEDGER block.
- `estimate-spec-write-reaches-the-approved-spec` — pending — `rule-spec-write` (draft) — method: `pytest tests/test_ratified.py -k approved_spec`; by hand a Case ratified in Work Mode.
- `estimate-sprint-close-runs-in-the-librarian-run` — pending — `rule-sprint-close` (draft) — method: `pytest tests/test_sprint_close.py -k tick`; by hand after the librarian's run of the session that closes a sprint, its ledger, spec.md, handoff.md, event log, report and `vault/archive/`. This run: the session's `spec.md` holds no unticked task line with `guppi sprint-close` and `--apply`; no close ran. `guppi archive`: no stdout line, no stderr line, exit 0.
- `estimate-sprint-close-takes-the-readings-in-groups` — pending — `rule-sprint-close` (draft) — method: by hand after the Work Mode of the session that closes a sprint.
- `estimate-sprint-migration-leftovers-gone` — pending — `entity-sprint-migration` (draft) — method: one reading of the tree by hand in the Work Mode of the session that closes the sprint, before the librarian's run.
- `estimate-sprint-migration-merges` — pending — `entity-sprint-migration` (draft) — method: `make test` on the last commit of migration, in the Work Mode of the session that closes it, before the librarian's run. This run: `make test` 1166 passed, 6 skipped, on the uncommitted tree of branch `migration`.
- `estimate-synthesis-clusters` — pending — `rule-synthesis` (draft) — method: by hand, the yaml and the report after a live librarian run whose yaml holds at least two lesson entries. This run: the yaml holds 1 lesson entry; 2 synthesis entries appended.
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — pending — `rule-work-mode` (draft) — method: `uv run guppi render --check`; by hand a `/work` at the fork, one `/box` calls, and the `/work` of a session that closes a sprint.

## Flags

- No entry marked `incomplete`, `failed`, `near` or `unparsed` (`unparsed: []`).
- Failed Estimate: `estimate-handoff-holds-each-fact-once` (L7), failed again.
- Stale defers (lint): `rule-complaint-becomes-a-lesson` 1 time since case 504; `rule-ledger-line-withdrawn-on-re-ratification` 1 time since case 594; `rule-morph` 1 time since case 239; `rule-subagent-guppi` 31 times since case 29.
- Lint: 35 finding lines — 4 `deferred`, 31 `unread` (30 pending, 1 failed); exit 2. The handoff gives the same 35 lines before and after the work.
- Handoff: "`rule-ask` takes five `update` entries in one run (633.1, 633.2, 634.1, 634.2)"; the ledger and the yaml hold four `rule-ask` entries, one per case named. Each applied; none failed.
- Handoff: the `## How it works` sections of `rule-cleanup` and `rule-sprint-close` were removed by hand in Work Mode, before this run; the 632.1 entries carry a `change` (and `sections.Purpose` for `rule-sprint-close`) and applied.
- Handoff note: 632.3, the `given` of 632.4 and the new paragraph of `rule-orchestration` still point to `rule-sprint-close` for facts that leave its page; left as it stands at `/pre-spec`.
- MOC candidates: none raised. Contradictions: none found.
- Read outside the frame's list: the synthesis entries of `vault/raw/2026-10-04/1934/materialize.yaml` (L161–183), for the form of `set.children` in a synthesis `update` — the synthesis; the handoff did not ask for it.

## Next session

### Cases

- `estimate-handoff-holds-each-fact-once` failed again: decide whether the Debt of `handoff.md` keeps one line per Estimate, or the Criterion allows the lines grouped by moment (handoff, For the next session).

### Work

- `estimate-sprint-migration-lint-clean`
- `estimate-sprint-close-next-session-opens-the-sprint`
- `estimate-hi-writes-frontier`
- `estimate-hi-takes-a-conserved-spec`
- `estimate-insights-schema-checked`
- `estimate-orchestration-asks-in-the-grill-me-shape`
- `estimate-ask-finds`
- `estimate-ask-searches-at-prespec`
- `estimate-prespec-reconciles`
- `estimate-prespec-confirms-the-findings-once`
- `estimate-orchestration-shows-the-built-case`
- `estimate-ask-query-before-a-create`
- `estimate-backlog-renders`
- `estimate-brief-written`
- `estimate-case-build-checks-the-finished-case`
- `estimate-case-build-writes-the-case`
- `estimate-case-check-judges-a-lone-sub-case-with-its-stored-parent`
- `estimate-case-check-requires-each-question-of-the-rounds`
- `estimate-case-check-sends-back-a-case-number-held-by-another-agent`
- `estimate-case-check-sends-back-a-clash-with-another-case`
- `estimate-case-check-sends-back-a-ratified-case-in-another-shape`
- `estimate-lint-runs-every-step`
- `estimate-session-start-context`
- `estimate-spec-write-reaches-the-approved-spec`
- `estimate-sprint-close-runs-in-the-librarian-run`
- `estimate-sprint-close-takes-the-readings-in-groups`
- `estimate-sprint-migration-leftovers-gone`
- `estimate-sprint-migration-merges`
- `estimate-synthesis-clusters`
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`

### Ask the person

none

## Readings at the close

- `make test`: 1166 passed, 6 skipped.
- `make lint`: 35 finding lines (4 `deferred`, 31 `unread`), exit 2.
- Pages under `vault/wiki/`: decisions 1073, entities 4, estimates 209, insights 30, lessons 78, rules 77. Under `vault/archive/`: 791 `.md` files; `guppi archive` moved no unit.
