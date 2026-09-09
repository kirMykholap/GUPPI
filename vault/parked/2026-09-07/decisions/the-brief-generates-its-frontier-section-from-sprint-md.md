---
title: "`brief.md` generates its frontier section from `sprint.md`"
type: decision
status: current
authority: brief-frontier-generation
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-30
created: 2026-08-30
target_kind: action
target: the-brief-generates-its-frontier-section-from-sprint-md
sources: ["archive/2026-08-30/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form/handoffs/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form.md"]
tags: [vault, process, harness]
---

# Context

**The frontier's third carrier is not built.** `sprint.md` is the frontier between sessions and where
a deferred pointer lands; `brief.md` is its view at session start
([[the-frontier-is-one-concept-with-three-carriers]]). Nothing writes that view.

**`brief.md` is derived and is never a source**, so the section cannot be typed into it by a
librarian: it would be gone at the next ingest and was never anywhere else. That much was already
ruled on 2026-08-29 and is the one part of the predecessor page that survives.

# The question

**What makes the between-sessions frontier visible at session start, rather than reachable only by a
grep?**

# How it works after

**The brief's generation reads `sprint.md` and prints a frontier section**: a numbered list, one line
per open item, with its status. A session opens with the list in front of it instead of discovering
the open items by searching `wiki/decisions/` for pages that happen to be live.

**Until it exists, the items deferred on 2026-08-30 arrive at the next session as decision pages
found by a grep.** Sixteen questions were deferred that evening and the mechanism that would have
presented them is the one not built. That is the concrete cost and it is being paid immediately.

# Recommendation

**Build it as part of the brief's generation and not as a separate file**, because a second file
holding the same list is a second thing to keep true.

# Ratification

**The owner selected it** by approving the plan of 2026-08-30, having defined the frontier's three
carriers the same day.

**Not built.** This decision is open and stays live in `wiki/decisions/` until the work exists.

*(Compiled from `raw/handoffs/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form.md`.)*
