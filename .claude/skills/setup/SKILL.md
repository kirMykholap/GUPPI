---
name: setup
description: "Set up a project that installed GUPPI: the setup Case of rule-morph, before the first sprint opens. Run it when the hook on /hi says that the setup of the project is not done."
---

The `guppi.toml` of this project holds `setup_done = false`: its settings are still those of the clean version of GUPPI. This session sets them in one setup Case, as `rule-morph` sets it, before `/sprint-open` opens the first sprint. While `guppi.toml` holds `setup_done = false`, the ledger hook writes every decision line, though no sprint is open.

1. Assemble no Frontier and start no `/sprint-open` yet: the setup Case comes first, and no other item of the session is taken up before the person ratifies it.
2. Dispatch `case-guppi` for the setup of the project, with the Case id that `uv run --project .guppi guppi caseid --next --session <id>` prints, the eight-character session id — the second token of the `hi:` line the `UserPromptSubmit` hook put in the context at `/hi`, between the time and the folder, not the time of the folder —, and write into the prompt of the call that the setup Case:
   - asks the person, in its rounds, for the language of the repository and the language of the chat, each a code of the table of `.guppi/guppi/config.py`, the commands of the keys `test` and `style` of `guppi.toml`, and the description of the project;
   - takes the name of the folder of the saved transcripts of this project under `~/.claude/projects` from the path of the project, and shows it for the person to correct;
   - where the folder `guppi-set-aside/` stands, shows what each file under it holds, by its old path, and asks the person to keep or drop each part of it, such as an instruction, a hook or a permission;
   - holds an `update` of `rule-guppi-config` whose Render holds the languages, the commands and `setup_done = true`, an `update` of `rule-claude-md` whose Render holds the description between its lines `<!-- project-description -->` and `<!-- /project-description -->`, and an `update` of `rule-permissions` whose read rules name the folder of the saved transcripts of this project, with a render line for each file they write;
   - puts each kept part into the page that writes its file, such as `rule-claude-md` for an instruction of `CLAUDE.md`, `rule-hook-registry` for a hook and `rule-permissions` for a permission; writes a kept part of a file that no page writes, such as `.gitattributes`, by a task; and holds a task that deletes `guppi-set-aside/`;
   - asks for no category set, no name of the main branch and no git remote, reads no code of the project and creates no page.
3. The person ratifies or corrects the setup Case as any other. The reply that acknowledges it holds the `LEDGER` block, its heading and its changes, as `vault/wiki/orchestration.md` sets it, and no Frontier, since none is written yet; it ends with the open question on what the first sprint is to build, which `/sprint-open` asks first. When the person answers, start `/sprint-open` and take that answer as the answer to its open question, which it does not ask again.
4. The settings change at the librarian's run of this session, which writes the pages of the setup Case and renders `guppi.toml`, `CLAUDE.md` and `.claude/settings.json` from them; from then on `guppi.toml` holds `setup_done = true`, and `/hi` starts no `/setup`.
