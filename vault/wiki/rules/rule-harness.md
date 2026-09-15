---
type: rule
kind: MOC
purpose: Prevents the tools of the harness from drifting apart from the pages that describe them
status: built
children: ["[[rule-render-harness]]", "[[rule-settings]]", "[[rule-lint]]", "[[rule-governed-files-hook]]", "[[rule-claude-md]]", "[[rule-bash-guard]]", "[[rule-tests-clock-pinned]]"]
estimates: ["[[estimate-harness-pipeline]]"]
origin: raw/2026-09-10/ledger.md#case-37
sprint: migration
created: 2026-09-10
tags: [harness, workflow]
---

## Purpose

Prevents the tools of the harness from drifting apart from the pages that describe
them. Three rules belong to no phase of the session: the renderer, the page
`.claude/settings.json` is assembled from, and lint. They run together in `make lint`, in this order: the harness files are checked against their pages before the pages. Four more belong here and run in no pipeline: the hook that refuses a hand edit of a rendered file, the hook that refuses a heredoc with a backslash or a file write, the page `CLAUDE.md` is rendered from, and the pinned clock of the tests (cases 59.6, 59.8, 127, 145.1).

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-37
- 2026-09-10 estimate estimate-harness-pipeline added · raw/2026-09-10/ledger.md#case-37
- 2026-09-10 status: draft → built · cascade
- 2026-09-12 child rule-governed-files-hook added · [[decision-case-59.6]]
- 2026-09-12 child rule-claude-md added · [[decision-case-59.8]]
- 2026-09-12 updated: two children outside the make lint pipeline — the guard hook and the CLAUDE.md page (case 66) · [[decision-case-66]]
- 2026-09-12 child rule-settings added · [[decision-case-85.2]]
- 2026-09-12 updated: rule-settings takes the slot of rule-hook-registry, which becomes its child (case 85.2) · [[decision-case-85.2]]
- 2026-09-12 updated: rule-settings takes the slot of the hook registry in the Purpose too (case 99) · [[decision-case-99]]
- 2026-09-14 child rule-bash-guard added · [[decision-case-127]]
- 2026-09-14 updated: the bash guard hook counted among the children outside the pipeline (case 132) · [[decision-case-132]]
- 2026-09-14 child rule-tests-clock-pinned added · [[decision-case-145.1]]
- 2026-09-14 updated: rule-tests-clock-pinned added (case 145.2) · [[decision-case-145.2]]
- 2026-09-14 updated: three rules in make lint, four outside it; the pipeline's Method without tests/test_index.py (case 153) · [[decision-case-153]]
- 2026-09-14 status: built → draft · cascade
- 2026-09-14 child rule-index archived · cleanup
- 2026-09-15 status: draft → built · cascade
