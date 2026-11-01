---
type: estimate
kind: QA
status: passed
target: "[[rule-handoff]]"
purpose: /handoff stops on a dirty tree, writes handoff.md from memory into the session's folder, dispatches the librarian with its path, shows report.md and commits it alone after the librarian's commit, or, in a session that /box runs, hands back to /box
method: "by hand, after a /handoff whose .claude/skills/handoff/SKILL.md holds the Render of rule-handoff that commits report.md: the event log vault/raw/<date>/event_log.md, handoff.md and git log, and the dispatch line and the text shown to the person read in the transcript of that session under ~/.claude/projects/, against the Criterion, the transcript named in the estimate line; by hand, after a /handoff in a session that /box runs: the event log, and the step of /box that follows read in the transcript of that session under ~/.claude/projects/, against the Criterion, the transcript named in the estimate line"
checked: 2026-11-01
origin: raw/2026-09-10/ledger.md#case-38.3
sprint: migration
created: 2026-09-10
tags: [session, workflow, harness]
---

## Criterion

When:
The agent calls `/handoff` on `PreToolUse Skill` after the reply that ends Retro, or the person types `/handoff` on `UserPromptSubmit`, the gate of `.guppi/guppi/gate.py` reads the tree, and the agent runs the skill `.claude/skills/handoff/SKILL.md` as rendered from `rule-handoff`.

Then:
The skill's context holds `git status --porcelain`. On a dirty tree the skill stops and says "commit first", and nothing is written.
**＋** On a clean tree the day's event log `vault/raw/<date>/event_log.md` holds the `handoff` mark of the call.
**＋** The agent writes `handoff.md` into the session's folder `vault/raw/<date>/<hi HHMM>/`: one document with no `---` and the sections that `rule-handoff` names, with no Read call on the artifacts.
**＋** Then the agent dispatches `librarian-guppi` with one line, `Materialize <date> from <path of handoff.md>.`, the path being that of the file just written.
**＋** After the librarian's report, the agent shows the text of `vault/raw/<date>/<hi HHMM>/report.md` unchanged, or, when no `report.md` stands there, the returned report unchanged and one line that says that `report.md` is missing.
**＋** When `report.md` stands, the agent commits it alone, in one commit after the librarian's, with the message `docs(vault): librarian report, <date>`, and never with `--amend`.
**－** In a session whose `raw/<date>/<hi HHMM>/work.md` holds `## Conserved Spec` — one that `/box` runs — the agent dispatches nothing after `handoff.md` and goes back to the step of `/box` that follows `/handoff`.
**－** No commit follows the handoff but the librarian's and the commit of `report.md`, and no reply between the call and the librarian's report carries a `LEDGER` block.

## Result

2026-11-01, Work reading of session 2038, the /handoff of session 0141 in the transcript ~/.claude/projects/c--PROJECTS-GUPPI/b91d8531-1bea-46ba-a54a-0282b108e453.jsonl lines 1554-1601, the event log and git log: the skill at ce0231ab holds the Render of rule-handoff; Tree empty; mark 03:48:01 b91d8531 handoff; handoff.md written at 03:48:26 into raw/2026-11-01/0141/, no --- line, the seven sections, no Read call before it; librarian-guppi dispatched with "Materialize 2026-11-01 from vault/raw/2026-11-01/0141/handoff.md.", in the same message as the Write; report.md shown unchanged, 62 of 62 lines, and committed alone as 994ade11 after the librarian's d0f9b153, no --amend, the commit before the showing; no other commit and no LEDGER block after the call; not exercised: a dirty tree, a missing report.md, a session of /box

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-38.3
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L87
- 2026-09-12 criterion: case 73.7 added · [[decision-case-73.7]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/1229/ledger.md#L4
- 2026-09-29 updated: the Criterion replaced whole — the head and the block 73.7 into one When and Then, the dispatch by the path; purpose and method set, Context and Method out (case 499.2) · [[decision-case-499.2]]
- 2026-09-30 updated: the Criterion replaced whole — the trigger covers the agent's call after the reply that ends Retro; the sections are those of rule-handoff; no LEDGER block before the librarian's report (case 531.6) · [[decision-case-531.6]]
- 2026-10-02 updated: the Criterion replaced whole — in a session that /box runs, /handoff hands back to /box (case 591.9) · [[decision-case-591.9]]
- 2026-10-03 updated: method names the kind of its moment (case 613.3) · [[decision-case-613.3]]
- 2026-10-04 status: pending → passed · raw/2026-10-04/0004/ledger.md#L1
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-31 updated: the Criterion replaced whole — /handoff shows report.md and commits it alone · [[decision-case-956.3]]
- 2026-11-01 deferred · [[decision-case-976]]
- 2026-11-01 defer by decision-case-976 superseded · [[decision-case-982.3]]
- 2026-11-01 updated: the defer of decision-case-976, archived as superseded, retired; the reading waits for its event · [[decision-case-982.3]]
- 2026-11-01 status: pending → passed · raw/2026-11-01/2038/ledger.md#L16
