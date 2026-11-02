<!-- approved 03:32:28 · session 68effdf4 -->

# Session 0254 — a refused /hi tells the person in the chat to turn plan mode on

## Case 1001 — rule-morph ships only once it is built

> **context:**
> The workflow `.github/workflows/prod.yml` builds the clean version of GUPPI by `guppi ship` on a push of a tag `prod-x.y.z` and writes it to the branch `prod`. `is_draft_core` of `.guppi/guppi/pages.py`, which `guppi ship` and `guppi lint` import, accepts a rule or an entity with `core: true` that stands `draft` and whose History holds no line that set it `built`, or one of whose Estimates stands `failed`; while one stands, the build writes nothing (case 996.1). The brief of the last session reports, under Flags, the last `guppi check`: "Lint (`guppi check`, exit 1, 2 lines): `status: a page with core: true that is draft` on `rule-morph` and `rule-skill-approve-spec`." So `estimate-sprint-plugin-ci-writes-a-clean-branch`, the one item of the current milestone The clean branch of `entity-sprint-plugin`, cannot be read: `rule-morph` waits for its setup skill, an item of the later milestone The plugin, and `rule-skill-approve-spec` waits for its CLI trial, the Ask item A1 of this session. `rule-clean-branch` already sets the way out: "A page that blocks the build and that a new project can go without loses `core` until it is `built`". At `/pre-spec` of case 822 the person kept `core: true` on `rule-morph` while `rule-skill-merge-main` and `rule-skill-pr-review` lost it (Spec of session 2026-10-15 0553, the `**Change**` item of case 822). The person now takes `core` off `rule-morph` until it is built, since `rule-morph` itself says that until its setup step is built `/hi` puts the opening Case first in every project, so a new project gets no setup step either way. `rule-skill-approve-spec` keeps `core`: when its Estimate passes, the cascade of `.guppi/guppi/generate.py` (`cascade`, read whole) sets it `built`, and `is_draft_core` then accepts it no more. The `set` of an `update` puts its value into the page as it stands (the loop over `set` in `.guppi/guppi/generate.py`), so `core: null` leaves `is_core` false, as case 822.8 did for the two skills; `put` of `.guppi/guppi/ratified.py` takes `set` as a YAML mapping. The milestone item of `rule-morph` in The plugin gains that the Case that builds it gives `core: true` back. The Criterion of `estimate-clean-branch-refuses-a-draft-core-page` lists the pages that carry no `core` until built, so the Case replaces it whole: its other lines are carried word for word, and its line that names `rule-skill-merge-main` and `rule-skill-pr-review` is not carried but replaced by one that names `rule-morph` beside them, which is the change the person chose; the Case also sets its `method` anew: the search of the pages can find the change only after the librarian's run applies the `update` of `rule-morph`, so that part of the reading waits for that run. Its `purpose` states no list of pages and stands. A Grep of `rule-morph` over `{vault/wiki,.claude,.guppi/guppi,.guppi/tests}/**` printed 15 files: `brief.md`, `backlog.md`, `sprint.md`, `log.md`, `entity-sprint-plugin.md`, `estimate-lint-checks-the-statuses.md`, `rule-clean-branch.md`, `rule-guppi-config.md`, `rule-plugin-install.md`, `estimate-morph-sets-up-the-project-at-the-first-hi.md`, `estimate-morph-takes-in-the-set-aside-files.md`, `rule-permissions.md`, `estimate-clean-branch-ships-neutral-texts.md`, `lesson-sprint-open-asks-no-goal-of-a-new-project.md` and `rule-claude-md.md`. A Grep for `^core:` over `rule-permissions`, `rule-guppi-config`, `rule-plugin-install` and `rule-claude-md` under `vault/wiki/` printed `core: true` on `rule-permissions`, `rule-guppi-config` and `rule-claude-md`; `rule-plugin-install` carries no `core` and does not ship. `rule-claude-md` names `rule-morph` only in a History line; its Purpose already says the setup Case of a project. The Purpose of `rule-permissions` says the setup Case of `rule-morph` sets the folder name of the project, and the Purpose of `rule-guppi-config` says the setup Case of `rule-morph` sets the project's own commands and that the questions asked at setup stay with `rule-morph`. Once the clean version leaves `rule-morph` out, those sentences name a page it does not hold, which `estimate-clean-branch-ships-neutral-texts` counts as a sentence that holds only in the repository of GUPPI; at `/pre-spec` the person chose that this Case rewords them to say the setup Case of a project, as `rule-claude-md` does. `estimate-clean-branch-ships-neutral-texts` then still holds and checks those texts; its Criterion stands, since it states the rule in general and names no sentence that changes. The changed Purposes touch no Estimate of `rule-permissions` or `rule-guppi-config`, since an `update` of a Purpose sets none `pending`, and no test under `.guppi/tests/` reads either page live (a Grep of `rule-permissions|rule-guppi-config|setup Case` over `.guppi/tests` printed `test_config.py` and `test_render.py`, which use their own copies). The two Estimates of `rule-morph` stand: each waits for the session that builds its setup skill, whose Case gives `core` back, so the copy of `guppi ship --allow-draft` that `estimate-morph-takes-in-the-set-aside-files` installs then holds the page. `estimate-sprint-plugin-ci-writes-a-clean-branch` stands: it speaks of a blocking page in general and names `estimate-clean-branch-refuses-a-draft-core-page` for it. The Result of `estimate-lint-checks-the-statuses` names `rule-morph` as a past reading, and the last line of the Criterion of `estimate-clean-branch-ships-neutral-texts` names it as the page whose setup sets the values of two Renders; both stand: `estimate-lint-checks-the-statuses` ships, since `rule-lint` carries `core: true`, but `guppi ship` writes its `## Result` as one line of the date and the pass, as `rule-clean-branch` sets it, so the name does not ship, and `estimate-clean-branch-ships-neutral-texts` does not ship, since `rule-clean-branch` carries no `core`. A Grep of `estimate-clean-branch-refuses-a-draft-core-page` over the same paths printed 3 files: `log.md`, `estimate-sprint-plugin-ci-writes-a-clean-branch.md` and `rule-clean-branch.md`, and none of them lists the pages without `core`. No test under `.guppi/tests/` reads `rule-morph`, `entity-sprint-plugin` or the Estimate live. The session's ledger holds one `error` lesson with no mark, `lesson-orchestration-acknowledging-reply-leaves-the-frontier-heading-untranslated`; its cause is the main agent keeping the heading `## Frontier` in English in an acknowledging reply, which this Case does not touch, so the Case carries no `{addresses:...}` mark.

