---
title: "Translating the repository's Russian past into English — every line carrying Cyrillic, and tests/ is the risky half"
type: proposal
status: current
authority: english-sweep-design
basis: measurement
sprint: S1
created: 2026-08-15
sources: ["CLAUDE.md", "[[english-is-the-rule-and-the-russian-past-is-deferred]]"]
decided_by: [[english-is-the-rule-and-the-russian-past-is-deferred]]
tags: [process, testing]
---

# What a translation pass would actually be

**Raised by the owner on 2026-08-15, and not scheduled.** His position: **all knowledge should be
in English**; the chat with him stays Russian; and the "new work only" clause was his — *"I added
it because I did not want to deal with the rest at the time"* — which has since gone stale as a
standing rule. The decision half of this is
[[english-is-the-rule-and-the-russian-past-is-deferred]], and it says **deferred, not exempt**.
**Nothing here has been decided.** This page is the design, so that it stops living in a chat log.

## The size, measured 2026-08-15

Lines **containing** Cyrillic, not lines to translate: a line with one Russian word inside an
English sentence counts once, so the number is an upper bound on files touched and a lower bound on
the reading.

```
rg -l --no-ignore '[\x{0400}-\x{04FF}]' src tests docs scripts | wc -l
rg -c --no-ignore '[\x{0400}-\x{04FF}]' src tests docs scripts | awk -F: '{s+=$NF} END {print s}'
```

and per bucket with `-g '*.py'` / `-g '*.html'` over `src/`.

**Take that command literally.** The first attempt used `grep -P` with a Cyrillic range and
returned **zero** matches over a tree holding 10,947 such lines — `-P` is unsupported in this
environment and the failure is silent, green, and indistinguishable from a clean answer. The
figures below are `rg`'s ([[a-measurement-agreeing-with-no-expectation-needs-a-different-instrument]]).

| bucket | files | lines |
|---|---|---|
| `tests/` | 42 | 4916 |
| `docs/` | 15 | 3740 |
| `src/` — Python and `app.css` | 35 | 2044 |
| `src/` — templates, the product UI | 12 | 228 |
| `scripts/` | 3 | 19 |
| **total** | **107** | **10947** |

The `src/` split is 34 `.py` files carrying 2004 lines plus `app.css` carrying 40; the templates are
counted apart because they are the one bucket that is out of scope by rule rather than by cost.

*(The title read "Translating the repository's Russian past into English — 10,947 lines, and tests/
is the risky half" until 2026-08-18, and the number now lives here, in the section that carries its
date and the command that produced it. **It is a measurement of one past state of the repository**,
true on 2026-08-15 and drifting with every commit since — which is the shape a title cannot hold at
all: what survives is a count stamped with the point it was taken at, and *"it is now N"* has failed
every time it was tried ([[a-stated-count-drifts-from-the-list-it-heads]]). That reasoning stood in
a `quantity:` line until the field was rejected and the rule was made unconditional in both halves
([[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]]); the title now names what was
counted — every line carrying Cyrillic — instead of counting it
([[a-title-names-what-is-counted-instead-of-counting-it]]).)*

## What is in scope, and what never will be

- **The 228 template lines are not in scope and never will be.** That is product content the owner
  reads on screen, and it has its own standing ground — the language rule puts what he sees while
  using the tool in Russian, and only identifiers cross back
  ([[statuses-stay-english-identifiers]]). A translation pass that reached the templates would be a
  product change wearing a housekeeping commit.
- **`docs/` — 3740 lines — is plans and specs, which are records of what was decided when.**
  Arguably they should not be rewritten at all: a record rewritten later is no longer a record of
  what was written, and this vault's own first rule is that nothing is deleted. The cheapest honest
  position is that `docs/` is history and stays in the language it was written in; the alternative
  — translating it — needs an argument nobody has made yet.
- **`tests/` — 4916 lines — is the risky part**, and it is the part with a standing refusal behind
  it: **263 Russian test names**, and renaming them was rejected because the diff is unreviewable
  and every reference in the older plans breaks. That refusal was recorded, and this proposal does
  not overturn it; it only records that the refusal is now the *open* question rather than the
  settled one.
- **`src/` Python — 2044 lines — is the cheap and uncontentious half.** Docstrings and comments are
  already covered by the standing rule when they are substantially rewritten
  ([[docstrings-drift-inside-their-own-commit]] is the reason they get rewritten at all), so this
  bucket is where a migration would consume the least judgement per line.
