---
title: "The `/pre-task` is performed by dispatch, and the rule forbidding an unasked dispatch is the wrong one"
type: decision
status: current
authority: unasked-dispatch-resolution
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-25
created: 2026-08-25
sources: ["archive/2026-08-25/2026-08-25-the-twelve-items-are-decided-and-the-owner-names-what-the-discussion-costs/handoffs/2026-08-25-the-twelve-items-are-decided-and-the-owner-names-what-the-discussion-costs.md", ".claude/agents/pre-task.md"]
tags: [agents, process, harness]
---

# The ruling, 2026-08-25

> **owner:** «/pre-task выполняется только через dispatch агента - это правильно. сессия не имеет
> права диспатчить агента, которого ты не просил - неправильно.»

**The fork is resolved in favour of dispatch.** A session that reaches the ritual dispatches the
agent, and it does not ask first.

**The rule that loses is the one forbidding an agent the owner did not ask for**, as it is written.
It was never meant to reach a ritual the owner had already ordered; what it is about is a session
inventing work for a subagent.

# What it closes

**The contradiction recorded on 2026-08-24 has an answer.** That page put both rules side by side,
asked the owner for the one dispatch, and left the fork standing for the next session
([[divergence-the-session-dispatched-an-agent-where-its-instructions-forbid-one-unasked]]).
**Its ground is gone**: the next session does not meet the same fork.

**A divergence page is not retired by this.** It records what happened on the day it happened, and
what changed is that nobody has to break a rule to run the ritual again.

# Not done

**No rule text was changed.** The prohibition on an unasked dispatch still stands as written in the
harness, and this page is the decision that it must be narrowed rather than the narrowing. **Which
file carries it, and what the narrowed sentence says, is the next session's**
([[the-plan-is-committed-and-the-execution-moves-to-a-session-of-its-own]]).

# The ritual still has an ordering problem, and it is a different one

**The session that decided this ran the ritual late**, because its first write was the plan file
itself ([[divergence-the-pre-task-ran-after-the-first-write-rather-than-before-the-approval]]). **That
is about when the ritual fires, not about who may dispatch**, and nothing here answers it.

# The rule is cancelled outright, and it exists in no file this repository can reach — 2026-08-26

> **owner:** «Я вообще хочу убрать правило про "не диспетчерить агентов без твоей просьбы". Оно
> мешает больше, чем помогает. Хук правильно тебя словил, мы всегда сверяем план с вики. Более того
> - хук не пропустит тебя дальше без "/pre-task". Так что в любом случае диспатч.»

**Dispatching an agent is the norm of this project rather than an exception.** `/pre-task` is
performed only by dispatching the `pre-task` agent, and the `PreToolUse:Write` hook does not let a
first write past without one ([[a-pre-task-runs-between-the-plan-and-its-approval]],
[[the-plan-check-hook]]).

## The search for the rule's source closed with a zero

**Checked 2026-08-26 and reported as a negative rather than as a repair.** `CLAUDE.md` was read
whole and carries no such rule. The pattern
`do not (call|dispatch|use).{0,40}(agent|subagent|Task)` over `job_hunt_ai_vault/wiki`, `.claude/`
and `CLAUDE.md` returns **zero matches**; twelve rule pages mention dispatch and none forbids
anything.

**Also checked and clean:** `.claude/settings.json`, `.claude/settings.local.json`,
`~/.claude/settings.json`, the output styles in both trees, `.vscode/settings.json`, the VS Code
user settings, `~/.claude.json`, and VS Code's `globalStorage` and `workspaceStorage`.
`~/.claude/CLAUDE.md` does not exist. **The only occurrence of the phrase *"unless the user
requested"* anywhere on disk is the transcript of the session that received it.**

**So the rule arrives in the system prompt at runtime, from outside this repository**, and no session
can remove it at any permission level. **It is cancelled by the owner's word alone** until something
outside this repository changes.

## The rule he remembered as living in `CLAUDE.md` is a different one, and it is untouched

> **owner:** «Мы не трогаем правило про паралельный диспатч.»

**[[dispatch-librarians-in-parallel-only-for-reading]] is the only dispatch rule in `CLAUDE.md`**, and
it is about a write race in a parallel fan-out — a neighbour of the cancelled rule rather than the
rule itself ([[parallel-librarians-break-the-one-writer-property]],
[[the-parallel-dispatch-rule-closes-by-a-page]]).

## The librarian was not dispatched to delete it, and that substitution is the session's reading

*(the session understood it, and it is filed as understanding rather than as his instruction.)* He
said «пусть бибилотекарь посмотрит где это правило и уберет его». **The session performed the search
itself and returned a zero**, on the ground that a dispatch to confirm a negative costs 150,000 to
400,000 tokens ([[agent-round-trip-cost]]).

*(Compiled from `raw/handoffs/2026-08-26-the-carried-questions-are-answered-and-the-plan-is-corrected-before-it-is-built.md`.)*
