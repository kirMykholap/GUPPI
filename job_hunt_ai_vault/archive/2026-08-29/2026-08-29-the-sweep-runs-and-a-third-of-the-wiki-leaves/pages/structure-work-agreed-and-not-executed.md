---
title: "The structure work agreed on 2026-08-16 and not executed, each row with what waiting costs"
type: decision
status: archived
authority: structure-deferrals
binding: deferral
basis: human
sprint: S1
decided: 2026-08-16
created: 2026-08-16
sources: ["archive/2026-08-16/2026-08-16-the-structure-questioned/handoffs/2026-08-16-the-structure-questioned.md"]
tags: [vault, process]
---

# Deferred, with the consequence written beside each

The session of 2026-08-16 spent about three hours on the shape of this store and committed four
changes. Everything below was agreed, designed or decided and **not done**. It is recorded as one
page because it is one decision — *not now, and here is what that costs* — taken at one sitting by
the owner.

**Rejected: doing them inside the session that raised them.** Several are supersessions, one is a
migration blocked on a tool that does not exist, and two are the owner's call about how much
structure he wants to hold ([[the-librarian-writes-unattended]]).

| Not doing now | What waiting costs |
|---|---|
| Superseding [[lint-waits-for-an-open-sprint]] — **decided**, not executed | a `current` page keeps a title falsified in 2026-08-15, and twelve inbound links wait to move with it |
| The second retitle, [[staleness-checks-run-at-different-times-and-ask-different-questions]] | **undecided by the owner**; its *filename* is false too, so the cost is higher than the first |
| Rewriting `index.md` down to hubs | the map keeps three copies of what `CLAUDE.md` and `sprint.md` own ([[the-index-reads-and-the-schema-writes]]); audit finding #3 stays open |
| The mechanism for S1 criterion 4 | a `CLAUDE.md` claim can still go stale unnoticed — four instances so far, the newest created this session by a file move ([[claude-md-may-point-and-may-not-assert]]) |
| Alias-to-page in the dictionary | written as a proposal and not taken ([[an-alias-may-point-at-a-page-not-only-at-a-tag]]); the mechanism that inflates the big tags keeps working |
| `tasks/` | the owner's call, and he does not want to hold that much structure yet ([[the-wiki-has-five-folders-and-tasks-is-not-one]]) |
| The product's own shape — module map, CLI, data model | `entities/` holds fifteen pages, **none of them about the application**, and they have no source in `raw/` to be compiled from ([[reconciling-entities-against-the-decision-register]]) |
| Moving `raw/` into a dated `archive/` | blocked on a path rewriter — **115 of 124 pages cite `raw/` in `sources:`** ([[moving-raw-into-a-dated-archive]]) |
| Structure inside `raw/` — `plans/`, `specs/`, `notes/` | agreed as nearly free, and still not done |
| `/vault-ask` as a mask rather than a dispatch | the fork is context pollution against tokens and wall-clock, and it is not obvious either way ([[a-skill-is-a-mask-and-a-subagent-is-a-body]]) |
| Pinning `.gitattributes` itself | it warns on its own commit; outside the scope of the finding it belongs to ([[markdown-is-pinned-to-lf]]) |

## Two rows are supersessions and only one of them is decided

The first two rows are the retitles of finding #1 in
[[the-audits-findings-are-owed-to-the-owner]], and they are now also instances of a general
rule ([[a-title-names-what-is-counted-instead-of-counting-it]]). **The librarian may not perform
either from this page.** A retitle is supersession, the owner has decided only the first, and the
second is undecided — so an ingest that executed them would be choosing on his behalf.

## What is deferred here and what is designed elsewhere

This page records *that* we said not now. Where a design sits behind a row it has a proposal of its
own, which is the boundary [[proposals-are-a-folder-not-a-status]] draws. Rows with no proposal
behind them — `tasks/`, the structure inside `raw/`, `.gitattributes` — have nothing designed yet,
and that is the honest state rather than an omission.

## Three rows moved on 2026-08-16, in the later session of the same day

**Nothing was executed** — the rows below gained a decision or a design, not a change on disk. The
new session's own deferrals are a separate page, [[what-the-harness-build-waits-on]], because they
are a separate sitting.

