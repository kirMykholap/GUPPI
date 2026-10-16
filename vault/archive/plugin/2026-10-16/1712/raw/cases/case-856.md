## Case 856 — The clean version holds no sentence true only in the repository of GUPPI

> **context:**
> `guppi ship` builds the clean version of GUPPI that a project installs. It writes each rule and entity with `core: true`, the files rendered from them, and each `passed` Estimate of those pages whose `method` names no target of the `Makefile` (`ships` of `.guppi/guppi/ship.py`, lines 359–367). A sentence there that holds only in the repository of GUPPI misleads that project. The reading of `estimate-clean-branch-ships-neutral-texts` at the `/hi` of session 0342 (line 2 of `vault/raw/2026-10-16/0342/ledger.md`) failed on three such sentences. Two are the description of the field `core` in the Render of `rule-rules-schema` and of `rule-entities-schema`, which ends "a page without it stays in this repository only". The third is the sentence of the Render of `rule-ratification` that says the sprints `migration` and `plugin` keep plain Case ids to their close. The reading also listed four shipped Estimates. `estimate-skill-sprint-close-migration-merged-into-main` describes one past event, the merge of `migration` into `main`. The methods of `estimate-sprint-close-archives-done-insights-and-lone-lessons`, `estimate-sprint-close-archives-the-decisions` and `estimate-sprint-close-archives-the-sprint-page-and-keeps-the-rest` preview `--sprint migration`. The handoff of session 0342 says that the reading was a keyword grep and not a read of every sentence.
>
> Case 856.1 rewrites the three sentences, and Case 856.2 deals with the four Estimates. Case 856.3 takes up `decision-case-828`, which put off a fix of `rule-rules-schema`. The Render of that page still says that a page with `core: true` comes into a new project without its Estimates. That is false since `guppi ship` writes those Estimates (the Purpose of `rule-clean-branch`, as set in case 822); an Estimate whose `method` names a target of the `Makefile`, such as `estimate-harness-pipeline`, stays in the repository of GUPPI, so the new sentence names that limit. The new wording of `core` follows Case 824, which named "the repository of GUPPI" where a shipped page meant this repository. The new sentence of `rule-ratification` names the list `PLAIN_SPRINTS` of `.guppi/guppi/caseid.py`, which ships. The two sprint names go into a bracket with the pointer to case 788.2, and `guppi ship` removes that bracket whole, as `rule-clean-branch` and `case-schema.md` (case 807.4) set it for the new text of a page with `core: true`. Each new text keeps its pointer in a bracket at the end of its sentence.
>
> `estimate-skill-sprint-close-migration-merged-into-main` is deleted. Its rule, `rule-skill-sprint-close`, now says that the closing Case holds no task line for the merge, and `estimate-skill-sprint-open-merges-the-closed-sprint-branch` (`passed`) checks the merge as it works today, with a merge commit and not a fast-forward. A `delete` sets the page `archived` (`delete` of `.guppi/guppi/generate.py`) and does not touch the `estimates` of its target, so Case 856.2 sets that field on `rule-skill-sprint-close`. The three methods change by `set` alone, so their Criterion and their `passed` status stand.
>
> How each sub-case is checked: Case 856.1 reads `estimate-clean-branch-ships-neutral-texts` again. Its Criterion stands, since it already promises the change, and it is written back unchanged with the status `pending`. Its method is set anew so that the reading waits for the librarian's run of this session, where the pages change, and reads each sentence whole. Case 856.2 rests on the same reading: the fourth `Then` line of that Criterion has the reader list each sentence of a shipped Estimate that holds only in the repository of GUPPI, and Case 856.2 is checked when that list holds no sentence of the four Estimates it changes; the known line of `estimate-ratification-case-id-carries-the-sprint` may stay on the list for a later Case. Case 856.3 replaces the Criterion of `estimate-rules-schema-checked`, whose `description` line names the old sentence. `estimate-entities-schema-checked` and `estimate-rules-schema-checked` name the description of `core` only as a name described in `fields`, so Case 856.1 leaves them alone. One line of the Criterion of `estimate-ratification-case-id-carries-the-sprint` says that the sprints `migration` and `plugin` keep plain ids by a fixed list in `.guppi/guppi/caseid.py`. That line stands: it is true of the code that ships, and the person chose to leave it for the next reading to list. `estimate-ratification-loaded` promises only that the file equals the Render.
>
> Searches. A Grep for `without its Estimates|stays in this repository only|keep that form to their close` over the repository outside `vault/raw/` and `vault/archive/` printed nine files: `vault/wiki/ratification.md`, `vault/wiki/rules/schema.yaml`, `vault/wiki/entities/schema.yaml`, `vault/wiki/estimates/estimate-clean-branch-ships-neutral-texts.md`, `vault/wiki/rules/rule-ratification.md`, `vault/wiki/rules/rule-rules-schema.md`, `vault/wiki/estimates/estimate-rules-schema-checked.md`, `.guppi/guppi/caseid.py` and `vault/wiki/rules/rule-entities-schema.md`. The three rendered files follow the render. The docstring of `caseid.py` names the sprints of `PLAIN_SPRINTS` and not the two sprints, so it stands. The Result of `estimate-clean-branch-ships-neutral-texts` quotes the old sentences as its reading and stands. A Grep for `estimate-skill-sprint-close-migration-merged-into-main` over the same paths printed `vault/wiki/log.md`, `vault/wiki/estimates/estimate-clean-branch-ships-neutral-texts.md` and `vault/wiki/rules/rule-skill-sprint-close.md`. The log and the Result are records and stand, and the `estimates` field of the rule enters Case 856.2. A Grep for `ratification\.md|rules/schema\.yaml|entities/schema\.yaml|rule-ratification|rule-rules-schema|rule-entities-schema` over `.guppi/tests/` printed `test_ledger.py`, `test_materialize.py` and `test_ship.py`, which read a string or a copy under a temporary folder. `.guppi/tests/test_schemas.py` builds the path of the live `schema.yaml` from the category and reads only its lists, which no sub-case changes.

