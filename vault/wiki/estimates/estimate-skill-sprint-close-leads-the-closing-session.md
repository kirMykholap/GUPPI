---
type: estimate
kind: QA
status: passed
target: "[[rule-skill-sprint-close]]"
purpose: Whether /sprint-close refuses in a session that ratified another Case, puts off the other Cases lines, sorts the readings and has the closing Case built with the close line, while orchestration.md no longer holds the steps of the closing session
method: by hand, at the Retro of the session of case 746, the live Renders of rule-skill-sprint-close and rule-orchestration, .claude/skills/sprint-close/SKILL.md, vault/wiki/orchestration.md and entity-sprint-migration read against the Criterion
checked: 2026-10-09
origin: raw/2026-10-08/2352/ledger.md#case-743.8
sprint: migration
created: 2026-10-08
tags: [sprint, workflow, harness]
---

## Criterion

When:
The person takes up on the Frontier the line of the sprint that names `/sprint-close`, and the main agent starts the skill `/sprint-close` of `.claude/skills/sprint-close/SKILL.md`, rendered from `rule-skill-sprint-close`, on `PreToolUse Skill`, or the person types `/sprint-close` on `UserPromptSubmit`.

Then:
When the session's ledger holds a decision line other than a `defer`, the main agent closes the close line `[-] … · sprint · defer`, tells the person that the close needs a session of its own, and the skill stops.
**＋** Otherwise the main agent closes each other open line under `## Cases` of `frontier.md` by the closer of its source put off, the person's pick of the close line standing as the words that ratify each short-form defer, leaves the lines under `## Work` and `## Ask` open, and shows the Frontier.
**＋** It sorts the Estimates that stand `pending` or `failed` into groups by the kind of moment their `method` names and dispatches `case-guppi` for the closing Case with the groups in the prompt, and the closing Case names the groups in its `context`, holds one `by hand` task per moment that Work Mode sets up and one `read` line per Estimate, and holds the task line `uv run guppi sprint-close --sprint <id> --apply` with the person's choice for each Estimate still unread.
**＋** When the sprint ran on a branch of its own, the closing Case holds a task line for the merge of that branch into the main branch, which Work Mode leaves unticked, so that the brief gives it as Work to the session that opens the next sprint.
**＋** Work Mode takes each reading whose moment came and neither runs nor ticks the close line; the librarian runs it, as `.claude/agents/librarian-guppi.md` sets it.
**＋** `vault/wiki/orchestration.md` holds no paragraph on the closing session, names the two skills in one sentence, and counts the start of `/sprint-close` among the moments of a short-form defer.
**＋** The close line of `entity-sprint-migration` reads ``- the close of `migration` — `/sprint-close`, a session of its own``, and its `## Backlog` holds no line on the merge.
**－** Besides the closing Case, the session ratifies only the Cases that prepare its readings.

## Result

2026-10-09, Retro, by hand: .claude/skills/sprint-close/SKILL.md, vault/wiki/orchestration.md and entity-sprint-migration read against the Criterion — step 1 defers the close line and stops when the ledger holds a decision line other than a defer; step 2 puts off the other Cases lines with the pick as the ratifying words, Work and Ask left open, the Frontier shown; steps 3–4 sort pending and failed Estimates by moment, the closing Case with one by hand task per moment, one read line per Estimate, the sprint-close --apply line with the person's choice and the merge line left unticked; step 5–6 Work Mode neither runs nor ticks the close line, the librarian runs it; orchestration.md names the two skills in one sentence and counts the start of /sprint-close among the moments of a short-form defer; the close line reads "- the close of `migration` — `/sprint-close`, a session of its own" and the Backlog holds no merge line

## History

- 2026-10-09 created · [[decision-case-743.8]]
- 2026-10-09 status: pending → failed · raw/2026-10-08/2352/ledger.md#L38
- 2026-10-09 updated: sent back for a reading at the Retro of the session of case 746, the Criterion unchanged; the moment of the old method passed unread (case 746.3) · [[decision-case-746.3]]
- 2026-10-09 status: pending → passed · raw/2026-10-09/0200/ledger.md#L18
