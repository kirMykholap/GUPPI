---
type: estimate
kind: QA
status: pending
target: "[[entity-sprint-plugin]]"
purpose: Whether a new install in a git project made by git init -b master has its setup Case show master as the main branch for correction, its opening Case and Work Mode take master as the main branch in the same session, and its librarian's run write main_branch = "master" into guppi.toml and master into the rendered skills that name the main branch
method: "by hand, after the librarian's run of the session that sets this method: the plugin guppi installed from a copy that uv run --project .guppi guppi ship --allow-draft wrote into a local folder, in a git project made by git init -b master, /guppi:install typed, Claude Code reopened, /hi typed and that session taken to its librarian's run, the transcript of that session under ~/.claude/projects, its ledger and the files written in it read against the Criterion, recorded in the estimate line"
origin: raw/2026-11-26/1515/ledger.md#case-1070.7
sprint: plugin
created: 2026-11-26
tags: [sprint, git, plugin]
once: true
---

## Criterion

When:
In a git project made by `git init -b master`, the person installs the plugin `guppi` from a copy that `uv run --project .guppi guppi ship --allow-draft` wrote after the librarian's run of the session that ratified this check, types `/guppi:install`, reopens Claude Code, types `/hi`, and takes that session to its librarian's run.

Then:
The setup Case of `rule-morph`, which `/setup` of `rule-skill-setup` builds, shows `master` as the name of the main branch for the person to correct, and asks no question on it.
**＋** Its `update` of `rule-guppi-config` holds `main_branch = "master"`, and it holds a render line for each of the four files below.
**＋** In that session, the opening Case of the first sprint takes `master` as the main branch: its first task line runs `git switch -c <id>`, with no push and no pull request, and Work Mode runs that line first and the rest of the Spec on the branch `<id>`.
**＋** After that librarian's run, `guppi.toml` holds `main_branch = "master"`, and `.claude/skills/sprint-open/SKILL.md`, `.claude/skills/sprint-close/SKILL.md`, `.claude/skills/work/SKILL.md` and `vault/wiki/where-to-stop.md` name `master` in each place where the copy names `main` as the main branch.

## History

- 2026-11-26 created · [[decision-case-1070.7]]
