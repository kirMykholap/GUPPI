---
title: "Ordinals count in a title and in a filename, `first` does not, and every word in the list is a promise"
type: decision
status: archived
authority: quantity-word-list
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-18
created: 2026-08-19
sources: ["log.md", "scripts/vault-check.sh"]
tags: [retrieval, vault, harness]
---

# The ruling, taken 2026-08-18 and built 2026-08-19

**Ordinals join the word list the no-quantity predicate reads** — `second` through `twentieth`,
beside the cardinals it already held. The rule itself is unchanged and is
[[a-title-names-what-is-counted-instead-of-counting-it]], extended to the address by
[[the-title-rule-extends-to-filenames]]; what is decided here is **which words the check treats as
counting**, in both halves of it.

**Until this, the list ran *two … twenty, dozen, both, twice, thrice* and stopped.** So a title or a
name built on an ordinal was a violation of the rule that nothing printed — the shape
[[knowing-a-rule-is-not-a-mechanism]] names, and this is the second time that gap has been found in
this same rule.

## What produced it: names the check could not see in the sweep it was guiding

Measured in a worktree at `1520164`: **the advisory named 13 filenames while 16 were renamed.** The
three it could not see were built on *second*, *fourth* and *fifth*. They were renamed anyway,
because the sweep was reading the rule and not only the check's output
([[a-page-rename-is-sed-and-verify]]), which is exactly why the gap was visible at all — a session
obeying only the printed list would have left three counting addresses behind and the run would
have stayed green.

## `second` is in, over a measurement that argued against it

**Measured across the corpus on 2026-08-18: three titles carried `second`, and three of three meant
*another* rather than the second of n.**

| title, as it read at `a1b89d9` | what `second` was doing |
|---|---|
| "The steward is a script that runs after the librarian, not a **second** unattended writer" | *another* writer — a design invariant, not a position |
| "…a figure that agrees with no expectation needs a **second** instrument before it is quoted" | *a different* instrument, which is what the page's own gloss already said |
| "The end of a run resets the chips first and re-reads the table **second**, through one listener" | sequencing — the table re-reads because the chips response announced itself |

`git grep -h -i '^title:.*\bsecond\b' a1b89d9 -- job_hunt_ai_vault/wiki job_hunt_ai_vault/archive`
prints those three; the same search over the tree today prints nothing, all three having been
repaired ahead of the verdict.

**The owner was shown that measurement and ruled the word in anyway.** The reason is a preference
between two kinds of predicate: one with **no measured exemptions to remember**, against one that is
**right more often**. A predicate a reader can state in a sentence is worth more than a predicate a
reader has to carry a list of exceptions for — and the exceptions are where this rule has failed
before ([[the-turn-that-explains-a-rule-adds-exceptions-to-it]]).

**Rejected: leaving `second` out on the measurement.** It is written down here rather than only in
the outcome, because *a decision that overrode its own evidence is worth more than one that agreed
with it* — the next reader who loses a correct title to this word needs the argument, not the
verdict ([[measurement-settled-what-argument-could-not]]).

## `first` is out, and it mirrors `one`

**Measured 2026-08-18: 13 pages use `first` in a title or a slug, and every one uses it as a
position or a pronoun** — "the first hit", "the first narrowing", "migrates first". None of them
counts anything that could drift. The reading is:

```
{ rg -li '^title:.*\bfirst\b' wiki archive; rg --files wiki archive | rg -i first; } | sort -u | wc -l
```

Run from the vault root on 2026-08-19 it returns **14**, and the fourteenth is this page's own name
— which is the demonstration as well as the figure: a page arguing that `first` is not a count is
free to say so in its address, and would not have been under the word it rules in.

**`one` had already been measured the same way on 2026-08-17** — 14 titles, every one a pronoun
("a known one") or an invariant ("exactly one finaliser"). **They are the same number in two words
and they are treated the same way**, which is why `first` is exempt while `second` is not: the
asymmetry is not an oversight, and it is the one thing about this list a reader is likely to
mistake for one.

## Why the list is short now, and what a word in it commits to

**While a page could declare itself exempt, a word only had to be *usually* a count.** A false
positive cost one line of frontmatter, so admitting a word was cheap and the list could be
generous.

**With the escape hatch withdrawn there is no appeal**
([[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]]), so a false positive is paid
for by **rewriting correct prose** — a real price, charged to whoever happens to be writing the
page. **So every word in the list is now a promise that the word is always a count**, and a word
enters it only on that promise.

**`second` is the known, deliberate exception to that promise**, and it is written here and in rule
10's own comment for one reason: the first author who loses a correct title to it should find an
answer rather than a surprise ([[the-title-check-asks-and-the-answer-is-a-retitle]]).

## What it obliged, and the order it was done in

**The corpus was repaired before the predicate was widened**, which is the ordering the field's
rejection already fixed and for the same reason: tightening first reddens pages nobody can legally
fix in one session ([[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]]). Four
pages carried an ordinal into that repair and each records it in place —
[[proposals-are-a-folder-not-a-status]] (*the fifth category*),
[[table-refreshes-itself]] (*re-reads the table second*),
[[reconciling-entities-against-the-decision-register]] (*the owner's third lint check*) and
[[a-measurement-agreeing-with-no-expectation-needs-a-different-instrument]] (*a second
instrument*).

**Verified on the run of 2026-08-19**: `bash scripts/vault-check.sh` exits 0,
`… | grep -c 'the title counts'` returns 0 and `… | grep 'filename(s) count'` is empty. **The
tightening reddened nothing**, which is the whole of what the ordering was for.

## What this page does not decide

**It is neither a supersession of the field's rejection nor an extension of it.** That page answers
*may a page declare a number harmless*; this one answers *which words the predicate reads*. What
this page extends is the reach of the no-quantity rule itself
([[a-title-names-what-is-counted-instead-of-counting-it]]), the way the filename half did before it.
The two decisions meet at one point only, and it is named above: the hatch going is what turned a
word in the list from a heuristic into a promise.

**Nothing here says how a flagged page is repaired.** A flagged title is retitled in place
([[a-title-corrected-in-place-is-not-a-supersession]]) and a flagged filename is renamed on a
scheduled sweep, because the filename half is an advisory and the title half is red
([[the-filename-verdict-is-an-advisory-while-the-title-verdict-is-red]]).
