---
type: rule
kind: Leaf
purpose: Prevents the session that closes a sprint from mixing the close with other decisions, or from reaching the close without the readings sorted, while the text that leads it stays out of the sessions that close no sprint
status: built
enforcement: render
governs: .claude/skills/sprint-close/SKILL.md
render_mode: full
parent: "[[rule-plan-mode]]"
estimates: ["[[estimate-skill-sprint-close-leads-the-closing-session]]", "[[estimate-skill-sprint-close-migration-merged-into-main]]"]
origin: raw/2026-10-08/2352/ledger.md#case-743.8
sprint: migration
created: 2026-10-08
tags: [sprint, workflow, harness]
core: true
---

## Purpose

Prevents the session that closes a sprint from mixing the close with other decisions, or from reaching the close without the readings sorted, while the text that leads it stays out of the sessions that close no sprint. Until case 743 these steps stood in a paragraph of `orchestration.md`, which every session loads. The skill starts when the person takes up the close line of the sprint, which [[rule-skill-sprint-open]] writes in a fixed form as the last item of the last milestone, or when the person types it (case 743.8). It reaches the librarian through the close line of the Spec, which `.claude/agents/librarian-guppi.md` runs ([[rule-sprint-close]], case 628.1).

## Render

<!-- rule-skill-sprint-close -->
---
name: sprint-close
description: "Lead the session that closes the sprint. Run it when the person takes up the line of the sprint that names /sprint-close, or types /sprint-close."
---

This session closes the sprint that `vault/wiki/sprint.md` names. Its Plan Mode holds only the closing Case and the Cases that prepare its readings, so that all of its decisions belong to the sprint it closes.

1. Write nothing into `.git`, so run no `git fetch`: `gh api repos/{owner}/{repo}/commits/main --jq .sha` prints `<hash>`, the commit of `main` on GitHub. When `git merge-base --is-ancestor <hash> HEAD` exits other than 0, the branch does not hold `main`, and this session cannot close the sprint: close the line of the close in `frontier.md` as `[-] … · sprint · defer`, tell the person to run `/merge-main` in a session of its own first, and stop the skill here (case 791). When `gh api` fails, show its output, close the line the same way and stop the skill here. When the session's `raw/<date>/<hi HHMM>/ledger.md` holds a decision line other than a `defer`, this session cannot close the sprint. Close the line of the close in `frontier.md` as `[-] … · sprint · defer`, tell the person that the close needs a session of its own, opened by `/hi`, and stop the skill here.
2. Close each other open line under `## Cases` of `frontier.md` as put off, by the closer of its source that `vault/wiki/orchestration.md` sets: `[-] … · sprint · defer`, `[-] … · backlog · kept`, or a short-form defer and `[-] … · defer case N`. The person's pick of the close line stands as the words that ratify each such defer, shown in one reply as `## The short form — deferred decisions` of `vault/wiki/orchestration.md` sets it. Leave the lines under `## Work` and `## Ask` open: their readings serve the close. Show the Frontier.
3. Sort the Estimates under `vault/wiki/estimates/` that stand `pending` or `failed` into groups by the kind of moment their `method` names.
4. Dispatch `case-guppi` for the closing Case as `vault/wiki/orchestration.md` sets it, with the groups in the prompt of the call. The closing Case names the groups in its `context`, holds one `by hand` task per moment that Work Mode sets up and one `read` line per Estimate, and holds the task line `uv run guppi sprint-close --sprint <id> --apply` with the person's choice, `--carry` or `--archive-unread`, for each Estimate still unread after Work Mode and each one read `failed` in Work Mode that the sprint page does not list; an Estimate of the sprint page is never carried. The closing Case holds no task line for the merge of the sprint's branch into `main`: the opening Case of the next sprint holds the merge, as `/sprint-open` sets it (case 775.2). A Case that prepares a reading is built the same way, and no other Case is ratified in this session.
5. In Work Mode set up each moment and take each reading whose moment came. Work Mode neither runs nor ticks the close line.
6. The librarian runs the close line after `guppi generate`, as `.claude/agents/librarian-guppi.md` sets it. The close moves the finished pages, the finished sessions of `vault/raw/` and the old event logs to the archive, and `guppi sprint` then marks the sprint closed in `vault/wiki/sprint.md`; the next session opens the next sprint by `/sprint-open`.
<!-- /rule-skill-sprint-close -->

## History

- 2026-10-09 created · [[decision-case-743.8]]
- 2026-10-09 estimate estimate-skill-sprint-close-leads-the-closing-session added · [[decision-case-743.8]]
- 2026-10-09 updated: the parent is rule-plan-mode, as case 743.8 set it (case 746.1) · [[decision-case-746.1]]
- 2026-10-09 status: draft → built · cascade
- 2026-10-10 estimate estimate-skill-sprint-close-migration-merged-into-main added · [[decision-case-762]]
- 2026-10-10 updated: step 4: the close line also names an Estimate read failed in Work Mode that the sprint page does not list · [[decision-case-763.2]]
- 2026-10-10 deferred · [[decision-case-771]]
- 2026-10-11 defer by decision-case-771 superseded · [[decision-case-775.2]]
- 2026-10-11 updated: the closing Case leaves no merge line; the opening Case of the next sprint holds the merge · [[decision-case-775.2]]
- 2026-10-13 updated: /sprint-close refuses while the branch does not hold origin/main, and asks for /merge-main first (case 791) · [[decision-case-791]]
- 2026-10-13 updated: ships in the clean version (case 804) · [[decision-case-804.5]]
