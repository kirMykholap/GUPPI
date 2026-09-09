---
title: "A copy of a list drifts from the list; a sweep cannot"
type: lesson
status: archived
authority: copied-list-drift
basis: code
sprint: S2
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-the-ritual-gets-a-retro/handoffs/2026-08-17-the-ritual-gets-a-retro.md", "scripts/vault-check-selftest.sh", "scripts/vault-check.sh"]
tags: [testing, vault]
---

# Two selftest cases had gone quiet, and nothing said so

`link_only_in_raw` and `fenced_link_reg` both test the orphan rule, and both had to clear the
subject page's inbound links first. **They cleared them from a list of registers copied into the
case** — while `vault-check.sh` reads a longer one. When `tags.md` gained a link to the subject,
neither case was testing anything: the link the case had not thought to clear kept the page
reachable, so the rule stayed silent for a legitimate reason and the case passed for the wrong one
([[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]]).

**Both were replaced by a sweep of the whole copy** — clear every register the fixture has, rather
than the ones the case remembered.

# The general shape

A copy of a list is correct on the day it is written and has **no mechanism** for staying correct.
The list it copied grows for its own reasons, and the copy does not fail — it narrows, silently,
which is the failure mode that produces a green run over an untested subject.

**A sweep restates the intent rather than the enumeration**, so it cannot fall behind. The cost is
that a sweep is coarser; the benefit is that its coarseness is visible while a stale copy's
narrowness is not.

# Where else this project pays for a copy

- **The handoff mapping in six files**, found only by grepping for a distinctive string
  ([[the-mapping-is-documented-at-each-hop-and-copied-nowhere]]).
- **A stated count at the head of a list it does not read**
  ([[a-stated-count-drifts-from-the-list-it-heads]]).
- **The catalogue**, which is the counter-example: generated and diffed rather than maintained
  ([[the-catalogue-is-generated-not-maintained]]).

The rule that follows: **when a test needs to know a set the subject also knows, derive it or sweep
it — never write it down twice.**

## The second recorded instance, 2026-08-17

**`empty_vault` in `vault-check-selftest.sh` held its own copy of the vault layout** and went red
when `wiki/rules/` arrived — for a reason the case is not about. The case asserts something about an
empty vault; what broke it was a folder list it had no business owning.

**Verified as pre-existing**: the written list predates that session, which only exposed it. It now
mirrors the pristine copy rather than restating it.

The same day produced the rule's positive form: **rule 11's governed set is swept, never listed**,
precisely because two lists of one set drift and this suite had already lost cases to that
([[the-governed-set-is-swept-and-markdown-by-property]]). And the general repair, when a copy has
drifted twice, is deleting the copy rather than adding the missing row
([[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]]).
