---
title: "DIVERGENCE: a bulk renormalisation swept a file the owner had ruled untouched that morning"
type: decision
status: archived
authority: bulk-operation-ruling-check
basis: human
binding: divergence
sprint: S3
decided: 2026-08-26
created: 2026-08-26
sources: ["archive/2026-08-26/2026-08-26-the-checks-get-an-entry-point-and-the-handoff-gets-a-gate/handoffs/2026-08-26-the-checks-get-an-entry-point-and-the-handoff-gets-a-gate.md"]
tags: [process, harness, vault]
---

# The rule, and what was done against it

**The rule: an archived page is not edited**, and the owner had ruled that morning that the archived
journal of 2026-08-17 specifically stays as it is
([[the-vault-crlf-files-are-renormalised-and-no-rule-is-written-for-them]],
[[what-an-archived-page-asserts-is-frozen-and-how-it-is-found-is-live]]).

**What was done:** that file sat in a list of 115 CRLF working copies and went through a bulk `rm`
plus `git checkout` **without the list being checked against the ruling**. Its 337 CR bytes are gone
from the working copy.

# Why it looked unnecessary at the time

**The operation was framed as restoring the working copy to what the index already held** — which is
true, and is exactly why nobody read the members. A restore is not an edit, so the question "does
this touch anything I was told not to touch" never got asked about the list.

**No commit resulted and `git diff` reports the content identical to the blob**, so the repository is
unchanged. **The instruction was still direct and the check before the bulk operation was still not
made.**

# The rejected alternative

**Check the list against the day's rulings before running a bulk operation over it.** It is one pass
over 115 names against a conversation that had happened hours earlier.

# What this costs, stated rather than softened

**A bulk operation dissolves the moment at which a rule would have been consulted.** Each of the 115
files individually would have been a decision; as a list they were a single action with one
justification, and the justification was true of the list as a whole and false of one member.

**This is the same shape as the sweep that could not tell an address from a quotation**, where the
remedy was to narrow what the sweep touched rather than to trust the operator
([[the-prose-path-detector-is-refused-on-its-own-measurement]]).

# What the owner did about the ruling itself

**He corrected it by a dated note rather than by restoring CRLF or by narrowing its wording**, and its
substance stands: an archived page is not edited. What was false is the part treating line endings as
something the ruling preserved — the blob was 0 CR at HEAD and at its own commit
([[the-vault-crlf-files-are-renormalised-and-no-rule-is-written-for-them]]).

**That correction does not discharge this divergence.** The ruling being unimplementable as stated is
a separate fact from the instruction being disobeyed without anybody noticing.
