---
title: "A decision is discharged by being handed to its target, and the session never reports that the work is done"
type: decision
status: archived
authority: decision-discharge-criterion
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-30
created: 2026-08-30
target_kind: action
target: the-sweep-reads-the-handshake-before-it-releases-a-decision
sources: ["archive/2026-08-30/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form/handoffs/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form.md"]
tags: [vault, process, harness]
---

# Context

**Two questions were being answered by one predicate**: whether the decision was answered, and
whether the work it caused was finished. A decision that produced a task stayed open until the task
was done, so the register of open decisions was really a register of unfinished work with no way to
tell the two apart.

# The question

**What counts as a decision being done?**

# How it works after

**Handing it to the target it names.** **owner:** «что считать выполненым descsion = передача его в
то место(и цепочку), которое он указывает(rule/proposal/action)». What happens to the work afterwards
is **not the decision's responsibility** — that is the decision-and-task split, and this is where it
is cut.

**The old criterion read the wrong field.** A decision left `wiki/decisions/` when a live page named
it in `decided_by:`, which records **causation** and was being read as **carriage**. It has already
taken a page out of view whose claim nothing live carried
([[the-sweep-reads-the-handshake-before-it-releases-a-decision]]).

**And the session never reports whether the work is done.** That is read off the tree, because a
session reporting "done" is a self-report — the same class that already produces false green smoke
rows here ([[the-smoke-gate-hooks]]). The feedback line carries the **target**; the tree carries the
answer.

# Recommendation

**Cut the criterion at the handover**, against a predicate that waits for the work. The register is
then answerable while the work queue stays visible as pages that have not yet been named back.

# Ratification

**The owner said it**, on 2026-08-30, in his own words, quoted above. It is the same split he had
stated earlier the same day between a decision and a task.

*(Compiled from `raw/handoffs/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form.md`.)*
