<!-- approved 19:32:12 · session 8b3cba41 -->

# Session 1712 — the sprint plugin: neutral texts of the clean version

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

```then
update:
- slug: rule-rules-schema
  replace:
  - old: The page ships in the clean version of GUPPI that `guppi ship` writes for the branch `prod`; a page without it stays in this repository only.
    new: 'The page is part of GUPPI: in the repository of GUPPI, `guppi ship` writes it into the clean version that a project installs; a page without it is a page of the project that holds it.'
  change: the description of core names the repository of GUPPI and says that a page without it is a page of the project that holds it
- slug: rule-entities-schema
  replace:
  - old: The page ships in the clean version of GUPPI that `guppi ship` writes for the branch `prod`; a page without it stays in this repository only.
    new: 'The page is part of GUPPI: in the repository of GUPPI, `guppi ship` writes it into the clean version that a project installs; a page without it is a page of the project that holds it.'
  change: the description of core names the repository of GUPPI and says that a page without it is a page of the project that holds it
- slug: rule-ratification
  replace:
  - old: 'and the sprints `migration` and `plugin` keep that form to their close: every reader takes both forms, and no such id is renamed.'
    new: and the sprints that `PLAIN_SPRINTS` of `.guppi/guppi/caseid.py` lists keep that form to their close (the sprints `migration` and `plugin` of the repository of GUPPI, as set in case 788.2). Every reader takes both forms, and no such id is renamed.
  change: the sentence on plain Case ids names the list PLAIN_SPRINTS, and the sprints migration and plugin stand in the bracket of its pointer
- slug: estimate-clean-branch-ships-neutral-texts
  set:
    status: pending
    method: 'by hand, after the librarian''s run of the session that set this method, with a tag prod-x.y.z in the history of HEAD: uv run --project .guppi guppi ship --allow-draft into an empty temporary folder, and each sentence of the pages and the files it wrote read whole against the Criterion, never found by a keyword search, each sentence that holds only in the repository of GUPPI listed in the estimate line (the session of case 856)'
  sections:
    Criterion: |-
      When:
      Someone reads the pages and the files of the clean version that `uv run --project .guppi guppi ship --allow-draft <folder>`, as `rule-clean-branch` sets it, writes into an empty folder.

      Then:
      `entity-guppi` describes GUPPI as a harness and a vault, and not as the thing that the project builds.
      **＋** `rule-language` and `rule-case-build` name the language of the repository and the language of the chat by their role, not as English and Russian.
      **＋** No other sentence of the rules, the entities and `CLAUDE.md` of the clean version holds only in the repository of GUPPI, such as one that takes its repository on GitHub or its languages for those of the project.
      **＋** The reader lists, in the estimate line, each sentence of the `purpose`, the `method` and the `## Criterion` of each shipped Estimate that holds only in the repository of GUPPI, for a Case of a later session to rewrite.
      **－** A sentence of a shipped Estimate on that list does not fail this promise.
      **－** The History of a page, a sample in a code span or a fenced block, and the values of the Render of `rule-guppi-config` are no part of this promise.
  change: read again after the three sentences are rewritten; the method waits for the librarian's run of this session and reads each sentence whole
```

```tasks
- [x] update `rule-rules-schema`
- [x] update `rule-entities-schema`
- [x] update `rule-ratification`
- [x] update `estimate-clean-branch-ships-neutral-texts`
- [x] `uv run --project .guppi guppi render`: `vault/wiki/rules/schema.yaml`
- [x] `uv run --project .guppi guppi render`: `vault/wiki/entities/schema.yaml`
- [x] `uv run --project .guppi guppi render`: `vault/wiki/ratification.md`
- [x] read `estimate-clean-branch-ships-neutral-texts`
```

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

```then
update:
- slug: rule-skill-sprint-close
  set:
    estimates:
    - '[[estimate-skill-sprint-close-leads-the-closing-session]]'
  change: estimate-skill-sprint-close-migration-merged-into-main removed from estimates
- slug: estimate-sprint-close-archives-done-insights-and-lone-lessons
  set:
    method: pytest .guppi/tests/test_sprint_close.py -k insights; by hand, the output of the preview uv run --project .guppi guppi sprint-close --sprint <id> over the live vault, <id> the sprint that vault/wiki/sprint.md names, read against the Then
  change: the hand step previews the open sprint, not migration
- slug: estimate-sprint-close-archives-the-decisions
  set:
    method: pytest .guppi/tests/test_sprint_close.py -k decisions; by hand, the output of the preview uv run --project .guppi guppi sprint-close --sprint <id> over the live vault, <id> the sprint that vault/wiki/sprint.md names, read against the Then
  change: the hand step previews the open sprint, not migration
- slug: estimate-sprint-close-archives-the-sprint-page-and-keeps-the-rest
  set:
    method: pytest .guppi/tests/test_sprint_close.py -k sprint_page; by hand, the output of the preview uv run --project .guppi guppi sprint-close --sprint <id> over the live vault, <id> the sprint that vault/wiki/sprint.md names, read against the Then
  change: the hand step previews the open sprint, not migration
