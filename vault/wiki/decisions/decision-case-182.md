---
type: decision
case: "182"
status: current
defer: ["[[rule-plan-mode]]", "[[rule-page-generation]]", "[[rule-materialize]]", "[[rule-lint]]", "[[rule-pretask]]"]
supersedes: ["[[decision-case-178]]"]
origin: raw/2026-09-15/2225/ledger.md#case-182
sprint: migration
created: 2026-09-15
tags: [session, workflow, harness, ledger]
---

## Context

An Estimate today is one page per rule: a head Criterion from the moment of `create`, plus one `### case N` block per `contract: changed`, appended by the script; only `{supersedes:case N}` removes a block; `Result` is overwritten by the last reading of any block; `Method` is one per page although the blocks are checked by a test here and by a reading there. The promise of a rule is written three times — How it works, Render, the blocks — and the copies drift apart (174, 179/181). `rule-page-generation` holds 10 blocks, `rule-materialize` 9. Question 178 — who names the block a new contract removes — is a symptom.

## Problem

Nobody judges an Estimate page as a whole: it is stitched from deltas, and "what the rule promises now" is written nowhere. Session 2225 took this apart down to a model that changes `estimates/schema.md`, `rules/schema.md`, `case-schema.md`, `index.md` §6–§7, `materialize`, `generate`, `lint`, pre-task and the form of Plan Mode — the size of a Slice, not of a Case. The model must be kept whole and run as the Plan Mode of the next session, before 3b: Work Mode leans on "an Estimate is the red test".

## Deferred

### [[rule-plan-mode]]

Slice 3d — the Estimate model agreed in session 2225; supersedes 178: the question "who names the block to remove" disappears — there are no blocks.

What an Estimate is
1. An Estimate = one promise + one way to check it + the last result with its date. The split: one action (`when`) — one Estimate; the ＋/－ lines stay in its `then` while one run checks them; a line with a test or a reading of its own is split off (§6). The axis of the split is the promise, not the method: a test in a temp repository ("on payload X the script does Y") and a live reading ("the hook is registered and fires in the client") are two promises, two Estimates, no text duplicated.
2. `kind` QA/Research stays; Research is when the result is unknown before the build — its `then` a question, its Result the finding. Reading a known criterion by eye is QA by hand, not Research.
3. The promise is written once — the Estimate's Criterion: Given/When/Then. The rule keeps `purpose`, Purpose (the failure it prevents), Render (when rendered), `estimates` — the table of contents of its promises — and `implementation_ref`/`code_ref`. How it works is dropped on a Leaf — the mechanism lives in the code and its docstring; kept on a MOC ("why in this order"). Render is a promise too: the file equals the Render (the render Estimate) and the agent does what is written (the live-reading Estimate).
4. A MOC exists when there is a promise about the whole — an order, a chain — that no child holds alone; that promise is the MOC's Estimate, checked by a make target. A grouping without such a promise is `tags.md`, not a MOC.
5. Estimate fields: `kind`, `status`, `target`, `purpose` (one line for the list on the rule), `method` (one line: the test command; where and when to read; what is measured in Research), `checked` (the date from the time of the estimate line). Sections: Criterion, Result. Context and the Method section go. Slugs: existing ones stay, new ones are `estimate-<target>-<promise>`. The pages will number ~90–120 — no harm: `ask-guppi` searches the index lines of rules, entities, lessons and insights, never Estimates; the rule page lists its Estimates with their `purpose`, only the touched ones are read; no Estimate index, as today (§11).

