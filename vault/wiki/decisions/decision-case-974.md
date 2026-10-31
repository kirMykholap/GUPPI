---
type: decision
case: "974"
status: current
create: ["[[estimate-case-build-reads-the-readers-of-a-new-files-folder]]"]
update: ["[[rule-case-build]]", "[[insight-case-build-changes-a-step-without-reading-its-readers]]"]
origin: raw/2026-10-31/2307/ledger.md#case-974
sprint: plugin
created: 2026-10-31
tags: [session, workflow, harness, case-build, prespec]
---

## Problem

A builder that searches for the readers of a new file by its name misses the code that takes every file of the folder, so the miss shows only when a test fails in Work Mode.

## Recommend

- **What the builder searches for a new file**
  - Recommended: (a) the paths of the folders that hold the file, the calls that walk a folder, and the ignore files of git, then each reader that takes every file of such a folder.
  - Answer: (a), by the recommendation.
- **Which new files the search covers**
  - Recommended: (a) each new file that is no vault page.
  - Answer: (a), by the recommendation.
- **How the change is checked**
  - Recommended: (a) a new Estimate, `estimate-case-build-reads-the-readers-of-a-new-files-folder`, read by hand after the first `/pre-spec` of a session in which a Case adds such a file.
  - Answer: (a), by the recommendation.
- **What happens to the reopened pattern note**
  - Recommended: (a) this Case sets `insight-case-build-changes-a-step-without-reading-its-readers` `actioned`.
  - Answer: (a), by the recommendation.
- **Whether item C5 is part of this Case**
  - Recommended: (a) apart; C5 stays its own Frontier item.
  - Answer: (a), by the recommendation.

## History

- 2026-11-01 created · raw/2026-10-31/2307/ledger.md#case-974