delete:
- slug: estimate-skill-sprint-close-migration-merged-into-main
  impact: the one reading of the merge of migration into main leaves the live vault and the clean version; estimate-skill-sprint-open-merges-the-closed-sprint-branch checks the merge of a closed sprint
  change: 'deleted: it records one past merge, which the opening Case of a sprint now holds'
```

```tasks
- [x] delete `estimate-skill-sprint-close-migration-merged-into-main`
- [x] update `rule-skill-sprint-close`
- [x] update `estimate-sprint-close-archives-done-insights-and-lone-lessons`
- [x] update `estimate-sprint-close-archives-the-decisions`
- [x] update `estimate-sprint-close-archives-the-sprint-page-and-keeps-the-rest`
```

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

```then
update:
- slug: rule-rules-schema
  replace:
  - old: 'a page with `core: true` comes into a new project without its Estimates, and that project writes its own through its Cases (case 804).'
    new: 'a page with `core: true` comes into a new project with each of its Estimates that passed in the repository of GUPPI and whose `method` names no target of the `Makefile`, and that project writes its other Estimates through its Cases (as set in cases 804 and 822).'
  change: 'a page with core: true comes into a new project with its passed Estimates'
- slug: estimate-rules-schema-checked
  set:
    status: pending
    method: 'pytest .guppi/tests/test_schemas.py -k rules on the live vault/wiki/rules/schema.yaml — a page in the shape, then one defect at a time; by hand, after the librarian''s run of the session that sets this method: the live vault/wiki/rules/schema.yaml read against the Criterion, and the live reading uv run --project .guppi guppi check, no schema finding on wiki/rules/ but the placeholders'
  change: 'the Criterion replaced whole — the description says that a page with core: true comes into a new project with its passed Estimates'
```

```tasks
- [x] update `rule-rules-schema`
- [x] update `estimate-rules-schema-checked`
- [x] `uv run --project .guppi guppi render`: `vault/wiki/rules/schema.yaml`
- [x] read `estimate-rules-schema-checked`
```

## Case 857 — The close commit takes each file the render writes

> **context:**
> At the end of its run the librarian makes one commit, by the command that the Render of `rule-close` writes into `.claude/agents/librarian-guppi.md`: `git add vault CLAUDE.md .claude guppi.toml`, and never a path outside those four. The render writes each file that a live Rule page names in `governs` (`plan` and `write_all` of `.guppi/guppi/render.py`), and since case 818.1 one of them, `plugin/skills/install/SKILL.md` of `rule-plugin-install`, lies outside the four paths. The brief of session 0342 reports it under Flags: "The render wrote `plugin/skills/install/SKILL.md`, which lies outside the four paths of the close commit (`vault`, `CLAUDE.md`, `.claude`, `guppi.toml`); it stays modified after this run's commit." `git status` shows that file modified now; the Work item of the Frontier on the dirty tree commits it, and this Case does not.
>
> The person chose that `guppi render` gets an option `--paths`, which prints each file the render writes, and that the commit adds `vault` and those files. A fixed list that names `plugin` was turned down: `rule-close` has `core: true` and ships, a project that installs GUPPI has no `plugin/` folder since `rule-plugin-install` does not ship, and the sentence would hold only in the repository of GUPPI, against the third `Then` line of `estimate-clean-branch-ships-neutral-texts`. The new Render holds no pointer to a case, so no bracket is needed for `guppi ship`. `--paths` prints the keys of `plan`, the same function that decides what the render writes, so the list is no second copy of that judgment (`rule-one-judgment-one-implementation`). A Grep for `governs` over `.guppi/guppi/` printed 68 matches in nine files: `generate.py`, `lint.py`, `sprint.py`, `guard.py`, `backlog.py`, `ship.py`, `glossary.py`, `prespec.py` and `render.py`. `governed_paths` of `prespec.py`, the map of `guard.py` and `governed` of `ship.py` answer other questions (the rule of a path named in a Spec, the guard of a hand edit, the files of the pages with `core: true`), and the task calls none of them and copies none.
>
> `estimate-close-commits` (passed) names the four paths in its `purpose` and its Criterion, and its last line forbids any other path, so this Case replaces its Criterion whole and sets its `purpose` and `method` anew. No old line of that Criterion is carried word for word: each one that names the four paths is written again with `vault/` and the list of `--paths`, and the lines on the single commit, its message, `--amend` and the report keep their meaning in the new wording. Claude Code loads an agent file when the agent is dispatched, so the librarian's run of this session still commits by the old command, and the first commit by the new one comes at the next librarian run after the render of `.claude/agents/librarian-guppi.md`: the `method` waits for that event. The Estimates of `rule-render-harness` speak of the render without a flag, with `--check` and with `--sync`, and not of `--paths`, so they stand. A Grep for `git add vault` over the repository outside `vault/raw/` and `vault/archive/` printed `vault/wiki/rules/rule-close.md`, `vault/wiki/estimates/estimate-close-commits.md` and `.claude/agents/librarian-guppi.md`: the two pages enter this Case, and the rendered agent file follows the render. A Grep for `librarian-guppi` over `.guppi/tests/` printed `test_grepguard.py`, which uses the name only as an agent type and does not read the file. `test_render.py` builds its vault under `tmp_path`. The last output of `guppi check` that the brief reports names no finding on these pages.

> **problem:**
> The close commit of the librarian names four fixed paths, and the render writes a file outside them, so that file stays uncommitted after the run.

> **recommend:**
> - **How should the close commit find the files the render wrote?**
>   - Recommended: (b) a command prints the files the render writes, and the commit adds `vault` and those files.
>   - Answer: agreed, (b).
> - **How is the fix checked?**
>   - Recommended: (a) replace the Criterion of `estimate-close-commits` whole.
>   - Answer: agreed, (a).

> **given:**
> `rule-close`: its Render sets the close commit of the librarian in `.claude/agents/librarian-guppi.md`.
> **＋** `estimate-close-commits`: its Criterion is replaced whole.
> **＋** `vault/`: the folder of the pages, which the commit takes whole.
> **＋** `.guppi/guppi/render.py`: `guppi render`, which gains the option `--paths`.
> **＋** `.guppi/tests/test_render.py`: the tests of the render.
> **＋** `rule-plugin-install`: renders `plugin/skills/install/SKILL.md`, outside `vault`, `CLAUDE.md`, `.claude` and `guppi.toml`.
> **＋** `rule-one-judgment-one-implementation`: the list of files comes from the code that writes them.
> **＋** `estimate-clean-branch-ships-neutral-texts`: a shipped sentence holds in any project.

> **when:**
> After a live run, the librarian commits at the close, as `.claude/agents/librarian-guppi.md` says, with the list that `uv run --project .guppi guppi render --paths` prints.

> **then:**
> `uv run --project .guppi guppi render --paths` prints each file that `guppi render` writes, one path per line, and writes nothing.
> **＋** `git log` shows one commit after the Retro commit, separate from the session's, with the message `docs(vault): librarian, <date>`, and never `--amend`.
> **＋** The commit takes `vault/` and each file of that list: `git add vault $(uv run --project .guppi guppi render --paths)`.
> **＋** After the commit, `git status` shows no file that `.guppi/guppi/render.py` wrote as modified or untracked.
> **＋** The report reaches the main agent with the counts, the flags and the lint total, in twenty lines or fewer.
> **－** The commit takes no path that neither `vault/` nor that list names.
> **－** In a project without `rule-plugin-install`, the list and the commit name no `plugin/skills/install/SKILL.md`.

```then
update:
- slug: rule-close
  replace:
  - old: 'files the render wrote: `git add vault CLAUDE.md .claude guppi.toml && git commit -m "docs(vault): librarian, <date>"`, never `--amend`, never a path outside those four. After the commit, no file the render wrote stands untracked.'
    new: 'files the render wrote: `git add vault $(uv run --project .guppi guppi render --paths) && git commit -m "docs(vault): librarian, <date>"`, never `--amend`, never a path that neither `vault` nor that list names. After the commit, no file the render wrote stands modified or untracked.'
  change: the commit takes vault and each file that guppi render --paths prints, in place of four fixed paths
