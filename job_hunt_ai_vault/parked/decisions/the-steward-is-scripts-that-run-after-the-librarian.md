---
title: "The steward is a script that runs after the librarian, not another unattended writer"
type: decision
status: current
authority: harness-writer
binding: prohibition
basis: human
sprint: S1
decided: 2026-08-16
created: 2026-08-17
sources: ["archive/2026-08-16/2026-08-16-the-harness-becomes-a-build/handoffs/2026-08-16-the-harness-becomes-a-build.md", "docs/superpowers/specs/2026-08-16-harness-and-schemas-design.md"]
tags: [harness, agents, vault]
---

# Decided 2026-08-16: one writer, and the second half is a script

**The librarian keeps its monopoly on `wiki/`** and writes both halves of a harness change: the
decision page and the rule page. **The steward — whatever renders the rules into the harness files
— is scripts that run after it**, not an agent working beside it.

*(The title read "The steward is a script that runs after the librarian, not a second unattended
writer" until 2026-08-18. **The "second" meant "another" and was never a count** — a third
unattended writer would not make the sentence stale, it would be refused by it. It came out anyway,
and that is the point of the ruling: **there is no longer any way for a page to declare itself
exempt**, so a number that is genuinely not a count still leaves the title
([[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]]). This page never carried a
`quantity:` line, so the repair is the retitle alone; **the owner ruled ordinals into rule 10's word
list on 2026-08-18** and the recorded order is corpus-before-check, so this lands ahead of the
predicate rather than reddening under it. The word the title wanted was "another"
([[a-title-names-what-is-counted-instead-of-counting-it]]). The heading above still reads "the
second half", and is left as it is: rule 10 reads the title and the filename, and the owner has not
extended it to body headings. Not a supersession
([[a-title-corrected-in-place-is-not-a-supersession]]).)*

## Rejected: a parallel steward agent

**Two unattended writers already lost a write here on 2026-08-14**, and the loss left no trace in
`git diff` — the file was written, just not with both writers' work in it
([[parallel-librarians-break-the-one-writer-property]]). A lost update is invisible by
construction, so the failure cannot be found by review.

**Sequencing costs nothing, because the steward's half is a script.** The argument for parallelism
is wall-clock, and there is no wall-clock to save: a script runs in the same seconds whether it is
started before or after the agent finishes.

## What it obliges

- The write ritual gains a step and stays ordered. With `updated` stamped by a script it becomes
  **stamp → catalogue → check**, because stamping modifies files and rule 9 would otherwise fail on
  the catalogue the stamp just invalidated
  ([[a-staleness-detector-from-updated-against-a-pages-sources]], [[vault-scripts]]).
- **Naming the steward is open and trivial** — a row on [[what-the-harness-build-waits-on]].
- The monopoly it preserves is the one that makes unattended writing reviewable at all
  ([[the-librarian-writes-unattended]], [[one-librarian-behind-every-caller]]).
