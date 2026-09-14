---
type: decision
case: "114"
status: current
update: [rule-page-generation]
supersedes: [decision-case-108]
origin: raw/2026-09-14/0747/ledger.md#case-114
sprint: migration
created: 2026-09-14
tags: [harness, workflow, ledger]
---

## Context

Twenty `clustered` lessons carry no `## Insight` section. The synthesis sets the `insight` field in the frontmatter, and nothing writes the section `lessons/schema.md` requires. They are 20 of lint's 125 schema findings. Deferred as 96 in session K, with its `purpose` cut short in the yaml and on `decision-case-96`. (Case 108 as it stands; 22 pages today.)

## Problem

Either the synthesis entry carries the section, or the schema stops asking for it. Both are a change of what a synthesis entry holds. (Case 108 as it stands.)

## Given

`lessons/schema.yaml`: `## Insight` optional, required when `status: clustered`; `schema.md:47`: "Script places the link once clustered". 23 live lessons carry `insight:`; one has the section (`lesson-hooks-sessionstart-cannot-block`, written by hand on 09-08); 22 do not — the two of session L among them.
**＋** `rule-synthesis` Render: the librarian appends an `update` of the lesson with `set: {status: clustered, insight: <slug>}` and nothing else; `deferred_by: [decision-case-108]`. The librarian writes no page: synthesis appends to the yaml, `generate` applies the yaml after it (frame steps 3 and 4), so the field and the section are one write.
**＋** `generate` writes a page's sections in `SECTION_ORDER`; a derived section is rebuilt from the field on every write of the page — `## Parent` from `parent`, `## Estimates` from `estimates`, `## Children` from `children` (`generate.py:361-366`). The cascade runs after all entries over every live rule, entity, decision and insight; lessons are read there for the recount only.
**＋** `rule-page-generation` is updated by 110 and 112.6 in this session; one more entry in ledger order. Its two Estimates: `estimate-generate-writes` (blocks 101.1, 104.1–104.3, 105.3, `failed` today) and `estimate-generate-walks-dates`; `estimate_slug: estimate-generate-writes`.
**－** `rule-synthesis` and the lessons schema do not change; the synthesis entry stays as it is.
**－** A lesson in the archive is not touched; `cleanup` and lint do not read the section.
**－** The Frontier line F5 closes on this Case.

## Criterion

- [[estimate-generate-writes]] § case 114

## History

- 2026-09-14 created · raw/2026-09-14/0747/ledger.md#case-114