> **problem:**
> The clean build writes nothing while `rule-morph`, a page of a later milestone, stands `draft` with `core: true`, so the current milestone cannot close before work of a later one is done.

> **recommend:**
> - **How rule-morph stops blocking the build**
>   - Recommended: (a) rule-morph ships only once it is built: `core` comes off it, and its item in the milestone The plugin says that the Case that builds it gives `core` back.
>   - Answer: agreed, (a).
> - **What happens to rule-skill-approve-spec**
>   - Recommended: (a) it keeps core, and the CLI trial clears it.
>   - Answer: agreed, (a); the trial can be made in this session.
> - **How the change is checked**
>   - Recommended: (b) rewrite the line of `estimate-clean-branch-refuses-a-draft-core-page` that lists the pages without core, so that it names `rule-morph` too.
>   - Answer: (b); close the Case now.
> - **Change**
>   - Asked: at `/pre-spec`, the line of the milestone item of `entity-sprint-plugin` names `rule-morph` in place of an unclear "it"; the `context` is set right on which pages carry `core` and on the ledger; and the Case also rewords the Purposes of `rule-permissions` and `rule-guppi-config` to say the setup Case of a project in place of `rule-morph`, `estimate-clean-branch-ships-neutral-texts` named as still holding.
>   - Taken: the pair of `entity-sprint-plugin` names `rule-morph`; the `context` is fixed; the Case updates `rule-permissions` and `rule-guppi-config` with those pairs and names that Estimate in `context`.

