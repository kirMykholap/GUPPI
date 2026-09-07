---
title: "A blocker can be dissolved by changing the design instead of answered"
type: lesson
status: archived
authority: blocker-dissolution
basis: human
sprint: S2
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-a-rule-is-written-once-and-rendered/handoffs/2026-08-17-a-rule-is-written-once-and-rendered.md"]
tags: [process, harness]
---

# The instance

*Which files may be exempt from "a rule with no region is red"* stood as **one of the three items
blocking the harness build** for a day ([[what-the-harness-build-waits-on]],
[[marked-regions-and-the-prose-outside-them]]). It was a real blocker: nothing could be built while
the exemption list was undecided, and the list could only be guessed at, because no region existed
yet to judge it against.

**It was never answered.** The verdict changed from red to advisory, and the question stopped
existing ([[a-governed-file-with-no-region-is-an-advisory]]). There is no exemption list, and there
is nothing to decide about one.

# Why the distinction is worth carrying

A blocker on a register invites one move: **go and settle it.** That move is often the expensive
one, because a question that cannot be answered yet usually cannot be answered because the design
around it is wrong — the exemption list here would have been a set of guesses, frozen into a rule,
maintained by hand, and drifting from the first day ([[a-copied-list-drifts-and-a-sweep-cannot]]).

So the question to ask of a blocking item is **not only "what is the answer" but "what would have
to be true for this question to matter"**. Here: the strictness of the verdict. Loosen it, and the
question is void rather than open.

**Recording the difference matters for the register itself.** A row removed because it was answered
and a row removed because it dissolved look identical afterwards, and only the second one carries a
transferable move. This one is written down for that reason, at the owner's request.
