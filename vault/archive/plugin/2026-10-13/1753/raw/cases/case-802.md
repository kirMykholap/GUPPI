## Case 802 — The first /hi of a new install sets the project up through one Case

> **context:**
> `rule-morph` is the step that sets GUPPI up when someone installs it in their own project. Since case 239 it has been a placeholder with only a Purpose, and it was put off four times. Some settings name this one machine or this one project. The read rules of `rule-permissions` name the folder `c--PROJECTS-GUPPI` of the saved transcripts. `guppi/box.py` holds the branch name `main` as `SHARED_NEVER`. On another person's machine these values are wrong. In the first round the person agreed with each recommendation. The install step is a skill whose answers become one Case that the person ratifies, so nothing changes outside a ratified Decision, as `rule-ratification` sets it. It runs at the first `/hi` in a project whose settings lack the answers. It finds the branch, the remote and the transcripts folder for itself, and asks only for the rest. The category set leaves `rule-morph` for a backlog line of its own. A project with code of its own gets its pages one Case at a time, not at install. That growth is a change to `rule-case-build`, which the main agent dispatches as a Case of its own. This session writes the design and the check. The skill is built in the milestone The plugin of `entity-sprint-plugin`. In the second round the person agreed with two more points. A Case lives only inside a session that `/hi` opened, so the install Case is the first Case of the first session. The category set waits as a plain line in the `## Backlog` of `entity-sprint-plugin`.
>
> This Case takes up the deferred page. Its decision line on `rule-morph` carries one `{supersedes:case N}` for each Case in its `deferred_by`: 239, 745, 750 and 758. Its Purpose and its `purpose` are written anew. Once the marks clear `deferred_by` and the page gains an Estimate, `is_placeholder` of `guppi/lint.py` no longer holds, and the schema of `rule-rules-schema` requires `kind` and `tags`, which the placeholder lacks; the `update` sets `kind: Leaf` and the tags. The page names no `enforcement`, which the schema leaves optional, since the Case that builds the skill sets how the rule has force. Case 804.5 of this session sets `core: true` on the same page by a decision line of its own, a field that this Case does not touch (`vault/raw/2026-10-13/1753/cases/case-804.md`). The milestone The plugin of `entity-sprint-plugin` named no line for the install step, so the `update` adds the line `[[rule-morph]]` under it, beside the line on the clean version made into a plugin, and `guppi sprint` writes `sprint.md` again. Case 804 changes other lines of that page. The last `make lint`, under `## Flags` of `vault/wiki/brief.md`, printed `rules/rule-morph: deferred: 4 times since case 239`; the marks clear that defer at the librarian's run. `estimate-morph-sets-up-the-project-at-the-first-hi` is the check. A Glob `vault/**/estimate-morph*` printed nothing, so the slug is free. The `create` has a `ref`, so no vault query runs before it. Its `method` waits for the session whose Work Mode builds the skill, in the `after` form of case 781. A Grep `category set|categories as data|at install|initiation` over `vault/wiki/`, with `log.md` and `brief.md` left out, printed `vault/wiki/backlog.md`, `vault/wiki/rules/rule-morph.md`, `vault/wiki/rules/rule-permissions.md` and `vault/wiki/rules/rule-guppi-config.md`. The same Grep over `.claude/` printed nothing. The Purpose of `rule-guppi-config` says that the category set stays with `rule-morph`, so this Case changes that sentence. Its one Estimate, `estimate-guppi-config-fills-the-languages`, speaks of the render of the languages, not of the install, and stands. The sentence of `rule-permissions` that leaves the folder name of another install to `rule-morph` stays true. `vault/wiki/backlog.md` is written by `guppi backlog` at the librarian's run, from the pages and the sprint Backlog. `/hi`, set by `rule-skill-hi`, changes only when the skill is built. The Criterion of `estimate-sprint-plugin-installs-as-a-plugin`, that `/hi` opens a working session in an empty project, stays true: the install Case comes inside that session. No other Estimate of `entity-sprint-plugin` speaks of its Backlog. A Grep `rule-morph|rule-guppi-config|entity-sprint-plugin` over `tests/` printed `tests/test_config.py`, `tests/test_lint.py`, `tests/test_prespec.py` and `tests/test_render.py`. Each one names a slug in a string, or writes a copy of a page under a temporary folder. No test reads the three pages live.

