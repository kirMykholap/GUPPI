---
title: "A reference-graph sweep naming every live-to-archive citation edge"
type: proposal
status: refused
basis: inference
sprint: S3
created: 2026-08-26
decided_by: [[the-live-to-archive-citation-advisory-is-refused-in-full]]
authority: reference-graph-sweep
sources: ["archive/2026-08-26/2026-08-26-the-harness-half-is-built-and-the-owner-rules-how-the-vault-empties-itself/handoffs/2026-08-26-the-harness-half-is-built-and-the-owner-rules-how-the-vault-empties-itself.md", "scripts/vault-check.sh"]
tags: [vault, harness, retrieval]
---

# What it would have been

**An advisory under `bash scripts/vault-check.sh --lint`, one line per citation edge running from a
live `wiki/` page into `archive/`.** The collector proposed it against the family headed by
[[a-live-page-can-argue-from-a-deprecated-one]]: a link into `archive/` resolves perfectly, so
nothing today distinguishes *citing history* from *arguing from a page that was replaced*.

**A narrower variant was offered by the session** — fire only where the cited page is superseded and
the citing page does not name the successor. That is the form that carries information rather than
volume.

# Refused in full — 2026-08-26

**The owner refused the class, not a size of it.** Both forms are refused, and the ruling carries
his words ([[the-live-to-archive-citation-advisory-is-refused-in-full]]).

# What the measurement said, and it is the reason the refusal is easy to defend

**313 edges from 199 of 653 live pages, naming 38 of the 50 archived slugs, gate green on every
one.** Measured by the collector at `9950dbd`.

**All 313 point at a page carrying `status: deprecated`**, so the narrow variant and the wide one
select the same set today. **The distinction has zero cases** and would acquire any only once the
lessons sweep begins moving pages that were never superseded
([[the-lessons-cycle-is-the-owners-and-a-lesson-leaves-when-a-page-outside-lessons-cites-it]]).

# What is left unanswered, and it is filed rather than solved

**The hole the family names is real and stays open.** A page reasoning from a deprecated claim is
not detected by anything, and the ruling says that is acceptable — not that it does not happen
([[a-live-page-can-argue-from-a-deprecated-one]]).
