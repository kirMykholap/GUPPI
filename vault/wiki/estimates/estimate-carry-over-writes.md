---
type: estimate
kind: QA
status: passed
target: "[[rule-carry-over]]"
purpose: /carry writes the brief and the mark and runs nothing else
method: pytest over the skill's render, plus one live reading of a carried-over session
checked: 2026-09-18
origin: raw/2026-09-16/1034/ledger.md#case-190.1
sprint: migration
created: 2026-09-16
tags: [session, workflow, harness]
---

## Criterion

Given:
The hook `guppi spec` on `PostToolUse` of `ExitPlanMode` wrote the Spec and printed the fork into the context: go on — Work Mode — or conserve until the next session.
**＋** The agent asked the person which of the two and got "conserve".
**＋** `guppi materialize` knows a conserved unit by the file `carry.md` in the session folder (case 190.3) — by its presence, not its content.
**－** The person does not type `/carry`; the path of the skill is the agent's call on `PreToolUse Skill`.

When:
The agent calls the skill `carry` after the person's answer at the fork.

Then:
The skill reads the tree; when it holds changes outside the session folder and `vault/wiki/brief.md`, it stops and says: work was done, the ordinary exit applies.
**＋** Otherwise it rewrites `brief.md` — that is the conservation: the next session starts from it.
**＋** It puts `carry.md` into the session folder — one line, a flag for `materialize`, not a document; the session that finishes the work deletes it.
**＋** It runs `make style` and commits `vault/raw/` and `vault/wiki/brief.md`.
**－** It runs no Work Mode, `/retro`, `/handoff`, librarian, `materialize`, `generate`, `cleanup` or `render`; it writes no page of `vault/wiki/` but the brief.
**－** The work stays sequential, session after session: one conserved Spec, no parallelism.
**－** `.claude/skills/carry/SKILL.md` equals the Render of the page; it is not edited by hand.

## Result

2026-09-18, the live /carry of session 2054 after ExitPlanMode and the person's "conserve": Tree held only raw/2026-09-18/2054/; brief.md rewritten in the short shape, carry.md one line, make style clean, commit ba0240b of vault/raw/ and vault/wiki/brief.md; nothing else run, no page of wiki/ but the brief; the fork line of guppi spec was not visible in the ExitPlanMode result — the agent asked the fork itself

## History

- 2026-09-16 created · [[decision-case-190.1]]
- 2026-09-16 updated: the Criterion replaced whole by case 196.1 — the agent's call after the fork, the brief, the flag, the commit, nothing else run (case 196.1) · [[decision-case-196.1]]
- 2026-09-17 ref removed · one-off migration · raw/2026-09-16/2238/spec.md#case-210
- 2026-09-18 updated: the Render changed under it — the Deferred paragraph; the Criterion stands as it was (case 233.4) · [[decision-case-233.4]]
- 2026-09-18 status: pending → passed · raw/2026-09-18/2054/ledger.md#L12
