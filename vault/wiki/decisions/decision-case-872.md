---
type: decision
case: "872"
status: current
children: ["[[decision-case-872.1]]", "[[decision-case-872.4]]", "[[decision-case-872.2]]", "[[decision-case-872.3]]", "[[decision-case-872.5]]", "[[decision-case-872.6]]", "[[decision-case-872.7]]", "[[decision-case-872.8]]"]
origin: raw/2026-10-16/2104/ledger.md#case-872
sprint: plugin
created: 2026-10-16
tags: [session, workflow, harness, case-build, tests, prespec]
---

## Problem

Agents that run at the same time read files that a sibling agent is still writing. A Case then rests on a sibling's half-done text. And the person gets a separate question just to pass a change from one Case to another.

## Recommend

- **What to do with the Insight**
  - Recommended: (a) during a joint send, `case-guppi` reads no file of a Case built at the same time; once all have answered, each Case that points at a sibling goes back once to read the finished file.
  - Answer: agreed, (a).
- **One promise or two parts**
  - Recommended: (a) two sub-cases, one on `rule-case-build` and one on `rule-orchestration` and `rule-prespec`.
  - Answer: not answered; replaced by the question One promise or several parts, after the person's words on the question round for another Case.
- **One promise or several parts**
  - Recommended: (a) three sub-cases: the build during a joint send, the second pass of the main agent, and the send of another Case with no question.
  - Answer: agreed, (a).
- **Which joint sends it covers**
  - Recommended: (a) every time Cases are out together, the first build of a batch included.
  - Answer: agreed, (a).
- **Agents that edit one working tree in Work Mode**
  - Recommended: (a) leave Work Mode out; `context` says that the full test run after the last task covers that lesson.
  - Answer: agreed, (a).
- **How the fix is checked**
  - Recommended: (a) a new Estimate for the hold-off and one for the second pass, read after the next joint send; the two Estimates that promise the question have their Criteria replaced whole.
  - Answer: agreed, (a).
- **Where the question about another Case goes away**
  - Recommended: (a) everywhere in Plan Mode: the main agent sends the other Case back by itself, and the person agrees or not at its showing; Work Mode stays as it is.
  - Answer: agreed, (a). The person had said that a separate round only to pass information between Cases is bad, and that the agent should handle it.
- **How the main agent knows which Case points at a sibling**
  - Recommended: (a) a new summary line `**Sibling:**` from `case-guppi`, naming each Case of the send whose file it did not read and on which its Case rests.
  - Answer: agreed, (a).
- **How the second pass runs**
  - Recommended: (a) one Case after another, once, with no further loop; then an `**Other Case:**` line that still stands sends its Case back with no question.
  - Answer: agreed, (a).

## History

- 2026-10-17 created · raw/2026-10-16/2104/ledger.md#case-872
