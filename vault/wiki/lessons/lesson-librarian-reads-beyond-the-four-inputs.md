---
type: lesson
kind: knowledge
root_cause: the agent prompt gives the librarian no description of how generate reads the yaml marks (near, librarian, synthesis), so it went to the code to learn the semantics; and rule-index-check lets it open a page when an index line is not enough while rule-synthesis forbids reading a lesson page, so the two rules disagree on the same act
status: clustered
source: raw/2026-09-10/event_log.md 11:49:55–11:50:15
insight: insight-librarian-frame-omits-required-reads
origin: raw/2026-09-10/ledger.md#L99
sprint: migration
created: 2026-09-10
tags: [harness, librarian]
---

## Trigger

on its first run the librarian read one lesson page and guppi/generate.py three times before any script had reported a problem, then edited the yaml by sed after the crash

## Root cause

the agent prompt gives the librarian no description of how generate reads the yaml marks (near, librarian, synthesis), so it went to the code to learn the semantics; and rule-index-check lets it open a page when an index line is not enough while rule-synthesis forbids reading a lesson page, so the two rules disagree on the same act

## Insight

- [[insight-librarian-frame-omits-required-reads]]

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#L99
- 2026-09-11 estimates removed: a lesson has no Estimate · [[decision-case-53.1]]
- 2026-09-11 updated: clustered by librarian: the frame omits reads the work needs, with lesson-frame-read-clauses-omit-candidate-check-and-brief · raw/2026-09-10/ledger.md#L132
- 2026-09-12 source set from its ledger line · [[decision-case-87]]
- 2026-09-14 insight section derived
