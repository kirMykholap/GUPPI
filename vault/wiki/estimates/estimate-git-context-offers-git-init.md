---
type: estimate
kind: QA
status: passed
target: "[[rule-git-context]]"
purpose: Whether /hi in a folder that is no git repository tells the person to type ! git init -b main and then /hi again, asks no question, runs no write of its own, opens no sprint and writes no Frontier, and whether the next /hi goes on in the repository the person made
method: "by hand, after the install stop of the Work Mode that sets this method, in a repository that holds the module of the command ship: in a folder that is no git repository and holds a CLAUDE.md and a code file of its own, GUPPI installed by /guppi:install from a copy that uv run --project .guppi guppi ship --allow-draft wrote into a local folder, Claude Code reopened there, /hi typed, ! git init -b main typed as the reply tells, then /hi typed again, and the replies, the context of each /hi and the session folders in the transcripts of those sessions under ~/.claude/projects/, and git branch --show-current, read against the Criterion, recorded in the estimate line"
checked: 2026-11-25
origin: guppi
sprint: guppi
created: 2026-11-28
tags: [session, harness, git]
core: true
---

## Criterion

When:
The person types `/hi` of `.claude/skills/hi/SKILL.md` in a project folder in Plan Mode, and its `Branch:` line, which runs `uv run --project .guppi guppi gitstate` of `rule-git-context`, reads `none: this folder is no git repository`.

Then:
Before `/sprint-open` and before the Frontier, the agent says that GUPPI works only in a git repository, tells the person to type `! git init -b main`, which names the first branch `main`, and then `/hi` again, and ends the reply.
**＋** The person's `! git init -b main` runs in Plan Mode as the person's own shell command and makes the repository.
**＋** The next `/hi` prints `main` under `Branch:` and goes on as `rule-skill-hi` sets it.
**－** That `/hi` asks the person no question, starts no `/sprint-open` and writes no `raw/<date>/<hi HHMM>/frontier.md`.
**－** The agent runs no `git init -b main` and writes nothing, as `rule-default-mode` sets it, and `allowed-tools` of `.claude/skills/hi/SKILL.md` does not name `git init -b main`.

## Result

2026-11-25, passed in the repository of GUPPI.

## History

- 2026-11-28 shipped with GUPPI
