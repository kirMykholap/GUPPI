---
type: lesson
kind: knowledge
root_cause: the agent prompt gives the librarian no description of how generate reads the yaml marks (near, librarian, synthesis), so it went to the code to learn the semantics; and rule-index-check lets it open a page when an index line is not enough while rule-synthesis forbids reading a lesson page, so the two rules disagree on the same act
status: new
estimates: [estimate-librarian-reads-beyond-the-four-inputs]
origin: raw/2026-09-10/ledger.md#L99
sprint: migration
created: 2026-09-10
tags: [harness, librarian]
---

## Trigger

on its first run the librarian read one lesson page and guppi/generate.py three times before any script had reported a problem, then edited the yaml by sed after the crash

## Root cause

the agent prompt gives the librarian no description of how generate reads the yaml marks (near, librarian, synthesis), so it went to the code to learn the semantics; and rule-index-check lets it open a page when an index line is not enough while rule-synthesis forbids reading a lesson page, so the two rules disagree on the same act

## Estimates

- [[estimate-librarian-reads-beyond-the-four-inputs]]

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#L99