- **`scripts/` — 19 lines — is a rounding error** and could be done in the commit that decides
  anything at all.

## What it would take

1. **A decision, per bucket**, not one decision for the tree. The four buckets have four different
   arguments and only one of them is about effort.
2. **A reviewable unit.** The reason the refusal has held is the diff: 10,947 lines of translation
   is a review nobody can perform, so what is proposed is one directory per commit, nothing else in
   that commit, and `uv run pytest -q` green as the only mechanical evidence — a translation commit
   that also changes behaviour is unreviewable twice over.
3. **A rename map, if test names go.** Every older plan and spec that quotes a Russian test name
   becomes a dangling reference the moment it is renamed, and those documents are records that will
   not be rewritten to match. The map is the artefact that keeps them followable, and nothing in
   this repository produces one today.

## What is open

- **Whether `docs/` is in scope at all.** The answer here leans no, and it is not the librarian's
  to give.
- **Whether the 263 test names are renamed**, which is the whole weight of the proposal: without
  them a "migration" is 2063 lines of comments and scripts, and with them it is the diff the
  original refusal was about.
- **What triggers it.** No trigger is proposed: nothing about a Russian docstring degrades over
  time, so this is work with no deadline, which is exactly the kind that stays undone until it is
  scheduled deliberately.

## What it would oblige

If a bucket is accepted, [[english-is-the-rule-and-the-russian-past-is-deferred]] is superseded for
that bucket and this page is retired with `superseded_by:` pointing at whatever decides it —
which is the mechanism that lets the vault answer *what did we plan and never do*
([[proposals-are-a-folder-not-a-status]]).

# Narrowed from a refusal into a method — 2026-08-20

**The owner ruled that the English rule is forward-only and the unit of translation is the file**
([[the-english-rule-is-forward-only-and-the-unit-is-the-file]]).

> «Мы переводим русский текст постепенно, когда наткнемся на него и увидим проблему, которую он
> создает.»

**So this page stops being *what we would have to do if we ever decided to* and becomes *what
happens by itself, file by file*.** The scope, the risks and the ordering it works out are still
what a deliberate sweep would need; what has changed is that no sweep is planned and none is
required.

**The half that keeps "gradually" from meaning "never": a file too large to translate in the same
change goes onto `sprint.md`.** Executed on the day of the ruling: `tests/conftest.py`, six Cyrillic
lines to zero. Deferred the same day: `tests/integration/test_migrations.py`, 206 Cyrillic lines of
951, now mixed-language by that session's own hand
([[the-deferrals-of-this-session-go-onto-the-sprint]]).

**This page is not retired**, because it is not built and not refused: it still carries the design
of the sweep that would be needed if the gradual method is ever judged too slow.

# `test_cli.py` is measured now, and it lands squarely inside this refusal — 2026-08-20

**`tests/integration/test_cli.py` carries 298 Cyrillic lines and 34 Russian test function names** —
the third-largest Cyrillic file in `tests/`. It was first reported as *"line 78 carries Cyrillic
prose"*, from a single `grep -n` hit that was never counted
([[a-grep-that-prints-one-line-is-a-report-about-the-first-match-and-not-a-count]]).

**The corrected figure puts it inside the bucket this page refuses**: Russian test names, a diff
nobody can review, and no rename map. It is not touched.

**And the sprint names only `test_migrations.py`**, so the scope of the English sweep is a decision
rather than an accident of which file somebody happened to open
([[the-english-rule-is-forward-only-and-the-unit-is-the-file]],
[[the-migration-test-translation-stands-with-its-remaining-cyrillic]]).

# One file left the backlog by being regenerated — 2026-08-31

**`docs/vault-cleanup-families.md` is English now**, and it got there by the forward-only rule rather
than by a sweep. It carried **696 Cyrillic lines of 1,819**; regenerating it whole put every line under
the obligation, because the unit is the file.

**owner selected, 2026-08-31: «переводим».** Put to him against the alternative of writing a page
declaring the file an exception, and he took the translation. **Rejected: an exception page.**

**What that avoided is worth naming.** The session's own first plan would have minted a **second**
Russian file in `docs/` beside it — a hand-written verdicts file — which the forward-only rule would
have caught on its first regeneration anyway.

**This is one file off a backlog this proposal does not enumerate**, and it changes nothing else here.

*(Extended at the ingest of `raw/handoffs/2026-08-31-the-families-become-rules.md`.)*
