---
type: lesson
kind: error
root_cause: the store of the Case-file check keeps an entry under every Case id it once checked and drops none that the file of its top-level Case no longer holds; only a {supersedes} mark in the ledger leaves such an entry out, and that mark comes only with the ratification the refusal blocks
status: clustered
insight: "[[insight-case-check-a-case-id-leaves-only-by-a-supersedes-line]]"
origin: raw/2026-10-07/1804/ledger.md#L27
sprint: migration
created: 2026-10-07
tags: [harness, workflow]
---

## Trigger

at the /pre-spec of session 1804 the case-guppi of Case 713 wrote it as sub-cases 713.1 and 713.2, which the check stored, then went back to the ratified 713 and built Case 719 to supersede it; the Stop check refused the showing of 719 twice on pairs only the stale 713.1 and 713.2 held, and 719 was dropped and its fixes put off (cases 720, 721)

## Root cause

the store of the Case-file check keeps an entry under every Case id it once checked and drops none that the file of its top-level Case no longer holds; only a {supersedes} mark in the ledger leaves such an entry out, and that mark comes only with the ratification the refusal blocks

## History

- 2026-10-07 created · raw/2026-10-07/1804/ledger.md#L27
- 2026-10-07 updated: clustered under insight-case-check-a-case-id-leaves-only-by-a-supersedes-line (synthesis) · raw/2026-10-07/1804/ledger.md#L27