> **problem:**
> GUPPI has no step that sets a new install up. A second person's project would run on the settings of this machine, and the plan for that step is still a placeholder that has been put off again and again.

> **recommend:**
> - **What is the install step, and how do its answers become settings?**
>   - Recommended: (a) a skill whose answers become the project's first Case; the person ratifies it, and the render writes the settings files.
>   - Answer: agreed, (a).
> - **When does the install step run?**
>   - Recommended: (a) `/hi` starts it when the settings are missing.
>   - Answer: agreed, (a).
> - **What does the install step ask, and what does it find for itself?**
>   - Recommended: (a) it finds the branch, the remote and the transcripts folder, asks the rest, and shows every value in the one Case.
>   - Answer: agreed, (a).
> - **Does choosing the category set stay part of the install step?**
>   - Recommended: (a) move it out to its own backlog item; every project uses the development set.
>   - Answer: agreed, (a).
> - **How do pages grow in a project that already has code?**
>   - Recommended: (a) each Case covers the code it touches: `case-guppi` reads code that no page covers, and offers in a round a page for the thing the Case changes alone.
>   - Answer: agreed, (a).
> - **One Case or two?**
>   - Recommended: (a) two separate Cases: this one on the install step, page growth as its own Case on `rule-case-build`.
>   - Answer: agreed, (a).
> - **What does this session deliver for the install step?**
>   - Recommended: (a) write the design now and the check the built skill must pass; build it in the milestone The plugin.
>   - Answer: agreed, (a).
> - **Where does the install step run in relation to the session that `/hi` opens?**
>   - Recommended: (a) the install Case is the first Case of the first session, and the Work Mode of that session writes the settings.
>   - Answer: agreed, (a).
> - **Where does the category set wait as its own backlog item?**
>   - Recommended: (a) a plain line in the `## Backlog` of `entity-sprint-plugin`.
>   - Answer: agreed, (a).

> **given:**
> `rule-morph`: the install step; its Purpose is written anew.
> **＋** `estimate-morph-sets-up-the-project-at-the-first-hi`: the new check of the install step.
> **＋** `rule-skill-hi`: the skill `/hi`, which opens the session and writes `raw/<date>/<hi HHMM>/frontier.md`.
> **＋** `rule-guppi-config`: renders `guppi.toml`, which holds `documentation_lang` and `chat_lang`; one sentence of its Purpose changes.
> **＋** `rule-permissions`: renders the read rules of the folder of saved transcripts under `~/.claude/projects`.
> **＋** `entity-sprint-plugin`: the sprint page; its milestone The plugin names `rule-morph`, and its `## Backlog` takes the category set.
> **＋** `rule-ratification`: nothing changes without a ratified Decision.
> **＋** `vault/raw/2026-10-13/1753/cases/case-804.md`: Case 804 sets `core` on `rule-morph` and changes other lines of `entity-sprint-plugin`.

> **when:**
> In a project with GUPPI installed, whose settings hold no answers of the install step of `rule-morph`, the person types `/hi`.

> **then:**
> `/hi` opens the session as `rule-skill-hi` sets it, and puts the install Case first, before the items of `raw/<date>/<hi HHMM>/frontier.md`.
> **＋** The install step takes the name of the main branch and the git remote from git, and the name of the project's folder of saved transcripts under `~/.claude/projects` from the path of the project.
> **＋** It asks the person only for the values it cannot find, such as `documentation_lang` and `chat_lang`.
> **＋** Every value stands in that one install Case, which the person ratifies or corrects.
> **＋** The Work Mode of the same session writes the settings by the render of the rule pages that hold them, such as `guppi.toml` from `rule-guppi-config` and the read rules of the saved transcripts from `rule-permissions`.
> **－** No settings file changes before the person ratifies the install Case.
> **－** The install step does not ask for the category set: the project takes the development set, as `entity-sprint-plugin` keeps the category set as data in its `## Backlog`.
> **－** The install step reads no code of the project and creates no page for it.
> **－** A project whose settings hold the answers gets no install Case at `/hi`.

