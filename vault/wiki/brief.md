# Brief — 2026-10-04, session 0112: the handoff said once, the method of four Estimates, the two forms of ask-guppi

## Where things stand

- Ratified in session 0112: 624; 625; 626 (626.1, 626.2). C1 and C2, the items of Slice 5, left on the sprint page.
- Code and tests: none changed. `make test` at the handoff: 1132 passed, 6 skipped; `make style` clean.
- Readings: ledger lines 1, 2, 9 and 13, all passed. Lesson: line 14.
- This run, from `raw/2026-10-04/0112/materialize.yaml` (14 entries and 2 of the synthesis); the yaml of 0004 was extended with 0 entries and `generate` changed 0 pages for it:
  - created: decisions 5 (`decision-case-624`, `625`, `626`, `626.1`, `626.2`); estimates 1 (`estimate-ask-query-before-a-create`, on `rule-ask`); lessons 1 (`lesson-work-mode-a-staged-moment-promised-inside-a-run-with-no-stop`, clustered).
  - updated: estimates 10 pages — 4 readings passed (`estimate-generate-rewords` and `estimate-prespec-checks-the-frontier` pending → passed, `estimate-orchestration-shows-the-built-case` failed → passed, `estimate-case-check-sends-back-a-faulty-case` pending → passed); the Criteria of `estimate-handoff-holds-each-fact-once` (624) and `estimate-ask-finds` (626.1) replaced whole, both failed → pending; the `method` of `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`, `estimate-prespec-onward-sends-the-agent-on`, `estimate-retro-onward-sends-the-agent-to-the-handoff` and `estimate-retro-runs-on-to-the-handoff` (625), all four still `passed`. Rules 2 by Case (`rule-handoff`; `rule-ask`, its `deferred_by` `decision-case-553` cleared by `{supersedes:case 553}` and `estimate-ask-query-before-a-create` added to its `estimates`) and 2 by the cascade, `draft → built`: `rule-page-generation`, `rule-prespec`. Insights 1 (`insight-session-vault-knowledge-not-loaded`, a child added by the synthesis, severity 1 → 2, stays `open`). Decisions 1 (`decision-case-553` set `superseded` by `decision-case-626.1`).
  - `guppi cleanup` moved 1 page: `decision-case-553` to `vault/archive/migration/2026-10-04/0112/decisions/`.
  - `guppi archive` printed nothing and moved nothing: it looks only at units dated before the day of the run, and both session folders of `raw/2026-10-04/` (0004, and 0112, the session of the run) are of that day.
  - rendered: `.claude/skills/handoff/SKILL.md` and `.claude/agents/ask-guppi.md`.
  - Spec boxes ticked: 11 in `raw/2026-10-04/0112/spec.md` (the 9 update and create boxes of 624, 625, 626.1 and 626.2, the 2 render boxes); 1 in `raw/2026-10-04/0004/spec.md` (`read estimate-prespec-checks-the-frontier`).
  - `backlog.md`: 21 → 20 items; `rule-ask` left it; `insight-session-vault-knowledge-not-loaded` now shows severity 2. `sprint.md` and `glossary.md` unchanged.
- The handoff's checks: the yaml carries the Cases as the Spec built them again — the Debt sentence of 624 ("these lines stand in the section and are not debt"), the moment "a Plan Mode that closes its last Case" in the `method` of `estimate-prespec-onward-sends-the-agent-on`, four replace pairs of 626.1 on `rule-ask`, one on the `## Problem` of a page's `deferred_by` at `/pre-spec`; all applied. `rule-ask` has no `deferred_by` after `generate`, and `backlog.md` no longer lists it. The Criterion lines of `estimate-ask-query-before-a-create` on a page asked in either language, a crossed rule, a named slug, an archived page and the archive not searched by meaning stand in the old Criterion of `estimate-ask-finds` (its lines 24–27 and 31 before the run).
- Index check: the yaml holds one `create`, an Estimate, which has no index; the `lesson` entry is compared in the synthesis below; no merge and no `near`.
- Synthesis: the Grep `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 75 lines; the Grep `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 31 lines.
  - `lesson-work-mode-a-staged-moment-promised-inside-a-run-with-no-stop` joined `insight-session-vault-knowledge-not-loaded`: the stretch with no stop is written in `vault/wiki/where-to-stop.md`, which no session loads, and the agent promised the moment without reading it.
  - The Insight stays `open`; the lesson entry carries no `addressed_by`.

