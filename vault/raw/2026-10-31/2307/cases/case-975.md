## Case 975 — The rules schema names a guard that prevents a case

> **context:**
> The rules schema, `vault/wiki/rules/schema.yaml`, the Render of `rule-rules-schema`, says in its opening that a Rule is a standing condition one case can break, with a guard that refuses that case, and in its Enforcement paragraph that in the harness a thing is a Rule when its code is a guard that refuses a case. Some hook Rules refuse nothing: `rule-link-graph-at-session-start` writes `.guppi/links.md` on `SessionStart` and stops no session on an error, and `rule-librarian-report-copy` copies the librarian's report into `report.md` on `SubagentStop`; both pages, read whole, say so in their Purpose. By the letter of the schema neither is a Rule. The schema also contradicts itself, since its own list of what a hook does names a write that refuses nothing, a hook that appends to `log.md` on every page change. Case 967.3 of session 1831 kept `rule-link-graph-at-session-start` a Rule and left this gap to a later Case, as its `context` and the handoff of that session say. The purpose lines of other hook Rules describe a state the hook keeps rather than a call it refuses, such as `rule-compact-recall`, which puts the texts that `/hi` loads back into the context after a compaction, and `rule-spec-capture`, which keeps the approved Spec in a file of the repository. The person chose that a guard refuses a case or prevents it, a hook preventing it when it writes a file or gives the agent a text, and that the change is checked by the Criterion of `estimate-rules-schema-checked` replaced whole. The rule that governs the change is `rule-rules-schema` itself: the check of a Rule, one case that can refute it and something that stops that case, holds for a hook that keeps the state in place, and the new wording keeps a condition no hook, check or render can detect out of `rules/`. A Grep `its code is a guard|refuses a case|refuses that case|with a guard` over `vault/wiki/` printed `entities/entity-glossary.md`, `glossary.md`, `rules/rule-rules-schema.md` and `rules/schema.yaml`: the two sentences of the Render change by two pairs, the row of Rule in `entity-glossary` changes by one pair, and `glossary.md` and `schema.yaml` are rendered from those pages. The row of the glossary is checked by `estimate-glossary-terms-defined`, whose Criterion says that no claim of the meaning of a row contradicts its `where` page; it stands, since the new row agrees with the new schema. The table of `## Terms` of `entity-glossary`, read whole, holds the row of Rule as one sentence of clauses split by semicolons, and the pair changes its first two clauses alone; the rows of Hook, a script behind a Rule page, and of Estimate, on a Rule a test that the guard works, agree with the new row and stand; no other Case of this session writes into the page. The `purpose` and the `method` of `estimate-rules-schema-checked` state no content of the description, the method reading the live file against the Criterion after a librarian's run, so both stand. `estimate-rules-schema-leaf-carries-no-how-it-works` speaks of the section `## How it works` and stands. `rule-hook-registry`, which registers a new hook only with the hook's Rule, agrees with the new wording. The block `## rule-rules-schema` of `.guppi/links.md` names `entity-glossary` as the one neighbour whose purpose bears on the change; the block `## vault/wiki/rules/schema.yaml` names readers of the file by command, none of which reads the prose of `description`. A Grep `(REPO|ROOT|repo_root|LIVE)[^\n]*(rules|schema)` over `.guppi/tests/` printed `test_case_schema.py`, `test_orchestration.py`, `test_generate.py` and `test_schemas.py`; each reads or copies the live `schema.yaml` for its lists of `properties` and `body`, which this Case does not change, so no test fails on the new text. Cases 972, 973 and 974 of this session change none of these pages. The ledger of this session holds no `error` lesson, so no `{addresses:...}` mark stands.

> **problem:**
> The rules schema says a Rule's guard refuses a case, while hook Rules of the vault, such as the one that writes the graph of links at the start of a session, refuse nothing and only keep a file in place, so the schema and those pages contradict each other.

> **recommend:**
> - **What the rules schema says about a hook that refuses nothing**
>   - Recommended: (b) name any hook that makes a state hold instead of refusing a call: a guard refuses the case or prevents it, and a hook prevents it when it writes a file or gives the agent a text, in the opening of the schema, its Enforcement paragraph and the glossary row of Rule.
>   - Answer: (b), as recommended.
> - **How the change is checked**
>   - Recommended: (a) replace the Criterion of `estimate-rules-schema-checked` whole, with a new line on the opening and the Enforcement paragraph; the glossary row stays with its own Estimate.
>   - Answer: (a), as recommended.

