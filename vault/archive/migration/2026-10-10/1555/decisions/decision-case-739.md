---
type: decision
case: "739"
status: archived
children: ["[[decision-case-739.1]]", "[[decision-case-739.2]]"]
origin: raw/2026-10-08/2134/ledger.md#case-739
sprint: migration
created: 2026-10-08
tags: [session, workflow, harness, hooks]
---

## Problem

A Case can update a page that the cascade of `generate` archives in the same run, after an item of another Case of the session or of its own. No script reports it, so the update is lost in the archive unless a person or `ask-guppi` sees it.

## Recommend

- **Where does the fix for a missed cascade live?**
  - Recommended: (a) a step in the instructions of `case-guppi`, which follows the cascade of each related Case onto the pages its own Case changes.
  - Answer: none of the options. The person wants a check by script that takes the logic of the cascade from the script that writes the pages, so that the Cases are checked at `/pre-spec`, before the pages are written. The person asked whether it should also run earlier, on one Case.
- **Where does the script check of the cascade run?**
  - Recommended: (a) at both moments, the check of the file of a Case and `/pre-spec`, by one shared function.
  - Answer: agreed, (a).
- **Does a cascade hit block the Case or only warn?**
  - Recommended: (a) a note: the Case drops the update or its `context` says why it stands, and the person may keep the target.
  - Answer: agreed, (a).
- **Which steps of the cascade does the check cover?**
  - Recommended: (a) the steps that archive a page: the lessons of an Insight set `actioned`, an `open` Insight with no live child, and a superseded Decision page.
  - Answer: agreed, (a).
- **How is the change split, and what checks it?**
  - Recommended: (a) one Case with two sub-cases, the note of `/pre-spec` and the note of the check of the file, each with a new Estimate read by its unit tests; the rules of the cascade go into one shared function of `guppi/generate.py`, and `estimate-generate-cascades` stands.
  - Answer: agreed, (a).
- **Which changes of a Case get the note?**
  - Recommended: (a) an `update` only; a `delete` of such a page ends where the cascade ends.
  - Answer: agreed, (a).
- **Does a Case that both sets the status and changes the page get the note?**
  - Recommended: (a) no note inside one Case and its sub-cases, as in the note on a page another Case puts off.
  - Answer: (b): a note inside one Case too, its sub-cases compared with each other as well.

## History

- 2026-10-08 created · raw/2026-10-08/2134/ledger.md#case-739
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
