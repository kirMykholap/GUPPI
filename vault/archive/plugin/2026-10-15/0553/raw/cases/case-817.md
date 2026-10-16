## Case 817 — The install Case comes at the first /hi after /guppi:install

> **context:**
> `rule-morph` sets up a new project. At the first `/hi` of a project, one install Case shows the values that the install step finds in git and the values it asks for, and the person ratifies it; the render then writes the settings. The page says that `/hi` puts that Case first while the settings hold no answers of the install, and that no settings file changes outside that Case. Under the installer model of Case 818, the plugin `guppi` carries one skill, `/guppi:install`, which copies the files of the clean version into the project, the settings among them, and the person then reopens Claude Code and types `/hi`, which renders by `guppi render --sync`. So the settings are never empty: the copied `guppi.toml` holds the languages of this repository, and the copied `.claude/settings.json` names the folder of this repository's saved transcripts. The test of the page never fires, and its sentence on the settings files is false. The person chose the following. The install Case stays at the first `/hi`, now after `/guppi:install` and a reopening of Claude Code, since the one rule of `rule-ratification` says that nothing changes without a ratified Decision, and only that order keeps the settings a ratified decision. A key of `guppi.toml`, rendered by `rule-guppi-config`, marks the install as done: the install Case sets it, the clean version holds it unset, and `/hi` puts the install Case first while it is not set. The person agreed, on Case 818, that the install step is no skill named `install`, so that a project never holds both `/install` and `/guppi:install`. This session changes the text of `rule-morph` and the Criterion of its one Estimate only. The page stays `draft`. A later session builds the key, the skill, its step in `/hi` and the change of `guppi ship` that ships the key unset. So `rule-guppi-config`, `rule-clean-branch`, `guppi/config.py` and `guppi/ship.py` do not change here, and Cases 816 and 818, which change `rule-clean-branch`, need no change. `parse` of `guppi/config.py` checks only the keys `documentation_lang` and `chat_lang`, so a later key does not break it. The Purpose of `rule-guppi-config` names those two keys and stays true until that later Case. Whether `/hi` opens a session in a new project at all is the promise of `estimate-sprint-plugin-installs-as-a-plugin`, whose Criterion Case 818.2 replaced: Case 819.1 moves the code under `.guppi/`, so the clean version holds no `pyproject.toml` at its root, and Case 821.3 makes `guppi ship` write `vault/wiki/sprint.md`, `backlog.md` and `brief.md` as skeletons. Two other Cases of this session leave values to the install Case. Case 820.2 adds the keys `test` and `style` to `guppi.toml` and leaves the questions of an install, those two commands among them, to `rule-morph`. Case 821.4 has `guppi ship` write a blank description of the project into `rule-claude-md` and `CLAUDE.md`, which the install Case of `rule-morph` replaces. The person decided, at the pre-spec of this session, that `rule-guppi-config` ships with this repository's values, `test` and `style` included, and that the install Case sets the project's own. So the new text of `rule-morph` and the new Criterion name the description of the project and the commands of `test` and `style` among the values that the install step asks for, and `CLAUDE.md` from `rule-claude-md` among the files that the render writes. The person also decided there that `rule-morph` keeps `core: true`, so the `core: null` of Case 821.7 on `rule-morph` is undone in that Case, and this Case sets no `core`. The milestone line of `rule-morph` on `entity-sprint-plugin` stays open, since the install step is not built, and this Case rewords it to what remains. The bootstrap writes the files before any Case. The new text names that as the one exception to the rule that no settings file changes outside the install Case: the copy and the render of `/hi` take the values as the clean version holds them, and they change no value. A Grep `rule-morph|estimate-morph` over `vault/wiki/`, with `log.md` and `brief.md` left out, printed `sprint.md`, `backlog.md`, `entities/entity-sprint-plugin.md`, `rules/rule-guppi-config.md`, `rules/rule-permissions.md`, `rules/rule-morph.md` and `estimates/estimate-morph-sets-up-the-project-at-the-first-hi.md`. `sprint.md` is written from `entity-sprint-plugin` by `guppi sprint`. The Backlog line on the category set stays true. `rule-guppi-config` leaves the questions of an install to `rule-morph`, which still holds. `rule-permissions` leaves the folder name of another install to `rule-morph`, which still holds. The Criterion of `estimate-morph-sets-up-the-project-at-the-first-hi` is replaced whole, with its `purpose` and `method`. Five of its lines change: the trigger line, on settings that hold no answers, becomes the line on `/guppi:install` and the key of `guppi.toml`; the line on the values it asks for gains the keys `test` and `style` and the description of the project; the line on the render of Work Mode gains `CLAUDE.md` and the key; the exception that no settings file changes before the install Case gains the copy and the render of `/hi`; and the exception on a project whose settings hold the answers now names the key. Its other lines stand word for word.

