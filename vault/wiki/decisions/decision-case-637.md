---
type: decision
case: "637"
status: current
children: ["[[decision-case-637.1]]", "[[decision-case-637.2]]", "[[decision-case-637.3]]", "[[decision-case-637.4]]"]
origin: raw/2026-10-04/2245/ledger.md#case-637
sprint: migration
created: 2026-10-04
tags: [hooks, harness, workflow, session]
---

## Problem

Seven Estimates cannot close while their methods wait for live events that may not come before the sprint closes. Each needs a reading that can be taken at any time, or a promise cut to what such a reading checks.

## Recommend

- **How should the five checks of the answer hook be read?**
  - Recommended: (a) pytest alone; the live hook setup counts as proven by the check that passed live; the main agent's part of the clash check is settled in a later round.
  - Answer: agreed with the recommendation, (a).
- **How should the check that make lint runs every step be read?**
  - Recommended: (a) a new pytest runs the real `make lint` with a fake `uv` first on the search path that fails the backlog step, and asserts that all five steps ran in order and that the exit code is non-zero; the put-off question is taken up.
  - Answer: agreed with the recommendation, (a).
- **How should the check of a session opened without /hi be read?**
  - Recommended: (a) the method keeps only `make test-session-start`.
  - Answer: agreed with the recommendation, (a).
- **What happens to the part of the clash check that reads the main agent?**
  - Recommended: (a) the promise of the clash check is rewritten whole without the main agent's part and its trigger line; the main agent's step stays as text in `orchestration.md` with no check of its own.
  - Answer: agreed with the recommendation, (a).
- **How should this Case be split?**
  - Recommended: (a) four sub-cases: the four answer-hook checks whose method becomes pytest alone, the clash check, the `make lint` check with its new test, and the session-start check.
  - Answer: agreed with the recommendation, (a).
- **Change**
  - Asked: at pre-spec, the half of the dropped Criterion line on what `case-guppi` does after a clash stood in no live page, agent file or code; the person chose to add it to `rule-case-build` in 637.2, with no check of its own.
  - Taken: 637.2 replaces the sentence of `rule-case-build` on findings sent back with that sentence and the new one, and renders `.claude/agents/case-guppi.md` again; the Criterion of the clash Estimate is written under `sections.Criterion`, so the new line stays out of it.

## History

- 2026-10-05 created · raw/2026-10-04/2245/ledger.md#case-637
