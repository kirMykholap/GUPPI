---
title: "No decision with an `action` target can close until tasks exist, and tasks are next"
type: decision
status: current
authority: tasks-scheduling
binding: deferral
basis: human
sprint: S3
decided: 2026-08-30
created: 2026-08-30
target_kind: none
target: none
sources: ["archive/2026-08-30/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form/handoffs/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form.md"]
tags: [vault, process, retrieval]
---

# Context

**`target_kind: action` means the decision is discharged the moment the task exists**
([[a-decision-is-discharged-by-being-handed-to-its-target]]). **`wiki/tasks/` does not exist** and is
deferred to S4 ([[the-folder-set-is-closed-and-tasks-is-not-in-it]]).

**Almost everything this project decides is a code or harness change.** Nine of the twenty decisions
filed on 2026-08-30 alone carry an `action` target.

# The question

**What happens to `action` decisions in the gap?**

# How it works after

**They accumulate live in `wiki/decisions/` with no mechanical exit, and that is by design rather than
by neglect.** The chain has no other route: the archiver cannot release them, because the target they
name cannot exist.

**It is a queue and not a defect, and it is visible** — a grep for live decisions carrying
`target_kind: action` is the list. **But nothing in the design said so**, and the owner would have met
it as a surprise, which is why it is written here.

**Tasks are the next thing built.** **owner:** «окей, постараемся перейти к action как можно быстрее,
но уже не сегодня».

**The largest consequence in the journal of 2026-08-30 is this one**, by the session's own reckoning.

# Recommendation

**Name the queue rather than invent a placeholder exit.** A route out that does not lead to a task
would discharge decisions into nothing, which is the failure the whole lifecycle was built against.

# Ratification

**The owner said it**, on 2026-08-30, in his own words, quoted above.

**A repeated deferral must name the sprint it happens in or be refused**
([[a-repeated-deferral-names-the-sprint-it-happens-in-or-is-refused]]). **This one names S4 by way of
the folder-set page and nothing more precise**, and the owner's «уже не сегодня» does not name a
sprint. **Raised for him rather than resolved by the librarian.**

*(Compiled from `raw/handoffs/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form.md`.)*