> **tasks:**
> - [ ] update `rule-morph`
>   - set:
>     ```
>     kind: Leaf
>     purpose: "Prevents a new install of GUPPI from running on the settings of another machine or project: at the first /hi of a project with no answers in its settings, one install Case that the person ratifies sets them"
>     tags: [session, harness, plugin]
>     ```
>   - sections.Purpose:
>     ```
>     Prevents a new install of GUPPI from running on the settings of another machine or project: at the first `/hi` of a project with no answers in its settings, one install Case that the person ratifies sets them. Some settings name one machine or one project until then: the read rules of [[rule-permissions]] name the folder of this repository's saved transcripts under `~/.claude/projects`, and the code takes the main branch to be `main` (case 693).
> 
>     The install step is a skill. `/hi` opens the session as always and, while the settings hold no answers of the install, puts the install Case first, before the Frontier: a Case lives only inside a session that `/hi` opened. The skill takes the name of the main branch and the git remote from git, and the name of the project's folder of saved transcripts from the path of the project, and asks the person only for the rest, such as the language of the repository and of the chat. Every value stands in that one Case; the person ratifies or corrects it, and the Work Mode of the same session writes the settings by the render of the rule pages that hold them, such as [[rule-guppi-config]] for `guppi.toml` and [[rule-permissions]] for the read rules. No settings file changes outside that Case ([[rule-ratification]]).
> 
>     The install step does not set the category set: every project takes the development set — entity, rule, estimate — and the category set as data waits as a line of the `## Backlog` of [[entity-sprint-plugin]]. It reads no code of the project and creates no page for it: the pages of a project with code of its own grow one Case at a time. The skill is built in the milestone The plugin of [[entity-sprint-plugin]] (case 802).
>     ```
>   - change: `taken up: the install step is a skill at the first /hi whose answers become one ratified Case; the category set leaves for the Backlog of entity-sprint-plugin (case 802)`
> - [ ] create `estimate-morph-sets-up-the-project-at-the-first-hi`
>   - ref: `rule-morph`
>   - kind: `QA`
>   - purpose: `Whether the first /hi of a project with no answers in its settings puts one install Case first, with the values it finds and the values the person gives, and whether the settings change only by the render after that Case is ratified`
>   - method: `by hand, after the session whose Work Mode builds the install skill of rule-morph: /hi typed in an empty project with GUPPI installed and no answers in its settings, the transcript of that session and the files its Work Mode writes read against the Criterion, recorded in the estimate line`
>   - tags: `[session, harness, plugin]`
> - [ ] update `rule-guppi-config`
>   - old: `` The questions asked at install and the category set stay with `rule-morph` (case 476.1). ``
>   - new: `` The questions asked at install stay with `rule-morph` (cases 476.1, 802); the category set as data waits as a line of the `## Backlog` of `entity-sprint-plugin` (case 802). ``
>   - change: `the category set leaves rule-morph for the Backlog of entity-sprint-plugin (case 802)`
> - [ ] update `entity-sprint-plugin`
>   - old: `- the clean version made into a Claude Code plugin`
>   - new:
>     ```
>     - the clean version made into a Claude Code plugin
>     - [[rule-morph]] — the install step that the first `/hi` of a new install runs
>     ```
>   - sections.Backlog: `- The category set as data: the person sets the categories of a project, the development set entity, rule, estimate by default, and the harness holds them as data, so a changed set rewrites no rule; taken out of rule-morph (case 802); the categories discussion of session 1119, vault/archive/migration/2026-09-17/1119/raw/categories-discussion.md`
>   - change: `the milestone The plugin names rule-morph, the install step; the Backlog takes the category set as data, out of rule-morph (case 802)`
> - [ ] `uv run guppi sprint`
> - [ ] read `estimate-morph-sets-up-the-project-at-the-first-hi`

> **ratification:**
> ```
> - decision[case 802][update][rule-morph]{ref:rule-morph}{supersedes:case 239}{supersedes:case 745}{supersedes:case 750}{supersedes:case 758}
> - decision[case 802][create][estimate-morph-sets-up-the-project-at-the-first-hi]{ref:rule-morph}{tags:session,harness,plugin}
> - decision[case 802][update][rule-guppi-config]{ref:rule-guppi-config}
> - decision[case 802][update][entity-sprint-plugin]{ref:entity-sprint-plugin}
> ```
