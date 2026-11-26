---
type: estimate
kind: QA
status: passed
target: "[[rule-morph]]"
purpose: Whether the Render of rule-skill-setup and the Purpose of rule-morph say that the first /hi after /guppi:install, in a project whose guppi.toml holds setup_done = false, puts one setup Case first, with the values it finds — the folder of saved transcripts and the main branch from the branch /hi printed, which goes into its prompt — and the values the person gives, and that the librarian's run of that session renders the settings and each file that names the main branch by the key main_branch
method: "by hand, at the Retro of the session that sets this Criterion: the new Render of rule-skill-setup and the new Purpose of rule-morph in the Spec read against the Criterion, and after it the Render of rule-skill-setup in .claude/skills/setup/SKILL.md, rendered from it, recorded in the estimate line"
checked: 2026-11-26
origin: raw/2026-10-13/1753/ledger.md#case-802
sprint: plugin
created: 2026-10-13
tags: [session, harness, plugin]
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

2026-11-26, Retro, vault/raw/2026-11-26/1515/spec.md Case 1070.3: the new Render of rule-skill-setup (its pairs over the live Render) and the new Purpose of rule-morph read against each line of the Criterion: step 2 writes the branch of Branch: into the prompt, the setup Case takes the transcripts folder from the path and the main branch from that branch, main where none, shows each for correction with no question, its update of rule-guppi-config holds main_branch, it holds a render line for each file whose Render names the main branch by the placeholder and step 4 renders them, it asks for no category set and no git remote; the other lines stand in the live texts

## History

- 2026-10-13 created · [[decision-case-802]]
- 2026-10-15 updated: the Criterion replaced whole — the install Case comes at the first /hi after /guppi:install, while guppi.toml does not mark the install as done · [[decision-case-817]]
- 2026-10-15 updated: the Criterion replaced whole — the setup Case comes first at the first /hi and /sprint-open follows it in the same session; /guppi:install is no Case · [[decision-case-825]]
- 2026-10-30 updated: the Criterion replaced whole — the files that /guppi:install sets aside count beside its copy among the changes before the setup Case · [[decision-case-932.5]]
- 2026-11-03 updated: the Criterion replaced whole — /setup builds the setup Case, the reply that acknowledges it asks what the first sprint is to build, the settings land at the librarian's run, and no main branch or git remote is taken · [[decision-case-1017.4]]
- 2026-11-04 updated: the put-off retired before it was applied; the reading taken at the install stop of Work Mode · [[decision-case-1026.1]]
- 2026-11-04 status: pending → failed · raw/2026-11-04/0358/ledger.md#L25
- 2026-11-20 updated: the Criterion replaced whole — the setup asks on tests and style only where the project holds code of its own · [[decision-case-1031.3]]
- 2026-11-25 updated: the method set anew — the project with code is the one of the git init offer, the project with no code the one that holds only a LICENSE, at the install stop of Work Mode · [[decision-case-1055.2]]
- 2026-11-25 status: pending → passed · raw/2026-11-25/0816/ledger.md#L26
- 2026-11-26 updated: the Criterion replaced whole — the texts of the setup say that the setup Case proposes the name of the main branch from the branch /hi printed and writes it into guppi.toml; purpose and method read those texts in the Spec at Retro, and the install moves to a one-off Estimate of the sprint page · [[decision-case-1070.3]]
- 2026-11-26 status: pending → passed · raw/2026-11-26/1515/ledger.md#L38