| Row above | What moved |
|---|---|
| The mechanism for S1 criterion 4 | **designed whole**: the harness becomes a build ([[the-harness-is-compiled-not-maintained]]), with [[marked-regions-and-the-prose-outside-them]] aimed at the residue. Whether "a working answer" requires it to be **built** is the owner's reading |
| Moving `raw/` into a dated `archive/` | **decided**: `archive/<session date>/`, one wave, artefacts included ([[archive-is-dated-by-session-and-holds-what-left-the-working-set]], [[raw-holds-testimony-and-artefacts-are-frozen]]). Still blocked on the rewriter |
| The product's own shape — module map, CLI, data model | **decided, and sequenced**: `entities/` gets one page per package, after `asserts:` and the staleness detector exist ([[entities-describe-the-application-once-the-detector-exists]]) |

The two supersession rows are **unchanged and still the owner's**, and a third joins them: the
handoff template's numbers, decided away by
[[the-handoff-template-moves-out-of-raw-and-drops-its-numbers]] while
[[the-handoff-template-maps-onto-the-categories]] still describes what is on disk.

## The two retitle rows read on 2026-08-19: the undecided one is done and the decided one is not

**Row two is closed on both halves.** [[staleness-checks-run-at-different-times-and-ask-different-questions]]
was retitled at `b6fc6d8` on 2026-08-17 — from *"Two staleness checks, at two different times…"* to
the title it carries now — and its **filename**, which this row prices as *"false too, so the cost
is higher than the first"*, was renamed on 2026-08-19 in the sweep of sixteen addresses
([[a-page-rename-is-sed-and-verify]]). The row said the retitle was *undecided by the owner*, and
that is how it stood when it was written; what settled it was a general rule rather than a ruling on
this page — a title carrying a measurable quantity is a violation, unconditionally
([[a-title-names-what-is-counted-instead-of-counting-it]]).

**Row one is not closed, and it is the one that was decided.**
[[lint-waits-for-an-open-sprint]] still carries *"/lint has never run"* in its title, and `/lint`
ran on 2026-08-15. **Nothing has been performed there**, because the falsehood is not a count and
no instrument can see it: rule 10 reads a title for *counting words*, never for truth, and
`bash scripts/vault-check.sh | grep -c 'the title counts'` returns 0 on a corpus that still holds
this one. It is reported here rather than repaired — a title states the page's claim, and the sweep
that could legally touch it was scoped to quantities ([[knowing-a-rule-is-not-a-mechanism]]).

**Its price, however, is dead.** The row charges *"twelve inbound links wait to move with it"*.
**A retitle moves no address at all** (owner, 2026-08-17 —
[[a-title-corrected-in-place-is-not-a-supersession]]), so the links that wait number zero, whatever
the page's inbound count is; for the record it is 27 today, read with
`rg -o '\[\[lint-waits-for-an-open-sprint\]\]' wiki archive index.md tags.md sprint.md log.md | wc -l`.
That figure is the cost of a **rename**, which nobody has proposed for this page.

**And "the librarian may not perform either from this page" held exactly.** Neither was done from
here. The retitle of row two was performed by a session executing the general rule, and the rename
by a sweep the owner commissioned — which is the difference between a deferral being honoured and a
deferral being forgotten.

## The `raw/` structure row is decided, and it is still not executed — 2026-08-19

**The row reading *"Structure inside `raw/` — `plans/`, `specs/`, `notes/` | agreed as nearly free,
and still not done"* now has an ordering behind it**: it happens **before** the archive move, not
after, because doing it after would make the rewrite run twice
([[raw-gains-its-internal-structure-before-the-move]]).

**Nothing was executed.** The row moves from *agreed* to *decided and sequenced*, which is the same
move three other rows made on 2026-08-16 and is recorded the same way. **The honest state is that
this page's own closing observation still holds**: rows with nothing designed behind them are the
ones that stay, and this one now has a design
([[emptying-raw-by-a-script-that-moves-and-rewrites-its-citations]]).

**And the row above it — moving `raw/` into a dated `archive/` — gained a level and a mechanism** on
the same day ([[the-archive-gains-a-folder-per-session-inside-the-date]],
[[raw-is-emptied-by-a-script-and-the-move-lives-inside-the-ingest]]). Its price is re-measured and
has grown: 150 of 165 pages name `raw/handoffs` and 23 of those in prose, against the 115 of 124
this page records.
