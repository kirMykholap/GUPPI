---
type: decision
case: "310.3"
status: archived
create: ["[[estimate-sprint-migration-index-dissolved]]"]
origin: raw/2026-09-22/1121/ledger.md#case-310.3
sprint: migration
created: 2026-09-22
tags: [sprint, workflow, harness]
---

## Context

`guppi sprint` writes `sprint.md` from the page `entity-sprint-migration`: an item `- [[slug]] — …` gets `[x]` by the status of its page, a plain line renders `- [ ] …` and is never ticked, and a milestone holding one never closes. Themes 1–6 of Slice 3f are plain lines: 304–306 did themes 1–3, but the lines stand open and nothing can close them. In the Frontier a sprint item not taken in a session closes only by `[-] · defer case N` — hence 18 defer decisions on Slice 3b that decide nothing; in 0014 themes 4–6 were closed `· work` with a note, which is not true. Pages: `entity-sprint-migration` `draft`; `rule-sprint` `built`, of its three Estimates the Case touches `estimate-sprint-renders-the-backlog`; `rule-skill-hi` `built`, it touches `estimate-hi-writes-frontier`; `rule-prespec` `built`, it touches `estimate-prespec-checks-the-plan`; `rule-page-schemas` `draft`, `rule-glossary` `built`, `estimate-generate-writes-rules-from-applies-to` `passed`. The slugs `estimate-sprint-migration-index-dissolved` and `estimate-sprint-migration-file-route-gone` are free by the Grep over `estimates/`; the nearest is `estimate-sprint-migration-rule-class-files-dissolved`, the Estimate of the whole Slice — themes 4 and 5 are its parts that fail and are fixed apart, the Atomicity Rule.

## Problem

How a sprint item without a page closes; where a task of a milestone goes as prose so that the agent sees it; how the Frontier closes a sprint item not taken this session without a defer decision.

## History

- 2026-09-22 created · raw/2026-09-22/1121/ledger.md#case-310.3
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
