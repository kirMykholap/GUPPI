---
type: estimate
kind: QA
status: passed
target: "[[rule-git-context]]"
purpose: Whether /hi in a folder that is no git repository asks to run git init -b main, runs it on the person's yes and ends, ends on a no, and opens no sprint and writes no Frontier either way
method: "by hand, after the librarian's run, in a repository that holds the module of the command ship: in an empty folder that is no git repository, GUPPI installed by /guppi:install from a copy that uv run --project .guppi guppi ship --allow-draft wrote into a local folder, Claude Code opened there, /hi typed and answered no, /hi typed again and answered yes, then /hi typed a third time, and the replies, the context of each /hi, the session folders and git branch --show-current read against the Criterion"
checked: 2026-10-29
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
**＋** The next `/hi` prints `main` under `Branch:` and goes on as `rule-skill-hi` sets it, `/sprint-open` first when the hook of `rule-skill-sprint-open` asks for it.
**＋** On the person's no, the agent tells the person to type `/hi` again after `git init -b main`.
**－** After either answer, that `/hi` starts no `/sprint-open` and writes no `raw/<date>/<hi HHMM>/frontier.md`.
**－** `git init -b main` is the one write before a ratified Case that `rule-default-mode` allows, and `allowed-tools` of `.claude/skills/hi/SKILL.md` does not name it.

## Result

2026-10-29, Work Mode of session 0327, installs A and B from scratchpad/catalogue-0327 (guppi ship --allow-draft) into empty folders with no git, transcripts bc61060a and b2a4f5e7 of C:/tmp/guppi-0327-a and -b: /hi said that GUPPI works only in a git repository and asked "Запустить `git init -b main`?", with no /sprint-open and no frontier.md; A, yes: plan mode refused the command until the person switched to auto, then git init -b main ran (branch main), the reply said the repository is made and to type /hi again, and the next /hi started /sprint-open; B, no: the reply said to type /hi again after git init -b main, no git repository stands, vault/raw/2026-10-29 holds event_log.md alone; allowed-tools of .claude/skills/hi/SKILL.md names render --sync, gitstate and tail only

## History

- 2026-10-16 created · [[decision-case-851.1]]
- 2026-10-16 deferred · [[decision-case-862]]
- 2026-10-29 defer by decision-case-862 superseded · [[decision-case-900.1]]
- 2026-10-29 updated: the defer retired, the reading taken at the install stop of Work Mode; the method states that it runs where the command ship stands · [[decision-case-900.1]]
- 2026-10-29 status: pending → passed · raw/2026-10-29/0327/ledger.md#L32
