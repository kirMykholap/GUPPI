---
type: decision
case: "962"
status: current
create: ["[[estimate-backlog-keeps-the-work-taken-out-of-a-built-page]]"]
update: ["[[entity-sprint-plugin]]"]
origin: raw/2026-10-31/0431/ledger.md#case-962
sprint: plugin
created: 2026-10-31
tags: [sprint, workflow]
---

## Problem

A line of a closed sprint's Backlog that names a page leaves the backlog list once that page is `built`, even when it names work beyond the page. The open work of Work Mode would drop out of sight that way, and the second part of the Spec box already has.

## Recommend

- **What happens to the open work of Work Mode?**
  - Recommended: (a) a note line in the Backlog of the live sprint `entity-sprint-plugin`, in its own words, taken out of `rule-work-mode`.
  - Answer: agreed, (a).
- **What happens to the second part of the Spec box?**
  - Recommended: (a) bring it back the same way as the work of Work Mode, as a note line on the live sprint page.
  - Answer: agreed, (a).
- **How is it checked that the list keeps the open work?**
  - Recommended: (a) a new Estimate on `rule-backlog`, read by hand on the live list after the librarian's run.
  - Answer: agreed, (a). The person noted that it is a one-time check and asked to discuss telling one-time Estimates apart from those that promise a behaviour; that is a separate Frontier item.

## History

- 2026-10-31 created · raw/2026-10-31/0431/ledger.md#case-962
