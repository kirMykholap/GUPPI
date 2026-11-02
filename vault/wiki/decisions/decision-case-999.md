---
type: decision
case: "999"
status: current
children: ["[[decision-case-999.1]]", "[[decision-case-999.2]]"]
origin: raw/2026-11-02/0039/ledger.md#case-999
sprint: plugin
created: 2026-11-02
tags: [sprint, harness, workflow, session, hooks, render, case-build]
---

## Problem

`case-guppi` must read whole a block of a generated file of about seven thousand lines to find what points to a page it changes, and the long blocks get cut. The graph meant to make that search quick and cheap became a long list read in full, and the step it serves has failed twice.

## Recommend

- **Which names the search takes**
  - Recommended: (b) the slug, the file name of each path, the name of the agent or the skill with its slash, and `guppi <command>` for each module that carries a command.
  - Answer: (b).
- **The purpose line beside each neighbour**
  - Recommended: (b) a second search over the pages on the list that prints the purpose line of each.
  - Answer: (b).
- **How the new search step is checked**
  - Recommended: (a) rename the failed Estimate and replace its Criterion by the new step.
  - Answer: (a).
- **How the removal of the graph is checked**
  - Recommended: (a) a new one-time Estimate on the sprint page.
  - Answer: (a).
- **The sprint Estimate on the bare link**
  - Recommended: (a) read it now, before the page moves.
  - Answer: (a).

## History

- 2026-11-02 created · raw/2026-11-02/0039/ledger.md#case-999
