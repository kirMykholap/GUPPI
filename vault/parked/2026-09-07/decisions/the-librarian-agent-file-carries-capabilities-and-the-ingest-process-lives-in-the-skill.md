---
title: "The librarian's agent file carries its capabilities, and the ingest process lives in the skill"
type: decision
status: current
authority: librarian-file-scope
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-29
created: 2026-08-29
sources: ["archive/2026-08-29/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md", ".claude/agents/vault-librarian.md", ".claude/skills/ingest/SKILL.md"]
tags: [vault, agents, harness]
---

# The ruling, 2026-08-29

**owner:** «@.claude/agents/vault-librarian.md должен содержать инструкции про : как искать и писать в
vault, какие субагенты и инструменты у него есть в распоряжении. Но у него не должно быть описания
процесса Ingest. Процесс ingest описывается тут @.claude/skills/ingest/SKILL.md»

**The agent file describes capabilities.** How to search the vault, how to write it, which tools it
holds and which subagents are at its disposal. **It never describes a ritual's process.**

**The ingest process lives in `.claude/skills/ingest/SKILL.md`** — including the instruction to
dispatch the decisions and lessons subagents and wait for them.

**He was correcting a session that had read the two as interchangeable.**

# What it obliges

**A step of `/ingest` written into the agent file is in the wrong file**, and the repair is to move it
rather than to copy it. Two copies of one process drift, which is the standing ground here for one
list of one set ([[one-librarian-behind-every-caller]]).

**The dispatch instruction is a process step and belongs to the skill**, even though the *capability*
to dispatch belongs to the agent file — the tool list is a capability, the order to use it is a
process ([[the-librarian-dispatches-its-own-reading-agents-and-returns-once]]).

**The agent file is a governed file**, so a rule page rendering into it is the mechanism that keeps
the capability half true ([[vault-librarian]],
[[the-shared-reading-discipline-renders-into-every-agent-that-reads-the-vault]]).

**Not built.** No file was moved this session; the ruling is recorded and the work is S3 item 36.

*(Compiled from `raw/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md`.)*
