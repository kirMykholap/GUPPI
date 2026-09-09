---
title: "The hooks merge into a common pipeline"
type: proposal
status: current
authority: hook-pipeline-merge
basis: human
sprint: S3
created: 2026-08-25
decided_by: [[the-session-end-rule-is-instrumented-by-asking-the-tree]]
sources: ["archive/2026-08-25/2026-08-25-the-twelve-items-are-decided-and-the-owner-names-what-the-discussion-costs/handoffs/2026-08-25-the-twelve-items-are-decided-and-the-owner-names-what-the-discussion-costs.md", ".claude/settings.json"]
tags: [harness, agents, process]
---

# What it is, and it is his idea

> **owner:** «откладывваем как proposal»

**The hooks registered in `.claude/settings.json` become one pipeline rather than a set of separate
programs.** Eight are registered today across six events
([[session-hooks]]).

# How it got here, and the history matters

**It was raised while a session-end hook was being designed, dropped when that hook was refused, and
then recovered deliberately.** The owner refused the hook and kept the merge
([[the-session-end-rule-is-instrumented-by-asking-the-tree]]).

# What is open, and it is nearly everything

- **What "one pipeline" means**: a dispatcher per event, or one entry point that reads the event.
- **What it buys.** No cost has been measured and no defect is named that the merge repairs.
- **What it risks.** Every hook here is advisory except the ones that refuse, and merging changes
  which failures are shared ([[a-refusal-is-possible-on-pretooluse-alone-and-the-register-is-a-test]]).

**Nothing about it is designed**, which is why it is a proposal rather than a plan.

# A fourteenth hook was added rather than merged — 2026-08-30

**`.claude/hooks/serve-the-rule.ps1` is registered on `PreToolUse` with `Edit|Write`, alongside
`ask-the-vault.ps1` which already sits on the same event with the same matcher**
([[the-rule-server-hook]]).

**The session recommended a branch inside the existing hook and the owner ruled a separate one**, on
the ground that the mechanism is complex enough to deserve its own home
([[the-rule-server-is-a-hook-of-its-own]]).

**Two grounds found afterwards say the merge would not have worked as proposed, and they are the part
this page should carry.** `ask-the-vault.ps1` is a chain that **picks exactly one note**, by its own
design, and the new mechanism has to be able to speak on the same edit that trips one of those. And it
needs a `Read` matcher that script does not have, so it is a separate `settings.json` entry whatever
happens.

**That is the first concrete thing this proposal's *what it risks* line was reaching for.** "One
pipeline" over a set of hooks that each select one message needs a rule for what happens when two of
them have something to say, and no version of this proposal has one.

**The count in the text above is stale and is not rewritten here.** It reads *"eight are registered
today"*; the repository carried thirteen hooks before this session and fourteen after, of which two
can refuse — `lock-the-librarian.ps1` and `gate-the-handoff.ps1`, both through `permissionDecision`.
The rest print `additionalContext` and block nothing.

*(Extended 2026-08-30 from `raw/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md`.)*