- slug: estimate-close-commits
  set:
    status: pending
    purpose: The librarian's run ends in one separate commit of vault and each file the render writes, with no rendered file left modified or untracked, and a report of twenty lines or fewer
    method: 'uv run --project .guppi pytest .guppi/tests/test_render.py -k paths; by hand, after the librarian''s run of the next session, whose .claude/agents/librarian-guppi.md holds the new Render of rule-close: git log shows its commit and the paths it touched, git status shows no file the render wrote as modified or untracked, and the report is read in the transcript'
  change: the Criterion replaced whole — the commit takes vault and each file that guppi render --paths prints
```

```tasks
- [x] update `rule-close`
- [x] update `estimate-close-commits`
- [x] `.guppi/guppi/render.py`: the option `--paths`, in the group of `--check` and `--sync`, prints the keys of `plan`, one per line, writes nothing, ticks nothing and exits 0; a render error goes to stderr with exit 1 and prints no path; the docstring names the option and the close commit that reads it.
- [x] `.guppi/tests/test_render.py`: tests `paths` — a vault with a `full` and a `partial` page on two files prints each `governs` path once and writes nothing; a render error prints no path and exits 1.
- [x] `uv run --project .guppi guppi render`: `.claude/agents/librarian-guppi.md`
- [ ] read `estimate-close-commits`
```

## Case 859 — The starter session files open the sprint at the first /hi in a git repository

> **context:**
> `guppi ship` writes starter session files into the clean version of GUPPI in place of the session files of this repository: a closed sprint page, a backlog, a glossary, a brief that opens the next sprint and a log. With them, the first `/hi` of a new project starts `/sprint-open`. `estimate-clean-branch-writes-the-session-files` checks this. Its reading at the Retro of session 0104 passed every line but the last. In an empty folder with no git repository, the first `/hi` stopped on `fatal: not a git repository`. After `git init`, the next `/hi` started `/sprint-open` before the Frontier (its `## Result`). Since the render of session 0342, `/hi` in a folder with no git runs `uv run --project .guppi guppi gitstate`, asks whether to run `git init -b main`, and ends after either answer. Only the next `/hi` starts `/sprint-open` (the Render of `rule-git-context`, as set in case 851.1). So the last line of the Criterion, "the first `/hi` starts `/sprint-open`", cannot pass in a folder with no git, even when the starter files are right. Case 855 put the Estimate off until that render, which has run. The brief of session 0342 reports it under Flags: "Lint: `unread: failed` — `estimate-clean-branch-ships-neutral-texts`, `estimate-clean-branch-writes-the-session-files`."
>
> The person chose to replace the Criterion whole. Its last `Then` line now speaks of the first `/hi` whose `Branch:` line names a branch. A `－` line leaves the `/hi` that reads `none: this folder is no git repository` out of this promise. `estimate-git-context-offers-git-init` already checks that `/hi`, and that the next `/hi` starts `/sprint-open`. Nothing is signed twice (`rule-case-protocol`), so this Estimate does not repeat the git step. The `When` says that the person types `/hi` again after the git step where the folder has no git, so that the Criterion reads without the Case. Two lines change: the `＋` line of the `When` on the install and `/hi`, and the last `＋` line of the `Then` on the first `/hi`. The other lines keep their words. The `purpose` names the old promise, so it is set anew in the same `update`. The `method` is set anew too. Its hand reading waits for the librarian's run of this session, since the new Criterion lands on the page only then. The reading shares the copy and the empty folder with no git of the reading of `estimate-git-context-offers-git-init`. The third `/hi` of that reading is the first `/hi` in a git repository. Both readings belong to the install session that Frontier item C3 plans, after that run, and this Case does not take up C3. Keeping the Criterion and narrowing only the method was turned down: the words would still promise the first `/hi` in any empty project. Dropping the line was turned down too: this Estimate would no longer check that the starter files open a sprint.
>
> The person chose to take up the defer now. The decision line carries `{supersedes:case 855}` and names the Estimate, so `generate` retires the defer and `backlog.md` drops the Estimate at the next `guppi backlog`. The mark retires the one defer of `decision-case-855`, so the cascade archives that page after this Case. Case 858 of this session would have added an `updated:` History line to that page. The person took it back by the short Case 863, so no History line is added, and `decision-case-855` goes to the archive without a correction. It stays the record of what was true when the defer was signed.
>
> How it is checked: this Case replaces the Criterion of `estimate-clean-branch-writes-the-session-files`, which sets it `pending`.
>
> Searches. A Grep for `writes-the-session-files` over the repository outside `vault/raw/` and `vault/archive/` printed `vault/wiki/brief.md`, `vault/wiki/backlog.md`, `vault/wiki/log.md`, `vault/wiki/rules/rule-clean-branch.md` and `vault/wiki/estimates/estimate-clean-branch-writes-a-clean-copy.md`. The brief and the log are records. `guppi backlog` rewrites the backlog. The rule lists the Estimate in `estimates`, which stays true. The other Estimate points to this one for the files it writes in place of the session files, and that part does not change. A Grep for `writes-the-session-files` over `.guppi/tests/` printed nothing, so no test reads the page live. A Grep for ``first `?/hi`?`` over `vault/wiki/rules/` printed `rule-clean-branch.md`, `rule-git-context.md`, `rule-plugin-install.md` and `rule-morph.md`. The Purpose of `rule-clean-branch` says that the first `/hi` finds each file it loads, which holds in either folder. It says that `/hi`, not the first `/hi`, starts `/sprint-open`, so it stands. The `How it works` of `rule-git-context` tells the history of the git error and stands. `rule-plugin-install` says that the first `/hi` renders the harness, which this Case does not touch. `rule-morph` is `draft`, and its setup Case, which comes at the first `/hi` before the first sprint, is not built. Case 851 set the git step before it, and this Case does not change that order. `estimate-morph-sets-up-the-project-at-the-first-hi` (`pending`, target `rule-morph`) speaks of the same first `/hi`. Its `When` is the `/hi` typed after `/guppi:install` and a reopen. Its `Then` puts the setup Case first, then `/sprint-open` in the same session, and takes the name of the main branch from git. In a folder with no git, that `/hi` ends at the git step, so its Criterion has the same fault as the line this Case replaces. It stands in this Case for two reasons. Its `method` waits for the session whose Work Mode builds the setup skill of `rule-morph`, so no reading of it runs before that skill is built. Also, the Case that builds that skill writes the setup step and can set where it stands beside the git step. This Case changes no promise of `rule-morph`.

