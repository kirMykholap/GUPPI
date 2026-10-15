## Case 825 — Setup comes before the first sprint at the first /hi

> **context:**
> A new project gets GUPPI in three moves. The person installs the plugin `guppi`, types `/guppi:install`, which only copies the files and builds the Python environment, then reopens Claude Code and types `/hi`. Two pages claim that first `/hi`. `rule-morph` puts the Case that sets the project's settings first (case 817). The session files that `guppi ship` writes make `/hi` start `/sprint-open` first, so the first sprint opens (case 822.3, `estimate-clean-branch-writes-the-session-files`). Neither page gives an order. The pages also call the setup "the install Case" and "the install step", which reads as if `/guppi:install` were itself a Case.
>
> The person chose setup first and the sprint after it, in the same session (Q1). They chose the name "setup" for the Case, "install" only for `/guppi:install` (Q2). They chose the Purpose of `rule-morph` as the one place that tells the whole start in order (Q3), and the Criterion of `estimate-morph-sets-up-the-project-at-the-first-hi` replaced whole as the check (Q4). The person also said that `/guppi:install` is no Case and is never ratified, and that the setup is a Case. The new Purpose says both.
>
> The rule that governs the order is the ledger hook of `rule-ledger-write`. `refused_without_sprint` of `.guppi/guppi/ledger.py` refuses each decision line but a `defer` while no live `entity-sprint-` page stands, until a `create` of one stands. The Render of `rule-skill-sprint-open` says "the opening Case is the first Case the session ratifies", and its first step says that no other item is taken up before the opening Case is ratified. The Render of `rule-skill-hi` starts `/sprint-open` first when the brief opens with `open the next sprint`. The Criterion of `estimate-sprint-close-next-session-opens-the-sprint` promises that refusal, and the Criterion of `estimate-skill-sprint-open-starts-at-hi` promises the hook line at `/hi`. These texts stand in this Case. They state what the code and the live skills do today. The key of `guppi.toml` that marks the setup as done does not exist yet. A live skill that waited for that key would show a setup Case in the repository of GUPPI too. So the new Purpose of `rule-morph` says that these steps, the pass of the ledger hook and the key are built in the milestone The plugin, and the milestone line of `entity-sprint-plugin` names them as what remains. The Case that builds them changes those Renders, that rule and those two Estimates. `estimate-clean-branch-writes-the-session-files` and its sentence in `rule-clean-branch`, that the first `/hi` starts `/sprint-open` before the Frontier, stand. With setup first, `/sprint-open` still starts before the Frontier.
>
> A Grep of `install Case|install step|install as done` over `vault/wiki/` printed `log.md`, `rules/rule-clean-branch.md`, `rules/rule-claude-md.md`, `rules/rule-guppi-config.md`, `entities/entity-sprint-plugin.md`, `rules/rule-morph.md` and `estimates/estimate-morph-sets-up-the-project-at-the-first-hi.md`. `log.md` is not read. Each other hit enters this Case. The same Grep over `.claude/` printed nothing. A Grep of `at install\b` over `vault/wiki/` printed `log.md`, `rules/rule-guppi-config.md`, `rules/rule-morph.md` and `rules/rule-permissions.md`. "The questions asked at install" in `rule-guppi-config` and "whose initiation at install sets the folder name" in `rule-permissions` name the setup, and both enter this Case. The hits in `rule-morph` stand in its History, and `log.md` is not read. Case 824 also changes the last sentence of the Purpose of `rule-permissions`, and its pair there replaces only the words before the colon. The pair of this Case replaces only words after the colon, so the two do not overlap, and the ledger applies Case 824 first. Read side by side, the sentence then says that the read rules name the folder of the repository of GUPPI, after where that repository sits on the person's disk, and that another install waits for `rule-morph`, whose setup Case sets the folder name. Both texts fit. Case 824 is built again to write "setup Case" in its own texts, so the pairs of this Case do not need to catch its text. The rename is a pair under `replace` on each page, not a `reword`. `reword_pairs` of `.guppi/guppi/generate.py` fails an entry whose `new` does not already stand in the owner's text, by `owner_text`, and no page holds "setup Case" yet. The sections of the other Estimates whose text says "the install" mean `/guppi:install`, and they stand.
>
> Case 824 of this session changes two sentences of the Purpose of `rule-morph`. The ledger applies it before this Case, and this Case writes that Purpose whole, so the new text keeps the words of Case 824: "of the repository of GUPPI" for the commands and for the folder of saved transcripts. The new texts of `rule-morph`, `rule-claude-md` and `rule-guppi-config`, which carry `core: true`, keep each pointer in a bracket at the end of its sentence (case 807.4). The `purpose` and `method` of `estimate-morph-sets-up-the-project-at-the-first-hi` state the old promise, and are set anew in its `update`. Its `method` waits for the session that builds the setup step, the same event as before. No line of its old Criterion is carried word for word. Each old line comes back with "install Case" or "install step" renamed "setup Case" or "setup step". The new Criterion adds the order before `/sprint-open`, the pass of the ledger hook and the line that `/guppi:install` is no Case. The tests of `.guppi/tests/` that read live pages, `test_guppi_package.py` among them, look for old command and path words that these texts do not hold.

