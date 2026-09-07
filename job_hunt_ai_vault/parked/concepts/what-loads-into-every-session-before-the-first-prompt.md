---
title: "What loads into every session before the first prompt, and the nested `CLAUDE.md` is re-injected"
type: concept
status: current
authority: session-fixed-context-cost
basis: measurement
sprint: S3
created: 2026-08-30
sources: ["archive/2026-08-30/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form/handoffs/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form.md"]
tags: [vault, agents, harness]
---

# The fixed cost, measured 2026-08-29

| file | bytes |
|---|---|
| `job_hunt_ai_vault/CLAUDE.md` | 25,020 |
| `job_hunt_ai_vault/brief.md` | 14,050 |
| the repository's `CLAUDE.md` | 9,296 |
| `MEMORY.md` | 2,253 |

**About 50 KB, or ~13,000 tokens of project-controlled text, before a single question is asked** —
and **the vault's own schema document is half of it.**

**The largest single project-controlled fixed cost per session and per agent is the vault describing
itself.** That is the finding, and it is not a complaint about any one file: it is what the arithmetic
says about where the budget goes.

**It does not include the harness's own system prompt and tool schemas**, which are larger and which a
session cannot measure.

# And the nested file is injected twice

**`job_hunt_ai_vault/CLAUDE.md` entered one session's context TWICE, 25,020 bytes each time** — once
on the first read of a file under that directory, and again later.

**So the nested `CLAUDE.md` is re-injected rather than held once**, and the largest fixed cost is paid
more than once per session.

**What this does not establish is the trigger for the second injection.** The session that measured it
did not isolate it, and nothing here should be read as knowing when it fires.

# Why it matters more than the raw number

**It is paid per agent, not per session.** Every dispatch — the librarian, `/pre-task`, the two reading
agents — pays the same entry cost before it reads anything it was sent for. A fan-out of four agents
pays it four times.

**And it compounds with a corpus that is mostly about itself**
([[the-corpus-is-mostly-about-itself-and-the-owner-noticed-before-any-instrument-did]]). The schema
document grows as the store's own rules grow, so the fixed cost rises with every ruling about how the
store works and with none about the product.

**Nothing acts on this.** It is recorded as a measurement with its date, so a later reading can be
compared against it rather than started from nothing.

*(Compiled from `raw/handoffs/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form.md`.)*
