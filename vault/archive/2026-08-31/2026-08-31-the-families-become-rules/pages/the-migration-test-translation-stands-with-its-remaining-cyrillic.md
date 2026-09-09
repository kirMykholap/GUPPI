---
title: "The translation of `test_migrations.py` stands with its Cyrillic fixture data and stderr substrings"
type: decision
status: archived
authority: translation-remainder-scope
basis: human
binding: prohibition
sprint: S2
decided: 2026-08-20
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-lock-fires-and-deadlocks-the-vaults-only-writer/handoffs/2026-08-20-the-lock-fires-and-deadlocks-the-vaults-only-writer.md", "tests/integration/test_migrations.py"]
tags: [process, testing, architecture]
---

# The ruling, 2026-08-20

> **owner: «норм, пусть остаются.»**

**Sprint item 3 is closed with Cyrillic still in the file, deliberately.** Comments, docstrings and
assertion messages went to English — **59 replacements, 191 insertions against 190 deletions**. What
stayed is fixture data and substrings asserted against what a migration prints.

**Rejected: translating the assertion substrings.** Doing so reaches `migrations/versions/`, which
is a widening of scope and therefore a question rather than a notification
([[narrowing-a-scope-notifies-and-widening-it-asks]]).

## Why a Cyrillic grep was never the target

**The rule's own text says so** — the boundary is what a string is *for*, not which alphabet it is
in ([[english-in-the-repository-russian-with-the-owner]],
[[the-english-rule-is-forward-only-and-the-unit-is-the-file]]). A translated file greping clean
would have meant fixture names were anglicised, which nothing asked for. **Keeping the assertion
substrings needs no language argument at all**: the scope argument alone settles them.

## Two readings of what remains, and they are different questions

| the reading | the figure | what it counts |
|---|---|---|
| what is in the file after the translation | **20 Cyrillic lines** — 13 fixture data, 7 stderr substrings | the state that shipped |
| what must survive **any** correct translation | **18 lines** — 11 fixture data, 7 stderr substrings | the floor, measured against the rule |

**The difference is two fixture lines that could have gone and did not**, and it is recorded rather
than reconciled: the first is what the file holds, the second is what the rule obliges, and reading
one as the other is how a floor becomes a ceiling. Fixture data named in both:
`name="Кирилл"` in four places and twice more inside raw SQL, `description_raw="Опис"`,
`notes="Хорошая вакансия"`, `collection_cities=["Київ"]`, and the assertion that reads it back.

## What the seven stderr substrings actually depend on

**They are Russian because five migrations are**, not because a policy says a warning is product
text — and the newest migration already contradicts that reading in practice
([[the-language-of-a-migration-warning-is-unsettled]]). **So this file's remainder is pinned by
files the sprint item does not name.**

**The run of the tests is still owed.** `pytest --collect-only` reports 14 tests in 0.06 s; the
tests themselves were not run, because Docker was down and the suite hangs rather than failing
([[the-integration-suite-hangs-rather-than-failing-when-docker-is-down]],
[[a-deferred-check-must-be-run-when-its-condition-arrives]]). No executable statement changed, and
the interpolation set was proved identical before and after
([[collect-only-cannot-exercise-an-assertion-message]]).
