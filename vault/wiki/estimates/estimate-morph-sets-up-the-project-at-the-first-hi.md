---
type: estimate
kind: QA
status: passed
target: "[[rule-morph]]"
purpose: Whether the Render of rule-skill-setup and the Purpose of rule-morph say that the first /hi after /guppi:install, in a project whose guppi.toml holds setup_done = false, puts one setup Case first, with the values it finds — the folder of saved transcripts and the main branch from the branch /hi printed, which goes into its prompt — and the values the person gives, and that the librarian's run of that session renders the settings and each file that names the main branch by the key main_branch
method: "by hand, at the Retro of the session that sets this Criterion: the new Render of rule-skill-setup and the new Purpose of rule-morph in the Spec read against the Criterion, and after it the Render of rule-skill-setup in .claude/skills/setup/SKILL.md, rendered from it, recorded in the estimate line"
checked: 2026-11-26
origin: guppi
sprint: guppi
created: 2026-11-28
tags: [session, harness, plugin]
core: true
---

## Criterion

When:
Someone reads the `## Render` of `rule-skill-setup` and the `## Purpose` of `rule-morph`, in the Spec at the Retro of the session that ratified this Criterion, or after it the Render of `rule-skill-setup` in `.claude/skills/setup/SKILL.md`, rendered from it, and the `## Purpose` of `rule-morph` in the Spec of the last session that changed it.

Then:
The two texts say that, after `/guppi:install` of `rule-plugin-install`, the first `/hi` in a project whose `guppi.toml` holds `setup_done = false` starts `/setup`, which puts the setup Case of `rule-morph` first, before the opening Case of the first sprint and before the Frontier.
**＋** They say that step 2 of `/setup` writes the branch that `/hi` printed under `Branch:` into the prompt of the setup Case.
**＋** They say that the setup Case takes the name of the project's folder of saved transcripts from the path of the project, and the name of its main branch from that branch, `main` where that line names no branch, and shows each for the person to correct.
**＋** They say that it asks the person for the language of the repository, the language of the chat and the description of the project, and that, where the file paths of the project show a file of a programming language outside `.guppi/`, `vault/`, `.claude/` and `guppi-set-aside/`, one plain question asks how the project's own tests and style check run beside GUPPI's, whose commands stay first in the keys `test` and `style`.
**＋** They say that the `update` of `rule-guppi-config` of the setup Case holds `main_branch` with the name of the main branch, and that the ledger hook of `rule-ledger-write` writes its decision lines though no sprint is open.
**＋** They say that the setup Case holds a render line for each file its updates write and for each file whose `## Render` names the main branch by the placeholder of the key `main_branch`, and that the librarian's run of that session renders them.
**＋** They say that the reply that acknowledges the setup Case shows no Frontier and ends with the open question on what the first sprint is to build, and that `/sprint-open` starts in the same session with the person's answer.
**－** They say that `/guppi:install` is no Case and that the person ratifies nothing at it.
**－** They say that the setup Case asks for no category set and no git remote, asks no question on the main branch, reads no code of the project and creates no page.
**－** They say that, where the file paths show no such file, it asks nothing on tests or style, and that its question names no key of `guppi.toml`.
**－** The reading does not run the setup: a new install is read by the one-off Estimate `estimate-sprint-plugin-setup-takes-a-main-branch-other-than-main`.

## Result

2026-11-26, passed in the repository of GUPPI.

## History

- 2026-11-28 shipped with GUPPI
