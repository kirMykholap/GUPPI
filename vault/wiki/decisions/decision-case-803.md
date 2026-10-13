---
type: decision
case: "803"
status: current
create: ["[[estimate-case-build-offers-a-page-for-code-no-page-covers]]"]
update: ["[[rule-case-build]]", "[[rule-case-protocol]]"]
origin: raw/2026-10-13/1753/ledger.md#case-803
sprint: plugin
created: 2026-10-13
tags: [session, workflow, harness, ledger]
---

## Problem

In a project with code that no page covers, an item on that code gives `case-guppi` no page to start from, and nothing lets it read the code or offer a page. The pages cannot grow with the Cases.

## Recommend

- **When does code count as covered by a page?**
  - Recommended: (a) a live page names its file, or a folder that holds it, in `code_ref`, `implementation_ref` or `governs`.
  - Answer: agreed, (a).
- **What does the round offer for code no page covers?**
  - Recommended: (a) the path added to a page that already describes the thing, or else a new page for the thing the Case changes, its category by the schema check, with its slug, purpose, parent and paths; where the person turns both down, `case-guppi` asks which page the Case changes.
  - Answer: agreed, (a).
- **Where does the new page stand?**
  - Recommended: (a) in the same Case, as a task, with the Estimate of the change on that page.
  - Answer: agreed, (a).
- **Does the schema sentence on page parts change?**
  - Recommended: (a) it stands; only `rule-case-build` changes for the new step.
  - Answer: agreed, (a).
- **How is the change checked?**
  - Recommended: (a) a new Estimate, read by hand at the Retro of this session against the new Render in the Spec.
  - Answer: agreed, (a).

## History

- 2026-10-13 created · raw/2026-10-13/1753/ledger.md#case-803
