---
type: estimate
kind: QA
status: pending
target: "[[rule-agent-writing]]"
purpose: The section stands in CLAUDE.md and one reply of the session holds to it — facts with a source, short sentences, the answer first, the not-done named
method: one reading by hand in the next session — the section in CLAUDE.md and one reply of the agent against it
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
The facts stay and the sales pitch goes; a claim names a real source or goes; short sentences, active voice, a common word over a term; the answer first; what is done and what is not done are named, the not-done never implied.
**－** The rule is about the agent's text, not about code — `make style` holds the style of the code.

## History

- 2026-09-20 created · [[decision-case-272.3]]
