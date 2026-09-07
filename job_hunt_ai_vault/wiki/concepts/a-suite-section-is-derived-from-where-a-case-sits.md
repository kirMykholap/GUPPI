---
title: "A suite section is derived from where a case sits, and no list of it is maintained anywhere"
type: concept
status: current
authority: selftest-section-derivation
basis: code
sprint: S3
created: 2026-08-29
sources: ["archive/2026-08-29/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md", "scripts/vault-check-selftest.sh"]
tags: [testing, harness, vault]
---

# The mechanism

**`--only` matches a case name *or* the section the case is written under**, and `--list` prints both.

**A case's section is the last section declared above it**, set as that line prints its own record. So
the grouping falls out of where the case sits in the file, and **no list of sections is maintained
anywhere**.

**Move a case and its section changes with it.** Rename a section and every case under it is renamed
at once. There is nothing to keep in step, because there is only one statement of the fact.

# Why the derived form was chosen over a maintained one

**The owner asked whether a `wiki/rules/` page should hold the suite's case list**, and the session
recommended against it on the ground that `--list` computes the list from the script's own text at every
run — so a page would be a third copy of one thing. **He accepted the recommendation against his own
proposal** ([[no-rules-page-holds-the-suites-case-list]]).

**Section matching is what makes the derived form usable.** A `--only` that can select only a case name
forces a caller to know 181 names; one that selects a section lets the file's own structure be the
index ([[the-case-list-is-swept-from-the-file-because-some-cases-have-no-dispatcher]]).

# What the derivation does not protect against

**A sweep counts whatever matches its literal, including its own explanation.** `--list` finds an
inline case by the literal `report "..."`, and the comment above the sweep quotes exactly that — so a
case named `...` was listed every time
([[a-comment-quoting-the-literal-a-sweep-looks-for-is-counted-by-that-sweep]]).

**Deriving a fact from the text does not make the derivation right; it makes it single.** The
instrument that catches a wrong derivation is a case pinning the printed list against a real run, and
that case did not exist until 2026-08-29 ([[vault-scripts]]).

*(Compiled from `raw/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md`.)*
