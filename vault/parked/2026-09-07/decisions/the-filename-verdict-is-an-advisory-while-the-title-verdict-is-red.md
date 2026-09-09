---
title: "The filename half of the rule prints an advisory while the title half stays red"
type: decision
status: current
authority: filename-verdict-severity
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-18
created: 2026-08-18
sources: ["archive/2026-08-18/2026-08-18-the-filename-half-lands-and-the-escape-hatch-falls/handoffs/2026-08-18-the-filename-half-lands-and-the-escape-hatch-falls.md", "scripts/vault-check.sh", "scripts/vault-check-selftest.sh"]
tags: [harness, vault, testing]
---

# Decided by the owner on 2026-08-18: the two halves are not the same severity

**A title that counts fails the run. A filename that counts prints and the run stays green.** Rule
10 reads the same predicate over both strings ([[the-title-rule-extends-to-filenames]]); what
differs is what the check does with the answer. Built at `2772439`, with the advisory's format
corrected at `c521a10`.

**Rejected: red, and it was priced out loud.** `vault-check.sh` would exit 1 on every run until the
renames landed, and a gate that is always red is not a gate — the reader learns to run it and ignore
it, which is the same argument this store has already made about advisories that stand for ever
([[the-dense-tags-are-not-split-and-the-standing-advisories-are-named-here]]).

**Rejected: renaming the six on the spot.** That widens the small half of the work into the large
one. Repairing a title costs an edit; repairing a filename moves an address, and an address is what
every `[[wikilink]]` resolves to ([[a-rewriter-must-be-paired-with-a-detector]]).

**What the owner asked of it, a printed line delivers in full:** *"a twelfth name is never minted
silently."* A page written today with a counting name is renamed in the minute it is written, before
anything cites it, and the advisory is what tells its author to do that. The standing offenders are
a scheduled sweep, not something a session repairs because a check went red
([[a-page-rename-is-sed-and-verify]]).

## The mechanism underneath, read in the file rather than taken on trust

**`note()` sets `fail=1` and the script ends `exit "$fail"`; an advisory is a bare `echo`.** That is
the whole of the red-versus-advisory choice in `scripts/vault-check.sh` — there is no severity
field and no third state. A verdict is red because it calls `note`, and for no other reason.

**Six standing offenders print today**, each of them a page whose *title* had already been repaired:
the corpus accumulated slugs like `two-staleness-checks-at-two-times` under corrected titles,
because a title is corrected in place and the address underneath it is left alone
([[a-title-corrected-in-place-is-not-a-supersession]]).

## The divergence recorded against it

**The filename half was built leaning on `quantity:`**, with `OWED TO THE OWNER` written beside the
lean in the script and the lean taken anyway: one declaration line silences both strings, and two of
the six standing offenders carry no number in their title at all, so answering rather than waiting
was illegal for them until the store's schema gained a sentence.

**That the field had no authority at all was not knowable until the retrospective**
([[a-field-admitted-around-the-admission-procedure-outlives-the-rule-it-softens]]), and the field
was rejected outright hours later
([[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]]). The lean is on the record
anyway, and it is the reason the check must not be tightened before the corpus is clean: the same
line that was leaned on is what keeps twenty-four pages green today.

## Corrected 2026-08-19: the example above was rewritten by the sweep it describes, and is restored

**The code span in "the corpus accumulated slugs like `…`" is back to the name it was written
about.** The rename sweep of 2026-08-19 ran `sed` over every reference to sixteen old slugs, and
`sed` cannot tell an address from a quotation: it rewrote this span too, leaving the sentence
offering, as its example of a slug that counts, a name that counts nothing — the opposite of what
the sentence was written to say. The span holds `two-staleness-checks-at-two-times` again, which is
what that page was called until `7abd317`.

**Restoring it breaks nothing, and the reason is worth keeping.** The property the sweep was
measured against is that no old slug survives **as an address**; a bare slug inside a code span is
not one. Rules 4 and 5 of `vault-check.sh` read `[[wikilinks]]`, and rule 10 reads `title:` and the
filename — none of the three can see this string. It is a quotation of a historical name, it is
correct as history, and it stands ([[a-page-rename-is-sed-and-verify]]).

**This is one of two places the same sweep over-reached**; the other is on
[[the-dense-tags-are-not-split-and-the-standing-advisories-are-named-here]], where the repair was
the opposite one — the sentence there names the compliant name the page carries today and is closed
as a correction rather than restored. Both are in `log.md`, and the general shape is now written
into rule 10's own comment: a rewriter over addresses will always reach into quotation, so a rename
ends in a read of its own diff and not in a clean exit code.

## And "six standing offenders" is false, measured 2026-08-19

**The number was never six for long and it is zero now.** Six was what the advisory *printed* on
2026-08-18, over a corpus where a `quantity:` line silenced the rest; with the field withdrawn and
the corpus cleared, the advisory named **thirteen** filenames at `1520164`, **sixteen** were
renamed, and the line has printed nothing since. The reading is the command rather than a figure
here: `bash scripts/vault-check.sh | grep 'filename(s) count'` is empty, and
`bash scripts/vault-check.sh | grep -c 'advisory:'` returns 19 with the run exiting 0.

**Three of the sixteen were invisible to the check that named them**, because rule 10's word list
held no ordinals — they were built on *second*, *fourth* and *fifth*. That gap is what the owner
ruled on, and the ruling has a page of its own
([[ordinals-count-and-first-does-not]]).

**And the divergence recorded above is discharged.** *"The same line that was leaned on is what
keeps twenty-four pages green today"* was true when it was written and describes nothing now: the
field stands on no page — `grep -rc '^quantity:' wiki archive` sums to 0 — and the check no longer
reads it at all. The ordering the sentence argued for held exactly: the corpus was cleaned first
and the tightening reddened nothing ([[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]]).

**The decision this page carries is untouched by all of it.** The filename half is still an
advisory and the title half is still red; what has changed is that the advisory has nothing to say.
