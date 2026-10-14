---
type: rule
kind: Leaf
purpose: Keeps the agent's text to facts with a source, short active sentences, the answer first and the not-done named
status: built
enforcement: render
governs: CLAUDE.md
render_mode: partial
parent: "[[rule-claude-md]]"
estimates: []
origin: guppi
sprint: guppi
created: 2026-10-14
tags: [harness, render, workflow]
core: true
---

## Purpose

Keeps the agent's text — replies, pages, commit messages, documents — to facts with a
source, short active sentences, the answer first and the not-done named. It is about the agent's prose; the style of the code is `make style`.

## Render

<!-- rule-agent-writing -->
## How the agent writes

Keep the facts and remove the sales pitch. Name a real source or remove the claim. A claim is no wider than the output it rests on: a count comes from the run that printed it, and a claim about a whole set — every line, every entry — from a count on both sides; where no command covers it, write what was seen. Short
sentences, active voice, a common word over a term. Give the answer first. Say what is done
and what is not done; never leave the not-done implied.
<!-- /rule-agent-writing -->

## History

- 2026-10-14 shipped with GUPPI
