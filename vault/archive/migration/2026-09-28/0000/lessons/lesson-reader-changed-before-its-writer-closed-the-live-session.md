---
type: lesson
kind: error
root_cause: the hooks run the code of the working tree, so a change of a reader takes effect in the session that writes it, before its writer exists; the Case named the new form only and no test seeded the log of the very session that would run it. A reader that drops an old form keeps it as a fallback until the new writer is measured live (case 111.6).
status: archived
insight: "[[insight-workflow-code-live-before-the-page-it-reads]]"
origin: raw/2026-09-14/0747/ledger.md#L49
sprint: migration
created: 2026-09-14
tags: [harness, hooks, ledger, workflow]
---

## Trigger

after case 111.3 was coded, the Stop hook of session M refused 13 reading lines: hi_recorded in the working tree required a stamped hi, every hi of the session was --------, and the writer of stamped lines (the UserPromptSubmit hook of 111.1) reaches settings.json only with the next render.

## Root cause

the hooks run the code of the working tree, so a change of a reader takes effect in the session that writes it, before its writer exists; the Case named the new form only and no test seeded the log of the very session that would run it. A reader that drops an old form keeps it as a fallback until the new writer is measured live (case 111.6).

## History

- 2026-09-14 created · raw/2026-09-14/0747/ledger.md#L49
- 2026-09-18 updated: clustered by librarian under insight-workflow-code-live-before-the-page-it-reads · raw/2026-09-17/1119/ledger.md#L43
- 2026-09-28 archived · insight actioned
- 2026-09-28 archived · cleanup
