# Backlog

19 items

## Conserved Specs

## Deferred

- `rule-ask` — Prevents a create from being proposed without the vault having been asked whether it already holds the thing, or forbids it · put off in 0 sessions
- `rule-case-rebuild-cost` — Prevents a Case from being rewritten whole and returned whole into the main agent's context when only a sub-case changed, and its context from listing searches that change nothing; options from session 2356 - the SubagentStop hook merges a changed sub-case into the stored answer, case-guppi writes the Case file itself and returns a short answer, the context keeps only what changes the decision, a large item split into several Cases · put off in 2 sessions
- `rule-complaint-becomes-a-lesson` — After each reply of the person a hook raises the question whether it holds a complaint about the agent's text or work, and a complaint becomes a lesson line; an idea of session 0137, not yet decided · put off in 1 session
- `rule-ledger-line-withdrawn-on-re-ratification` — Prevents a decision line of the first ratification of a Case from standing in the ledger after the Case is ratified again without its item, so that a rename or a dropped item does not need a new Case that supersedes the whole one · put off in 1 session
- `rule-ledger-write` — Prevents a ratified line from existing only in a chat reply, or landing in a session no /hi opened · put off in 2 sessions
- `rule-morph` — The initiation at install: the person sets the category set of the project — the development set entity, rule, estimate by default — and the harness holds it as data, so a changed set rewrites no rule; the categories discussion of session 1119, raw/2026-09-17/1119/categories-discussion.md; Slice 5 · put off in 3 sessions
- `rule-page-generation` — Prevents a ratified decision from ending the session without a page, or a page from carrying a field nobody ratified · put off in 0 sessions
- `rule-subagent-guppi` — Prevents implementation drifting from the ratified plan while it is being executed · put off in 29 sessions
- `insight-hi-skill-substitution-checked-by-a-model-call` — A `!` command of a skill is checked by a model call before it runs; when that call fails — a lapsed login, reported as the model unavailable — the substitution is refused and the Render: line comes back empty, while the SessionStart hook is not affected. · severity 1 · put off in 3 sessions
- `insight-session-vault-knowledge-not-loaded` — A fact the vault holds does not reach the session that needs it; only brief.md, CLAUDE.md, the skills and the agent frames are loaded, and everything else waits for a read the agent must first think to make. · severity 1 · put off in 0 sessions
- `insight-workflow-case-schema-silent-on-what-the-scripts-accept` — The Case schema does not say how the scripts read the text a Case writes — which forms they resolve, how far an edit pair reaches — so the agent writes a form the scripts do not handle, and only the pre-spec check finds it. · severity 3 · put off in 0 sessions
- `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it` — A fact is signed — in a Case, in a reading, in a ledger line — on a check narrower than the claim: the command that ran answered one question and the sentence it supports makes a wider one, while the wider check was one more command away. · severity 1 · put off in 1 session
- the product model: `kind: test | measurement | reading`, `ask-guppi` through Entities, the vault-query questions before a product's records (session 1119); `applies_to` and `rules` taken into Slice 3f (case 301) · put off in 0 sessions
- reuse, the edge: `uses` / `used_by` between Entities — `uses` written in the Case on the side that uses, `used_by` computed by the cascade of `generate`, the pair checked by lint, the pattern of `applies_to` / `rules`; no edge Rule → Rule (cases 305, 319) · put off in 0 sessions
- reuse, the question: the vault query before a `create` asks a second question — what of the existing this thing could use, by the index lines of the Entities — and the answer stands in `context`; the Case names what it found in `uses` or says why it is not used (case 319) · put off in 0 sessions
- reuse, the hook: a lint finding on two live Entities naming one path in `code_ref` with no edge between them; a new module written beside an existing one in another file is caught by the question alone, not by a script (case 319) · put off in 0 sessions
- a template engine for the rendered files — one script with the shape of each file declared, once a third render beside `sprint.md` and `glossary.md` appears (case 301) · put off in 0 sessions
- `rule-work-mode` — Prevents implementation starting before the plan, branch and baseline exist · put off in 30 sessions
- `rule-spec-box` — Prevents a conserved Spec from being built on a branch that lacks the current vault, or its pages from being written anywhere but on the shared branch · put off in 6 sessions
