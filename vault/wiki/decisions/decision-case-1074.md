---
type: decision
case: "1074"
status: current
create: ["[[estimate-guppi-repository-readme-shows-the-path-of-a-decision]]"]
update: ["[[entity-guppi-repository]]"]
supersedes: ["[[decision-case-1068]]"]
origin: raw/2026-11-26/2333/ledger.md#case-1074
sprint: plugin
created: 2026-11-26
tags: [readme, github, ci, git]
---

## Problem

`README.md` uses terms it never explains, shows no question the person answers, and does not show how a signed answer becomes an enforced rule. A newcomer cannot picture the work before installing GUPPI.

## Recommend

- **What information the README gains**
  - Recommended: (b) key terms and the path of a decision, plus one short example question of a round.
  - Answer: agreed, (b).
- **Which diagram the README holds**
  - Recommended: (b) the path of one decision, from the person's answer to the rendered harness file.
  - Answer: agreed, (b).
- **How the diagram is drawn**
  - Recommended: (a) a Mermaid block in the README text, which GitHub draws.
  - Answer: agreed, (a).
- **How the change is checked**
  - Recommended: (a) a new Estimate on `entity-guppi-repository`, read by the person's answer at the Retro of this session.
  - Answer: agreed, (a).

## History

- 2026-11-27 created · raw/2026-11-26/2333/ledger.md#case-1074
