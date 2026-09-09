---
title: "A gate that claimed byte equality did not have it: `$( )` strips the trailing newline before either side is read"
type: concept
status: current
authority: injector-comparison-blindness
basis: code
sprint: S2
created: 2026-08-18
sources: ["archive/2026-08-18/2026-08-18-the-marker-carries-its-type-and-the-gate-was-blind/handoffs/2026-08-18-the-marker-carries-its-type-and-the-gate-was-blind.md", "scripts/vault-inject.sh"]
tags: [harness, testing, vault]
---

# The defect, and how long it was live

**Both sides of the injector's comparison arrived through `$( )`**, which strips *every* trailing
newline from a command substitution. So the shell deleted the difference before either side was
read, and a region carrying one blank line the slice does not carry got
`vault-inject: every rule agrees with the region it governs`, exit 0, and `0 region(s) rewritten` in
write mode.

**It was live from the day the mechanism was built** and fixed at `97895a9`. `scripts/vault-inject.sh`
says *"Byte equality, not a normalised or hashed comparison"* directly above it, and that sentence is
what a reader trusts.

## The fix is a sentinel inside the same substitution

`$(slice_of …; printf 'X')` then `${s%X}`. The sentinel is emitted **inside** the substitution, so
whatever the shell would have stripped is now interior bytes; stripping the sentinel afterwards is a
parameter expansion, which removes exactly one known character and nothing else.

**A second implementation was not an option.** Rule 12 asks its question by *running the writer* and
reading its lines ([[a-check-asks-by-running-the-writer-it-checks]]), so this is the one comparison
in the project that moves — and it must not grow a copy, or the two would have to be kept equal by
somebody remembering.

## The live consequence, independent of any planned change

**A blank line hand-added inside any of the ten regions passed the gate**, which is the one thing a
rendered region is supposed to make impossible. A hand-edit inside a marked region is already
forbidden by nothing ([[hand-edits-of-the-wiki-are-a-recorded-divergence]]); this measured that the
gate did not catch one form of it either.

## Narrower and worse than the caveat already on the record

[[a-gate-guarantees-agreement-never-truth]] says a gate promises the region matches the page and
never that the page is right. **This is the level below that**: the gate did not deliver the
agreement it claimed either. A caveat about what a mechanism cannot promise does not cover a
mechanism failing at what it does promise, and the two are worth keeping apart.

**It was found at `/pre-task` and reproduced end to end against the real script**, not inferred from
reading it ([[a-pre-task-paid-for-itself-in-findings-nobody-would-have-made]],
[[hand-probe-a-new-mechanism-before-running-the-suite]]).