## Readings due

- `estimate-ask-finds` — pending · `rule-ask` `draft` · box `raw/2026-10-04/0112/spec.md:274`; method: by hand at the /hi of a later session, the answer of ask-guppi at a /pre-spec after the render of `.claude/agents/ask-guppi.md` by case 626.1, read in its agent transcript against the event log
- `estimate-ask-query-before-a-create` — pending · `rule-ask` `draft` · box `raw/2026-10-04/0112/spec.md:315`; method: by hand at the /hi of a later session, the transcript of a case-guppi that built a Case with a create without a ref after that render, its Grep and Glob calls and the context of its Case
- `estimate-case-check-requires-each-question-of-the-rounds` — pending · `rule-case-check` `draft` · method: pytest `-k rounds`, then by hand a Case the hook sends back for a missing title
- `estimate-case-check-sends-back-a-case-number-held-by-another-agent` — pending · `rule-case-check` `draft` · box `archive/migration/2026-10-03/0115/raw/spec.md:398`; method: pytest `-k clash`, then by hand an answer the hook sends back for this reason
- `estimate-case-check-sends-back-a-faulty-round` — pending · `rule-case-check` `draft` · box `archive/migration/2026-10-03/0115/raw/spec.md:141`; method: pytest `-k round_form`, then by hand a round the hook sends back live
- `estimate-case-check-sends-back-a-ratified-case-in-another-shape` — pending · `rule-case-check` `draft` · box `archive/migration/2026-10-03/0115/raw/spec.md:353`; method: pytest `-k shape`, then by hand an answer the hook sends back for this reason
- `estimate-handoff-holds-each-fact-once` — pending · `rule-handoff` `draft` · box `raw/2026-10-04/0112/spec.md:87`; method: one reading by hand at the /hi of a later session, of a handoff.md written by the skill as rendered from `rule-handoff` after case 624, against the close of its Retro
- `estimate-hi-takes-a-conserved-spec` — pending · `rule-skill-hi` `draft` · box `raw/2026-10-04/0004/spec.md:176`; method: `uv run guppi render --check`; by hand, a session whose person takes a conserved Spec at the Frontier
- `estimate-lint-runs-every-step` — pending · `rule-lint` `draft` · method: by hand, the make lint of the Baseline of a /work of a later session whose backlog step is red
- `estimate-orchestration-signs-a-batch-together` — pending · `rule-orchestration` `draft` · method: by hand at a Plan Mode in which the person's word asks that a ratified Case change
- `estimate-ratification-ledger-line-form` — pending · `rule-ratification` `draft` · method: by hand, a session where a lesson and the Case that closes its cause stand together, and a Case that takes up a decision with more than one Case in its `deferred_by`
- `estimate-session-start-context` — pending · `rule-session-start` `draft` · method: `make test-session-start`; by hand, a session opened without /hi whose reply carries a LEDGER block
- `estimate-spec-write-reaches-the-approved-spec` — pending · `rule-spec-write` `draft` · method: pytest `-k approved_spec`; by hand, a Case ratified in Work Mode
- `estimate-sprint-close-archives-done-insights-and-lone-lessons` — pending · `rule-sprint-close` `draft` · box `archive/migration/2026-10-03/0317/raw/spec.md:300`; method: by hand after the first close of a sprint
- `estimate-sprint-close-archives-the-decisions` — pending · `rule-sprint-close` `draft` · box `archive/migration/2026-10-03/0317/raw/spec.md:263`; method: by hand after the first close of a sprint
- `estimate-sprint-close-archives-the-sprint-page-and-keeps-the-rest` — pending · `rule-sprint-close` `draft` · box `archive/migration/2026-10-03/0317/raw/spec.md:336`; method: by hand after the first close of a sprint
- `estimate-sprint-close-settles-unread-estimates` — pending · `rule-sprint-close` `draft` · box `archive/migration/2026-10-03/0317/raw/spec.md:375`; method: by hand, the record of the first close of a sprint
- `estimate-sprint-migration-leftovers-gone` — pending · `entity-sprint-migration` `draft` · method: one reading of the tree by hand at the close of the sprint
- `estimate-sprint-migration-lint-clean` — pending · `entity-sprint-migration` `draft` · method: `make lint`, exit 0 — or only unread lines on the Estimates of `entity-sprint-migration`
- `estimate-sprint-migration-merges` — pending · `entity-sprint-migration` `draft` · method: `make test` on the last commit of migration, then git log of main after the merge

