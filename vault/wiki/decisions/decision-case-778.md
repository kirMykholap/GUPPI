---
type: decision
case: "778"
status: current
update: ["[[rule-skill-hi]]", "[[estimate-hi-takes-its-readings]]"]
origin: raw/2026-10-12/1449/ledger.md#case-778
sprint: plugin
created: 2026-10-12
tags: [session, harness, workflow]
---

## Problem

`/hi` makes a Cases line for an open `W` reading of an Estimate of the live sprint page that waits by design, so the person closes a line that needed no decision.

## Recommend

- **What should `/hi` do with a waiting sprint-page check**
  - Recommended: (a) it stays open in Work, as the close-of-sprint checks do.
  - Answer: not answered; replaced by the question on which readings skip the decision item at `/hi`.
- **How should `/hi` tell that a sprint check's work is not done**
  - Recommended: (a) no judgment of done at `/hi`: any open Work line of a check of the live sprint page that cannot be read now stays open in Work.
  - Answer: agreed, (a).
- **Which check confirms the change**
  - Recommended: (a) add one exception line to `estimate-hi-takes-its-readings` and set its purpose anew; its method stands.
  - Answer: agreed, (a).
- **Which readings should skip the decision item at `/hi`**
  - Recommended: (a) only the checks of the live sprint page; any other reading `/hi` cannot take still becomes a decision item.
  - Answer: agreed, (a). The person first proposed that every reading `/hi` cannot take stays in Work, is flagged by the librarian, and goes to the backlog by a defer at the next `/hi`, and asked whether such checks stay visible; after the answer the person agreed with the recommendation.
- **Should a check be allowed to wait for some event**
  - Recommended: (a) not in this Case; checks that wait for another event stay not allowed, and a wider rule is an item of its own.
  - Answer: agreed, (a).

## History

- 2026-10-12 created · raw/2026-10-12/1449/ledger.md#case-778