> **problem:**
> The last promise of `estimate-clean-branch-writes-the-session-files` says that the first `/hi` in an empty project starts `/sprint-open`. Since the git step of `/hi`, that `/hi` ends in a folder with no git, so the Estimate cannot pass there, and it stays failed and put off although the event its defer waited for has come.

> **recommend:**
> - **What should the last promise say about the first `/hi`?**
>   - Recommended: (a) the first `/hi` in a git repository: replace the Criterion whole, its last line on the first `/hi` whose `Branch:` line names a branch, with the purpose and the method written again to match.
>   - Answer: agreed, (a).
> - **Should the Estimate leave the backlog now?**
>   - Recommended: (a) take it up now: retire the defer, and run the reading in the same empty folder with no git as the reading of `estimate-git-context-offers-git-init`.
>   - Answer: agreed, (a). Before the answer, the main agent noted that the new Criterion lands on the page only at the librarian's run of this session, so the hand reading runs in the install session of item C3, after that run.

> **given:**
> `estimate-clean-branch-writes-the-session-files`: its Criterion is replaced whole, and the defer of `decision-case-855` is retired.
> **＋** `rule-clean-branch`: `guppi ship` writes the starter session files into the clean version.
> **＋** `vault/wiki/sprint.md`, `vault/wiki/backlog.md`, `vault/wiki/glossary.md`, `vault/wiki/brief.md` and `vault/wiki/log.md`: the starter session files, the first written by `closed_form` of `.guppi/guppi/sprint.py`.
> **＋** `/guppi:install`: the skill of the plugin that copies GUPPI into a project, as `rule-plugin-install` sets it.
> **＋** `rule-git-context`: the `Branch:` line of `/hi`, which runs `uv run --project .guppi guppi gitstate`, and the git step outside a repository.
> **＋** `estimate-git-context-offers-git-init`: checks the `/hi` in a folder with no git, and its reading shares the install.
> **＋** `rule-skill-sprint-open`: its hook on `/hi` asks for `/sprint-open` before the Frontier.