> **given:**
> `rule-rules-schema`: the page whose Render holds the opening and the Enforcement paragraph.
> **＋** `vault/wiki/rules/schema.yaml`: the file rendered from it, which lint reads for each page of `vault/wiki/rules/`.
> **＋** `estimate-rules-schema-checked`: its Criterion is replaced whole.
> **＋** `entity-glossary`: the row of Rule, rendered into `vault/wiki/glossary.md`.

> **when:**
> `guppi render` writes `vault/wiki/rules/schema.yaml` from `rule-rules-schema`, and `guppi lint` reads a page of `vault/wiki/rules/`.

> **then:**
> The file equals the Render. Lint reads from it: required `type, kind, purpose, status, estimates, origin, sprint, created, tags`; optional `enforcement, implementation_ref, governs, render_mode, parent, children, deferred_by, applies_to, core`; values `kind: MOC | Leaf`, `status: draft | built | archived`, `enforcement: hook | check | render`, `render_mode: full | partial`, `core: true`; conditional — `hook` and `check` require `implementation_ref`, `render` requires `governs`, `render_mode` and the section `## Render`, `MOC` requires `children` and forbids `enforcement: hook | check`; the sections `## Purpose` and `## History` required, `## Render` and `## How it works` optional.
> **＋** The file also holds `ordered_children: true`, which lint does not read.
> **＋** A Rule page with these fields, values and sections has no `schema` finding; one lacking a required field, with a value outside the list, with a conditional not met or lacking a required section has one finding per defect; a rule with `applies_to` on a live Entity has none.
> **＋** A Rule page in the shape with `core: true`, `origin: guppi` and `sprint: guppi` has no `schema` finding.
> **＋** `fields` and `sections` describe each name of these lists, `core` among them, and the descriptions of `origin` and `sprint` name the value `guppi` on a page with `core: true` in the clean version; `description` holds the introduction, Ordering, MOCs and enforcement, Enforcement, the sentence on the edge Rule → Entity, the one on the guard of the agent's own conduct and the one on the Estimates that a shipped page brings along; `examples` holds the example pages.
> **＋** That last sentence says that a shipped page arrives with each of its Estimates that passed in the repository it came from and whose `method` names no target of the `Makefile`, and that the receiving project writes its other Estimates through its own Cases.
> **＋** The description of `## How it works` under `sections` says that the section is for a MOC alone and that a Leaf carries none, and no example of a Leaf under `examples` carries the section.
> **＋** The opening of `description` says that a Rule's guard refuses a case or prevents it, and the Enforcement paragraph says that in the harness a guard refuses a case or prevents it, a hook preventing a case when it writes the file, or gives the agent the text, whose absence or age would be that case.
> **－** Neither the opening nor the Enforcement paragraph says that a guard must refuse a call for its page to be a Rule.

> **tasks:**
> - [ ] update `rule-rules-schema`
>   - old: `A Rule is a standing condition one case can break, with a guard that refuses that case when it occurs. The check: can one case refute it, and is there something to refuse that case?`
>   - new: `A Rule is a standing condition one case can break, with a guard that refuses that case when it occurs or prevents it from occurring. The check: can one case refute it, and is there something to refuse or prevent that case?`
>   - old: `In the harness a thing is a Rule when its code is a guard — it refuses a case: a hook, a check, a render that refuses drift.`
>   - new: `In the harness a thing is a Rule when its code is a guard — it refuses a case: a hook, a check, a render that refuses drift — or it prevents a case: a hook that writes the file, or gives the agent the text, whose absence or age would be that case, so that the case never occurs, such as a hook that writes a file at the start of a session (as set in case 975).`
>   - change: `a guard refuses a case or prevents it; a hook that writes a file or gives the agent a text is a guard`
> - [ ] update `entity-glossary`
>   - old: `with a guard that refuses that case when it occurs; the check: can one case refute it, and is there something to refuse it;`
>   - new: `with a guard that refuses that case when it occurs or prevents it from occurring, such as a hook that writes a file the session needs; the check: can one case refute it, and is there something to refuse or prevent it;`
>   - change: `the row of Rule: a guard refuses a case or prevents it`
> - [ ] update `estimate-rules-schema-checked`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the opening and the Enforcement paragraph name a guard that prevents a case`
> - [ ] `uv run --project .guppi guppi render`: `vault/wiki/rules/schema.yaml`
> - [ ] `uv run --project .guppi guppi glossary`
> - [ ] read `estimate-rules-schema-checked`

> **ratification:**
> ```
> - decision[case 975][update][rule-rules-schema]{ref:rule-rules-schema}
> - decision[case 975][update][entity-glossary]{ref:entity-glossary}
> - decision[case 975][update][estimate-rules-schema-checked]{ref:rule-rules-schema}
> ```
