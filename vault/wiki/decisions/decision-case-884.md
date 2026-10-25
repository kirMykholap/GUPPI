---
type: decision
case: "884"
status: current
create: ["[[estimate-ledger-write-keeps-the-window-past-a-later-resume]]"]
update: ["[[rule-ledger-write]]", "[[rule-ledger-write]]", "[[rule-orchestration]]"]
defer: ["[[rule-orchestration]]"]
supersedes: ["[[decision-case-876]]"]
origin: raw/2026-10-17/2307/ledger.md#case-884
sprint: plugin
created: 2026-10-17
tags: [session, hooks, ledger, harness, workflow]
---

## Problem

A session resumed, or compacted, on a later date than its `/hi` loses its `hi`, its folder and its plan file in every hook and command that reads its window, and so does a session whose log on a later date holds a tool line with the text of its start line. Its ledger lines are refused, `guppi caseid` prints no id, and a second `/hi` opens a new folder.

## Recommend

- **Which start line ends the walk back**
  - Recommended: (a) only a new session ends it: a `startup` or a `fork` start line.
  - Answer: agreed, (a).
- **What checks the fix**
  - Recommended: (a) a new Estimate on `rule-ledger-write`, checked by new tests and one reading on the live logs.
  - Answer: agreed, (a).
- **Whether the page `rule-ledger-write` gets a sentence**
  - Recommended: (a) a History line only.
  - Answer: agreed, (a).
- **Where the sprint close's new rule on old logs goes**
  - Recommended: (b) a new Case beside Case 884.
  - Answer: (b).
- **Change**
  - Asked: the person agreed to the fixes of the findings of `/pre-spec`: name `estimate-event-log-records` and `estimate-compact-recall-reloads` and say why each stands, and carry over the put-off of `rule-orchestration` from `decision-case-876`, so that it stays in `backlog.md`.
  - Taken: the `context` names both Estimates and why each stands; the Case gains a `defer` of `rule-orchestration` with the text of `decision-case-876` on that page, and an `update` of it with only a `change`, so that `generate` moves the put-off to this Case.
- **Change**
  - Asked: the person chose to add to this Case the second cut of the window, by a tool line whose text holds the stamp and the word `session-start`.
  - Taken: the walk ends only at a start line read by its form, a `－` line of `then` says that a tool line ends no walk, a test puts such a tool line on a later date, the Estimate covers both cuts, and the decision line on `rule-ledger-write` addresses the lesson of the second cut too.

## Deferred

### [[rule-orchestration]]

Each round and each rebuild resumes the same case-guppi by SendMessage with its whole transcript, so its context only grows, and nothing caps it or hands a rebuild to a fresh agent with the case file and the reason alone (lesson-case-build-agent-context-grows-on-every-resume); moved here from the defer of the lesson by Case 836, and carried over from decision-case-876 by Case 884

## History

- 2026-10-26 created · raw/2026-10-17/2307/ledger.md#case-884