> **when:**
> `uv run --project .guppi guppi ship <folder>`, as `rule-clean-branch` sets it, builds the clean version of the project from its working tree into an empty folder.
> **＋** Or, in an empty project, the person installs the plugin `guppi` from such a copy, types `/guppi:install`, reopens Claude Code there and types `/hi`, and types `/hi` again after the git step of `rule-git-context` where the folder is no git repository.

> **then:**
> It writes `vault/wiki/sprint.md` as `closed_form` of `.guppi/guppi/sprint.py` writes it for the sprint `guppi`, so its first `## ` heading carries the mark of a closed sprint.
> **＋** It writes `vault/wiki/backlog.md` and `vault/wiki/glossary.md` as `guppi backlog` and `guppi glossary` write them over the clean version, by their own code.
> **＋** It writes a `vault/wiki/brief.md` whose `Cases` of its `## Next session` open with the line `open the next sprint — no sprint is open since the close of guppi`, and a `vault/wiki/log.md` that holds its heading and the paragraph under it alone.
> **＋** Over the clean version, `guppi sprint --check`, `guppi backlog --check` and `guppi glossary --check` print nothing and exit 0.
> **＋** In that project, the first `/hi` whose `Branch:` line, the output of `uv run --project .guppi guppi gitstate`, names a branch starts `/sprint-open` before the Frontier.
> **－** A `/hi` whose `Branch:` line reads `none: this folder is no git repository` is no part of this promise.
> **－** It writes no `sprint.md`, `backlog.md`, `brief.md`, `glossary.md` or `log.md` of the project it builds from.

```then
update:
- slug: estimate-clean-branch-writes-the-session-files
  set:
    status: pending
    purpose: Whether guppi ship writes sprint.md in the closed form of the sprint guppi, backlog.md and glossary.md by their writers, a brief.md that opens the next sprint and a log.md with its heading alone, so that the checks of those files pass and the first /hi of a new project in a git repository starts /sprint-open
    method: 'uv run --project .guppi pytest .guppi/tests/test_ship.py -k skeleton; by hand, after the librarian''s run of the session that set this method, with a tag prod-x.y.z in the history of HEAD: in an empty folder that is no git repository, guppi installed from a copy that uv run --project .guppi guppi ship --allow-draft wrote into a local folder, the copy and the folder being those of the reading of estimate-git-context-offers-git-init where that reading runs at the same commit, /guppi:install typed, Claude Code reopened, /hi typed until its git step has run git init -b main, the next /hi typed, and guppi sprint --check, guppi backlog --check and guppi glossary --check run over the copy, read against the Criterion'
  change: 'the Criterion replaced whole — the first /hi whose Branch: line names a branch starts /sprint-open, and the /hi of the git step is no part of the promise; the defer of case 855 retired'
```

```tasks
- [x] update `estimate-clean-branch-writes-the-session-files`
- [ ] read `estimate-clean-branch-writes-the-session-files`
```

## Case 860 — estimate-harness-pipeline leaves the backlog

