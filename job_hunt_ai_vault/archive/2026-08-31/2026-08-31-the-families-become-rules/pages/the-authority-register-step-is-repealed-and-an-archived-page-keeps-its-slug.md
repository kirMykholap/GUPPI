---
title: "The authority register step is repealed, and a page goes to `archive/` keeping its slug"
type: decision
status: archived
authority: retirement-register-step
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-29
created: 2026-08-29
supersedes: "[[retiring-a-page-removes-its-slug-from-the-authority-register]]"
sources: ["archive/2026-08-29/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md", "authority.md", "scripts/vault-authority.sh"]
tags: [vault, process, harness]
---

# The ruling, 2026-08-29

**owner:** «снимаем это правило, оно мешает и не несет пользы. Страница уходит в архив с о slug и
authority»

**The fourth supersession step of 2026-08-22 is gone.** A page moving into `archive/` keeps its
`authority:` field and keeps its row in `authority.md`. **Nothing removes a row.**

**Rejected: the three options the session put to him** — revert the 239-page move, teach
`scripts/vault-archive.sh` to edit the register, or have the session edit the register once and
record it as a divergence. He took none of them and struck the rule instead.

**It reverses an owner-selected ruling of 2026-08-22**, which is why the page it replaces is retired
rather than corrected ([[retiring-a-page-removes-its-slug-from-the-authority-register]]).

# What it obliges

**`scripts/vault-authority.sh --check` was narrowed the same day.** A register row is stale only when
**no page in `wiki/` or `archive/`** carries the slug; the other direction still asks about `wiki/`
alone ([[a-register-row-is-stale-only-when-no-page-anywhere-carries-the-slug]]).

**A librarian does not remove a row when it retires a page**, and the supersession procedure is three
steps again: write the successor with `supersedes:`, mark the old page `deprecated` with
`superseded_by:`, move it into `archive/`.

**The register agreed with the tree at 507 slugs** after the repeal and after the sweep, which is the
reading that says the two halves are consistent.

# Why the repeal rather than the repair

**The rule deadlocked the work it governed, on the day the sweep first ran.** The sweep moved 239
pages, the register kept 239 rows whose pages had left `wiki/`, `--check` reddened on every one of
them, and `lock-the-librarian.ps1` read the red gate as a refusal to dispatch — locking out the only
party permitted to write `authority.md` ([[the-librarian-lock-hook]],
[[a-lock-on-a-red-tree-hides-the-health-of-what-it-guards]]).

**The obligation was in neither the plan nor the `/pre-task` run against it.** It is a rule the brief
carries under *what must not be broken*, and `/pre-task` answers per item of the plan, so an
obligation the plan does not contain is invisible to it
([[a-plan-touching-the-vaults-own-machinery-enumerates-what-must-not-be-broken-as-items]]).

**His ground is that the rule obstructs and buys nothing.** The register's job is to say **which slugs
answer the same question**, and an archived page still answers its question — what it asserts is
frozen and how it is found is live
([[what-an-archived-page-asserts-is-frozen-and-how-it-is-found-is-live]]). Deleting the row removed
the archived page from the one lookup that could reach it.

# What is left unanswered, deliberately

**An asymmetry was created and not closed.** A row whose page has been archived is no longer stale,
while an archived page is still not required to be grouped in the register
([[the-authority-check-asymmetry-created-by-the-repeal-is-left-standing]]).

**Rows deleted before today are not restored.** Pages retired under the repealed rule had their rows
removed, so asking `archive/` for a group would light up every one of them at once. That is why the
narrowing went into the *stale* direction only.

**Whether `--near`, `--group` and `--list` should reach archived pages is open.** The repeal points
straight at it and the session deliberately did not build it, because widening the cached corpus walk
would change four subcommands at once.

*(Compiled from `raw/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md`.)*
