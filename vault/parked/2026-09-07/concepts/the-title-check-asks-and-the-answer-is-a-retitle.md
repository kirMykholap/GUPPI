---
title: "The title check asks and does not judge, and the answer it asks for is a retitle"
type: concept
status: current
authority: title-check-mechanism
basis: human
sprint: S2
created: 2026-08-18
sources: ["archive/2026-08-18/2026-08-18-the-filename-half-lands-and-the-escape-hatch-falls/handoffs/2026-08-18-the-filename-half-lands-and-the-escape-hatch-falls.md", "scripts/vault-check.sh", "scripts/vault-check-selftest.sh"]
tags: [vault, testing, harness]
supersedes: [[the-title-check-asks-and-does-not-judge]]
---

# What the check can and cannot decide, which has not changed

Rule 10 of `vault-check.sh` flags a title, and now a filename, containing a digit or a number word.
**It cannot decide whether the number was legitimate**, and that timidity was measured rather than
chosen:

| title | verdict | why |
|---|---|---|
| *"Two staleness checks, at two different times"* | violation | there are three, and the third arrived without touching the page |
| *"...are two different properties"* | not a violation | a third property would make the page **wrong**, not stale |

The two are grammatically identical. What separates them is whether the counted set belongs to the
page or to the world outside it, and no script reads that.

**Four things are exempt without any declaration**, each because it is not a count: a code span
(how this corpus writes identifiers), an ISO date (a fixed boundary), a digit glued to a letter
(`cp1252` is a name), and the word *one*, which was measured out of the rule rather than argued out
([[measurement-settled-what-argument-could-not]]).

# What changed on 2026-08-18: the answer is a retitle, not a declaration

**The predecessor of this page ended the sentence differently** — it said the flagged page answers
once, in free text, in a `quantity:` line, and the run goes green
([[the-title-check-asks-and-does-not-judge]]). **The owner rejected that field**, and the rule stands
unconditional: a flagged title is retitled, and a flagged filename waits for its rename
([[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]],
[[a-title-names-what-is-counted-instead-of-counting-it]]).

**So the check still asks, and the set of legal answers shrank by one.** Nothing about the lexical
argument above depends on the escape hatch; what depended on it was the idea that a page could
settle the question about itself.

# The state of the code, which is not the decision

**The escape hatch is still in `scripts/vault-check.sh` and twenty-four pages still carry the
field.** That is a measurement of the tree at `c521a10`, not a rule anybody may lean on. Removing
the branch before the corpus is clean reddens twenty-four pages in one run, so the order is corpus,
filenames, schema, then check.

**Rule 10's `answered` flag returns before the slug is evaluated**, so one `quantity:` line silences
the title half and the filename half together. **Seven filenames are exempt on it today** and six
print in the advisory ([[the-filename-verdict-is-an-advisory-while-the-title-verdict-is-red]]).

# The instrument that was supposed to catch this, and did not

The rule shipped with its own alarm: **if the declarations ever much outnumber the retitles, the
boundary is drawn in the wrong place**, and they are countable with `grep -c "^quantity:" wiki/*/*.md`.

**Nobody read it.** At the retrospective the count stood at **24 declarations against 23 retitles**,
and 5 against 5 since the rule became checkable — an instrument sitting at parity, installed by its
own author, reporting exactly the misalignment it was built to report
([[an-instrument-that-contains-its-own-answers-can-be-gamed]],
[[a-field-admitted-around-the-admission-procedure-outlives-the-rule-it-softens]]).

**Why the rule is in the script and not only in the vault.** The page stating it was followed, the
next day, by a title saying *five* while the check printed *seven* — written by the librarian, a day
after the librarian wrote the rule. Prose does not stop an agent
([[no-rule-reads-a-harness-file]]).

# The predicate on 2026-08-19: the exemption list moved at both ends

**"Four things are exempt without any declaration" is now five, and the fifth is `first`.** It was
measured out exactly as *one* was — 13 pages used it in a title or a slug on 2026-08-18 and every
use was a position or a pronoun. **And the word list gained the ordinals**, `second` through
`twentieth`, with `second` ruled in over a measurement that said all three of its uses in this
corpus meant *another* ([[ordinals-count-and-first-does-not]]).

**That ruling changes what a word in the list means, and it changes it because of this page's own
subject.** While a page could answer in a declaration, a word only had to be *usually* a count. With
the answer withdrawn, a false positive is paid for by rewriting correct prose, so **every word in
the list is now a promise that the word is always a count** — and the sentence above, *"the set of
legal answers shrank by one"*, is what made that so.

**The state-of-the-code section above describes a tree that is gone.** The escape hatch is out of
`scripts/vault-check.sh`, no page carries the field, and there is no `answered` flag to return
before the slug is evaluated. The order it prescribed — corpus, filenames, schema, then check — was
followed in full ([[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]]), and the
tightening reddened nothing: the run of 2026-08-19 exits 0 with nineteen advisories and an empty
filename line.

**What has not changed is the whole of this page's claim.** The check still cannot decide whether a
number was legitimate; the two grammatically identical titles in the table above still get opposite
verdicts for a reason no script can read. What shrank is the set of answers, and now the set of
words a page may use without meaning a count.

# What the check reads, bounded on 2026-08-19

**Two strings, and nothing else.** The `awk` behind rule 10 stops evaluating a page at the closing
`---` of its frontmatter — `done { next }` — and calls its `verdict()` with `title` and `FILENAME`.
A counting heading in the body is never scanned, and after 2026-08-19 that is a decision rather
than a hole in the predicate
([[the-no-quantity-rule-reads-the-title-and-the-filename-and-never-the-body]]).

**Nothing measures how long either string is**, and no check should
([[the-length-of-a-title-is-unbounded-and-no-check-measures-it]]). The check asks whether a title
is *false*; length cannot make one false.
