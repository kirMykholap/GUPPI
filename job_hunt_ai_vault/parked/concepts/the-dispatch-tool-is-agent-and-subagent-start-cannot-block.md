---
title: "The dispatch tool is `Agent` with `Task` as an alias, and `SubagentStart` cannot block"
type: concept
status: current
authority: dispatch-hook-surface
basis: external
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock/handoffs/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock.md", ".claude/settings.json"]
tags: [harness, agents, process]
---

# Two facts about the harness, both established from the documentation before anything was built

**The dispatch tool is `Agent`.** It was renamed from `Task` in 2.1.63 and the old name is kept as
an alias. **So a matcher naming only one of them is a lock that silently does not exist on some
version**, and the matcher for the librarian lock names both
([[the-librarian-lock-hook]], [[the-locks-matcher-is-pinned-by-a-selftest-case-rather-than-widened]]).

**`SubagentStart` looks like the right event and cannot block.** It is on the documented list of
events whose exit code is **ignored**, beside `SessionStart` and `InstructionsLoaded`. **A lock
built there would have looked identical to one that works** — it would have run, printed, exited
non-zero, and permitted the dispatch.

# Why both were read rather than assumed

Because the failure mode of a wrong answer here is invisible. A hook that never fires and a hook
with nothing to say produce the same output, and this project has already shipped that once
([[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]]).

**`PreToolUse` is the event that can deny**, which is why the lock is there and why it is `Pre`
rather than `Post` unlike the journal gate: the condition is knowable before the act, and the act
is what costs ([[the-journal-gate-hook]], [[agent-round-trip-cost]]).
