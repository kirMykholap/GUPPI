# Backlog

17 items

## Conserved Specs

- `vault/raw/2026-10-04/1439/spec.md` — Cases 627, 628, 629, 630, 631
  - update `rule-sprint-close` · case 627.1
  - update `entity-sprint-migration` · case 627.1
  - update `rule-decisions-schema` · case 627.1
  - update `rule-cleanup` · case 627.1
  - update `estimate-sprint-close-archives-the-decisions` · case 627.1
  - update `rule-insights-schema` · case 627.2
  - update `rule-lessons-schema` · case 627.2
  - update `estimate-sprint-close-archives-done-insights-and-lone-lessons` · case 627.2
  - update `estimate-sprint-close-archives-the-sprint-page-and-keeps-the-rest` · case 627.3
  - update `estimate-sprint-close-settles-unread-estimates` · case 627.4
  - update `rule-synthesis` · case 627.5
  - update `estimate-synthesis-clusters` · case 627.5
  - create `estimate-sprint-close-runs-in-the-librarian-run` · case 628.1
  - update `rule-sprint-close` · case 628.1
  - update `rule-documentation` · case 628.1
  - update `rule-retro` · case 628.1
  - update `rule-orchestration` · case 628.1
  - update `rule-case-protocol` · case 628.1
  - create `estimate-sprint-close-takes-the-readings-in-groups` · case 628.2
  - create `estimate-sprint-close-next-session-opens-the-sprint` · case 628.3
  - update `rule-ledger-write` · case 628.3
  - update `rule-materialize` · case 628.3
  - update `rule-work-mode` · case 628.4
  - update `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` · case 628.4
  - update `rule-sprint` · case 628.5
  - update `estimate-sprint-ticks-the-spec` · case 628.5
  - update `estimate-generate-writes` · case 628.6
  - update `rule-skill-hi` · case 628.7
  - update `estimate-hi-writes-frontier` · case 628.7
  - update `rule-brief` · case 628.8
  - update `estimate-brief-written` · case 628.8
  - update `entity-sprint-migration` · case 628.9
  - update `estimate-sprint-migration-merges` · case 628.9
  - update `estimate-sprint-migration-lint-clean` · case 628.10
  - update `estimate-sprint-migration-leftovers-gone` · case 628.11
  - update `rule-backlog` · case 628.12
  - update `estimate-backlog-renders` · case 628.12
  - create `estimate-case-check-sends-back-a-clash-with-another-case` · case 629.1
  - update `rule-case-check` · case 629.1
  - update `rule-orchestration` · case 629.1
  - update `rule-case-build` · case 629.2
  - update `estimate-case-build-writes-the-case` · case 629.2
  - delete `rule-case-rebuild-cost` · case 629.2
  - create `estimate-case-check-judges-a-lone-sub-case-with-its-stored-parent` · case 629.3
  - update `estimate-case-check-requires-each-question-of-the-rounds` · case 629.4
  - update `rule-case-build` · case 629.5
  - update `estimate-case-build-checks-the-finished-case` · case 629.5
  - defer `estimate-spec-write-reaches-the-approved-spec` · case 630
  - defer `estimate-lint-runs-every-step` · case 631

## Deferred

- `entity-guppi` — GUPPI as the thing this repository builds — the harness and the vault it keeps; its parts the sprint and the glossary · put off in 0 sessions
- `rule-complaint-becomes-a-lesson` — After each reply of the person a hook raises the question whether it holds a complaint about the agent's text or work, and a complaint becomes a lesson line; an idea of session 0137, not yet decided · put off in 1 session
- `rule-ledger-line-withdrawn-on-re-ratification` — Prevents a decision line of the first ratification of a Case from standing in the ledger after the Case is ratified again without its item, so that a rename or a dropped item does not need a new Case that supersedes the whole one · put off in 1 session
- `rule-morph` — The initiation at install: the person sets the category set of the project — the development set entity, rule, estimate by default — and the harness holds it as data, so a changed set rewrites no rule; the categories discussion of session 1119, raw/2026-09-17/1119/categories-discussion.md; Slice 5 · put off in 3 sessions
- `rule-page-generation` — Prevents a ratified decision from ending the session without a page, or a page from carrying a field nobody ratified · put off in 0 sessions
- `rule-subagent-guppi` — Prevents implementation drifting from the ratified plan while it is being executed · put off in 29 sessions
- `insight-hi-skill-substitution-checked-by-a-model-call` — A `!` command of a skill is checked by a model call before it runs; when that call fails — a lapsed login, reported as the model unavailable — the substitution is refused and the Render: line comes back empty, while the SessionStart hook is not affected. · severity 1 · put off in 3 sessions
- `insight-session-vault-knowledge-not-loaded` — A fact the vault holds does not reach the session that needs it; only brief.md, CLAUDE.md, the skills and the agent frames are loaded, and everything else waits for a read the agent must first think to make. · severity 2 · put off in 0 sessions
- `insight-workflow-case-schema-silent-on-what-the-scripts-accept` — The Case schema does not say how the scripts read the text a Case writes — which forms they resolve, how far an edit pair reaches — so the agent writes a form the scripts do not handle, and only the pre-spec check finds it. · severity 3 · put off in 0 sessions
- `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it` — A fact is signed — in a Case, in a reading, in a ledger line — on a check narrower than the claim: the command that ran answered one question and the sentence it supports makes a wider one, while the wider check was one more command away. · severity 3 · put off in 1 session
- the product model: `kind: test | measurement | reading`, `ask-guppi` through Entities, the vault-query questions before a product's records (session 1119); `applies_to` and `rules` taken into Slice 3f (case 301) · put off in 0 sessions
- reuse, the edge: `uses` / `used_by` between Entities — `uses` written in the Case on the side that uses, `used_by` computed by the cascade of `generate`, the pair checked by lint, the pattern of `applies_to` / `rules`; no edge Rule → Rule (cases 305, 319) · put off in 0 sessions
- reuse, the question: the vault query before a `create` asks a second question — what of the existing this thing could use, by the index lines of the Entities — and the answer stands in `context`; the Case names what it found in `uses` or says why it is not used (case 319) · put off in 0 sessions
- reuse, the hook: a lint finding on two live Entities naming one path in `code_ref` with no edge between them; a new module written beside an existing one in another file is caught by the question alone, not by a script (case 319) · put off in 0 sessions
- a template engine for the rendered files — one script with the shape of each file declared, once a third render beside `sprint.md` and `glossary.md` appears (case 301) · put off in 0 sessions
- `rule-spec-box` — Prevents a conserved Spec from being built on a branch that lacks the current vault, or its pages from being written anywhere but on the shared branch · put off in 6 sessions
