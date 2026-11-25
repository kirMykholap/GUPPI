---
type: decision
case: "1053"
status: current
children: ["[[decision-case-1053.1]]", "[[decision-case-1053.2]]"]
origin: raw/2026-11-25/0816/ledger.md#case-1053
sprint: plugin
created: 2026-11-25
tags: [harness, workflow, hooks, session, ledger]
---

## Problem

A new Case beside a ratified one can take the number of a short-form Case, since nothing stops a case file under a number that only the ledger holds. A Case can also put a reading at a stop of Work Mode before the render of the file it tests, and `/pre-spec` let one through.

## Recommend

- **How does a new Case stop taking the number of a Case with no file?**
  - Recommended: (a) the guard refuses the first write under a number the ledger already holds, a `defer` included, and names a free number.
  - Answer: (a), as recommended.
- **Where is a reading placed before the render it tests caught?**
  - Recommended: (b) a coded finding in `guppi prespec --check` for a Case with a render line of a file, a `stop:` task, and a `when` or `then` that names that file.
  - Answer: (b), as recommended.
- **Does this Case close the Insight?**
  - Recommended: (a) set `insight-workflow-code-live-before-the-page-it-reads` `actioned` by the sub-case that fixes the second fault.
  - Answer: (a), as recommended.
- **What happens to the empty file of the wrong number?**
  - Recommended: (a) leave it.
  - Answer: (a), as recommended.

## History

- 2026-11-25 created · raw/2026-11-25/0816/ledger.md#case-1053
