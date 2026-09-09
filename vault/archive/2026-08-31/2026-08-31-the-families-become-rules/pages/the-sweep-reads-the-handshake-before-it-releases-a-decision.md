---
title: "The sweep reads the handshake before it releases a decision, and carriage stops being read off `decided_by:`"
type: decision
status: archived
authority: decision-release-criterion
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-30
created: 2026-08-30
target_kind: action
target: the-sweep-reads-the-handshake-before-it-releases-a-decision
supersedes: [[a-decision-is-processed-when-a-live-page-names-it-in-decided-by]]
sources: ["archive/2026-08-30/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form/handoffs/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form.md", "scripts/vault-archive.sh"]
tags: [vault, harness, process]
---

# Context

**The sweep releases a decision from `wiki/decisions/` when some live page cites it.** That reads
`decided_by:`, which records **causation**, as **carriage** — and the two are not the same thing.

**It has already taken a page out of view whose claim nothing live carried.**
`the-lessons-collector-is-a-reading-dispatch` left `wiki/` because four live proposals named it, and
every one of them was a draft it had **produced** rather than a page **describing** it.

# The question

**What criterion releases a decision, now that a decision declares its own target?**

# How it works after

**The release criterion for `wiki/decisions/` narrows to the handshake**
([[a-decision-declares-its-target-and-the-handshake-closes-it]]): a decision carrying `target:` must
have been **named back** by that target in `decided_by:`, not merely cited by some live page that
happens to mention it.

**A target that does not exist is not a failure** — it is what *open* means, and it is the state the
whole list of unbuilt decisions is read from.

**Built only in part on 2026-08-30.** Rule 17 of `scripts/vault-check.sh` performs the handshake as a
gate verdict; `scripts/vault-archive.sh` does **not** yet read it before releasing. This decision is
the unbuilt half.

# Recommendation

**Narrow the criterion rather than add a second one beside it**, because a page that leaves on either
of two tests leaves on the weaker of them.

# Ratification

**The owner selected it** by approving the plan of 2026-08-30.

**Not built.**

*(Compiled from `raw/handoffs/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form.md`.)*
