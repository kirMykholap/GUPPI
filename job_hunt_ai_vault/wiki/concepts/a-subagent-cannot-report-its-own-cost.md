---
title: "A subagent cannot report its own token cost, so a measurement reaches the log only through the feedback section"
type: concept
status: current
authority: agent-cost-reporting
basis: code
sprint: S0
created: 2026-08-14
sources: ["archive/2026-08-14/2026-08-14-acceptance-and-the-shortened-claude-md/handoffs/2026-08-14-acceptance-and-the-shortened-claude-md.md", ".claude/skills/handoff/SKILL.md"]
tags: [agents, vault]
---

# The one number the librarian cannot write down

The harness reports an agent's cost — as `subagent_tokens` — **to the main session, when the agent
finishes.** The agent itself never sees it. And `log.md` has exactly one writer, the librarian,
which is an agent ([[the-librarian-writes-unattended]]).

So the two ends do not meet: **the party that knows the number may not write it, and the party that
writes may not know it.**

That is why `- measure: tokens=` lines travel through **section 7 of the journal** — the main
session records what the harness told it into [[vault-feedback-file]], `/handoff` moves it into
section 7, and `/ingest` copies it into `log.md`. The first design, "have the librarian record its
own cost", was not merely awkward: it was impossible, and the difference matters when someone
proposes it again.

## What the number is, and what it is not

`subagent_tokens` has **undocumented composition** — input, output, or both is not stated anywhere
we can read. It is therefore recorded **as observed**, never converted to money and never restated
as a rate. A figure whose units are unknown becomes a wrong figure the moment it is multiplied by a
price, and it then travels ([[a-stated-count-drifts-from-the-list-it-heads]]).

The measured figures for a librarian call, and the boundary they carry, are on
[[agent-round-trip-cost]].

## The agent can report its own *shape*, and that report is weaker than the harness figure

**On 2026-08-20 the ingest reported its own tool calls** — 79 calls, 41 read-type against 38
write-type, first write 4m34s into a 24m30s run — beside the harness's **224,128 tokens, 82 tool
uses, 25m34s**. **The two counts of tool uses disagree by three**, which is the point rather than a
defect: one is measured from outside and one is recalled from inside.

**So a self-report is admissible and is ranked below the harness figure standing next to it.** It
answered a question the harness cannot — what fraction of the run was read-only
([[read-only-scouts-one-per-folder-ahead-of-the-librarian]]) — and it is labelled as a self-report
wherever it is quoted ([[agent-round-trip-cost]]).

**The rule this page states is unchanged**: the token cost reaches `log.md` only through the
journal's feedback section, because the party that knows it may not write it.
