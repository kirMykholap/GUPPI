---
type: estimate
kind: QA
status: passed
target: "[[rule-orchestration]]"
purpose: "Whether the main agent writes under ## Ask of the Frontier one line of the source stop for each From the person line of a ratified Case, in Plan Mode and in Work Mode, shows it in the acknowledging reply, and closes it with no reading when it sees the file, the data or the person's word on the action, while Work Mode still stops before the task"
method: "by hand at Retro of the session that changes it: the new Render of rule-orchestration in the Spec, read against the Criterion, recorded in the estimate line"
origin: guppi
sprint: guppi
created: 2026-11-28
tags: [session, workflow]
core: true
---

## Criterion

When:
A Case or a sub-case is ratified, in Plan Mode or in Work Mode, and the summary of its `case-guppi` holds a line `**From the person:**`, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.
**＋** Or the person gives, in Plan Mode or at the stop in Work Mode, the thing that an open line of the source `stop` of `raw/<date>/<hi HHMM>/frontier.md` waits for.

Then:
Before the reply that acknowledges the Case, the main agent writes under `## Ask` of `raw/<date>/<hi HHMM>/frontier.md` one line `- [ ] A<n> — case N — <what the person gives> · stop` for each such summary line, N the Case or sub-case of the task.
**＋** The reply shows that line in its Frontier.
**＋** A Case ratified again keeps the line it has and gets no second one.
**＋** The main agent closes the line `[x] … · stop · work` when it sees the thing: a file when a `Read` or a `Glob` of the path the line names finds it, data when the person's message holds it, and an action on the person's word that it is done.
**＋** The close of such a line writes no reading into the ledger.
**－** Work Mode still stops before the `stop:` task, as the fourth condition of `vault/wiki/where-to-stop.md` sets it, whether the line is closed or not.

## Result

2026-11-27, passed in the repository of GUPPI.

## History

- 2026-11-28 shipped with GUPPI
