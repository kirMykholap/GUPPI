---
title: "A title carries no measurable quantity, and names what is counted instead of counting it"
type: decision
status: archived
authority: title-quantities
binding: prohibition
basis: human
sprint: S1
decided: 2026-08-16
created: 2026-08-16
sources: ["archive/2026-08-16/2026-08-16-the-structure-questioned/handoffs/2026-08-16-the-structure-questioned.md"]
tags: [retrieval, vault]
---

# Decided 2026-08-16, and the rule is unconditional

**No measurable quantity appears in a page title.** Not "seven AST tests", not "one librarian with
four callers", not "two moments". A title is read long after the number in it stopped being true,
and a false title is worse than a vague one because it is asserted rather than looked up.

**The technique that replaces it: name what is being counted instead of counting it.**

| instead of | write |
|---|---|
| "two staleness checks" | "staleness is checked before the brief is written and again before it is read" |

**Rejected twice on the way to it.** A version allowing counts that are bound to a date, and a
version allowing design invariants — *one* finaliser, *one* writer — where the count is the claim.
The owner refused both, and the rule is unconditional: a rule with exceptions is a rule nobody can
apply, and the exceptions were being proposed by the same turns that were explaining the rule
([[the-turn-that-explains-a-rule-adds-exceptions-to-it]]).

## What it obliges, and what was deliberately not done

**Eight titles in this corpus are out of compliance**, counted on 2026-08-16. **Three of the eight
will be broken by S2 on purpose** — the folder count, the count of rules in the repository's
`CLAUDE.md`, and the script count — because S2 changes all three of those numbers. Whoever executes
S2 should expect to rename them as part of that work rather than discover them afterwards.

