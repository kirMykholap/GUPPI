---
title: "A verdict that cannot be cleared survived a full design pass again, and was caught in the same place as before"
type: lesson
status: current
authority: unclearable-verdict-recurrence
basis: measurement
sprint: S3
created: 2026-08-30
sources: ["archive/2026-08-30/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form/handoffs/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form.md", "scripts/vault-check.sh"]
tags: [testing, vault, harness]
---

# The incident

**The handshake as planned would have reddened every `repeal` decision for good.** Rule 17 says a
decision whose target exists must be named back by it in `decided_by:`. A `repeal` decision:

- **lives forever** — Case 2.1 forbids it to leave `wiki/decisions/`, because it is the only live
  carrier of the fact that something is gone;
- **has a target that exists by definition** — you cannot repeal a page that was never written;
- **can never be named back**, because `decided_by:` is forbidden on entities and concepts.

**All three at once make the verdict permanently red with no action that clears it.** It was caught by
`/pre-task`, before anything shipped, and the repair was to scope the verdict to targets in
`proposals/` and `rules/` alone ([[the-unreachable-verdict-is-dropped-and-replaced]]).

# The class, and this is its third instance

**Three verdicts of this shape have now survived a full design pass**, and **all three were caught at
exactly the same point** — the plan check, never the design and never the review before it.

**The direction differs between the two halves of the class and the page should say which.** The
archived [[a-verdict-that-cannot-fire-is-worse-than-no-verdict]] is about a verdict that can never
**fire** — a check that passes everything. This one is about a verdict that can never be **cleared** —
a check that fails something forever. They are opposite failures of the same omission: nobody asked
what the verdict does across the whole population it ranges over.

# What it costs and what to do about it

**A verdict that cannot be cleared is worse than one that cannot fire**, because a permanently red
gate is what `lock-the-librarian.ps1` reads as a refusal to dispatch — locking out the only writer
permitted to clear it ([[a-lock-on-a-red-tree-hides-the-health-of-what-it-guards]]). The failure mode
is not noise; it is a stopped store.

**The question that would have caught all three is one sentence long:** *for every page this verdict
ranges over, name the action that turns it green.* If any class has none, the verdict is wrong before
it is written.

**Three instances, one detector, and the detector runs late.** `/pre-task` finds them because it reads
the tree against the plan; nothing earlier asks the question at all. That is the gap, and it is named
here rather than proposed as a fix.

*(Compiled from `raw/handoffs/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form.md`.)*
