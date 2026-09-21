---
type: decision
case: "288.1"
status: current
update: ["[[rule-internal-context]]", "[[estimate-internal-context-loaded]]"]
origin: raw/2026-09-21/0019/ledger.md#case-288.1
sprint: migration
created: 2026-09-21
tags: [session, harness]
---

## Context

`CLAUDE.md` is the Render of `rule-claude-md` whole, with `rule-language` and `rule-agent-writing` in their markers. It enters the system prompt of every session and of every subagent — the librarian, `ask-guppi`, the subagents of Work Mode. Today it holds: the first paragraph (the description of the project and the one rule — ratification, autonomy over the how, "when unsure: it does", the vault as the only memory), "What is loaded here", the `@` import of the glossary, a paragraph on `index.md` not being imported, "Migration mode" (four items, each a Rule with its Render in the harness by now; "nothing prints it yet" stale since case 125) and "Commands" (`make style` before a commit stands in the Render of `rule-retro`; "no new dependencies" came with the hand-written file in 59.8, never decided on its own). The glossary through `CLAUDE.md` is paid by every subagent; a subagent receives the `CLAUDE.md` hierarchy and not the content of an invoked skill (Claude Code docs, sub-agents). `case-schema.md` opens with a line on how it is loaded and holds the form of a Case; the one rule is not in it.
The pages: `rule-claude-md` `built` — `estimate-claude-md-rendered` `passed` 1749, touched; `rule-internal-context` `built` — `estimate-internal-context-loaded` `passed` 1749, touched, its How it works says the glossary arrives through `CLAUDE.md`; `rule-case-protocol` `draft` — `estimate-case-protocol-loaded` `passed` 2106, touched, the other three Estimates not, its Purpose says "`CLAUDE.md` keeps the one rule and the glossary". Three `update` with a `ref`, no vault query due. `rule-info` rejected in the chat: the description of a project is no Rule by the glossary's check.

## Problem

The system prompt carries a retelling of rules that live in their own Renders, stale lines and a glossary every subagent pays for, and the one rule stands where no Case is held. What stays in `CLAUDE.md`, where the glossary goes and where the one rule.

## History

- 2026-09-21 created · raw/2026-09-21/0019/ledger.md#case-288.1
