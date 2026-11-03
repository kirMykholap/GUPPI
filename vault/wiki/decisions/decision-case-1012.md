---
type: decision
case: "1012"
status: current
create: ["[[rule-frontier-hook]]", "[[estimate-frontier-hook-refuses-an-open-box-with-a-closer]]"]
update: ["[[rule-hook-registry]]", "[[insight-orchestration-frontier-closer-leaves-the-box-open]]"]
origin: raw/2026-11-02/2155/ledger.md#case-1012
sprint: plugin
created: 2026-11-02
tags: [hooks, harness, session, render, orchestration, workflow]
---

## Problem

An edit that adds a closer to a Frontier line and leaves its box `[ ]` passes unseen until `/pre-spec`, and a text of `orchestration.md` that the agent has to remember did not stop it twice.

## Recommend

- **How should the box and the closer get written together?**
  - Recommended: (a) a hook refuses the edit.
  - Answer: (a).
- **Which rule should own the new hook?**
  - Recommended: (a) a new rule page for the hook, `rule-frontier-hook`, under `rule-plan-mode`, with `rule-hook-registry` updated.
  - Answer: (a).
- **What should the hook refuse?**
  - Recommended: (a) only an open box with a closer.
  - Answer: (a).
- **Which lines should the hook look at?**
  - Recommended: (a) every line of the text the call would leave.
  - Answer: (a).
- **How should we check that the hook works?**
  - Recommended: (a) a new Estimate with a test.
  - Answer: (a).

## History

- 2026-11-03 created · raw/2026-11-02/2155/ledger.md#case-1012