> **problem:**
> Two pages each put a different Case first at the first `/hi` of a new project, with no order between them, and the pages call the setup "the install Case", as if `/guppi:install` were a Case.

> **recommend:**
> - **In what order do setup and the first sprint come?**
>   - Recommended: (a) setup first, then the sprint, in one session.
>   - Answer: agreed, (a).
> - **Should the "install Case" be renamed "setup Case"?**
>   - Recommended: (a) rename to "setup" everywhere.
>   - Answer: agreed, (a).
> - **Where does the start-to-finish description live?**
>   - Recommended: (a) in the Purpose of `rule-morph`.
>   - Answer: agreed, (a).
> - **How is the order checked?**
>   - Recommended: (a) rewrite that check's promise.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: a `/pre-spec` finding: `rule-permissions` still says that the folder name is set "at install".
>   - Taken: a pair on `rule-permissions` names the setup Case of `rule-morph` there.

> **given:**
> `rule-morph`: the rule of the setup Case, whose Purpose tells the start of a new project in order.
> **＋** `estimate-morph-sets-up-the-project-at-the-first-hi`: the check of that rule, whose Criterion is replaced whole.
> **＋** `rule-plugin-install`: the rule of `/guppi:install`, the copy before the setup.
> **＋** `rule-skill-hi` and `rule-skill-sprint-open`: the rules of `/hi` and of `/sprint-open`, which opens a sprint.
> **＋** `rule-ledger-write`: the rule of the ledger hook that refuses decision lines while no sprint is open.
> **＋** `rule-guppi-config`, `rule-claude-md` and `rule-permissions`: the rules whose Renders hold the settings of the setup Case, the read rules of the saved transcripts under `~/.claude/projects` among them.
> **＋** `rule-clean-branch` and `entity-sprint-plugin`: pages whose text names the setup Case.

> **when:**
> In a project where the person installed the plugin `guppi` and typed `/guppi:install`, as `rule-plugin-install` sets it, and whose `guppi.toml` does not mark the setup of `rule-morph` as done, the person reopens Claude Code and types `/hi`.

> **then:**
> `/hi` opens the session as `rule-skill-hi` sets it, and puts the setup Case first, before the opening Case of `rule-skill-sprint-open` and before the Frontier.
> **＋** Once the person ratifies the setup Case, `/hi` starts `/sprint-open` in the same session, and the ledger hook of `rule-ledger-write` writes the decision lines of the setup Case though no sprint is open.
> **＋** The setup step takes the name of the main branch and the git remote from git, and the name of the project's folder of saved transcripts under `~/.claude/projects` from the path of the project.
> **＋** It asks the person only for the values it cannot find, such as `documentation_lang`, `chat_lang`, the commands of the keys `test` and `style` of `guppi.toml`, and the description of the project.
> **＋** Every value stands in that one setup Case, which the person ratifies or corrects.
> **＋** The Work Mode of the same session writes the settings by the render of the rule pages that hold them, such as `guppi.toml` from `rule-guppi-config`, the description of the project in `CLAUDE.md` from `rule-claude-md` and the read rules of the saved transcripts from `rule-permissions`, and `guppi.toml` then marks the setup as done.
> **－** `/guppi:install` is no Case, and the person ratifies nothing at it.
> **－** Between `/guppi:install` and the ratified setup Case, no settings file changes but by the copy of `/guppi:install` and the render that `/hi` runs.
> **－** The setup step is no skill named `install`.
> **－** The setup step does not ask for the category set: the project takes the development set, as `entity-sprint-plugin` keeps the category set as data in its `## Backlog`.
> **－** The setup step reads no code of the project and creates no page for it.
> **－** A project whose `guppi.toml` marks the setup as done gets no setup Case at `/hi`.

