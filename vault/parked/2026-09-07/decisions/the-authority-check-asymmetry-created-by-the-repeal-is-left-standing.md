---
title: "The `--check` asymmetry created by the repeal is left standing, and named"
type: decision
status: current
authority: authority-check-asymmetry
binding: deferral
basis: human
sprint: S3
decided: 2026-08-29
created: 2026-08-29
sources: ["archive/2026-08-29/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md", "scripts/vault-authority.sh", "authority.md"]
tags: [vault, retrieval, harness]
---

# What was deferred, 2026-08-29

**`bash scripts/vault-authority.sh --check` now asks its two directions over different trees.**

- **Register against tree:** a row is stale only when **no page in `wiki/` or `archive/`** carries the
  slug.
- **Tree against register:** only pages in **`wiki/`** are required to appear in a family.

**So an archived page keeps its row and is never required to have one.** A page archived tomorrow with
no family entry produces no verdict in either direction.

**It was created deliberately in the hour the register step was repealed**, and not closing it was the
call ([[the-authority-register-step-is-repealed-and-an-archived-page-keeps-its-slug]]).

# Why the second direction was not widened with the first

**Rows deleted under the repealed rule are gone.** Every page retired between 2026-08-22 and
2026-08-29 had its row removed while the rule stood, so asking `archive/` for a group would light up
every one of them at once — a hundreds-of-lines red on work that was correct when it was done
([[a-register-row-is-stale-only-when-no-page-anywhere-carries-the-slug]]).

**The narrowing that was needed went into the *stale* direction only**, because that is the direction
the sweep had just reddened.

# What it costs while it stands

**An archived page can fall out of the lookup silently.** It keeps its `authority:` field and its row
if it had one, and nothing notices if it never had one.

**And the lookup itself does not reach `archive/` yet.** Whether `--near`, `--group` and `--list`
should is open and deliberately unbuilt: widening the cached corpus walk changes four subcommands at
once, and none of them was in the day's scope
([[the-day-is-scoped-to-the-optimisation-archiving-and-process-items-of-s3]]).

*(Compiled from `raw/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md`.)*
