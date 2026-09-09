---
title: "A lock on a red tree hides the health of the thing it guards"
type: concept
status: current
authority: lock-diagnostic-masking
basis: measurement
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-lock-fires-and-deadlocks-the-vaults-only-writer/handoffs/2026-08-20-the-lock-fires-and-deadlocks-the-vaults-only-writer.md", ".claude/hooks/lock-the-librarian.ps1"]
tags: [harness, agents, testing]
---

# The mechanism

**The lock denies at `PreToolUse`, which is before the agent type is resolved**
([[the-librarian-lock-hook]]). So a denied dispatch proves the hook fired and proves **nothing**
about whether the agent it names still exists.

**Two denials told us nothing about the registry. The first *accepted* dispatch answered it in one
move.**

# The instance, and the order the answers arrived in is the finding

The owner moved `.claude/agents/vault-librarian/AGENT.md` to `.claude/agents/vault-librarian.md`
mid-session. **Both layouts are legal** ([[claude-code-config-loading]]), and whether the registry
re-reads after a move inside a running session was untested.

**It could not be asked while the gate was red**, because every dispatch was denied before the
lookup. The moment the tree went green, the first real dispatch was accepted and launched — so
`.claude/agents/vault-librarian.md` resolves, the registry re-reads, and the mid-session move cost
nothing ([[vault-librarian]]).

**The answer was free and it was unavailable.** That sequence is the general claim: **a guard that
refuses on a broken tree also suppresses the diagnostics that would tell you whether what it guards
is healthy.**

# What it obliges

- **A red-tree denial is not evidence about the agent.** Reading one as *the librarian is fine, it
  was just blocked* is the same error as reading a green suite that never ran
  ([[a-verdict-that-cannot-fire-is-worse-than-no-verdict]]).
- **Questions about the guarded thing are asked on a green tree, and only there.** They are cheap
  then and impossible before.
- **It is a second argument for the escape hatch** that
  [[a-gate-that-refuses-work-without-an-open-sprint]] leaves open — the first being the deadlock
  ([[the-one-writer-clause-reaches-a-citation-and-not-only-a-register]]). A hatch is not only about
  clearing the gate; it is about being able to look through it.
