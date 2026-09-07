---
title: "A decision with a rule target cannot close inside a single ingest, and the mechanisms deciding it are named"
type: concept
status: current
authority: rule-landing-two-parties
basis: code
sprint: S3
created: 2026-08-30
sources: ["archive/2026-08-30/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form/handoffs/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form.md", "scripts/vault-check.sh", "scripts/vault-archive.sh", ".claude/hooks/lock-the-librarian.ps1"]
tags: [vault, harness, process]
---

# The shape

**Landing a rule takes two parties and at least two rituals.** The page under `wiki/rules/` is the
librarian's write; the paired `<!-- rule: slug -->` markers in the governed file are the session's
([[a-region-is-a-paired-comment-named-for-a-rule]]). A plan that treats the landing as one act is
wrong about the machinery, and the plan of 2026-08-30 was.

**Three mechanisms decide it together, and no page stated them together before this one.**

1. **`lock-the-librarian.ps1` runs the whole gate before dispatching and denies on red.** The
   librarian is reachable only from a green tree
   ([[a-lock-on-a-red-tree-hides-the-health-of-what-it-guards]]).
2. **A region naming a rule page that does not exist is red.** Rule 12 of `scripts/vault-check.sh`
   reads both ends, so the markers cannot precede the page.
3. **A `deprecated` page left in `wiki/` is red, and only the archiver may release it** — and
   `scripts/vault-archive.sh` takes the **session folder** as an argument it never derives
   ([[the-archive-gains-a-folder-per-session-inside-the-date]]). That folder is named by the journal's
   own filename, which does not exist until `/handoff` has run.

# What follows from them, in order

**The page must be written before the markers.** (2) forbids the other order.

**The markers must be placed after the librarian returns.** (1) forbids placing them first, because
the region would be red and the librarian could not then be dispatched to write the page that clears
it.

**And a rule that supersedes another cannot land before the journal exists at all.** (3) puts the
retirement of the old page inside a ritual that has a session folder to hand, which is `/ingest`.

**So the earliest a `target_kind: rule` decision can be discharged is the ingest of the session after
the one that ratified it**, and the region stays red between the librarian's return and the session's
one edit. A red gate at that exact point is the correct state and not a failure — but only for the
region the rule names, and only until the session closes it.

# Why this is written as a mechanism and not as a lesson

**Nothing here went wrong.** Each of the three is doing what it was built for, and each was decided
separately with its own ground. What was missing is that no page put them side by side, so a plan
could be written that assumed a single act and pass every review — which is what happened on
2026-08-30 and was caught only when the landing was attempted.

**The consequence for a dispatch is concrete**: a dispatch ordering a render **names who marks the
region**. On 2026-08-29 a librarian placed markers in three harness files itself, the third
consecutive occurrence, and reported crossing the line rather than being caught at it.

*(Compiled from `raw/handoffs/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form.md`.)*