> **problem:**
> Under the installer model, `/guppi:install` writes the settings of this repository into the project before any `/hi`. So `rule-morph` has no test of a project that is not set up yet, and its rule that no settings file changes outside the install Case is false.

> **recommend:**
> - **Where the person gives the settings of a new project**
>   - Recommended: (a) the install Case at the first `/hi`, after the bootstrap of `/guppi:install`.
>   - Answer: agreed, (a).
> - **How much of the install step this session builds**
>   - Recommended: (a) this session changes the page and its Estimate only; a later session builds the skill and the check in `/hi`.
>   - Answer: agreed, (a).
> - **How `/hi` tells that the project has not been set up yet**
>   - Recommended: (a) `/hi` compares the transcripts folder that the read rules name with the one the project's path gives.
>   - Answer: (b) a new key in `guppi.toml` that the install Case sets and the clean version holds unset.
> - **What checks that this is done**
>   - Recommended: (a) replace the Criterion of `estimate-morph-sets-up-the-project-at-the-first-hi` whole.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: at the pre-spec, name the description of the project and the keys `test` and `style` among the values of the install Case, and `CLAUDE.md` among the files it renders; keep the milestone line of `rule-morph` on `entity-sprint-plugin` open with what remains; fix the sentence of `context` on what the copy holds.
>   - Taken: the new text of `rule-morph`, the new Criterion and `context` name them, and an `update` of `entity-sprint-plugin` rewords its milestone line.

> **given:**
> `rule-morph`: the rule of the install step at the first `/hi`.
> **＋** `estimate-morph-sets-up-the-project-at-the-first-hi`: its Criterion is replaced whole.
> **＋** `rule-plugin-install`, `vault/raw/2026-10-15/0553/cases/case-818.md`, `vault/raw/2026-10-15/0553/cases/case-820.md` and `vault/raw/2026-10-15/0553/cases/case-821.md`: the rule of `/guppi:install`, which copies GUPPI into the project, and the Cases of this session that create it, add the keys `test` and `style` and blank the description of the project.
> **＋** `entity-sprint-plugin`: the sprint page whose milestone The plugin names `rule-morph` and whose `## Backlog` keeps the category set as data.
> **＋** `rule-guppi-config`, `guppi.toml`, `rule-claude-md` and `CLAUDE.md`: the settings file, the file that holds the description of the project, and the rules that render them.
> **＋** `rule-permissions`: the rule of the read rules of the saved transcripts under `~/.claude/projects`.
> **＋** `rule-skill-hi` and `raw/<date>/<hi HHMM>/frontier.md`: the rule of `/hi` and the Frontier it writes.
> **＋** `rule-ratification`: the one rule, that nothing changes without a ratified Decision.

> **when:**
> In a project where the person installed the plugin `guppi` and typed `/guppi:install`, as `rule-plugin-install` sets it, and whose `guppi.toml` does not mark the install step of `rule-morph` as done, the person reopens Claude Code and types `/hi`.

> **then:**
> `/hi` opens the session as `rule-skill-hi` sets it, and puts the install Case first, before the items of `raw/<date>/<hi HHMM>/frontier.md`.
> **＋** The install step takes the name of the main branch and the git remote from git, and the name of the project's folder of saved transcripts under `~/.claude/projects` from the path of the project.
> **＋** It asks the person only for the values it cannot find, such as `documentation_lang`, `chat_lang`, the commands of the keys `test` and `style` of `guppi.toml`, and the description of the project.
> **＋** Every value stands in that one install Case, which the person ratifies or corrects.
> **＋** The Work Mode of the same session writes the settings by the render of the rule pages that hold them, such as `guppi.toml` from `rule-guppi-config`, the description of the project in `CLAUDE.md` from `rule-claude-md` and the read rules of the saved transcripts from `rule-permissions`, and `guppi.toml` then marks the install as done.
> **－** Between `/guppi:install` and the ratified install Case, no settings file changes but by the copy of `/guppi:install` and the render that `/hi` runs.
> **－** The install step is no skill named `install`.
> **－** The install step does not ask for the category set: the project takes the development set, as `entity-sprint-plugin` keeps the category set as data in its `## Backlog`.
> **－** The install step reads no code of the project and creates no page for it.
> **－** A project whose `guppi.toml` marks the install as done gets no install Case at `/hi`.

