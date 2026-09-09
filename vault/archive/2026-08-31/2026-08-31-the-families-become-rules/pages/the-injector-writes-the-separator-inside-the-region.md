---
title: "The injector writes the paragraph separator, and it goes inside the region"
type: decision
status: archived
authority: region-separator
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-18
created: 2026-08-18
sources: ["archive/2026-08-18/2026-08-18-the-marker-carries-its-type-and-the-gate-was-blind/handoffs/2026-08-18-the-marker-carries-its-type-and-the-gate-was-blind.md", "scripts/vault-inject.sh"]
tags: [harness, vault, testing]
---

# Decided by the owner on 2026-08-18: inside, and written by the injector

**A rendered region carries one blank line after its slice**, emitted by the writer, at `b311f0f`.
Without it two adjacent regions run together into one paragraph at the destination.

**Rejected: a trailing blank line on each rule page.** *Trailing whitespace is content* is already a
measured fragility here — the language rule's hard breaks are two trailing spaces that an editor
trimming on save would turn red — so a page whose last byte matters would redden rule 12 on a change
nobody typed ([[english-in-the-repository-russian-with-the-owner]]).

**Four more were priced and refused**, each on what it actually does at the destination:

| Alternative | Why not |
|---|---|
| an HTML comment | stripped along with the markers, so it does nothing |
| a line of spaces | that same trailing whitespace, one indirection away |
| a `---` | renders as a horizontal rule, and reads as frontmatter at the top of a block |
| a zero-width character | invisible junk in a file people edit by hand |

**Only a blank line is a paragraph break in markdown**, which is why the list closes there.

## Why it has to be inside the region rather than between them

**The blank line between two adjacent regions is stripped along with the markers** before the file
reaches the model — observed in this session's own injected copy
([[block-comments-are-stripped-before-claude-md-reaches-the-model]]). Outside the close marker the
separator is skeleton and disappears; inside it, it is content and survives. That measurement is
what decided the placement, not a preference about tidiness.

## It is idempotent by construction

The writer drops the old region body **wholesale** and rewrites it, so one blank line is written
however many times the injector runs. Emitting it after the close marker would accumulate one blank
line per run — a defect that grows silently and looks like an editor's doing.

**The rendered form is one variable read by both the writer and the comparison**, which is what
keeps the two from disagreeing ([[the-rendered-form-is-defined-once-and-read-by-the-writer-and-the-comparison]]).

## What is deferred: the outcome is unverified

**Whether the paragraph break actually reaches the model cannot be read from the session that makes
it** — that context was built before the edit. **owner: check it next session.**

- **Consequence of not doing it:** a mechanism believed to work with no evidence, on the one thing
  the change was for.
- **What closes it:** compare the injected `CLAUDE.md` against the file on disk. One minute.
- **If the break is still missing**, the stripping eats an in-region blank line too, and only a
  visible character remains — with every drawback in the table above already priced.

## The alarm is answered; the mechanism behind it still cannot be told apart — 2026-08-18

**Asked as posed, the answer is that no paragraph break is missing** in the rendered `CLAUDE.md`:
the eleven regions read as eleven paragraphs, the eleventh being the definition that landed this
session ([[a-retrospective-is-a-sessions-end-not-a-sprints-ritual]]).

**But separator-versus-collapse cannot be decided from this file.** Every region in it also carries
a blank line *outside* the region, so a mechanism that eats the in-region separator and one that
preserves it produce the same file. **Deciding it needs a region with text flush against it, and
none exists** — which is a fact about the corpus rather than about the injector, and it is why the
question is recorded as open instead of closed by an observation that could not have failed
([[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]],
[[the-evidence-was-not-wrong-the-instrument-was-too-coarse]]).