> **problem:**
> The clean version of GUPPI carries three sentences of rules and four shipped Estimates that hold only in the repository of GUPPI, and the Render of `rule-rules-schema` still says that a page with `core: true` ships without its Estimates.

> **recommend:**
> - **How should the `core` field read?**
>   - Recommended: (a) one wording true in both places: the page is part of GUPPI, `guppi ship` writes it in the repository of GUPPI into the clean version that a project installs, and a page without it is a page of the project that holds it.
>   - Answer: agreed, (a).
> - **How should the sentence on old Case ids in `rule-ratification` read?**
>   - Recommended: (a) name the list `PLAIN_SPRINTS` of `.guppi/guppi/caseid.py`, and put the two sprint names in a bracket with the pointer, which `guppi ship` removes.
>   - Answer: agreed, (a).
> - **What happens to the Estimate on the merge of `migration` into `main`?**
>   - Recommended: (a) delete it and remove it from the `estimates` of `rule-skill-sprint-close`.
>   - Answer: agreed, (a).
> - **What should the three methods that preview `--sprint migration` say?**
>   - Recommended: (a) preview the open sprint, `--sprint <id>` with `<id>` the sprint that `vault/wiki/sprint.md` names.
>   - Answer: agreed, (a).
> - **Does the fifth Estimate, which the reading missed, come in?**
>   - Recommended: (a) leave it for the next reading to list.
>   - Answer: agreed, (a).
> - **Should this Case also take up the put-off fix of `rule-rules-schema`?**
>   - Recommended: (a) take it up here as a sub-case.
>   - Answer: agreed, (a).
> - **How is the fix checked?**
>   - Recommended: (a) the same Estimate, read again, with every sentence read.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: at pre-spec, the check of Case 856.2 can never close while the line of `estimate-ratification-case-id-carries-the-sprint` stays on the list; the person agreed to narrow it.
>   - Taken: Case 856.2 is checked when the list of the reading holds no sentence of the four Estimates it changes; the line of the fifth Estimate may stay on the list for a later Case.

### Case 856.1 — The shipped rules name GUPPI and its sprints only where that holds

> **given:**
> `rule-rules-schema`: its Render, `vault/wiki/rules/schema.yaml`, describes the field `core`.
> **＋** `rule-entities-schema`: its Render, `vault/wiki/entities/schema.yaml`, describes the field `core`.
> **＋** `rule-ratification`: its Render, `vault/wiki/ratification.md`, says which sprints keep plain Case ids.
> **＋** `.guppi/guppi/ship.py`: `guppi ship`, which writes the clean version and removes a bracket that holds a pointer.
> **＋** `.guppi/guppi/caseid.py`: holds the list `PLAIN_SPRINTS`.
> **＋** `estimate-clean-branch-ships-neutral-texts`: read again, its Criterion unchanged.
> **＋** `rule-case-protocol`: a pointer in the new text of a page with `core: true` stands in a bracket at the end of its sentence.

