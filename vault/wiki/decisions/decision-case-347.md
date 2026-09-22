---
type: decision
case: "347"
status: current
update: ["[[rule-carry-over]]", "[[estimate-carry-over-writes]]"]
origin: raw/2026-09-22/2046/ledger.md#case-347
sprint: migration
created: 2026-09-22
tags: [session, workflow, harness, render]
---

## Context

Step 1 of the `/carry` skill — the Render of `rule-carry-over` — tells the agent to rewrite `vault/wiki/brief.md` "by the frame of `rule-brief` (the Render in `.claude/agents/librarian-guppi.md`)". It names the file and not the place in it. The frame stands between the `rule-brief` markers of that file, lines 77–93 today, and nothing in the instruction says so. The event log of the day records what follows: at 20:43:03, five seconds after `Skill: carry`, `grep -n -i "brief" .claude/agents/librarian-guppi.md`, and at 20:43:05 `sed -n '77,92p'` of the same file — the search for the frame and then the read of the marker range. The path of the brief itself is not the defect: step 1 names `vault/wiki/brief.md` in full, and step 3 commits it by name.
`rule-carry-over` stands `built`, a Leaf, `render_mode: full` over `.claude/skills/carry/SKILL.md`. Its one Estimate is `estimate-carry-over-writes`, `passed`, whose Criterion ends with a `－` line that the skill file equals the Render of the page; case 233.4 handled a change of this Render the same way — the page set `pending`, the Criterion kept. The reading of that Estimate needs a live `/carry`, so it falls to the next conserved session unless this one conserves again.

## Problem

The instruction names the file that holds the frame and not the place in it, so the agent searches for what the instruction could have pointed at.

## History

- 2026-09-23 created · raw/2026-09-22/2046/ledger.md#case-347
