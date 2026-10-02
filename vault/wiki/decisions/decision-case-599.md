---
type: decision
case: "599"
status: current
update: ["[[insight-prespec-main-agent-question-off-the-grill-me-shape]]"]
origin: raw/2026-10-02/2049/ledger.md#case-599
sprint: migration
created: 2026-10-02
tags: [session, workflow]
---

## Problem

The cause of the Insight is closed by a ratified rule, and the check of that rule passed once. The Insight still stands `open` in the backlog only because no decision marked it `actioned`. The question was whether to close it now, and which decision to name as the fix.

## Recommend

- **Should the Insight be marked closed now, and which decision should it name as the fix?**
  - Recommended: (a) close it now and name the decision that wrote the rule, `decision-case-561.13`. The cause is closed in `orchestration.md` and in the pre-spec skill, the check passed once on real questions at `/pre-spec`, and the schema says `addressed_by` names the decision that fixed the pattern.
  - Answer: (a).

## History

- 2026-10-02 created · raw/2026-10-02/2049/ledger.md#case-599
