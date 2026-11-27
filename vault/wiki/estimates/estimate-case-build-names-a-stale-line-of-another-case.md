---
type: estimate
kind: QA
status: passed
target: "[[rule-case-build]]"
purpose: Whether case-guppi, on a note that lists the Case file of another Case of the session, reads it, and names each line there that its change makes false with the change it needs on a line Other Case of its summary, or fixes its own Case where it is the one that is wrong
method: "by hand, after the first build in a session on the new Render of rule-case-build in which the note of the hook of rule-case-check lists the Case file of another Case of the session: the agent transcript of that case-guppi under ~/.claude/projects/, its case file and its summary read against the Criterion, the transcript in the estimate line"
checked: 2026-11-27
origin: raw/2026-11-20/1353/ledger.md#case-1039.2
sprint: plugin
created: 2026-11-20
tags: [session, workflow, harness, case-build]
---

## Criterion

When:
`case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, gets from the `SubagentStop` hook of `rule-case-check` a note that lists a file `raw/<date>/<hi HHMM>/cases/case-<M>.md` of another Case of the session, and answers again.

Then:
It reads that Case file whole by `Read`, as it reads each Case file of the session that a note names, and judges each line there that rests on what its own Case changes.
**＋** Where its change makes such a line false and the other Case should change, its `context` names that Case, the line and the change it needs, and the item of its Case in the summary carries a line `**Other Case:**` that names that Case and the change.
**＋** Where its own Case is the one that is wrong, it fixes its own Case instead.
**－** It reads no listed file of a Case that its prompt or a message names as built at the same time; its `context` names that Case and says why the file is not read.
**－** A line that its change leaves true needs no line `**Other Case:**`.

## Result

2026-11-27, /hi of session 0947, the transcript of the case-guppi of Case 1072 of session 2333 (~/.claude/projects/c--PROJECTS-GUPPI/3397fb1f-3741-4d29-83f5-2eb8f0cf5011/subagents/agent-a05161d566de45198.jsonl) and vault/raw/2026-11-26/2333/cases/case-1072.md; the SubagentStop note of rule-case-check listed vault/raw/2026-11-26/2333/cases/case-1073.md (line 281); Case 1073 was named as built at the same time, so case-guppi read no file of it and its context named that Case and the reason (line 316); at the second pass it read case-1073.md and case-1074.md whole by Read (lines 345, 462), found no line of them made false by its change, and its summary carried no line Other Case; the branches where another Case or its own Case needs a fix did not arise in this event

## History

- 2026-11-23 created · [[decision-case-1039.2]]
- 2026-11-27 status: pending → passed · raw/2026-11-27/0947/ledger.md#L1
