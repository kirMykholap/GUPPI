---
type: rule
kind: Leaf
purpose: "Prevents a new install of GUPPI from running on the settings of another machine or project: at the first /hi after /guppi:install, while guppi.toml does not mark the setup as done, one setup Case that the person ratifies sets them, before the first sprint opens"
status: built
estimates: ["[[estimate-morph-sets-up-the-project-at-the-first-hi]]", "[[estimate-morph-takes-in-the-set-aside-files]]"]
origin: guppi
sprint: guppi
created: 2026-11-28
tags: [session, harness, plugin]
core: true
---

## Purpose

Prevents a new install of GUPPI from running on the settings of another machine or project: at the first `/hi` after `/guppi:install`, while `guppi.toml` does not mark the setup as done, one setup Case that the person ratifies sets them, before the first sprint opens. The plugin `guppi` installs GUPPI by its skill `/guppi:install`, which copies the files of the clean version into the project, the settings among them. Until the setup Case, those settings name another project: `guppi.toml` holds the languages of the repository of GUPPI and, in its keys `test` and `style`, the commands of GUPPI, which the setup keeps, `CLAUDE.md` holds a blank description of the project, and the read rules of [[rule-permissions]] name the folder of the saved transcripts of the repository of GUPPI under `~/.claude/projects`. The setup Case sets the name of the main branch of the project in `guppi.toml`, which the code and the skills read.

A new project starts in this order. The install is no Case; the setup and the opening of the first sprint are Cases.

1. The person installs the plugin `guppi`, which the catalogue `guppi-marketplace` lists.
2. The person types `/guppi:install` in the project. It copies the files of GUPPI and builds its Python environment. It decides nothing, so it is no Case, and the person ratifies nothing at it.
3. The person reopens Claude Code in the project and types `/hi`, which opens the session as [[rule-skill-hi]] sets it: a Case lives only inside a session that `/hi` opened.
4. While `guppi.toml` holds `setup_done = false`, `/hi` starts the skill `/setup` of [[rule-skill-setup]], which puts the setup Case first, before the opening of a sprint and before the Frontier. The person ratifies or corrects it.
5. Once the setup Case is ratified, the reply that acknowledges it shows no Frontier and asks the open question on what the first sprint is to build, and `/sprint-open` starts in the same session with that answer, since the clean version holds the sprint `guppi` closed. The opening Case of [[rule-skill-sprint-open]] opens the first sprint of the project, and the Frontier comes after it.
6. The Work Mode of that session runs the tasks of the setup Case and of the opening Case, and the librarian's run of that session writes the pages of the setup Case and renders the settings from them.

The ledger hook of [[rule-ledger-write]] refuses each decision line but a `defer` while no sprint is open. While `guppi.toml` holds `setup_done = false`, it writes every decision line all the same, so that the setup Case is ratified before the opening Case.

The key `setup_done` of `guppi.toml`, which [[rule-guppi-config]] renders, marks the setup as done: the setup Case sets it to `true`, and the clean version holds `setup_done = false`. The setup step is the skill `/setup` of [[rule-skill-setup]], whose name is not `install`, so that a project never holds both `/install` and `/guppi:install`. The skill takes the name of the project's folder of saved transcripts from the path of the project, and the name of its main branch from the branch that `/hi` prints under `Branch:`, `main` where that line names no branch, shows each for the person to correct, and asks the person only for the rest: the language of the repository and of the chat, and the description of the project. GUPPI's commands stay in the keys `test` and `style` of `guppi.toml`. Where the file paths of the project show a file of a programming language of its own, the skill asks how the tests and the style check of the project run beside GUPPI's, says why it asks, and adds the commands after GUPPI's; where they show none, it asks nothing on them. It reads the paths alone. Every value stands in that one Case; the person ratifies or corrects it, and the librarian's run of the same session writes the settings by the render of the rule pages that hold them, such as [[rule-guppi-config]] for `guppi.toml`, [[rule-claude-md]] for the description of the project in `CLAUDE.md` and [[rule-permissions]] for the read rules, and so sets the key. No settings file changes outside that Case but by the copy and the setting aside of `/guppi:install` and the render that `/hi` runs, which take the values as the clean version holds them ([[rule-ratification]]). Where `/guppi:install` set aside files of the project in the folder `guppi-set-aside/`, the setup Case also shows what each of them holds, by its old path, and the person keeps or drops each part of it, such as an instruction, a hook or a permission. A kept part goes into the page of GUPPI that writes its file, such as [[rule-claude-md]] for an instruction of `CLAUDE.md`, [[rule-hook-registry]] for a hook and [[rule-permissions]] for a permission, and the render writes it into the file; for a file that no page writes, such as `.gitattributes` or `.github/workflows/checks.yml`, a task of the setup Case writes the kept part into that file. A dropped part reaches no file, the setup Case creates no page for a kept part, and a task of it deletes `guppi-set-aside/` in the Work Mode of the same session.

The setup step does not set the category set: every project takes the development set: entity, rule, estimate. It reads no code of the project and creates no page for it: the pages of a project with code of its own grow one Case at a time.

## History

- 2026-11-28 shipped with GUPPI