How a Case changes a promise
6. A Case: `context`/`problem`/`recommend` — the story for the person; the vault's answer — which Estimates of the rule are touched and which are not — in `context`. `given`/`when`/`then` — the technical contract, the description of the test or of the Research items; `given` holds conditions of the behaviour only, the state of pages moves to `context`. `tasks` without `contract` and "block N" lines. The chat form — eight sections — does not change; `case-schema.md`: "`when` + `then` are the criterion" → "`given` + `when` + `then` are the Estimate's Criterion". One signature (72.1): the contract is signed in the Case and copied by the script.
7. An `update` of `estimate-x` replaces the Criterion with the Case's `given`/`when`/`then` whole and sets `pending`; the `then` block carries `slug` only, and `set` when needed; a change of `method` alone writes the promise again word for word. The flag `contract: changed/same` goes; the `ref` of the ledger line is the Estimate itself. One contract per Case or sub-case; two touched promises are two sub-cases.
8. A change of a rule is the Case's judgment, not automation: only a replaced Criterion sets `pending`. An `update` of the rule's Purpose touches no Estimate (`when` — a reader opens the page, `then` — the new text); an `update` of the Render touches the live-reading Estimate of that Render. Pre-task checks that the named Estimates exist and asks `ask-guppi` whether an unnamed one speaks of the same thing. The hole: code in Work Mode touches a promise the Case did not name — only that promise's test catches it; hence a test for every promise where one is possible.
9. A new promise is an explicit `create` of an Estimate with `ref: rule-x`, its slug in the Case; a `create` of a rule with several promises — the parent creates the rule, sub-cases create one Estimate each. `method`, `estimate_kind`, `estimate_slug` on `create` go.
10. The Decision page: Context, Problem, the lists of decisions; Given goes (When is already absent, case 72.4), and the Criterion list of `[[estimate-x]] § case N` lines goes with the blocks — the contract is not its business. The old Criterion after a replacement stays in the Spec of the archived session, reached by `origin`, and in the Estimate's History.

Reading and building
11. A reading: `estimate[slug][passed|failed] text` as today; the date and the command as the first line of Result; Result is overwritten — it is about one run of one check; `built` = every Estimate `passed`, the cascade as today; `failed` is debt, archival by default.
12. TDD: an Estimate is the red test, described by `given`/`when`/`then` before the work; the test is written in Work Mode as the first step, before the code — a task of the Spec; Work Mode turns it green. A reading is taken in Plan Mode when the check can run there. Slice 3b (Work Mode) leans on this.
13. Lint: a finding `unread` for every `pending`/`failed` Estimate, exit 1 — red between a contract change and its reading by design, `guppi lint` runs whenever wanted; `make lint` does not block a commit. The flow: a rule changes → the touched Estimate `pending` → lint red → tests or reading → `passed` → lint clean.

Limits and migration
14. `materialize`/`generate` lose the blocks, `remove_criterion`, `contract`; `supersedes` stays for Decision pages and yaml entries. Lessons and Insights do not change. Entities: the same schema, none built, no migration.
15. The migration of the 42 pages: one Case per rule — a recut of signed text with no new contract — for the rules that get touched; the rest at their first touch; no separate marathon. 180 and 181 are applied by the librarian under the old model; block 180 is recut together with `rule-retro-commit`.
16. The Rule-class files of session 3d: `estimates/schema.md`, `rules/schema.md`, `decisions/schema.md`, `case-schema.md`, `index.md` §6–§7, `glossary.md`. `sprint.md`: Slice 3d before 3b, Slice 4 after both.

### [[rule-page-generation]]

Slice 3d — generate without Criterion blocks and remove_criterion; the Criterion replaced whole; the fields purpose, method, checked; see the purpose on rule-plan-mode

### [[rule-materialize]]

Slice 3d — materialize without contract, derived blocks, method/estimate_kind/estimate_slug on create; an update of an Estimate = a replaced Criterion; see rule-plan-mode

### [[rule-lint]]

Slice 3d — the finding unread on every pending/failed Estimate; the Estimate schema without Context and the Method section, with purpose, method, checked; see rule-plan-mode

### [[rule-pretask]]

Slice 3d — pre-task checks the Estimates of the rule named in context and asks ask-guppi whether an unnamed one speaks of the same thing; see rule-plan-mode

## History

- 2026-09-16 created · raw/2026-09-15/2225/ledger.md#case-182
