---
type: estimate
kind: QA
status: failed
target: "[[rule-agent-writing]]"
purpose: The section stands in CLAUDE.md and one reply of the session holds to it — facts with a source, short sentences, the answer first, the not-done named
method: one reading by hand in the next session — the section in CLAUDE.md and one reply of the agent against it
checked: 2026-09-26
origin: raw/2026-09-20/1308/ledger.md#case-272.3
sprint: migration
created: 2026-09-20
tags: [harness, render, workflow]
---

## Criterion

Given:
The conditions of the parent.
**＋** `rule-agent-writing` is a Leaf, `enforcement: render`, `render_mode: partial`, `governs: CLAUDE.md`, a child of `rule-claude-md`; its Render is the section `## How the agent writes` inside the marker `<!-- rule-agent-writing -->`.

When:
A session starts with `CLAUDE.md`, and the agent writes a text — a reply, a page, a commit message, a document.

Then:
The facts stay and the sales pitch goes; a claim names a real source or goes, and is no wider than the output it rests on — a count from the run that printed it, a claim about a whole set from a count on both sides (359); short sentences, active voice, a common word over a term; the answer first; what is done and what is not done are named, the not-done never implied.
**－** The rule is about the agent's text, not about code — `make style` holds the style of the code.

## Result

2026-09-26, CLAUDE.md lines 11–17 and the replies of session 1745 read by hand; most replies give the answer first with counts from their runs, but the Work Mode report says 10 Estimates wait for the next session where the ledger names 12, and the retro reply announces "three more" and lists two

## History

- 2026-09-20 created · [[decision-case-272.3]]
- 2026-09-20 status: pending → passed · raw/2026-09-20/1749/ledger.md#L4
- 2026-09-23 updated: the Criterion names the width of a claim (case 359) · [[decision-case-359]]
- 2026-09-26 status: pending → failed · raw/2026-09-26/1745/ledger.md#L36
