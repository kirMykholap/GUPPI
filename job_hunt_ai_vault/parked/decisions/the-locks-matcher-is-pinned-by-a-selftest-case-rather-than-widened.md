---
title: "The lock's matcher is pinned by a selftest case rather than widened to everything"
type: decision
status: current
authority: lock-matcher-strategy
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-20
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock/handoffs/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock.md", ".claude/settings.json", "scripts/hook-selftest.ps1"]
tags: [harness, agents, testing]
---

# Ruled 2026-08-20 by the owner

**The matcher stays `Agent|Task` and a selftest case asserts that the registration is what it says
it is.**

**Rejected: matching `.*` and filtering inside the script.** It is the obvious defence against a
tool word that changes again ([[the-dispatch-tool-is-agent-and-subagent-start-cannot-block]]), and
it **spawns a process on every tool call to guard a rare event**.

## What the case has to do, given the failure it guards

A matcher that names the wrong string produces a hook that never fires, and **that looks identical
to a hook with nothing to say** — the failure this project has shipped once already
([[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]]). So the case reads the registration in
`.claude/settings.json` rather than trusting the hook's own logic, and the eleven behavioural cases
sit behind it ([[the-librarian-lock-hook]]).

**What no case can reach is whether the harness fires the hook at all**, because hooks are read at
session start. That is an acceptance test after a restart and it is written in the hook's header.
