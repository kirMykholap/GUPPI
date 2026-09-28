---
type: decision
case: "473.1"
status: current
create: ["[[estimate-retro-red-check-of-an-updated-page-is-a-handoff-note]]"]
update: ["[[rule-retro]]"]
origin: raw/2026-09-28/0000/ledger.md#case-473.1
sprint: migration
created: 2026-09-28
tags: [session, workflow, harness, render]
---

## Context

Some Cases change two things at once: a reader in code, and the page or governed file it reads. The reader runs from the working tree as soon as the code is written. The page lands only at the librarian's run, and the governed file at the render in that run. Between those two moments the reader refuses or goes red, and this happens by construction. Two lessons record it. After case 111.3, the Stop hook of session M refused 13 ledger lines: the reader required a stamped `hi`, and the writer of stamped lines reached `.claude/settings.json` only with the next render. That loss was stopped by the 111.6 fallback, which case 136.3 removed once the writer was live. After cases 227 and 229.1, `make lint` was red on the sprint step until the librarian's run.
`insight-workflow-code-live-before-the-page-it-reads` is `open`, severity 2, and case 238 defers it. Its Proposal is one sentence in `rule-work-mode`. That rule is a `draft` with only a `Purpose`, and 20 Cases defer it. Naming it would take up the whole rule (case 467). So the person chose `rule-retro` for the red half, for now, and will review where it belongs when `rule-work-mode` is taken up. The person chose `rule-case-build` for the fallback half, because `case-guppi` builds every Case and reads its frame.
The frame. The Render of `rule-retro` already says "Do not run `make lint` here" and "Red tests: fix now … the handoff still needs green". The new sentence leaves tests under that rule. `make lint` runs `render --check`, `sprint --check`, `backlog --check`, `glossary --check` and `guppi lint`. The librarian runs it after the render. A note for the handoff is already one of the four ends of a frontier item, and `rule-handoff` already writes such a note as the end of its item, so `rule-handoff` is not changed. `estimate-retro-loads` promises the readings. `estimate-retro-report-holds-each-fact-once` promises the form of the report, and its frontier already holds "what the agent noticed during Work Mode". Neither Estimate is touched. `estimate-case-build-writes-the-case` promises that `case-guppi` reads the frame and fixes each contradiction, and that stays true. The fallback is a promise of its own, on a new Estimate. Both `create` lines carry a `ref`, so no vault query was run. A Glob of `vault/**/` finds no page for either new slug.
Not done: `rule-work-mode` stays in the backlog as it is, and no rule about tests changes.

## Problem

No text says that a check which reads a page or a file the same Spec updates is expected to be red in Work Mode, so its red is taken for a finding or for debt. No text asks the author of a Case to keep a refusing reader working until its new writer is live, so a write that is refused in the gap is lost.

## Given

`rule-retro` — its Render, the paragraph that keeps `make lint` out of Retro
**＋** `.claude/skills/retro/SKILL.md` — the skill rendered from `rule-retro`
**＋** `make lint` — the checks of the vault, which the librarian runs after the render
**＋** `rule-handoff` — writes a note for the handoff as the end of its item, unchanged
**＋** `estimate-retro-report-holds-each-fact-once` — the promise of the form of the report, unchanged
**＋** `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note` — the new promise

## History

- 2026-09-28 created · raw/2026-09-28/0000/ledger.md#case-473.1
