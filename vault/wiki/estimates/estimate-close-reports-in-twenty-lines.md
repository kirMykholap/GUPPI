---
type: estimate
kind: QA
status: pending
target: "[[rule-close]]"
purpose: Whether the librarian's report, as /handoff or /box shows it, gives the counts, the flags and the lint total in twenty lines or fewer
method: "by hand, after a librarian's run whose .claude/agents/librarian-guppi.md, when the run starts, holds the Render of rule-close: the person's answer on whether the report that /handoff, or /box in a session that /box runs, showed after that run gave the counts, the flags and the lint total in twenty lines or fewer"
origin: raw/2026-10-29/1930/ledger.md#case-903.2
sprint: plugin
created: 2026-10-29
tags: [harness, workflow, librarian]
---

## Criterion

When:
The librarian's run that `/handoff` of `.claude/skills/handoff/SKILL.md` dispatches ends, and `/handoff` shows its report to the person.
**＋** In a session that `/box` runs, `/box` of `.claude/skills/box/SKILL.md` dispatches that run and shows its report to the person instead.

Then:
The report reaches the person with the counts, the flags and the lint total.
**＋** The report holds twenty lines or fewer.

## History

- 2026-10-29 created · [[decision-case-903.2]]
