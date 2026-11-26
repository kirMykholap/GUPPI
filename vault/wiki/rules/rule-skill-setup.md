---
type: rule
kind: Leaf
purpose: Prevents a project that installed GUPPI from opening its first sprint on the settings of the clean version, while guppi.toml holds setup_done = false
status: built
enforcement: render
implementation_ref: [.guppi/guppi/sprint.py, .guppi/tests/test_sprint.py]
governs: .claude/skills/setup/SKILL.md
render_mode: full
parent: "[[rule-session-start]]"
estimates: ["[[estimate-skill-setup-starts-at-hi]]"]
origin: raw/2026-11-03/0316/ledger.md#case-1017.3
sprint: plugin
created: 2026-11-03
tags: [session, harness, plugin]
core: true
---

## Purpose

Prevents a project that installed GUPPI from opening its first sprint on the settings of the clean version, while `guppi.toml` holds `setup_done = false`. The skill `/setup` builds the setup Case of `rule-morph` first; the `UserPromptSubmit` hook `guppi sprint --hi` tells the agent at `/hi` to start it, and the reply that acknowledges that Case asks the open question on what the first sprint is to build, so that `/sprint-open` comes after it in the same session (as set in case 1017.3).

## Render

<!-- rule-skill-setup -->
---
name: setup
description: "Set up a project that installed GUPPI: the setup Case of rule-morph, before the first sprint opens. Run it when the hook on /hi says that the setup of the project is not done."
---

The `guppi.toml` of this project holds `setup_done = false`: its settings are still those of the clean version of GUPPI. This session sets them in one setup Case, as `rule-morph` sets it, before `/sprint-open` opens the first sprint. While `guppi.toml` holds `setup_done = false`, the ledger hook writes every decision line, though no sprint is open.

1. Assemble no Frontier and start no `/sprint-open` yet: the setup Case comes first, and no other item of the session is taken up before the person ratifies it.
2. Dispatch `case-guppi` for the setup of the project, with the Case id that `uv run --project .guppi guppi caseid --next --session <id>` prints, the eight-character session id — the second token of the `hi:` line the `UserPromptSubmit` hook put in the context at `/hi`, between the time and the folder, not the time of the folder —, and write into the prompt of the call the branch that `/hi` printed under `Branch:`, and that the setup Case:
   - asks the person, in its rounds, for the language of the repository and the language of the chat, each a code of the table of `.guppi/guppi/config.py`, and the description of the project, and, by the file paths of the project alone, reading no file, looks for a file of a programming language outside `.guppi/`, `vault/`, `.claude/` and `guppi-set-aside/`: where it finds none, it asks nothing on tests or style; where it finds one, it says in one plain question that GUPPI's own tests and style check keep running in this project, that it asks so that Work Mode, the close of a session and the checks on GitHub run those of the project too, and asks how the project's own tests and style check run beside them, naming no key of `guppi.toml` in the question (as set in case 1031.3);
   - takes the name of the folder of the saved transcripts of this project under `~/.claude/projects` from the path of the project, and the name of its main branch from the branch of `Branch:` that the prompt names, `main` where that line names no branch, and shows each for the person to correct, with no question on it;
   - where the folder `guppi-set-aside/` stands, shows what each file under it holds, by its old path, and asks the person to keep or drop each part of it, such as an instruction, a hook or a permission;
   - holds an `update` of `rule-guppi-config` whose Render holds the languages, the commands the person gave after GUPPI's commands, which leave neither key, `main_branch` with the name of the main branch, and `setup_done = true`, an `update` of `rule-claude-md` whose Render holds the description between its lines `<!-- project-description -->` and `<!-- /project-description -->`, and an `update` of `rule-permissions` whose read rules name the folder of the saved transcripts of this project, with a render line for each file they write and for each file whose Render names the main branch by the placeholder of the key `main_branch`, since a new name reaches such a file only at its render;
   - puts each kept part into the page that writes its file, such as `rule-claude-md` for an instruction of `CLAUDE.md`, `rule-hook-registry` for a hook and `rule-permissions` for a permission; writes a kept part of a file that no page writes, such as `.gitattributes`, by a task; and holds a task that deletes `guppi-set-aside/`;
   - asks for no category set and no git remote, reads no code of the project and creates no page; it asks no question on how it splits or how it is checked, and its `context` names the Estimates that already check the pages it updates (as set in case 1031.3).
3. The person ratifies or corrects the setup Case as any other. The reply that acknowledges it holds the `LEDGER` block, its heading and its changes, as `vault/wiki/orchestration.md` sets it, and no Frontier, since none is written yet; it ends with the open question on what the first sprint is to build, which `/sprint-open` asks first. When the person answers, start `/sprint-open` and take that answer as the answer to its open question, which it does not ask again.
4. The settings change at the librarian's run of this session, which writes the pages of the setup Case and renders `guppi.toml`, `CLAUDE.md`, `.claude/settings.json` and each file whose Render names the main branch by the placeholder of the key `main_branch` from them; from then on `guppi.toml` holds `setup_done = true`, and `/hi` starts no `/setup`.
<!-- /rule-skill-setup -->

## History

- 2026-11-03 created · [[decision-case-1017.3]]
- 2026-11-03 estimate estimate-skill-setup-starts-at-hi added · [[decision-case-1017.3]]
- 2026-11-03 status: draft → built · cascade
- 2026-11-20 updated: the prompt of the setup Case asks on tests and style only where the project holds code of its own · [[decision-case-1031.3]]
- 2026-11-26 updated: the branch /hi printed goes into the prompt of the setup Case, which takes the name of the main branch from it, shows it for correction, writes it into the key main_branch and renders each file that names the main branch by its placeholder · [[decision-case-1070.3]]
