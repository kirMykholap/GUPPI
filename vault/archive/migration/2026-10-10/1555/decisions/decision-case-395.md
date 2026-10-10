---
type: decision
case: "395"
status: archived
update: ["[[entity-sprint-migration]]"]
origin: raw/2026-09-24/1916/ledger.md#case-395
sprint: migration
created: 2026-09-24
tags: [sprint, workflow]
---

## Context

Today Slice 3g of `entity-sprint-migration` holds one note — a line with no wikilink — for the whole pass of Case 378 over the Estimates. A note never ticks and leaves only by the `update` that removes it, so it keeps the milestone open until the whole pass is done and does not show which part is done. One Frontier line of this size cannot close in one session; for the same reason the brief brings back `estimate-case-protocol-case-form` and `estimate-case-protocol-loaded` again and again as an item of their own: the note names no page. Counted on 2026-09-24 over 117 Estimate pages: `Given:` stands in the Criterion of 71; the eleven pages of the old model named by Case 378 all exist, 8 of them `passed`; three pages outside the eleven hold more than seven `＋` lines; `－` lines on the bounds of an edit stand on 28 pages; `### case N` blocks remain on 16 pages, and lint counts 21 pages `unmigrated`. `entity-sprint-migration` stands `draft`; its six Estimates speak of lint, the leftovers, the merge, the Rule-class files, `index.md` and the `file` route, none of the content of Slice 3g, so the Case does not touch them. An `update` with a `ref`, so no vault query; `frame-guppi` was not dispatched: the Case changes no behaviour of a rule or a hook.

## Problem

One note covers a pass over 117 pages: it cannot close in one session, and it does not show which part is done.

## Given

`entity-sprint-migration` — the section `## Milestones`, Slice 3g.
**＋** `vault/wiki/sprint.md` — its render, written by `uv run guppi sprint`.
**＋** `rule-sprint` — renders a line with no wikilink as a note that is never ticked.
**＋** `/hi` — assembles the Frontier from `vault/wiki/sprint.md`.

## History

- 2026-09-25 created · raw/2026-09-24/1916/ledger.md#case-395
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
