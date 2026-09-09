---
title: "Switching permission modes is cache-safe, and a `/pre-task` dispatch costs the main context nothing"
type: concept
status: current
authority: permission-mode-cache-safety
basis: external
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact/handoffs/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact.md"]
tags: [agents, process, harness]
---

# What a mode switch does not invalidate

**Changing the permission mode changes neither the system prompt nor the tool definitions**, which
is what a prompt cache is keyed on. Entering and leaving plan mode is therefore free of the
re-processing cost a session would otherwise pay for it.

**The exception is the `opusplan` model setting, which is not in use here** — checked rather than
assumed.

**Plan mode and skills append their instructions as conversation messages**, at the point they take
effect, rather than editing anything above the cache boundary.

# Why the ritual is affordable

**A subagent's call and its result append to the parent conversation.** So dispatching `/pre-task`
from inside plan mode adds the dispatch and the answer and invalidates nothing
([[plan-mode-blocks-edits-and-not-a-subagent-dispatch]]).

**That removes one of the two standing objections to the trigger.** The other is wall clock, and it
is measured: a pre-task question is 5m54s ([[agent-round-trip-cost]],
[[one-pre-task-per-approved-scope-and-the-answer-comes-back-per-item]]).
