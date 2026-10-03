---
type: estimate
kind: QA
status: passed
target: "[[rule-handoff]]"
purpose: /handoff stops on a dirty tree, writes handoff.md from memory into the session's folder and dispatches the librarian with its path, or, in a session that /box runs, hands back to /box, with no commit after
method: "by hand at the /handoff of a later session and at the /handoff of a session that /box runs: the event log, handoff.md, the dispatch line and git log"
checked: 2026-10-04
origin: raw/2026-09-10/ledger.md#case-38.3
sprint: migration
created: 2026-09-10
tags: [session, workflow, harness]
---

## Criterion

When:
The agent calls `/handoff` on `PreToolUse Skill` after the reply that ends Retro, or the person types `/handoff` on `UserPromptSubmit`, the gate of `guppi/gate.py` reads the tree, and the agent runs the skill `.claude/skills/handoff/SKILL.md` as rendered from `rule-handoff`.

Then:
The skill's context holds `git status --porcelain`. On a dirty tree the skill stops and says "commit first", and nothing is written.
**＋** On a clean tree the day's event log `vault/raw/<date>/event_log.md` holds the `handoff` mark of the call.
**＋** The agent writes `handoff.md` into the session's folder `vault/raw/<date>/<hi HHMM>/`: one document with no `---` and the sections that `rule-handoff` names, with no Read call on the artifacts.
**＋** Then the agent dispatches `librarian-guppi` with one line, `Materialize <date> from <path of handoff.md>.`, the path being that of the file just written, and shows the librarian's report to the person unchanged.
**－** In a session whose `raw/<date>/<hi HHMM>/work.md` holds `## Conserved Spec` — one that `/box` runs — the agent dispatches nothing after `handoff.md` and goes back to the step of `/box` that follows `/handoff`.
**－** No commit follows the handoff except the librarian's own, and no reply between the call and the librarian's report carries a `LEDGER` block.

## Result

2026-10-04, at the /hi of session 0004, by hand: session 0317 (transcript 5b311f89): after the reply that ends Retro and the commit 37c47bd1, /handoff called by Skill at 05:06:09 on an empty Tree line, the event log holding `05:06:09 5b311f89 handoff`; one Bash call counted the ledger lines and no Read call came before handoff.md was written at 05:06:38 into raw/2026-10-03/0317/, one document with no `---` and the seven sections of the skill; librarian-guppi dispatched at 05:06:39 with "Materialize 2026-10-03 from vault/raw/2026-10-03/0317/handoff.md.", its report shown at 05:13:39 in a blockquote, 30 of 30 lines equal; session 1416 (transcript 682b0e2f), work.md holding `## Conserved Spec`: /handoff at 14:40:53 on an empty Tree line, the mark `14:40:53 682b0e2f handoff`, handoff.md written at 14:41:19 with no Read call before it, no `---` and the seven sections; /handoff dispatched nothing, the next call at 14:41:26 being the switch and merge of /box, whose dispatch at 14:41:51 carries "Materialize 2026-10-03 from vault/raw/2026-10-03/1416/handoff.md."; the only commits after either handoff are the librarian's, fdd15ff3 and da671ebe, and no reply between a call and its report carries a LEDGER block; not exercised: a dirty tree

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