> **when:**
> Someone reads `vault/wiki/rules/schema.yaml`, `vault/wiki/entities/schema.yaml` and `vault/wiki/ratification.md` in the repository of GUPPI, and in the clean version that `uv run --project .guppi guppi ship --allow-draft <folder>` writes into an empty folder.

> **then:**
> Both schemas call `core` the mark of a part of GUPPI, which `guppi ship`, run in the repository of GUPPI, writes into the clean version that others install, and say that a page without the mark belongs to the repository that holds it.
> **＋** `vault/wiki/ratification.md` says that the sprints that `PLAIN_SPRINTS` of `.guppi/guppi/caseid.py` lists keep plain Case ids to their close.
> **＋** In the repository of GUPPI, a bracket at the end of that sentence names the sprints `migration` and `plugin` beside its pointer.
> **－** The clean version holds no such bracket, since `guppi ship` removes it whole.

> **tasks:**
> - [ ] update `rule-rules-schema`
>   - old: `` The page ships in the clean version of GUPPI that `guppi ship` writes for the branch `prod`; a page without it stays in this repository only. ``
>   - new: `` The page is part of GUPPI: in the repository of GUPPI, `guppi ship` writes it into the clean version that a project installs; a page without it is a page of the project that holds it. ``
>   - change: `the description of core names the repository of GUPPI and says that a page without it is a page of the project that holds it`
> - [ ] update `rule-entities-schema`
>   - old: `` The page ships in the clean version of GUPPI that `guppi ship` writes for the branch `prod`; a page without it stays in this repository only. ``
>   - new: `` The page is part of GUPPI: in the repository of GUPPI, `guppi ship` writes it into the clean version that a project installs; a page without it is a page of the project that holds it. ``
>   - change: `the description of core names the repository of GUPPI and says that a page without it is a page of the project that holds it`
> - [ ] update `rule-ratification`
>   - old: `` and the sprints `migration` and `plugin` keep that form to their close: every reader takes both forms, and no such id is renamed. ``
>   - new: `` and the sprints that `PLAIN_SPRINTS` of `.guppi/guppi/caseid.py` lists keep that form to their close (the sprints `migration` and `plugin` of the repository of GUPPI, as set in case 788.2). Every reader takes both forms, and no such id is renamed. ``
>   - change: `the sentence on plain Case ids names the list PLAIN_SPRINTS, and the sprints migration and plugin stand in the bracket of its pointer`
> - [ ] update `estimate-clean-branch-ships-neutral-texts`
>   - set:
>     ```
>     status: pending
>     method: "by hand, after the librarian's run of the session that set this method, with a tag prod-x.y.z in the history of HEAD: uv run --project .guppi guppi ship --allow-draft into an empty temporary folder, and each sentence of the pages and the files it wrote read whole against the Criterion, never found by a keyword search, each sentence that holds only in the repository of GUPPI listed in the estimate line (the session of case 856)"
>     ```
>   - sections.Criterion:
>     ```
>     When:
>     Someone reads the pages and the files of the clean version that `uv run --project .guppi guppi ship --allow-draft <folder>`, as `rule-clean-branch` sets it, writes into an empty folder.
>
>     Then:
>     `entity-guppi` describes GUPPI as a harness and a vault, and not as the thing that the project builds.
>     **＋** `rule-language` and `rule-case-build` name the language of the repository and the language of the chat by their role, not as English and Russian.
>     **＋** No other sentence of the rules, the entities and `CLAUDE.md` of the clean version holds only in the repository of GUPPI, such as one that takes its repository on GitHub or its languages for those of the project.
>     **＋** The reader lists, in the estimate line, each sentence of the `purpose`, the `method` and the `## Criterion` of each shipped Estimate that holds only in the repository of GUPPI, for a Case of a later session to rewrite.
>     **－** A sentence of a shipped Estimate on that list does not fail this promise.
>     **－** The History of a page, a sample in a code span or a fenced block, and the values of the Render of `rule-guppi-config` are no part of this promise.
>     ```
>   - change: `read again after the three sentences are rewritten; the method waits for the librarian's run of this session and reads each sentence whole`
> - [ ] `uv run --project .guppi guppi render`: `vault/wiki/rules/schema.yaml`
> - [ ] `uv run --project .guppi guppi render`: `vault/wiki/entities/schema.yaml`
> - [ ] `uv run --project .guppi guppi render`: `vault/wiki/ratification.md`
> - [ ] read `estimate-clean-branch-ships-neutral-texts`

