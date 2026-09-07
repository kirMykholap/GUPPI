---
title: "Sources summarised together lose the disagreement between them, and the disagreement was the evidence"
type: lesson
status: archived
authority: merged-source-summaries
basis: inference
sprint: S1
created: 2026-08-15
sources: ["raw/notes/2026-08-13-owners-note-second-brain-info.md", "raw/notes/2026-08-13-owners-note-second-brain-instructions.md", "scripts/vault-coverage.sh"]
tags: [vault, process]
---

# One list, two authors' worth of intent, and no way to tell which said what

On 2026-08-13 both of the owner's notes were read together and summarised in one bullet list on
[[the-handoff-splits-into-a-handoff-and-a-knowledge-base]]: *«three layers … `wiki/` as compiled
atomic notes (`entities/`, `concepts/`, `decisions/`, plus a `tasks/`) … kebab-case filenames»*.

Every clause of that is true of *the pair*. **No single note says any of it.** `concepts/` is in
one note only, `tasks/` in the other only, and "kebab-case filenames" flattens a real conflict:
one note asks for `[category]-[short-description].md`, the other gives `auth-module-redesign.md`
as its example, which carries no category prefix
([[the-owners-method-note-and-what-was-built-from-it]] tabulates all five).

*(The title read "Two sources summarised together lose the disagreement between them, and the
disagreement was the evidence" until 2026-08-18, and the paragraph above names the sources it was
counting: the owner's info note, and his instructions note. **Two was the scenario, not a count of
anything that exists** — the failure needs more than one source, and nothing about it stops at two.
That reasoning stood in a `quantity:` line until the field was rejected and the rule made
unconditional over titles and filenames alike
([[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]]), so an argument that a number
is not a count is no longer a way to keep one in a title. The title now names the condition —
sources summarised together — instead of counting the sources
([[a-title-names-what-is-counted-instead-of-counting-it]]), and that is a correction in place
rather than a supersession ([[a-title-corrected-in-place-is-not-a-supersession]]). The **filename**
still counts and waits for its rename, which moves an address
([[the-title-rule-extends-to-filenames]], [[a-page-rename-is-sed-and-verify]]).
**Closed 2026-08-19: the rename landed and the name counts nothing.** The sentence above was
written on 2026-08-18 and stood for one day; the wait is the record rather than an oversight,
because a filename is an address and the repair was scheduled as one sweep of sixteen names in a
single change, not taken by whichever session happened to open this page next.)*

## What it cost, with the date on it

**2026-08-14.** The instructions note was compiled line by line and the filename row was recorded
as *«diverged, and by nobody's recorded decision»* — a standing divergence between what the owner
asked for and what exists. It was carried as that for a day.

**The counter-evidence had been in `sources:` since 2026-08-13.** The other note, by the same
author on the same day, gives a prefix-free filename as its own example — so the build was not
diverging from the owner at all, it was following one of his two notes. A divergence that needed
an owner's decision was, on the evidence already in the vault, a choice between two things he had
written. The decision was still worth taking ([[filenames-carry-no-category-prefix]]), but it was
taken a day later than the evidence allowed, and against a worse description of the position.

## Why the toolchain could not see it

- **`vault-coverage.sh` accounts per source.** Each note is counted on its own, and a claim in one
  that contradicts a claim in the other is two units with two verdicts and no relation between
  them. Nothing in the sidecar format can express *«and the other source says the opposite»*.
- **`sources:` is a set, not an argument.** Rule 11 checks that each path resolves. Two paths in
  one `sources:` line read as corroboration by default, and a page summarising them speaks in one
  voice because prose has no other option ([[vault-scripts]]).
- **A summary is the natural shape and it is the lossy one.** This is the same failure as
  [[an-intent-note-compiled-as-testimony-describes-things-nobody-built]] one level up: there, the
  grammar of intent and of testimony is identical; here, the grammar of one source and of two is.

## The discipline

**Where a page cites more than one source for the same claim, name which source says what** — the
sentence costs six words and it is the only place the disagreement can survive. And **when a
divergence is recorded against "what the owner asked for", read every source that carries his
words before writing that phrase**: "the owner asked for X and we built Y" is a strong claim, and
it is false if his other note asked for Y.

The general form: a page that merges sources is asserting they agree. Assert it deliberately, or
do not merge them.
