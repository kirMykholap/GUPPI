---
title: "A field with no register produces unique values by default"
type: lesson
status: archived
authority: register-absence
basis: measurement
sprint: S1
created: 2026-08-17
sources: ["archive/2026-08-16/2026-08-16-the-harness-becomes-a-build/handoffs/2026-08-16-the-harness-becomes-a-build.md", "docs/superpowers/specs/2026-08-16-harness-and-schemas-design.md", "CLAUDE.md"]
tags: [vault, retrieval]
---

# The measurement, and why it is a prediction rather than a surprise

**133 unique slugs on 133 pages.** `authority` was designed as a **uniqueness declaration** — the
question a page is the sole answer to, so that two pages claiming one question are a contradiction
found mechanically. It behaves instead as a **per-page invention**.

**That is the predicted result of having nothing to consult.** The mechanism was copied from tags
without the machinery that makes tags work: a dictionary, an obligation to consult it before
minting, and an obligation to record the rejected word ([[aliases-carry-the-question-across-languages]]).
Copy the field and leave the machinery behind, and every writer, facing a blank, writes something
new — not out of carelessness but because there is no other available move.

## What the field became instead of what it was for

| designed as | behaves as |
|---|---|
| a **preventer** of duplicate ownership, consulted before writing | a **detector** that fires only when two writers happen to choose the same formulation |

And a detector with that trigger fires **exactly when the overlap had already been noticed** —
because reusing a slug means having found the page that owns it. It cannot catch the case it was
built for: two pages answering one question in two different words.

## The transferable rule

**Any future field claiming uniqueness needs its register in the same breath.** Not afterwards: the
corpus fills up with inventions between the two, and the register then has to be reconciled against
133 existing values rather than grown from zero.

The register itself is designed and not built:
[[an-authority-register-on-the-model-of-the-tag-dictionary]]. The same session found the sibling
failure — the documented command that would have detected duplicates does not
([[a-command-that-is-false-only-in-its-documentation-fails-nothing]]) — so the field had **neither**
a register nor a working manual check, and the only reason contradictions have been caught here at
all is that rule 3 of `vault-check.sh` implements it correctly ([[vault-scripts]]).