> **ratification:**
> ```
> - decision[case 856.1][update][rule-rules-schema]{ref:rule-rules-schema}
> - decision[case 856.1][update][rule-entities-schema]{ref:rule-entities-schema}
> - decision[case 856.1][update][rule-ratification]{ref:rule-ratification}
> - decision[case 856.1][update][estimate-clean-branch-ships-neutral-texts]{ref:rule-clean-branch}
> ```

### Case 856.2 — The shipped Estimates name no past event and no sprint of GUPPI

> **given:**
> `estimate-skill-sprint-close-migration-merged-into-main`: deleted.
> **＋** `rule-skill-sprint-close`: drops it from `estimates`.
> **＋** `estimate-sprint-close-archives-done-insights-and-lone-lessons`: its method changes.
> **＋** `estimate-sprint-close-archives-the-decisions`: its method changes.
> **＋** `estimate-sprint-close-archives-the-sprint-page-and-keeps-the-rest`: its method changes.
> **＋** `estimate-skill-sprint-open-merges-the-closed-sprint-branch`: checks the merge of a closed sprint.
> **＋** `.guppi/guppi/ship.py`: `guppi ship`, which writes only the `passed` Estimates.
> **＋** `vault/wiki/sprint.md`: names the open sprint.

> **when:**
> Someone reads the Estimates of the clean version that `uv run --project .guppi guppi ship --allow-draft <folder>` writes into an empty folder.

> **then:**
> The clean version holds no `estimate-skill-sprint-close-migration-merged-into-main`, since it stands `archived`.
> **＋** `rule-skill-sprint-close` no longer lists it in `estimates`.
> **＋** The hand step of the method of `estimate-sprint-close-archives-done-insights-and-lone-lessons`, `estimate-sprint-close-archives-the-decisions` and `estimate-sprint-close-archives-the-sprint-page-and-keeps-the-rest` previews `--sprint <id>`, `<id>` the sprint that `vault/wiki/sprint.md` names.
> **－** The Criterion and the `passed` status of those three Estimates do not change.
> **－** `estimate-skill-sprint-open-merges-the-closed-sprint-branch` still checks the merge of a closed sprint.

> **tasks:**
> - [ ] delete `estimate-skill-sprint-close-migration-merged-into-main`
>   - impact: `the one reading of the merge of migration into main leaves the live vault and the clean version; estimate-skill-sprint-open-merges-the-closed-sprint-branch checks the merge of a closed sprint`
>   - change: `deleted: it records one past merge, which the opening Case of a sprint now holds`
> - [ ] update `rule-skill-sprint-close`
>   - set:
>     ```
>     estimates: ["[[estimate-skill-sprint-close-leads-the-closing-session]]"]
>     ```
>   - change: `estimate-skill-sprint-close-migration-merged-into-main removed from estimates`
> - [ ] update `estimate-sprint-close-archives-done-insights-and-lone-lessons`
>   - set:
>     ```
>     method: "pytest .guppi/tests/test_sprint_close.py -k insights; by hand, the output of the preview uv run --project .guppi guppi sprint-close --sprint <id> over the live vault, <id> the sprint that vault/wiki/sprint.md names, read against the Then"
>     ```
>   - change: `the hand step previews the open sprint, not migration`
> - [ ] update `estimate-sprint-close-archives-the-decisions`
>   - set:
>     ```
>     method: "pytest .guppi/tests/test_sprint_close.py -k decisions; by hand, the output of the preview uv run --project .guppi guppi sprint-close --sprint <id> over the live vault, <id> the sprint that vault/wiki/sprint.md names, read against the Then"
>     ```
>   - change: `the hand step previews the open sprint, not migration`
> - [ ] update `estimate-sprint-close-archives-the-sprint-page-and-keeps-the-rest`
>   - set:
>     ```
>     method: "pytest .guppi/tests/test_sprint_close.py -k sprint_page; by hand, the output of the preview uv run --project .guppi guppi sprint-close --sprint <id> over the live vault, <id> the sprint that vault/wiki/sprint.md names, read against the Then"
>     ```
>   - change: `the hand step previews the open sprint, not migration`

