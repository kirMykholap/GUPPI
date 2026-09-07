---
title: "The guard chain appends the net rather than branching on it"
type: concept
status: current
authority: guard-chain-order
basis: code
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact/handoffs/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact.md", ".claude/hooks/ask-the-vault.ps1"]
tags: [harness, agents, vault]
---

# The chain picks one note, and the net is not part of the picking

**`.claude/hooks/ask-the-vault.ps1` is an `if / elseif` that picks exactly one note**, and the guard
branch that delivers a path-scoped rule is deliberately last
([[a-guard-branch-in-the-edit-hook-delivers-a-path-scoped-rule]]).

**A pre-task branch placed above it would shadow the delivery of a scoped rule on exactly the edits
a missing pre-task is most dangerous on** — the ones touching a file a rule guards. So the net is
**appended after** the chain has picked, rather than competing inside it.

**The invariant that survives is testable in those words:** *an earlier branch still wins its path*.
It holds because the branch that used to win still does; the net adds text after it rather than
replacing it.

# Why the chain assigns and prints once

**The branch chain no longer prints — it assigns, and one note is emitted at the end.** Two calls to
`Write-Note` would have put two JSON objects on one stdout, which nothing downstream reads
([[session-hooks]]).

That is a structural consequence of appending: the moment a hook has more than one thing to say, the
number of things it says and the number of times it writes have to be separated.

# What the net does not fire on

**A write into the vault arms nothing** ([[the-vault-is-excluded-from-the-pre-task-net]]), and a
payload with no `session_id` is answered with silence
([[the-write-net-requires-a-session-id]]). Both are exclusions applied to the appended net alone;
the chain above it is untouched by either.
