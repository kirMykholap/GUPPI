---
title: "Hooks configured in `settings.json` do apply inside subagents"
type: concept
status: current
authority: subagent-hook-reach
basis: external
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock/handoffs/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock.md", ".claude/settings.json"]
tags: [harness, agents, process]
---

# What the documentation says

**Hooks configured in `settings.json` apply inside subagents.** A subagent may additionally declare
its own in frontmatter; that is an addition, not a replacement.

# Why this is written down at all

**A closed GitHub issue says the opposite, and it was relayed into this project before the
documentation was read.** The correction cost nothing this time because the claim was checked
before anything was built on it — but the same claim, unchecked, would have decided whether the
guard on the librarian's own writes reaches the librarian.

**A closed issue is not documentation**, and the rule that follows is the store's own: a claim
about the harness is read out of the documentation before it is built on
([[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]]).

# The reach that is documented and not verified here

**Whether `.claude/hooks/ask-the-vault.ps1` actually fires for a subagent's writes was not tested.**
The documentation implies it; nothing measured it. **So an existing guard's reach is believed
rather than known**, and that is on the deferred list rather than assumed
([[the-deferrals-of-this-session-go-onto-the-sprint]]).

The measurement rule this sits under is the store's own: a hook is measured from PowerShell or not
at all, and the branch is proved to have fired before anything is read off it
([[a-hook-is-measured-from-powershell-or-not-at-all]]).

## Verified for the Write path on 2026-08-20, and it had been believed rather than known

**A `general-purpose` subagent was instructed to write a path ending in `CLAUDE.md`, and it received
the guard verbatim** — *"You are editing a file that carries a project rule…"* — from
`.claude/hooks/ask-the-vault.ps1`.

**That closes an unverified claim rather than adding one**: the reach of an existing guard was
documented and had never been exercised ([[the-deferrals-of-this-session-go-onto-the-sprint]]).
**It is the Write path specifically**; nothing here measures Edit, and nothing measures a matcher
that never fires ([[a-verdict-that-cannot-fire-is-worse-than-no-verdict]]).

**No offender had to be planted** — the test was one real dispatch against the real tree
([[a-tree-broken-for-a-real-reason-is-a-better-fixture-than-a-planted-offender]]).
