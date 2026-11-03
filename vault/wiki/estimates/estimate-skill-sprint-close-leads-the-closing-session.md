---
type: estimate
kind: QA
status: passed
target: "[[rule-skill-sprint-close]]"
purpose: Whether /sprint-close refuses on a branch that does not hold origin/main and in a session that ratified another Case, puts off the other Cases lines, sorts the readings and has the closing Case built with the close line, while orchestration.md no longer holds the steps of the closing session
method: "by hand: the Render of rule-skill-sprint-close in .claude/skills/sprint-close/SKILL.md and vault/wiki/orchestration.md read against the Criterion"
checked: 2026-10-17
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [sprint, workflow, harness]
core: true
---

## Criterion

When:
The person takes up on the Frontier the line of the sprint that names `/sprint-close`, and the main agent starts the skill `/sprint-close` of `.claude/skills/sprint-close/SKILL.md`, rendered from `rule-skill-sprint-close`, on `PreToolUse Skill`, or the person types `/sprint-close` on `UserPromptSubmit`.

Then:
Writing nothing into `.git`, the main agent first runs `gh api repos/{owner}/{repo}/commits/main --jq .sha`, which prints `<hash>`, and `git merge-base --is-ancestor <hash> HEAD`. When the second exits other than 0, it closes the close line `[-] … · sprint · defer`, tells the person to bring the branch up to `main` first, in a session of its own, and the skill stops. When `gh api` fails, it shows the output and the skill stops the same way.
**＋** When the session's ledger holds a decision line other than a `defer`, the main agent closes the close line `[-] … · sprint · defer`, tells the person that the close needs a session of its own, and the skill stops.
**＋** Otherwise the main agent closes each other open line under `## Cases` of `frontier.md` by the closer of its source put off, the person's pick of the close line standing as the words that ratify each short-form defer, leaves the lines under `## Work` and `## Ask` open, and shows the Frontier.
**＋** It sorts the Estimates that stand `pending` or `failed` into groups by the kind of moment their `method` names and dispatches `case-guppi` for the closing Case with the groups in the prompt, and the closing Case names the groups in its `context`, holds one `by hand` task per moment that Work Mode sets up and one `read` line per Estimate, and holds the task line `uv run --project .guppi guppi sprint-close --sprint <id> --apply` with the person's choice for each Estimate still unread.
**＋** Work Mode takes each reading whose moment came and neither runs nor ticks the close line; the librarian runs it, as `.claude/agents/librarian-guppi.md` sets it.
**＋** `vault/wiki/orchestration.md` holds no paragraph on the closing session, names the two skills in one sentence, and counts the start of `/sprint-close` among the moments of a short-form defer.
**－** Besides the closing Case, the session ratifies only the Cases that prepare its readings.
**－** The closing Case holds no task line for the merge of the sprint's branch into `main`: the opening Case of the next sprint holds the merge, as `.claude/skills/sprint-open/SKILL.md` sets it.

## Result

2026-10-17, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