> **ratification:**
> ```
> - decision[case 856.2][delete][estimate-skill-sprint-close-migration-merged-into-main]{ref:estimate-skill-sprint-close-migration-merged-into-main}
> - decision[case 856.2][update][rule-skill-sprint-close]{ref:rule-skill-sprint-close}
> - decision[case 856.2][update][estimate-sprint-close-archives-done-insights-and-lone-lessons]{ref:rule-sprint-close}
> - decision[case 856.2][update][estimate-sprint-close-archives-the-decisions]{ref:rule-sprint-close}
> - decision[case 856.2][update][estimate-sprint-close-archives-the-sprint-page-and-keeps-the-rest]{ref:rule-sprint-close}
> ```

### Case 856.3 — A core page comes into a project with its passed Estimates

> **given:**
> `rule-rules-schema`: its Render, `vault/wiki/rules/schema.yaml`, says what a page with `core: true` brings into a new project.
> **＋** `estimate-rules-schema-checked`: its Criterion is replaced whole.
> **＋** `.guppi/guppi/render.py`: `guppi render`, which writes the schema from the Render.
> **＋** `.guppi/guppi/lint.py`: `guppi lint`, which reads the schema.
> **＋** `.guppi/guppi/ship.py`: `guppi ship`, which writes each `passed` Estimate of a page it writes whose `method` names no target of the `Makefile`.
> **＋** `rule-case-protocol`: a pointer in the new text of a page with `core: true` stands in a bracket at the end of its sentence.

> **when:**
> `guppi render` writes `vault/wiki/rules/schema.yaml` from `rule-rules-schema`, and `guppi lint` reads a page of `vault/wiki/rules/`.

> **then:**
> The file equals the Render. Lint reads from it: required `type, kind, purpose, status, estimates, origin, sprint, created, tags`; optional `enforcement, implementation_ref, governs, render_mode, parent, children, deferred_by, applies_to, core`; values `kind: MOC | Leaf`, `status: draft | built | archived`, `enforcement: hook | check | render`, `render_mode: full | partial`, `core: true`; conditional — `hook` and `check` require `implementation_ref`, `render` requires `governs`, `render_mode` and the section `## Render`, `MOC` requires `children` and forbids `enforcement: hook | check`; the sections `## Purpose` and `## History` required, `## Render` and `## How it works` optional.
> **＋** The file also holds `ordered_children: true`, which lint does not read.
> **＋** A Rule page with these fields, values and sections has no `schema` finding; one lacking a required field, with a value outside the list, with a conditional not met or lacking a required section has one finding per defect; a rule with `applies_to` on a live Entity has none.
> **＋** A Rule page in the shape with `core: true`, `origin: guppi` and `sprint: guppi` has no `schema` finding.
> **＋** `fields` and `sections` describe each name of these lists, `core` among them, and the descriptions of `origin` and `sprint` name the value `guppi` on a page with `core: true` in the clean version; `description` holds the introduction, Ordering, MOCs and enforcement, Enforcement, the sentence on the edge Rule → Entity, the one on the guard of the agent's own conduct and the one on the Estimates that a shipped page brings along; `examples` holds the example pages.
> **＋** That last sentence says that a shipped page arrives with each of its Estimates that passed in the repository it came from and whose `method` names no target of the `Makefile`, and that the receiving project writes its other Estimates through its own Cases.

> **tasks:**
> - [ ] update `rule-rules-schema`
>   - old: `` a page with `core: true` comes into a new project without its Estimates, and that project writes its own through its Cases (case 804). ``
>   - new: `` a page with `core: true` comes into a new project with each of its Estimates that passed in the repository of GUPPI and whose `method` names no target of the `Makefile`, and that project writes its other Estimates through its Cases (as set in cases 804 and 822). ``
>   - change: `a page with core: true comes into a new project with its passed Estimates`
> - [ ] update `estimate-rules-schema-checked`
>   - set:
>     ```
>     status: pending
>     method: "pytest .guppi/tests/test_schemas.py -k rules on the live vault/wiki/rules/schema.yaml — a page in the shape, then one defect at a time; by hand, after the librarian's run of the session that sets this method: the live vault/wiki/rules/schema.yaml read against the Criterion, and the live reading uv run --project .guppi guppi check, no schema finding on wiki/rules/ but the placeholders"
>     ```
>   - change: `the Criterion replaced whole — the description says that a page with core: true comes into a new project with its passed Estimates`
> - [ ] `uv run --project .guppi guppi render`: `vault/wiki/rules/schema.yaml`
> - [ ] read `estimate-rules-schema-checked`

> **ratification:**
> ```
> - decision[case 856.3][update][rule-rules-schema]{ref:rule-rules-schema}{supersedes:case 828}
> - decision[case 856.3][update][estimate-rules-schema-checked]{ref:rule-rules-schema}
> ```