> **given:**
> `rule-morph`: the page that carries no `core` until it is built.
> **＋** `estimate-clean-branch-refuses-a-draft-core-page`: its Criterion is replaced whole.
> **＋** `entity-sprint-plugin`: the milestone item of `rule-morph`.
> **＋** `rule-clean-branch`: the rule of `guppi ship`, which lets a page a new project can go without lose `core` until it is built.
> **＋** `rule-permissions` and `rule-guppi-config`: the shipped pages whose Purpose names the setup Case of a project in place of `rule-morph`.
> **＋** `rule-skill-merge-main` and `rule-skill-pr-review`: the other pages without `core` until they are built.
> **＋** `.guppi/guppi/pages.py`, `.guppi/guppi/lint.py` and `.guppi/guppi/generate.py`: `is_draft_core`, the report of lint and the cascade that sets a page `built`.
> **＋** `.github/workflows/prod.yml`: the workflow that writes `prod`.

> **when:**
> `uv run --project .guppi guppi ship <folder>` or `uv run --project .guppi guppi ship --review <folder>`, as `rule-clean-branch` sets it, builds the clean version into an empty folder, with or without the option `--allow-draft`, or `uv run --project .guppi guppi lint` runs where the module of the command `ship` stands.

> **then:**
> A rule or an entity with `core: true` that stands `draft` blocks the build when its `## History` holds no line that set its status to `built`, or when one of its Estimates stands `failed`.
> **＋** While a page that blocks the build stands, `guppi ship` prints one line for each such page, writes nothing and exits 1.
> **＋** A `draft` page with `core: true` whose History holds such a line and none of whose Estimates stands `failed` gets no line, and the build writes it as it stands.
> **＋** With `--allow-draft`, the build writes the clean version all the same and prints those lines, which set no exit code; `.github/workflows/prod.yml` never passes that option.
> **＋** The build and lint tell a page that blocks the build by `is_draft_core` of `.guppi/guppi/pages.py`, imported by both, and a test runs the cascade of `.guppi/guppi/generate.py` that sets a page `built` and asserts that the page, set `draft` again, then blocks nothing.
> **＋** `rule-skill-merge-main`, `rule-skill-pr-review` and `rule-morph` carry no `core`, so the clean version holds none of them nor a file one of them renders.
> **－** `uv run --project .guppi guppi ship --check` does not judge the status of a page.

```then
update:
- slug: rule-morph
  set:
    core: null
  change: core taken off while the page is draft and never built; the Case that builds it gives it back
- slug: entity-sprint-plugin
  replace:
  - old: and the clean version that ships that key unset
    new: 'and the clean version that ships that key unset; until it is `built`, `rule-morph` carries no `core`, and the Case that builds it gives `core: true` back'
  change: the milestone item of rule-morph says that it carries no core until it is built
- slug: rule-permissions
  replace:
  - old: Until the setup Case of [[rule-morph]] sets the folder name of the project
    new: Until the setup Case of a project sets its folder name
  change: the Purpose names the setup Case of a project, not rule-morph, which ships only once it is built
- slug: rule-guppi-config
  replace:
  - old: until the setup Case of `rule-morph` sets the project's own commands
    new: until the setup Case of a project sets its own commands
  - old: these two commands among them, stay with `rule-morph`
    new: these two commands among them, belong to the setup Case of a project
  change: the Purpose names the setup Case of a project, not rule-morph, which ships only once it is built
- slug: estimate-clean-branch-refuses-a-draft-core-page
  set:
    status: pending
    method: 'uv run --project .guppi pytest .guppi/tests/test_ship.py .guppi/tests/test_lint.py -k draft_core; by hand, after the librarian''s run that applies the update of rule-morph: a Grep for ^core: in rule-skill-merge-main, rule-skill-pr-review and rule-morph, and for --allow-draft in .github/workflows/prod.yml, read against the Criterion'
  change: the Criterion replaced whole — rule-morph carries no core until it is built
```

```tasks
- [x] update `rule-morph`
- [x] update `entity-sprint-plugin`
- [x] update `rule-permissions`
- [x] update `rule-guppi-config`
- [x] update `estimate-clean-branch-refuses-a-draft-core-page`
- [x] `uv run --project .guppi guppi sprint`
- [x] read `estimate-clean-branch-refuses-a-draft-core-page`
```
