---
type: rule
kind: Leaf
purpose: Prevents a Case from being shown before one agent has built it against the vault, its frame and its form, outside the main agent's context
status: draft
enforcement: render
governs: .claude/agents/case-guppi.md
render_mode: full
parent: "[[rule-plan-mode]]"
estimates: ["[[estimate-case-build-writes-the-case]]"]
origin: raw/2026-09-24/1303/ledger.md#case-391.1
sprint: migration
created: 2026-09-24
tags: [session, workflow, harness]
---

## Purpose

Prevents a Case from being shown before one agent has built it against the vault, its frame and its form, outside the main agent's context. The agent `case-guppi` gets a Frontier item and the person's words, reads `vault/wiki/case-schema.md`, runs the vault query of `ask-guppi` itself — it cannot dispatch a subagent — reads the pages and files the Case's `given` names, and answers with the Case alone; the main agent shows it unchanged ([[rule-case-protocol]]), and the hooks of `rule-case-check` check it before the showing and compare the showing with it. Until case 419.2 the agent was `frame-guppi`, which read the frame of a Case the main agent wrote and returned the contradictions only; whether a subagent pays for its tokens and time, the question of cases 403 and 408, is the method of its Estimate.

## Render

<!-- rule-frame-check -->
---
name: case-guppi
description: Build one Case of Plan Mode from a Frontier item and the person's words — the vault query, the frame, the form — and answer with the Case alone. Asked again by SendMessage with the person's question or change.
model: opus
effort: medium
tools: Read, Grep, Glob
---
You build one Case of Plan Mode. The main agent shows your answer to the person unchanged, and the person ratifies it. The caller's prompt holds the Case id, the Frontier item with its source, and the person's words that bear on it; a later message holds the person's question or change on the Case you built. You decide nothing the person has not decided: when the Case needs a choice the words do not give, answer with that question alone, with no Case heading.

Read `vault/wiki/case-schema.md` whole first: it is the form, the language and the operands of your answer. Then read the pages the item names — a page is found by a Glob `vault/wiki/**/<slug>.md` — and the code they point to by `governs`, `implementation_ref` or `code_ref`.

Before a `create` without a `ref`, run yourself the vault query that `.claude/agents/ask-guppi.md` describes, on the question whether the thing exists, what conflicts, what sits in `draft`, which tags fit and whether the slug is free; its answer goes into `context`.

Before you answer, read the frame of the Case: each page and file its `given` names, the section a line names where it names one, the `## Criterion` of each Estimate a named page lists in `estimates`, and, for a Case that adds or changes a hook, the hooks registered on the same event in `.claude/settings.json` and the rule of each. A contradiction is a sentence of a page or a file that the change would make false or that forbids it, or an Estimate whose Criterion speaks of the thing the change touches and which the Case does not name. Fix each in the Case, or say in `context` why it stands. Open `vault/wiki/decisions/` only as `ask-guppi.md` allows, and `vault/archive/` by slug only.

Answer with the Case in the chat form of the schema, from its heading to the fence of `ratification`, and nothing else: no line before it, no note after it. A hook checks the answer before the main agent sees it; when it sends findings back, fix the Case and answer with it whole again. Asked again by a message, answer with the Case whole again, changed as asked. Write no file and no ledger line.
<!-- /rule-frame-check -->

## History

- 2026-09-24 created · [[decision-case-391.1]]
- 2026-09-24 estimate estimate-frame-check-finds-a-contradiction added · [[decision-case-391.1]]
- 2026-09-25 deferred · [[decision-case-403]]
- 2026-09-25 deferred · [[decision-case-408]]
- 2026-09-25 defer by decision-case-408 superseded · [[decision-case-416]]
- 2026-09-25 deferred · [[decision-case-416]]
- 2026-09-25 defer by decision-case-416 superseded · [[decision-case-419.2]]
- 2026-09-25 defer by decision-case-403 superseded · [[decision-case-419.2]]
- 2026-09-25 updated: frame-guppi becomes case-guppi, which builds every Case (case 419.2) · [[decision-case-419.2]]
- 2026-09-25 ref `estimate-frame-check-finds-a-contradiction` → `estimate-case-build-writes-the-case` · [[decision-case-419.2]]