> **context:**
> `guppi backlog` lists under `## Deferred` each live page whose `deferred_by` is not empty, whatever its status (`.guppi/guppi/backlog.py`). `estimate-harness-pipeline` carries `deferred_by: ["[[decision-case-833]]", "[[decision-case-849]]"]`. Both defers have the same problem: no Case gave the Estimate a reading moment after the librarian's run. Since then the Estimate was read and passed at the `/hi` of session 0342 (its `## Result` and the History line `status: failed → passed`). So `backlog.md` still lists it as put off in 2 sessions, although the event its defers waited for has come. The brief of session 0342 reports it under Flags: "`estimate-harness-pipeline` and `estimate-guppi-tests-green` are `passed` and keep `deferred_by` (cases 833 and 849; case 829), so `backlog.md` still lists them." The pages confirm the main agent's mapping: this Estimate carries cases 833 and 849, and `estimate-guppi-tests-green` carries case 829 alone.
>
> The fix follows "Taking up a deferred decision" of `rule-case-protocol`: one decision line names the page by an `update` with only `change`, since nothing on the page changes, and carries `{supersedes:case 833}` and `{supersedes:case 849}`. `generate` then drops both slugs from `deferred_by` and drops the empty field (`clear_deferred_by` of `.guppi/guppi/generate.py`), and the next `guppi backlog` leaves the Estimate out. An `update` of an Estimate with `change` alone writes its History and no Criterion (`.guppi/guppi/materialize.py`, case 588.2), so the status `passed`, `checked`, the Criterion and the Result stand. The marks retire the one defer of each of `decision-case-833` and `decision-case-849`, so the cascade sets both pages `superseded` and then `archived`. The person asked for the quick cleanup, so this Case gives the `method` no new reading moment; the Estimate passed with the `method` it has.
>
> By `rule-atomicity` this Case and Case 861, which clears `estimate-guppi-tests-green`, stay apart: each clears a different page by different marks, and one can fail while the other passes.
>
> How it is checked: `estimate-generate-writes-the-decision-page` already checks that a `supersedes` removes the earlier slug from the `deferred_by` of each target of its `defer` list that a decision line of the superseding Case names, and drops an empty `deferred_by`. `estimate-backlog-renders` checks that `## Deferred` holds each live page with a `deferred_by` that is not empty. This Case changes neither behaviour, so both Criteria stand, and the Criterion of `estimate-harness-pipeline` is not touched.
>
> Searches. A Grep for `harness-pipeline` over the repository outside `vault/raw/` and `vault/archive/` printed `vault/wiki/brief.md`, `vault/wiki/backlog.md`, `vault/wiki/log.md` and `vault/wiki/rules/rule-harness.md`. The brief and the log are records. `guppi backlog` rewrites the backlog. `rule-harness` lists the Estimate in `estimates`, which stays true. No file under `.guppi/tests/` names the page, so no test reads it live.

> **problem:**
> `estimate-harness-pipeline` passed, but it still carries the defers of cases 833 and 849, so `backlog.md` lists it as put off work.

> **recommend:**
> - Recommended: retire both defers by one `update` of the Estimate with only `change`, its decision line carrying `{supersedes:case 833}` and `{supersedes:case 849}`.
> - Answer: ratified as built

> **given:**
> `estimate-harness-pipeline`: the defers of `decision-case-833` and `decision-case-849` are retired.
> **＋** `rule-case-protocol`: a deferred decision is taken up by a Case that names the page and supersedes each Decision of its `deferred_by`.
> **＋** `.guppi/guppi/generate.py`: a `supersedes` clears `deferred_by` on the pages the superseding Case names.
> **＋** `.guppi/guppi/backlog.py` and `vault/wiki/backlog.md`: the backlog lists each live page with `deferred_by`.

> **when:**
> `uv run --project .guppi guppi generate` applies the decision line of this Case at the librarian's run.
> **＋** `uv run --project .guppi guppi backlog` runs after it.

> **then:**
> `estimate-harness-pipeline` carries no `deferred_by`.
> **＋** `vault/wiki/backlog.md` holds no line for `estimate-harness-pipeline`.
> **－** The status `passed`, the `checked` date, the Criterion and the Result of `estimate-harness-pipeline` do not change.

```then
update:
- slug: estimate-harness-pipeline
  change: the defers of case 833 and case 849 retired — the Estimate passed at the /hi of session 0342
```

```tasks
- [x] update `estimate-harness-pipeline`
```

## Case 861 — estimate-guppi-tests-green takes a method that fits a MOC and leaves the backlog

