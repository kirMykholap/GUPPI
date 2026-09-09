---
title: "An `authority` register, on the model of the tag dictionary"
type: proposal
status: implemented
authority: authority-register-design
basis: inference
sprint: S1
created: 2026-08-17
sources: ["archive/2026-08-16/2026-08-16-the-harness-becomes-a-build/handoffs/2026-08-16-the-harness-becomes-a-build.md", "docs/superpowers/specs/2026-08-16-harness-and-schemas-design.md", "CLAUDE.md", "archive/2026-08-26/2026-08-26-the-carried-questions-are-answered-and-the-plan-is-corrected-before-it-is-built/handoffs/2026-08-26-the-carried-questions-are-answered-and-the-plan-is-corrected-before-it-is-built.md"]
decided_by: [[what-the-harness-build-waits-on]]
tags: [vault, retrieval]
---

# The field works as designed and behaves as it was built

`authority` is meant to be a **declaration of sole ownership of a question**, so that two pages
claiming one question are a contradiction found mechanically. In practice **133 unique slugs sit on
133 pages** — every page inventing its own, which makes the field a detector that fires only when
someone reuses a formulation, which is when they had already noticed the overlap.

**The cause is structural, not carelessness:** the librarian's own definition never mentions the
field, so the only party that fills it is nowhere instructed how to choose a value, and there is no
register to look in. The general form is [[a-field-with-no-register-produces-unique-values-by-default]].

## What it would be

**`tags.md` for questions.** The tag dictionary is the working model and it has three parts, all of
which this field lacks:

1. a list of what is already claimed, with a definition beside each;
2. an obligation to consult it before minting;
3. an obligation to record the rejected candidate as an alias
  ([[aliases-carry-the-question-across-languages]]).

**With a register the field becomes rare rather than universal**, and the check moves from after the
fact to the moment of writing — which is the difference between a rule that fails a build and one a
tired session will not re-read ([[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]]).

**`proposals` carry no `authority`, and that is correct rather than accidental.** Two competing
proposals about one problem are legitimate; flagging them as a contradiction would be wrong.

**That paragraph is struck — 2026-08-26.** The objection it states was put to the owner and
**refused**: `authority:` stays required in every folder but `wiki/rules/`, `proposals/` included.
The answer lives on [[authority-becomes-the-index-and-is-required-outside-rules]], in the section
dated that day — a folder that may omit the field is a folder the admission lookup skips silently,
and a proposal carrying a finished design is exactly what a candidate page needs to find before it
is written. The text above stays as the record of what was argued on 2026-08-17, on `basis:
inference`, and is no longer the live instruction.

## What is open

**Where it lives, who writes it, whether it is generated, and what the librarian owes before minting
a slug.** Agreed in principle and undesigned — a row of [[what-the-harness-build-waits-on]]. If it
is generated, it is `catalogue.md`'s shape; if it is written, it is `tags.md`'s, and the two answer
differently on who may add a line.

**One correction belongs with it.** The vault's `CLAUDE.md` documents the duplicate check as
`rg "^authority:" wiki -o | sort | uniq -d`, which never compares slugs
([[a-command-that-is-false-only-in-its-documentation-fails-nothing]]).

Retired with `superseded_by:` the day it is built or refused
([[proposals-are-a-folder-not-a-status]]).

**That sentence is struck — 2026-08-26, and it is false in both halves.** An implemented proposal
moves to `archive/` with `status: implemented` and carries **neither** `superseded_by:` nor a
successor claiming to replace it
([[an-implemented-proposal-moves-to-archive-and-the-successor-carries-its-claim]]); a refused one
takes `status: refused` and carries no `superseded_by:` either
([[a-refused-proposal-is-archived-and-takes-status-refused]]). The page it cites has already
declared that clause false in a dated section of its own
([[proposals-are-a-folder-not-a-status]]). Struck here rather than left to be read in `archive/`,
which no check, no injector and no `/pre-task` ever opens.

# Read as implemented by the owner — 2026-08-26

*(the owner selected it.)* **`status: implemented`.** `job_hunt_ai_vault/authority.md` exists, holds
666 slugs in 15 families, and `bash scripts/vault-authority.sh --check` compares it against the tree
in both directions. The register this page designed is the register that is running.

**The mark opens a state rather than closing one.** The page stays in `wiki/` while it is tested for
having a live page that names it, and it moves only once it passes — with no `superseded_by:` and no
successor claiming to replace it
([[an-implemented-proposal-moves-to-archive-and-the-successor-carries-its-claim]],
[[implemented-joins-the-legal-status-values-and-the-status-block-enters-every-schema]]).

**The live pages that carry its claim** are
[[authority-becomes-the-index-and-is-required-outside-rules]], which made the field the index, and
[[authority-md-is-a-register-the-one-writer-clause-names]], which names its writer.

**Corrected 2026-08-26: the second name was wrong.**
[[authority-md-is-a-register-the-one-writer-clause-names]] does not name this page, its slug or its
claim anywhere — it rules who may write `authority.md`, which is a different question. What actually
named this page in `wiki/` on the day it was archived:
[[authority-becomes-the-index-and-is-required-outside-rules]],
[[a-field-with-no-register-produces-unique-values-by-default]], [[what-the-harness-build-waits-on]],
[[the-librarian-is-blind-to-a-recurring-family-from-where-it-stands]] and
[[the-session-hand-edited-the-vault-schema-and-the-clause-naming-its-writer-is-still-owed]]. That
set is what `scripts/vault-archive.sh` tested before it released the page, and it is how the page is
reached from `wiki/` now.

**The move itself is an S3 line** ([[the-plans-remaining-phase-moves-to-s3-and-the-ritual-runs-whole]]).

*(Compiled from `raw/handoffs/2026-08-26-the-carried-questions-are-answered-and-the-plan-is-corrected-before-it-is-built.md`.)*