**The retitles were not performed by the ingest that recorded this decision.** A title carries the
page's claim, so changing one is supersession and not an edit: the successor is written, the old
page is deprecated with `superseded_by:` and moved to `archive/`. Only one of the two outstanding
retitles has been decided by the owner ([[the-audits-findings-are-owed-to-the-owner]],
finding #1), so the compliance pass waits on him rather than on the librarian.

The companion rule, about what shape a compliant title takes, is
[[the-titles-form-follows-the-records-type]].

## Executed 2026-08-17, and one sentence above is corrected

**The compliance pass ran, and the estimate was low by a factor of four.** Measured over the corpus:
**37 titles of 165 carried a quantity — 18 were retitled and 19 answered in a `quantity:` line.**
The section above says *eight*, counted on 2026-08-16 by eye against a rule that had no written
boundary; the boundary arrived with rule 10 of `vault-check.sh`, and only then could anything be
counted against it ([[the-title-check-asks-and-does-not-judge]]). **The gap between eight and
thirty-seven is the evidence that the rule was unenforceable as written rather than merely
unenforced** ([[measurement-settled-what-argument-could-not]]).

**The paragraph above headed "The retitles were not performed" is corrected.** It says *"A title
carries the page's claim, so changing one is supersession and not an edit"*. **The owner decided
otherwise on 2026-08-17**: a title corrected in place is **not** a supersession, because in this
vault the filename is the identity and a corrected title moves no address
([[a-title-corrected-in-place-is-not-a-supersession]]). That is what made a pass of eighteen
retitles affordable in one session; as supersessions it would have been eighteen new pages, eighteen
archived, and every inbound link rewritten.

**The word *one* is exempt, and it was measured out rather than argued out**: all fourteen titles
using it used it as a pronoun or as an invariant. The three titles this page expected S2 to break on
purpose were among the thirty-seven and are already dealt with.

## Extended to filenames by the owner, 2026-08-17

**A filename carrying a measurable quantity is a violation too.** Rule 10 reads only `title:` by design,
and the reasoning written into it — the filename is the address, so renaming moves something and retitling
does not — is what made the pass of eighteen retitles affordable. **The owner decided the rule covers both**
anyway ([[the-title-rule-extends-to-filenames]]).

**Two pieces of work follow and they are not the same size**: a verdict in the check, which is small, and
the renames, which are blocked on the rewriter-and-detector pair because a filename is what every
`[[wikilink]]` resolves to. **At least four filenames carry a count today**, and the worst offender carries
23 inbound links ([[the-dense-tags-are-not-split-and-the-standing-advisories-are-named-here]]).

## Reaffirmed and hardened on 2026-08-18: the escape hatch is gone

**owner: the rule is unconditional. No digits in a title, none in a filename. The `quantity:` field
is rejected, and this question is closed permanently.** The full ruling, what it obliges and the
order the work has to be done in are on
[[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]].

**The section above records nineteen pages answering in a declaration.** Those declarations are
being withdrawn, not honoured: the count stood at **24 against 23 retitles** at the retrospective,
which is the instrument this rule shipped with reporting that the boundary had been drawn in the
wrong place ([[the-title-check-asks-and-the-answer-is-a-retitle]],
[[a-field-admitted-around-the-admission-procedure-outlives-the-rule-it-softens]]).

**And the "23 inbound links" figure repeated above does not reproduce.** Re-measured at `c521a10`:
the worst of the six standing filenames carries **20** inbound links in the link set, and the page
the figure was written about carries **14** ([[a-page-rename-is-sed-and-verify]]).

## Closed 2026-08-19: both pieces of work are done, and this page stops carrying the figure

**"Two pieces of work follow and they are not the same size" is finished on both sides.** The
verdict landed on 2026-08-18 — rule 10 reads the filename with the predicate it reads the title
with (`2772439`), printing one name per line (`c521a10`) — and **the renames landed on 2026-08-19**,
sixteen of them in one sweep. **The rewriter-and-detector pair they were said to be blocked on was
never built and was never needed**: the whole of it was `git mv`, one `sed -f` over `wiki/`,
`archive/`, `index.md`, `tags.md` and `sprint.md`, and a verification pass, with `log.md` swept by
hand because rules 4 and 5 do not read it ([[a-page-rename-is-sed-and-verify]],
[[log-md-is-outside-the-link-set-the-check-reads]]). **The wait itself is the record and stays
above**: the price was believed to be a tool nobody had, and it was two days before anyone measured
it.

**The figure goes and the command stays.** *"At least four filenames carry a count today"* was the
reading of 2026-08-17, was thirteen when the advisory could finally count them, and is nothing now.
The reading is:

```
bash scripts/vault-check.sh | grep 'filename(s) count'      # empty on 2026-08-19
bash scripts/vault-check.sh | grep -c 'the title counts'    # 0 on 2026-08-19
```

Run beside this sentence, the first prints nothing and the second returns 0, with the run exiting 0
and nineteen advisories. That is the repair a figure gets once it has been corrected more than once:
name the decider instead of the number, the way every acceptance criterion in `sprint.md` already
does ([[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]]).

**The nineteen declarations are withdrawn, not honoured, and the field is gone from the check too.**
`grep -rc '^quantity:' wiki archive` sums to 0, and rule 10 no longer reads the key at all — the
short-circuit, the reader and the offer of the field in its message were removed on 2026-08-19, so
a `quantity:` line written today would be an inert frontmatter key rather than a silencer
([[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]]).

**And the exemption list this page opened has grown at both ends.** *One* is still exempt, and
**`first` joined it on the same measurement** — 13 pages use it in a title or a slug and every use
is a position or a pronoun. **Ordinals went the other way**: `second` through `twentieth` are
counting words now, `second` in over a measurement that argued against it
([[ordinals-count-and-first-does-not]]). **With no way for a page to declare itself, a word in that
list is a promise that the word is always a count**, which is why the list is short and why the one
deliberate exception to the promise is written down rather than discovered.

## The rule's two boundaries, settled 2026-08-19

Both were settled the same evening, and both are **boundaries rather than debts** — the owner's
point in each case is that nothing is owed, and writing it down is what stops a future session
opening a task for it.

- **The rule reads the title and the filename, and never the body.** A counting heading inside a
  page is out of scope; the two strings the store addresses and retrieves by are in scope and
  nothing else. Three agents reported body headings as findings during the clean-up above, and the
  list they would have produced was refused rather than filed
  ([[the-no-quantity-rule-reads-the-title-and-the-filename-and-never-the-body]]).
- **A title's length is unbounded and no check measures it.** Naming what is counted is longer than
  counting it, so the pass recorded above is what produced the three longest titles this corpus has
  held. A limit was offered in the check and refused, because it would undo half of the accuracy
  just paid for ([[the-length-of-a-title-is-unbounded-and-no-check-measures-it]]).

**Neither boundary changes the rule stated at the top of this page.** They say what it is about,
the way [[ordinals-count-and-first-does-not]] says which words it reads.
