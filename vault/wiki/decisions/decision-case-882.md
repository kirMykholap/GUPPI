---
type: decision
case: "882"
status: current
children: ["[[decision-case-882.1]]", "[[decision-case-882.2]]"]
origin: raw/2026-10-17/2307/ledger.md#case-882
sprint: plugin
created: 2026-10-17
tags: [harness, workflow, librarian, session, ci, git, plugin]
---

## Problem

The clean version ships the Criteria of `passed` Estimates with sentences true only in the repository of GUPPI, and each rewrite sets its Estimate `pending`, which turns its rule `draft` and stops the build of the clean version until a reading passes.

## Recommend

- **What does this Case take?**
  - Recommended: (a) only the eight rewordings.
  - Answer: agreed, (a).
- **Which of the eight are reworded now?**
  - Recommended: (a) only the two that this session's Retro can read.
  - Answer: agreed, (a).
- **How is a sentence reworded?**
  - Recommended: (a) the same way as the last two sessions.
  - Answer: agreed, (a).
- **What happens to the put-off on `rule-clean-branch`?**
  - Recommended: (a) take it up and put it off again, naming only what is left.
  - Answer: agreed, (a).
- **Change**
  - Asked: the person agreed to the fixes of the findings of `/pre-spec`: name Case 883 on the reading of `estimate-generate-writes-the-decision-page`, name the `.gitignore` texts outside the Criteria in the put-off, and say that the old Decision page ends `archived`.
  - Taken: the `context` names Case 883 and the archive step of the cascade, and the purpose of the defer of 882.3 names the three `.gitignore` texts.

## History

- 2026-10-26 created · raw/2026-10-17/2307/ledger.md#case-882
- 2026-10-28 child decision-case-882.3 archived · cleanup
