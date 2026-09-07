---
title: "The title check asks and does not judge, because no lexical rule separates the shapes"
type: concept
status: deprecated
authority: title-check-mechanism
basis: code
sprint: S2
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-the-ritual-gets-a-retro/handoffs/2026-08-17-the-ritual-gets-a-retro.md", "scripts/vault-check.sh", "scripts/vault-check-selftest.sh", "CLAUDE.md"]
superseded_by: [[the-title-check-asks-and-the-answer-is-a-retitle]]
tags: [vault, testing]
---

# What the check does when it finds a number in a title

Rule 10 of `vault-check.sh` fails a page whose title contains a digit or a number word **and which
carries no `quantity:` line**. The page answers once, in free text, and the run goes green. It does
not decide whether the number was legitimate.

**That is measured timidity rather than the ordinary kind.** No lexical predicate separates the two
shapes:

| title | verdict | why |
|---|---|---|
| *"Two staleness checks, at two different times"* | violation | there are three, and the third arrived without touching the page |
| *"...are two different properties"* | not a violation | a third property would make the page **wrong**, not stale |

The titles are grammatically identical. What separates them is **whether the counted set belongs to
the page or to the world outside it**, and no script reads that. So the reason *is* the answer, and
an enum would be guessed at - which is why `quantity:` is free text
([[a-field-earns-its-place-by-being-read-or-by-being-a-checksum]]).

## What is exempt without a declaration

Four things, each because it is not a count: **a code span** (how this corpus writes identifiers),
**an ISO date** (a fixed boundary that cannot drift), **a digit glued to a letter** (`cp1252` is a
name), and **the word *one***, which was measured out of the rule rather than argued out - all
fourteen titles using it used it as a pronoun or as an invariant
([[measurement-settled-what-argument-could-not]]).

## The declarations are the instrument's own alarm

Measured over the corpus on 2026-08-17: **37 titles of 165 carried a quantity; 18 were retitled and
19 answered.** The criterion that asked for this rule was written expecting eight, and being low by
a factor of four is itself the finding - the rule had no written boundary, so nobody could count
against it ([[a-title-names-what-is-counted-instead-of-counting-it]]).

**If the declarations ever much outnumber the retitles, the boundary is drawn in the wrong place**,
and they are countable: `grep -c "^quantity:" wiki/*/*.md`. An instrument that reports its own
misalignment is the shape this project asks of a threshold
([[an-instrument-that-contains-its-own-answers-can-be-gamed]]).

**The eighteen retitles cost eighteen edits and no supersessions**
([[a-title-corrected-in-place-is-not-a-supersession]]), which is the only reason a compliance pass
of that size fitted in one session.

**Why the rule is in the script and not only in the vault.** The page stating the rule was followed,
the next day, by a title saying *five* while the check printed *seven* - written by the librarian, a
day after the librarian wrote the rule. Prose does not stop an agent
([[no-rule-reads-a-harness-file]]).