> **context:**
> `guppi backlog` lists under `## Deferred` each live page whose `deferred_by` is not empty, whatever its status (`.guppi/guppi/backlog.py`). `estimate-guppi-tests-green` passed on 2026-09-29, and since then case 829 put it off, so it carries `deferred_by: ["[[decision-case-829]]"]` and `backlog.md` lists it as put off in 1 session. The pages confirm the main agent's mapping: this Estimate carries case 829 alone, and `estimate-harness-pipeline` carries cases 833 and 849. The defer of case 829 is not stale. Its Problem says that no Case gave this Estimate a `method` that fits a MOC, and that problem stands. The target `entity-guppi` is a MOC, and its `method` reads "uv run --project .guppi guppi test, 0 failed; read after each Work Mode". On a MOC, `rule-estimates-schema` takes a `make <target>` of the Makefile or `pytest` with test files, and a command of the project alone earns a finding. The brief of session 0342 reports the last run of `guppi check` under Readings at the close as "12 lines (exit 1), as in Flags", and Flags holds: "Lint: `method` — `estimate-guppi-tests-green` (a MOC's Estimate names no `make <target>` or `pytest` with test files)".
>
> The person chose a reading by hand. The new `method` keeps the command and the moment, and opens with "by hand", the one spelling of a reading. `check_method` of `.guppi/guppi/lint.py` passes `by hand` on a MOC when every counted Estimate of its children is a reading. The children of `entity-guppi` are `entity-sprint` and `entity-guppi-repository`, with no Estimate, and `entity-glossary`, whose one Estimate, `estimate-glossary-terms-defined`, has a `method` with "by hand". The new `method` names no `pytest` and no Makefile target. So lint finds nothing on it, and `guppi ship` can still write the passed Estimate into the clean version, which `rule-clean-branch` refuses for a `method` that names a target of the `Makefile`. The part "after each Work Mode:" names its event before a colon, so it waits for that event and is no finding of a later session (`rule-case-protocol`, case 781). Going back to `make test` was turned down: case 820.7 made every live rule, entity and Estimate name `guppi test` and `guppi style` in place of the Makefile targets `test` and `style` (the History of `rule-guppi-config`), while the targets that run the pipeline of a MOC stay for now (the History and the Purpose of `rule-harness`), and `rule-harness` says that the clean version holds no `Makefile`. Changing the rule so that a top MOC may name `guppi test` was turned down as a promise of its own, larger than this cleanup. Retiring the defer alone was turned down, since lint would still report the `method`.
>
> The decision line names the page by an `update` that sets `method` alone, and carries `{supersedes:case 829}`. An `update` that sets a field other than `status` changes that field, and the Criterion and the status stand (`rule-case-protocol`, case 378.4). `generate` then drops `decision-case-829` from the `deferred_by` of this page, since the Case names it (`clear_deferred_by` of `.guppi/guppi/generate.py`), and sets `decision-case-829` `superseded`, so the cascade archives it. `estimate-page-schemas-one-file-per-rule`, the other page in the `defer` list of `decision-case-829`, is not named, so it keeps its `deferred_by` and stays in the backlog (case 467.3). The person chose to leave that page out of this Case, since its `method` needs a different fix. A slug in `deferred_by` that names an archived page is no `ref` finding, since lint takes a live or an archived page as a target.
>
> By `rule-atomicity` this Case and Case 860, which clears `estimate-harness-pipeline`, stay apart: each changes a different page and retires different defers, and one can fail while the other passes. Both act at the same `guppi generate` and `guppi backlog` of the librarian's run, on different pages, and do not contradict each other.
>
> How it is checked: `estimate-lint-checks-the-method` already checks this form. Its Criterion says that on a MOC `by hand` passes when every counted Estimate of the children is a reading, so its Criterion stands. `estimate-generate-writes-the-decision-page` and `estimate-backlog-renders` check the rest: the first that a `supersedes` removes the earlier slug from the `deferred_by` of each target of its `defer` list that a decision line of the superseding Case names, and keeps it on a target the Case does not name; the second that `## Deferred` holds each live page with a `deferred_by` that is not empty. This Case changes neither behaviour, so both Criteria stand. The Criterion of `estimate-guppi-tests-green` does not change, so the Estimate stays `passed`.
>
> Searches. A Grep for `guppi-tests-green` over the repository outside `vault/raw/` and `vault/archive/` printed `vault/wiki/brief.md`, `vault/wiki/backlog.md`, `vault/wiki/log.md`, `vault/wiki/entities/entity-guppi.md` and `vault/wiki/estimates/estimate-retro-red-in-the-baseline-is-not-charged.md`. The brief and the log are records. `guppi backlog` rewrites the backlog. `entity-guppi` lists the Estimate in `estimates`, which stays true. The other Estimate says that this one still wants `guppi test` with no failed test on the branch, which the unchanged Criterion keeps true. No file under `.guppi/tests/` names the page, so no test reads it live.

> **problem:**
> `estimate-guppi-tests-green` passed, but its `method` names `guppi test` alone, a form that lint refuses on the Estimate of a MOC, and the defer of case 829 that waits for a fitting `method` keeps it in `backlog.md`.

> **recommend:**
> - **What should the `method` of `estimate-guppi-tests-green` say?**
>   - Recommended: (a) a reading by hand of `guppi test` after each Work Mode, read against the Criterion, 0 failed.
>   - Answer: agreed, (a). Before the answer, the person asked why a MOC may not name `guppi test`; the reply was that the rule wants a MOC's Estimate to run the tests of its own part, which on the top MOC is the whole suite, and that a rule change would be a Case of its own.
> - **How is the fix checked?**
>   - Recommended: (a) the existing check covers it: `estimate-lint-checks-the-method`, whose Criterion stands.
>   - Answer: agreed, (a).
> - **Does the other check put off by the same defer join this Case?**
>   - Recommended: (a) leave `estimate-page-schemas-one-file-per-rule` out; it stays in the backlog.
>   - Answer: agreed, (a).

