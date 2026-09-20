---
type: rule
kind: Leaf
purpose: Keeps the agent's text to facts with a source, short active sentences, the answer first and the not-done named
status: built
enforcement: render
governs: CLAUDE.md
render_mode: partial
parent: "[[rule-claude-md]]"
estimates: ["[[estimate-agent-writing-followed]]"]
origin: raw/2026-09-20/1308/ledger.md#case-272.3
sprint: migration
created: 2026-09-20
tags: [harness, render, workflow]
---

## Purpose

Keeps the agent's text — replies, pages, commit messages, documents — to facts with a
source, short active sentences, the answer first and the not-done named. Until case 272 the
rule was the section `## Style` of the Render of `rule-claude-md`: a standing condition with
no page and no Estimate. It is about the agent's prose; the style of the code is `make style`.

## Render

<!-- rule-agent-writing -->
## How the agent writes

Keep the facts and remove the sales pitch. Name a real source or remove the claim. Short
sentences, active voice, a common word over a term. Give the answer first. Say what is done
and what is not done; never leave the not-done implied.
<!-- /rule-agent-writing -->

## History

- 2026-09-20 created · [[decision-case-272.3]]
- 2026-09-20 estimate estimate-agent-writing-followed added · [[decision-case-272.3]]
- 2026-09-20 status: draft → built · cascade
