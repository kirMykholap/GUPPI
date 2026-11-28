---
type: estimate
kind: QA
status: passed
target: "[[rule-orchestration]]"
purpose: Whether the main agent asks for no number when it sends a ratified Case back in Plan Mode and shows it under the number the summary of its case-guppi gives, a new number with supersedes marks included
method: "by hand, at the Retro of this session: the new Render of rule-orchestration in the Spec read against the Criterion; by hand, after a session in which a ratified Case comes back in another shape: the messages of the main agent to its case-guppi and the showing, read in the transcript of that session under ~/.claude/projects/ against the Criterion, the transcript in the estimate line"
checked: 2026-11-27
origin: guppi
sprint: guppi
created: 2026-11-28
tags: [session, workflow]
core: true
---

## Criterion

When:
In Plan Mode, with `vault/wiki/orchestration.md` loaded, the main agent sends a ratified Case back to its `case-guppi` and that `case-guppi` answers with the summary of the Case.

Then:
The main agent asks for no number in its message to `case-guppi`.
**＋** The main agent shows the Case under the number of the `**Case:**` line of the summary.
**＋** A new number whose decision lines carry `{supersedes:case N}` is shown as it stands, since the Splitting of `vault/wiki/case-schema.md` sets it.
**－** The main agent does not send the Case back to be built under its old number.

## Result

2026-11-27, passed in the repository of GUPPI.

## History

- 2026-11-28 shipped with GUPPI