> **tasks:**
> - [ ] update `rule-morph`
>   - set:
>     ```
>     purpose: "Prevents a new install of GUPPI from running on the settings of another machine or project: at the first /hi after /guppi:install, while guppi.toml does not mark the install as done, one install Case that the person ratifies sets them"
>     ```
>   - sections.Purpose:
>     ```
>     Prevents a new install of GUPPI from running on the settings of another machine or project: at the first `/hi` after `/guppi:install`, while `guppi.toml` does not mark the install as done, one install Case that the person ratifies sets them. The plugin `guppi` installs GUPPI by its skill `/guppi:install`, which copies the files of the clean version into the project, the settings among them, as `rule-plugin-install` sets it. Until the install Case, those settings name another project: `guppi.toml` holds the languages and the commands of the keys `test` and `style` of this repository, `CLAUDE.md` holds a blank description of the project, the read rules of [[rule-permissions]] name the folder of this repository's saved transcripts under `~/.claude/projects`, and the code takes the main branch to be `main` (as set in case 693).
>
>     A key of `guppi.toml`, which [[rule-guppi-config]] renders, marks the install as done: the install Case sets it, and the clean version holds it unset. The install step is a skill of the project whose name is not `install`, so that a project never holds both `/install` and `/guppi:install`. After `/guppi:install`, the person reopens Claude Code in the project and types `/hi`. `/hi` opens the session as always and, while `guppi.toml` does not mark the install as done, puts the install Case first, before the Frontier: a Case lives only inside a session that `/hi` opened. The skill takes the name of the main branch and the git remote from git, and the name of the project's folder of saved transcripts from the path of the project, and asks the person only for the rest, such as the language of the repository and of the chat, the commands of the keys `test` and `style` of `guppi.toml`, and the description of the project. Every value stands in that one Case; the person ratifies or corrects it, and the Work Mode of the same session writes the settings by the render of the rule pages that hold them, such as [[rule-guppi-config]] for `guppi.toml`, [[rule-claude-md]] for the description of the project in `CLAUDE.md` and [[rule-permissions]] for the read rules, and so sets the key. No settings file changes outside that Case but by the copy of `/guppi:install` and the render that `/hi` runs, which take the values as the clean version holds them ([[rule-ratification]]).
>
>     The install step does not set the category set: every project takes the development set — entity, rule, estimate — and the category set as data waits as a line of the `## Backlog` of [[entity-sprint-plugin]]. It reads no code of the project and creates no page for it: the pages of a project with code of its own grow one Case at a time. The key, the skill, its step in `/hi` and the clean version that holds the key unset are built in the milestone The plugin of [[entity-sprint-plugin]] (as set in cases 802 and 817).
>     ```
>   - change: `the install Case comes at the first /hi after /guppi:install, while a key of guppi.toml does not mark the install as done; the install step is no skill named install`
> - [ ] update `estimate-morph-sets-up-the-project-at-the-first-hi`
>   - set:
>     ```
>     status: pending
>     purpose: "Whether the first /hi after /guppi:install, in a project whose guppi.toml does not mark the install as done, puts one install Case first with the values it finds and the values the person gives, and whether the settings change only by the copy, the render of /hi and the render after that Case is ratified"
>     method: "by hand, after the session whose Work Mode builds the install skill of rule-morph and its step in /hi: in an empty project, the plugin guppi installed, /guppi:install typed, Claude Code reopened and /hi typed; the transcript of that session and the files its Work Mode writes read against the Criterion, recorded in the estimate line"
>     ```
>   - change: `the Criterion replaced whole — the install Case comes at the first /hi after /guppi:install, while guppi.toml does not mark the install as done`
> - [ ] update `entity-sprint-plugin`
>   - old: `` - [[rule-morph]] — the install step that the first `/hi` of a new install runs ``
>   - new: `` - [[rule-morph]] — the install step that the first `/hi` after `/guppi:install` runs; what remains: the install skill, its step in `/hi`, the key of `guppi.toml` that marks the install as done, and the clean version that ships that key unset ``
>   - change: `the milestone line of rule-morph names what remains of the install step`
> - [ ] `uv run guppi sprint`
> - [ ] read `estimate-morph-sets-up-the-project-at-the-first-hi`

> **ratification:**
> ```
> - decision[case 817][update][rule-morph]{ref:rule-morph}
> - decision[case 817][update][estimate-morph-sets-up-the-project-at-the-first-hi]{ref:rule-morph}
> - decision[case 817][update][entity-sprint-plugin]{ref:entity-sprint-plugin}
> ```