## Flags

- No entry of the 0112 yaml marked `incomplete`, `failed`, `near` or `unparsed` (`unparsed: []`); every entry carries `applied`. `guppi generate` printed its two summary lines; `cleanup`, `render`, `sprint`, `backlog`, `glossary` and `archive` printed nothing on stderr.
- Failed Estimates: none.
- Two `read` boxes stay unticked for readings that passed this run, both in archived Specs: `archive/migration/2026-10-03/0115/raw/spec.md:99` (`estimate-case-check-sends-back-a-faulty-case`, L13) and `archive/migration/2026-10-03/0317/raw/spec.md:122` (`estimate-orchestration-shows-the-built-case`, L9).
- The Specs archived before 2026-10-03 hold 591 unticked `- [ ]` lines, by a grep of all `spec.md` files under `vault/archive/` and `vault/raw/` (604 lines; 13 of them in the Specs of 2026-10-03 and 2026-10-04).
- Stale defers, from `make lint`: `rule-subagent-guppi` deferred 31 times since case 29; `rule-case-rebuild-cost` 2 times since case 566; `rule-complaint-becomes-a-lesson` 1 time since case 504; `rule-ledger-line-withdrawn-on-re-ratification` 1 time since case 594; `rule-morph` 1 time since case 239.
- `make lint`, exit 2, 26 lines: 5 `deferred`; 20 `unread: pending`; the make error line.
- A read my frame says the run does not need: a grep of the unticked `- [ ]` lines of every `spec.md` under `vault/archive/`, for the `Work` list of Next session (the unticked boxes of the Specs).
- No MOC candidate and no contradiction found.

## Next session

Cases:
- `rule-sprint-close` and where the close of a sprint runs, Slice 5, put off again (handoff, For the next session).
- Whether Work Mode gives the person a moment to ask a change of a ratified Case: `estimate-spec-write-reaches-the-approved-spec` waits for a Case ratified in Work Mode, and `/work` runs to the librarian with no stop for the person (handoff, For the next session).

Work:
- `estimate-ask-finds`
- `estimate-ask-query-before-a-create`
- `estimate-case-check-requires-each-question-of-the-rounds`
- `estimate-case-check-sends-back-a-case-number-held-by-another-agent`
- `estimate-case-check-sends-back-a-faulty-round`
- `estimate-case-check-sends-back-a-ratified-case-in-another-shape`
- `estimate-handoff-holds-each-fact-once`
- `estimate-hi-takes-a-conserved-spec`
- `estimate-lint-runs-every-step`
- `estimate-orchestration-signs-a-batch-together`
- `estimate-ratification-ledger-line-form`
- `estimate-session-start-context`
- `estimate-spec-write-reaches-the-approved-spec`
- `estimate-sprint-close-archives-done-insights-and-lone-lessons`
- `estimate-sprint-close-archives-the-decisions`
- `estimate-sprint-close-archives-the-sprint-page-and-keeps-the-rest`
- `estimate-sprint-close-settles-unread-estimates`
- `estimate-sprint-migration-leftovers-gone`
- `estimate-sprint-migration-lint-clean`
- `estimate-sprint-migration-merges`
- the unticked boxes of the Specs of 2026-10-03 and 2026-10-04: 4 `read` of `archive/migration/2026-10-03/0115/raw/spec.md`, 5 `read` of `archive/migration/2026-10-03/0317/raw/spec.md`, 1 `read` of `raw/2026-10-04/0004/spec.md`, 3 `read` of `raw/2026-10-04/0112/spec.md`; 11 name a reading above, 2 a reading that passed this run (Flags)

Ask the person:
- none

## Readings at the close

- `make test`: 1132 passed, 6 skipped.
- `make lint`: exit 2, 26 lines (5 deferred, 20 unread: pending, the make error line).
- Pages: rules 78, entities 4, estimates 202, lessons 76, insights 30, decisions 1031; archive 787 `.md` files, 865 files in all.
- Ledger lines: 0112 14 of 14 have an entry in the yaml.
