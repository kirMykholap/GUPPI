---
type: rule
kind: Leaf
purpose: Prevents one judgment of the pipeline from living in two implementations that drift apart under a green suite
status: built
enforcement: render
governs: CLAUDE.md
render_mode: partial
parent: "[[rule-claude-md]]"
estimates: ["[[estimate-one-judgment-one-implementation-followed]]"]
origin: raw/2026-09-23/0034/ledger.md#case-360
sprint: migration
created: 2026-09-23
tags: [harness, workflow, render, tests]
---

## Purpose

Prevents one judgment of the pipeline from living in two implementations that drift apart under a green suite. The rule cannot be checked in substance, so its guard is the one `rule-agent-writing` has: the text stands in `CLAUDE.md`, which every session and every subagent reads, `render --check` keeps it identical to this page, and the governed-files hook refuses a hand edit. It actions `insight-harness-one-rule-implemented-twice-drifts` (case 360).

## Render

<!-- rule-one-judgment-one-implementation -->
## One judgment, one implementation

Where code judges the same text in two places — a check and a writer, a ticker or another check — the pattern or the predicate lives in one module and both sides import it; a second copy of one judgment is a defect on the day it is written. Where the two sides cannot share the code, one test runs both over the same input and asserts they answer alike.
<!-- /rule-one-judgment-one-implementation -->

## History

- 2026-09-23 created · [[decision-case-360]]
- 2026-09-23 estimate estimate-one-judgment-one-implementation-followed added · [[decision-case-360]]
- 2026-09-25 status: draft → built · cascade
- 2026-09-27 deferred · [[decision-case-455]]
- 2026-09-27 defer by decision-case-455 superseded · [[decision-case-462]]
- 2026-09-29 status: built → draft · cascade
- 2026-09-29 status: draft → built · cascade