> **given:**
> `estimate-guppi-tests-green`: its `method` is set anew, and the defer of `decision-case-829` is retired.
> **＋** `entity-guppi`: the MOC the Estimate checks, whose children hold readings only.
> **＋** `rule-estimates-schema`: the forms of a `method` on the Estimate of a MOC.
> **＋** `.guppi/guppi/lint.py`: `check_method` judges the `method` of each Estimate.
> **＋** `rule-case-protocol`: a deferred decision is taken up by a Case that names the page and supersedes the Decision of its `deferred_by`.
> **＋** `.guppi/guppi/generate.py`: a `supersedes` clears `deferred_by` on the pages the superseding Case names.
> **＋** `.guppi/guppi/backlog.py` and `vault/wiki/backlog.md`: the backlog lists each live page with `deferred_by`.
> **＋** `estimate-page-schemas-one-file-per-rule`: the other page that `decision-case-829` puts off.

> **when:**
> `uv run --project .guppi guppi generate` applies the decision line of this Case at the librarian's run.
> **＋** `uv run --project .guppi guppi backlog` and `uv run --project .guppi guppi check` run after it.

> **then:**
> The `method` of `estimate-guppi-tests-green` is a reading by hand, after each Work Mode, of `uv run --project .guppi guppi test` against its Criterion.
> **＋** `guppi check` reports no `method` finding on `estimate-guppi-tests-green`.
> **＋** `estimate-guppi-tests-green` carries no `deferred_by`.
> **＋** `vault/wiki/backlog.md` holds no line for `estimate-guppi-tests-green`.
> **－** The status `passed`, the `checked` date, the `purpose`, the Criterion and the Result of `estimate-guppi-tests-green` do not change.
> **－** `estimate-page-schemas-one-file-per-rule` keeps `decision-case-829` in its `deferred_by` and stays in `vault/wiki/backlog.md`.

```then
update:
- slug: estimate-guppi-tests-green
  set:
    method: 'by hand, after each Work Mode: uv run --project .guppi guppi test, read against the Criterion, 0 failed'
  change: the method a reading by hand of guppi test, a form that fits a MOC; the defer of case 829 retired
```

```tasks
- [x] update `estimate-guppi-tests-green`
```

## Deferred

## Case 862 — The four hand readings of the install put off to one install session

> **context:**
> At /hi of session 1712 the person put off the four hand readings that the brief of session 0342 groups for one install session: `estimate-git-context-offers-git-init` (an empty folder with no git), `estimate-plugin-install-offers-to-install-uv` (a terminal with no `uv`), `estimate-plugin-install-undoes-the-copy-when-uv-sync-fails` (an offline install with an empty cache of `uv`) and `estimate-guppi-package-is-ready-after-the-install` (an install with `uv`). Each needs a copy written by `guppi ship --allow-draft` after a librarian's render and an install by hand into an empty project. No step of this session runs such an install.

> **problem:**
> No reading of the four install Estimates runs in this session, since each needs an install by hand into an empty project from a copy built after the librarian's render.

```then
defer:
  - slug: estimate-git-context-offers-git-init
    type: estimate
    purpose: "Whether /hi outside a git repository offers git init -b main and ends; its hand reading waits for one install session into an empty folder with no git; put off at /hi of session 1712"
  - slug: estimate-plugin-install-offers-to-install-uv
    type: estimate
    purpose: "Whether /guppi:install offers to install uv where it is missing; its hand reading waits for one install session from a terminal with no uv; put off at /hi of session 1712"
  - slug: estimate-plugin-install-undoes-the-copy-when-uv-sync-fails
    type: estimate
    purpose: "Whether /guppi:install undoes the copy when uv sync fails; its hand reading waits for one install session offline with an empty cache of uv; put off at /hi of session 1712"
  - slug: estimate-guppi-package-is-ready-after-the-install
    type: estimate
    purpose: "Whether .guppi is ready after /guppi:install on a machine with uv; its hand reading waits for one install session; put off at /hi of session 1712"
```

## Case 863 — The correction of decision-case-855 taken back

> **context:**
> At /pre-spec of session 1712 the person took back Case 858, which added an `updated:` History line to `decision-case-855` noting that the `/hi` that runs `git init` ends and the next `/hi` starts `/sprint-open`. The precedent it leaned on, Case 358 on `decision-case-347`, signed a text already on the page after the fact; the line of Case 858 signs no text but corrects one, a kind of line `rule-decisions-schema` does not allow. Case 859 of this session retires the one defer of `decision-case-855`, so the cascade archives that page; it stays the record of what was true when the defer was signed, and the correction stands in the case file of Case 858 and in the brief and handoff of session 0342. Case 858 creates no Estimate.

> **problem:**
> No Case of this session corrects the out-of-date sentence in the `## Context` of `decision-case-855` within the limits of `rule-decisions-schema`.

```then
defer:
  - slug: decision-case-855
    type: decision
    purpose: "Its Context says that Case 851 makes /hi go on to /sprint-open, while the ratified Case 851 ends that /hi; the correction by Case 858 was taken back, since rule-decisions-schema allows no correction line; put off at /pre-spec of session 1712"
```
