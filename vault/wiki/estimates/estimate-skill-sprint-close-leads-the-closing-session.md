---
type: estimate
kind: QA
status: passed
target: "[[rule-skill-sprint-close]]"
purpose: Whether /sprint-close refuses on a branch that does not hold origin/main and in a session that ratified another Case, puts off the other Cases lines, sorts the readings and has the closing Case built with the close line, while orchestration.md no longer holds the steps of the closing session
method: by hand, at the Retro of the session whose Spec set the new Render of rule-skill-sprint-close that the Criterion describes, that Render in its spec.md, vault/wiki/orchestration.md and entity-sprint-migration under vault/archive/migration/ read against the Criterion (the session of case 791)
checked: 2026-10-13
origin: raw/2026-10-08/2352/ledger.md#case-743.8
sprint: migration
created: 2026-10-08
tags: [sprint, workflow, harness]
---

## Criterion

When:
The person takes up on the Frontier the line of the sprint that names `/sprint-close`, and the main agent starts the skill `/sprint-close` of `.claude/skills/sprint-close/SKILL.md`, rendered from `rule-skill-sprint-close`, on `PreToolUse Skill`, or the person types `/sprint-close` on `UserPromptSubmit`.

Then:
Writing nothing into `.git`, the main agent first runs `gh api repos/{owner}/{repo}/commits/main --jq .sha`, which prints `<hash>`, and `git merge-base --is-ancestor <hash> HEAD`. When the second exits other than 0, it closes the close line `[-] … · sprint · defer`, tells the person to run `/merge-main` of `.claude/skills/merge-main/SKILL.md` in a session of its own first, and the skill stops. When `gh api` fails, it shows the output and the skill stops the same way.
**＋** When the session's ledger holds a decision line other than a `defer`, the main agent closes the close line `[-] … · sprint · defer`, tells the person that the close needs a session of its own, and the skill stops.
**＋** Otherwise the main agent closes each other open line under `## Cases` of `frontier.md` by the closer of its source put off, the person's pick of the close line standing as the words that ratify each short-form defer, leaves the lines under `## Work` and `## Ask` open, and shows the Frontier.
**＋** It sorts the Estimates that stand `pending` or `failed` into groups by the kind of moment their `method` names and dispatches `case-guppi` for the closing Case with the groups in the prompt, and the closing Case names the groups in its `context`, holds one `by hand` task per moment that Work Mode sets up and one `read` line per Estimate, and holds the task line `uv run --project .guppi guppi sprint-close --sprint <id> --apply` with the person's choice for each Estimate still unread.
**＋** Work Mode takes each reading whose moment came and neither runs nor ticks the close line; the librarian runs it, as `.claude/agents/librarian-guppi.md` sets it.
**＋** `vault/wiki/orchestration.md` holds no paragraph on the closing session, names the two skills in one sentence, and counts the start of `/sprint-close` among the moments of a short-form defer.
**＋** The close line of `entity-sprint-migration` reads ``- the close of `migration` — `/sprint-close`, a session of its own``, and its `## Backlog` holds no line on the merge.
**－** Besides the closing Case, the session ratifies only the Cases that prepare its readings.
**－** The closing Case holds no task line for the merge of the sprint's branch into `main`: the opening Case of the next sprint holds the merge, as `.claude/skills/sprint-open/SKILL.md` sets it.

## Result

2026-10-13, Retro by hand: the Render of rule-skill-sprint-close in spec.md (case 791) reads the commit of main by gh api and stops with /merge-main first when git merge-base --is-ancestor fails, writing nothing into .git; orchestration.md names the two skills in one sentence; the archived entity-sprint-migration holds the close line in its form

## History

- 2026-10-09 created · [[decision-case-743.8]]
- 2026-10-09 status: pending → failed · raw/2026-10-08/2352/ledger.md#L38
- 2026-10-09 updated: sent back for a reading at the Retro of the session of case 746, the Criterion unchanged; the moment of the old method passed unread (case 746.3) · [[decision-case-746.3]]
- 2026-10-09 status: pending → passed · raw/2026-10-09/0200/ledger.md#L18
- 2026-10-11 updated: the Criterion replaced whole — the closing Case holds no merge line, the opening Case of the next sprint holds the merge · [[decision-case-775.2]]
- 2026-10-11 status: pending → passed · raw/2026-10-10/2350/ledger.md#L11
- 2026-10-13 updated: the Criterion replaced whole — /sprint-close refuses while the branch does not hold origin/main · [[decision-case-791]]
- 2026-10-13 status: pending → passed · raw/2026-10-12/2349/ledger.md#L56
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 updated: the pointer of the method stands in a bracket at its end · [[decision-case-823.1]]