> **tasks:**
> - [ ] update `rule-morph`
>   - set:
>     ```
>     purpose: "Prevents a new install of GUPPI from running on the settings of another machine or project: at the first /hi after /guppi:install, while guppi.toml does not mark the setup as done, one setup Case that the person ratifies sets them, before the first sprint opens"
>     ```
>   - sections.Purpose:
>     ```
>     Prevents a new install of GUPPI from running on the settings of another machine or project: at the first `/hi` after `/guppi:install`, while `guppi.toml` does not mark the setup as done, one setup Case that the person ratifies sets them, before the first sprint opens. The plugin `guppi` installs GUPPI by its skill `/guppi:install`, which copies the files of the clean version into the project, the settings among them, as `rule-plugin-install` sets it. Until the setup Case, those settings name another project: `guppi.toml` holds the languages and the commands of the keys `test` and `style` of the repository of GUPPI, `CLAUDE.md` holds a blank description of the project, the read rules of [[rule-permissions]] name the folder of the saved transcripts of the repository of GUPPI under `~/.claude/projects`, and the code takes the main branch to be `main` (as set in case 693).
>
>     A new project starts in this order. The install is no Case; the setup and the opening of the first sprint are Cases.
>
>     1. The person installs the plugin `guppi`, which the catalogue `guppi-marketplace` lists, as [[rule-plugin-install]] sets it.
>     2. The person types `/guppi:install` in the project. It copies the files of GUPPI and builds its Python environment. It decides nothing, so it is no Case, and the person ratifies nothing at it.
>     3. The person reopens Claude Code in the project and types `/hi`, which opens the session as [[rule-skill-hi]] sets it: a Case lives only inside a session that `/hi` opened.
>     4. While `guppi.toml` does not mark the setup as done, `/hi` puts the setup Case first, before the opening of a sprint and before the Frontier. The person ratifies or corrects it.
>     5. Once the setup Case is ratified, `/hi` starts `/sprint-open` in the same session, since the clean version holds the sprint `guppi` closed ([[rule-clean-branch]]). The opening Case of [[rule-skill-sprint-open]] opens the first sprint of the project, and the Frontier comes after it.
>     6. The Work Mode of that session writes the settings of the setup Case and runs the tasks of the opening Case.
>
>     The ledger hook of [[rule-ledger-write]] refuses each decision line but a `defer` while no sprint is open. While `guppi.toml` does not mark the setup as done, it writes the decision lines of the setup Case all the same, so that the setup Case is ratified before the opening Case.
>
>     A key of `guppi.toml`, which [[rule-guppi-config]] renders, marks the setup as done: the setup Case sets it, and the clean version holds it unset. The setup step is a skill of the project whose name is not `install`, so that a project never holds both `/install` and `/guppi:install`. The skill takes the name of the main branch and the git remote from git, and the name of the project's folder of saved transcripts from the path of the project, and asks the person only for the rest, such as the language of the repository and of the chat, the commands of the keys `test` and `style` of `guppi.toml`, and the description of the project. Every value stands in that one Case; the person ratifies or corrects it, and the Work Mode of the same session writes the settings by the render of the rule pages that hold them, such as [[rule-guppi-config]] for `guppi.toml`, [[rule-claude-md]] for the description of the project in `CLAUDE.md` and [[rule-permissions]] for the read rules, and so sets the key. No settings file changes outside that Case but by the copy of `/guppi:install` and the render that `/hi` runs, which take the values as the clean version holds them ([[rule-ratification]]).
>
>     The setup step does not set the category set: every project takes the development set — entity, rule, estimate — and the category set as data waits as a line of the `## Backlog` of [[entity-sprint-plugin]]. It reads no code of the project and creates no page for it: the pages of a project with code of its own grow one Case at a time. The key, the setup skill, its step in `/hi` and in `/sprint-open`, the pass of the ledger hook for the setup Case and the clean version that holds the key unset are built in the milestone The plugin of [[entity-sprint-plugin]]; until then [[rule-skill-hi]], [[rule-skill-sprint-open]] and [[rule-ledger-write]] put the opening Case first in every project (as set in cases 802, 817 and 825).
>     ```
>   - change: `the Purpose tells the start of a new project in order: /guppi:install is no Case, the setup Case comes first at the first /hi, and /sprint-open follows it in the same session; the install Case is named the setup Case`
> - [ ] update `estimate-morph-sets-up-the-project-at-the-first-hi`
>   - set:
>     ```
>     status: pending
>     purpose: "Whether the first /hi after /guppi:install, in a project whose guppi.toml does not mark the setup as done, puts one setup Case first, before the opening of the first sprint, with the values it finds and the values the person gives, and whether the settings change only by the copy, the render of /hi and the render after that Case is ratified"
>     method: "by hand, after the session whose Work Mode builds the setup skill of rule-morph, its step in /hi and in /sprint-open and the pass of the ledger hook for the setup Case: in an empty project, the plugin guppi installed, /guppi:install typed, Claude Code reopened and /hi typed; the transcript of that session, its ledger and the files its Work Mode writes read against the Criterion, recorded in the estimate line"
>     ```
>   - change: `the Criterion replaced whole — the setup Case comes first at the first /hi and /sprint-open follows it in the same session; /guppi:install is no Case`
> - [ ] update `rule-claude-md`
>   - old: `until the install Case of a project writes its own description`
>   - new: `until the setup Case of a project writes its own description`
>   - change: `the Purpose names the setup Case of rule-morph by its new name`
> - [ ] update `rule-guppi-config`
>   - old: `` until the install Case of `rule-morph` sets the project's own commands ``
>   - new: `` until the setup Case of `rule-morph` sets the project's own commands ``
>   - old: `The questions asked at install, these two commands among them,`
>   - new: `The questions asked at setup, these two commands among them,`
>   - change: `the Purpose names the setup Case of rule-morph by its new name`
> - [ ] update `rule-permissions`
>   - old: `` whose initiation at install sets the folder name ``
>   - new: `` whose setup Case sets the folder name ``
>   - change: `the Purpose names the setup Case of rule-morph as the step that sets the folder name`
> - [ ] update `rule-clean-branch`
>   - old: `` which the install Case of `rule-morph` replaces with the description of the project ``
>   - new: `` which the setup Case of `rule-morph` replaces with the description of the project ``
>   - change: `the Purpose names the setup Case of rule-morph by its new name`
> - [ ] update `entity-sprint-plugin`
>   - old: `` the install step that the first `/hi` after `/guppi:install` runs; what remains: the install skill, its step in `/hi`, the key of `guppi.toml` that marks the install as done, and the clean version that ships that key unset ``
>   - new: `` the setup Case that the first `/hi` after `/guppi:install` puts before the opening of the first sprint; what remains: the setup skill, its step in `/hi` and in `/sprint-open`, the key of `guppi.toml` that marks the setup as done, the pass of the ledger hook for the setup Case while no sprint is open, and the clean version that ships that key unset ``
>   - change: `the milestone line of rule-morph names the setup Case, its order before the first sprint and what remains of it`
> - [ ] read `estimate-morph-sets-up-the-project-at-the-first-hi`

> **ratification:**
> ```
> - decision[case 825][update][rule-morph]{ref:rule-morph}
> - decision[case 825][update][estimate-morph-sets-up-the-project-at-the-first-hi]{ref:rule-morph}
> - decision[case 825][update][rule-claude-md]{ref:rule-claude-md}
> - decision[case 825][update][rule-guppi-config]{ref:rule-guppi-config}
> - decision[case 825][update][rule-permissions]{ref:rule-permissions}
> - decision[case 825][update][rule-clean-branch]{ref:rule-clean-branch}
> - decision[case 825][update][entity-sprint-plugin]{ref:entity-sprint-plugin}
> ```
