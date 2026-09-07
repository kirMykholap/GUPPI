---
title: "A claim labelled measured came from an instrument reporting its own exit code, and the last occurrence was while correcting the one before it"
type: lesson
status: archived
authority: instrument-reports-itself
basis: measurement
sprint: S2
created: 2026-08-19
sources: ["archive/2026-08-19/2026-08-19-the-gate-checked-itself-against-a-decoy-and-the-guard-objection-fell/handoffs/2026-08-19-the-gate-checked-itself-against-a-decoy-and-the-guard-objection-fell.md", "scripts/vault-check-selftest.sh"]
tags: [testing, process, harness]
---

# The incident

The session filed a `measure:` line saying the selftest *"exited 0 throughout, at 24/96 as at 119/1"*
and **drew a decision out of it** — that the exit code does not read the score.

**Both halves are false.** The script's last line is `[ "$fail" -eq 0 ]`, so its exit code has always
been its score; measured with one case planted broken it returns **1**.

**The instrument was a pipeline, every time**
([[an-exit-code-read-through-a-pipe-belongs-to-the-last-stage]]). And **the correcting run repeated
it**: the compound command that produced the correction ended in a `grep -c` over zero matches, so the
harness reported the measuring task as *failed with exit code 1* while the number it produced was
correct.

# What makes three in one hour worth a page rather than a retraction

**The third occurrence happened while correcting the second.** That is not carelessness compounding —
it is the same reading habit being applied to the fix, which is what a habit does. Nothing in the
session's attention was available to catch it, because the attention was on the claim rather than on how
the claim was read off.

**The store already holds this shape twice**, both times about an instrument answering a
well-formed question that was not the one asked
([[grep-with-an-escaped-cr-returns-a-line-count-and-not-a-cr-count]],
[[a-runbook-that-carries-the-nonce-cannot-be-read-by-what-it-measures]]). What is new here is that the
instrument was **the shell**, which nobody thinks of as an instrument at all.

# The correction was written in place, and that is deliberate

The `measure:` line was **corrected where it stood rather than left with a retraction beside it**,
because `/ingest` files those lines into `log.md` and **a false measurement filed as history is worse
than one never written**: the log is the only test data this system has
([[the-librarian-writes-unattended]]).

**The defence is one line and it is mechanical** — capture the status into a variable on the very next
statement — which is what makes this a habit to change rather than a thing to be careful about
([[knowing-a-rule-is-not-a-mechanism]]).
