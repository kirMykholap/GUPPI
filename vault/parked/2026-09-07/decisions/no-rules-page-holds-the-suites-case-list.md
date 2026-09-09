---
title: "No `wiki/rules/` page holds the suite's case list, because `--list` computes it at every run"
type: decision
status: current
authority: case-list-page-refusal
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-29
created: 2026-08-29
sources: ["archive/2026-08-29/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md", "scripts/vault-check-selftest.sh"]
tags: [vault, testing, harness]
---

# The ruling, 2026-08-29

**The owner proposed a `wiki/rules/` page holding the suite's case list. The session recommended
against it. He accepted the recommendation against his own proposal.**

**The ground: `--list` computes the list from the script's own text at every run**, so a page would be
a **third** copy of one thing — the cases, the printed list, and the page.

**Rejected: the page.** What was proposed instead and built is matching on the suite's own section
names, which are derived from where each case sits
([[a-suite-section-is-derived-from-where-a-case-sits]]).

# Why this is not the general rule about registers

**A printed list beats a maintained one only where something prints it.** This store keeps
`tags.md` and `authority.md` by hand for the opposite reason: **which slugs exist is in the tree and
needs no file, but which slugs answer the same question is nowhere and cannot be derived**
([[authority-becomes-the-index-and-is-required-outside-rules]]).

**So the test is whether the fact is already stated somewhere a machine can read.** The case list is;
a family of authority slugs is not.

# What nothing in the vault rules

**Whether a maintained case list would be *legal* beside the derived one is unruled.** The
printed-versus-maintained ruling this rests on is about which is better, not about which is permitted,
and no page draws that line ([[a-copied-list-drifts-and-a-sweep-cannot]]).

**It did not need deciding today** and is recorded so that the next person who wants such a page finds
the question rather than the argument.

*(Compiled from `raw/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md`.)*
