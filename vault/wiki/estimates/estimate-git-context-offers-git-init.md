---
type: estimate
kind: QA
status: failed
target: "[[rule-git-context]]"
purpose: Whether /hi in a folder that is no git repository asks to run git init -b main, runs it on the person's yes and ends, ends on a no, and opens no sprint and writes no Frontier either way
method: "by hand, after the librarian's run, in a repository that holds the module of the command ship: in an empty folder that is no git repository, GUPPI installed by /guppi:install from a copy that uv run --project .guppi guppi ship --allow-draft wrote into a local folder, Claude Code opened there, /hi typed and answered no, /hi typed again and answered yes, then /hi typed a third time, and the replies, the context of each /hi, the session folders and git branch --show-current read against the Criterion"
checked: 2026-11-04
origin: raw/2026-10-16/0342/ledger.md#case-851.1
sprint: plugin
created: 2026-10-16
tags: [session, harness, git]
---

## Criterion

When:
The person types `/hi` of `.claude/skills/hi/SKILL.md` in a project folder, and its `Branch:` line, which runs `uv run --project .guppi guppi gitstate` of `rule-git-context`, reads `none: this folder is no git repository`.

Then:
Before `/sprint-open` and before the Frontier, the agent says that GUPPI works only in a git repository and asks the person whether it runs `git init -b main`.
**＋** On the person's yes, the agent runs `git init -b main`, which Claude Code asks the person to allow, says that the repository is made, and tells the person to type `/hi` again.
**＋** The next `/hi` prints `main` under `Branch:` and goes on as `rule-skill-hi` sets it: `/setup` first when the hook on `/hi` says that the setup of the project is not done, and `/sprint-open` when the hook of `rule-skill-sprint-open` asks for it.
**＋** On the person's no, the agent tells the person to type `/hi` again after `git init -b main`.
**－** After either answer, that `/hi` starts no `/sprint-open` and writes no `raw/<date>/<hi HHMM>/frontier.md`.
**－** `git init -b main` is the one write before a ratified Case that `rule-default-mode` allows, and `allowed-tools` of `.claude/skills/hi/SKILL.md` does not name it.

## Result

2026-11-04, Work Mode of session 0358, ~/.claude/projects/C--PROJECTS-guppi-trial-0358-no-git/07cfacdd-aa2f-4da2-a0ad-3831ae6115b8.jsonl and 2b6bed0c-675a-46ff-8b0d-82e6d19838a8.jsonl: the first /hi read none under Branch:, asked whether to run git init -b main before /sprint-open and the Frontier, and on no told the person to type /hi after git init -b main, with no Frontier written; the second /hi asked again, and on yes the agent did not run git init -b main: the session stood in Plan Mode, set by "defaultMode": "plan" of .claude/settings.json, and the agent told the person to type `! git init -b main` (L64), which the person ran (L70); the third /hi printed main and started /setup

## History

- 2026-10-16 created · [[decision-case-851.1]]
- 2026-10-16 deferred · [[decision-case-862]]
- 2026-10-29 defer by decision-case-862 superseded · [[decision-case-900.1]]
- 2026-10-29 updated: the defer retired, the reading taken at the install stop of Work Mode; the method states that it runs where the command ship stands · [[decision-case-900.1]]
- 2026-10-29 status: pending → passed · raw/2026-10-29/0327/ledger.md#L32
- 2026-11-03 updated: the Criterion replaced whole — the /hi after git init -b main starts /setup first in a project whose setup is not done · [[decision-case-1017.9]]
- 2026-11-04 updated: the put-off retired before it was applied; the reading taken at the install stop of Work Mode · [[decision-case-1026.3]]
- 2026-11-04 status: pending → failed · raw/2026-11-04/0358/ledger.md#L27
