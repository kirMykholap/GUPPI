---
title: "The vault's directory name is the owner's to change, so nothing may depend on it"
type: entity
status: current
authority: vault-location
basis: code
sprint: S0
created: 2026-08-13
sources: ["archive/2026-08-13/2026-08-13-second-brain-phase-1/handoffs/2026-08-13-second-brain-phase-1.md", "scripts/vault-check.sh", ".claude/hooks/vault-path.ps1", "archive/2026-08-19/2026-08-19-the-gate-checked-itself-against-a-decoy-and-the-guard-objection-fell/handoffs/2026-08-19-the-gate-checked-itself-against-a-decoy-and-the-guard-objection-fell.md"]
tags: [vault, process]
---

# The vault directory

It sits at the repository root, is entirely tracked by git, and on 2026-08-13 it is
`job_hunt_ai_vault/`. **It was renamed four times in the session that created it.**

That is not indecision to be tolerated — it is the fact to design around. **Obsidian displays the
folder name**, so the name is product surface for the one person who reads it, and it is his to
choose.

## The consequences, all three of which have already bitten

- **No script and no page may hard-code the name.** The discovery idiom is "the top-level
  directory that contains a `wiki/`", and it is written this way in all three shell scripts:

  ```bash
  VAULT=$(find . -maxdepth 2 -type d -name wiki -not -path './.*' 2>/dev/null \
          | sed 's|/wiki$||; s|^\./||' | sort | head -1)
  ```

  **Both details are load-bearing, and the page carried an older shape until 2026-08-13.**
  `-not -path './.*'` excludes *every* dot-directory, not only `./.git/*` — a `wiki/` under any of
  them would otherwise be a candidate. And `sort` before `head -1` is what makes the answer
  deterministic and, more importantly, **the same answer that `.claude/hooks/vault-path.ps1`
  gives**: the PowerShell side is `Get-ChildItem | Sort-Object Name | Select-Object -First 1`, and
  the two used to differ — `Get-ChildItem` skips hidden directories and sorts, `find | head -1`
  did neither. With two candidate directories present they picked different vaults, and the hook
  would have printed a brief from one while every script read the other. **Copy this version, not
  a shorter one.**

- **The current name contains a space**, so every path in every command must be quoted. An
  unquoted `$(find ...)` split it into three words, every read failed, and `vault-check.sh`
  printed `VAULT-CHECK: ok` having examined nothing.
- **A path inside the vault is cited relative to the vault**, never to the repository root.
  Seventeen pages went on citing a stale prefix after a rename, and nothing noticed until a rule
  was added for it. See [[vault-scripts]].

## Also true of this directory

`.obsidian/` is in `.gitignore` — the workspace layout is not knowledge, and it changes on every
pane the owner drags. The rest of the vault, `raw/` and `archive/` included, is tracked, because
git is the audit log that makes unattended writing reviewable ([[the-librarian-writes-unattended]]).

## The name is fixed from 2026-08-17, and one field may now depend on it

**owner, 2026-08-17: the vault directory's name is fixed from now on** — renaming it was setup, and
setup is over. On that basis **`governs:` on a rule page is written as a path from the repository
root**, which means a rule governing a file inside the vault names this directory
([[governs-is-a-path-from-the-repository-root]]).

**The constraint above is retired for that field and for nothing else.** Every script named on this
page **goes on discovering the vault dynamically**, in the idiom quoted above, unchanged —
`vault-check.sh`, `vault-catalogue.sh`, `scripts/vault-inject.sh` (which appeared the same day) and
`.claude/hooks/vault-path.ps1`. Nobody may read *the name is fixed* as permission to delete
discovery: the name being stable is a statement about the owner's intentions, and discovery is what
makes a rename survivable if those change.

**One consequence is already scheduled.** The selftest case «the vault is renamed» is green today
and will go red the first time a rule governs a file inside the vault. It is a decision to retire,
not a bug to fix, and it sits on the register with its consequence
([[what-the-harness-build-waits-on]]).

*(This page was treated as a settled fact rather than as a question for the owner, and that cost a
mechanism designed, argued and thrown away the same afternoon —
[[a-vault-page-is-a-question-to-the-owner-not-a-settled-fact]]. The discovery block now stands in
four identical copies, which is itself worth re-reading:
[[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]].)*

## The corpus does depend on the name, eleven times, and nothing had recorded it — 2026-08-19

**The first consequence above says no script and no page may hard-code the name. Nine pages do**, in
`sources:`, and there are **eleven such citations**
([[the-corpus-names-the-vault-directory-and-a-rename-is-a-rewrite]]).

They are not a violation of anything decided — a `sources:` path from the repository root into the vault
**has no other spelling**, and the owner fixed the name on 2026-08-17. What is new is that the dependency
is now written down, so *the name is the owner's to change* carries its price beside it: a `sed` sweep
over eleven pages and a gate run, with rule 5b as the detector
([[a-page-rename-is-sed-and-verify]], [[a-rewriter-must-be-paired-with-a-detector]]).

**It was found by a fixture rather than by a rename.** The selftest's sandbox renamed the vault, those
eleven citations stopped resolving, and the placeholder loop materialised one of them into a directory
holding a `wiki/` — **a decoy that the discovery idiom quoted above then found and preferred**, because
it sorts before `vault_copy` ([[a-fixture-that-renames-what-the-corpus-names-stops-being-a-fixture-of-it]]).

**Discovery itself came out of it proved rather than doubted.** The same run found `a vault with spaces`
and named it in every message, which is the half the case exists for
([[the-renamed-vault-case-is-graded-on-the-question-it-asks]]).

## `wiki/` became a third smaller in one operation — 2026-08-29

**The first archiving sweep moved 239 pages out.** `wiki/` holds **523** pages where it held 762:
`decisions/` 341 to 276, `lessons/` 182 to 12, `proposals/` 49 to 45. `entities/`, `concepts/` and
`rules/` have no archival criterion and were untouched
([[the-sweep-runs-for-real-over-every-criterion-and-records-what-it-moved]],
[[entities-and-concepts-get-no-archival-criterion-today]]).

**They are in `archive/2026-08-29/2026-08-29-the-first-sweep/pages/`, each carrying
`status: archived`.** Nothing was deleted, and `[[wikilinks]]` into them still resolve — the link
check resolves against `wiki/` and `archive/` alike.

**What this changes for a reader:** a page named as a source or a successor by an older page may now
live in `archive/`, and that is expected rather than a fault. **`archive/` is history and `wiki/` is
the source of truth**, so a claim that is still live is reached through the page that carries it here
([[what-an-archived-page-asserts-is-frozen-and-how-it-is-found-is-live]]).

**What it does not change:** the register. An archived page keeps its `authority:` slug and its row,
by the repeal of 2026-08-29 — the register agreed with the tree at **507 slugs** after the move
([[the-authority-register-step-is-repealed-and-an-archived-page-keeps-its-slug]]).

**What it costs, measured:** the gate is green at **24 s**, against 23 s before, so the gate did not
get cheaper in any reading anyone has. The suite read **29m12s at 194 cases** against 34m08s at 178
cases five days earlier — sixteen more cases and five fewer minutes — which is suggestive and is not a
controlled experiment.

*(Compiled from `raw/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md`.)*

# The archive folder named in the section above no longer exists — 2026-08-29

> [!CAUTION] `archive/2026-08-29/2026-08-29-the-first-sweep/pages/` IS NOT A PATH IN THIS TREE
> **The 239 pages are in
> `archive/2026-08-29/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves/pages/`**, beside the
> journal that produced them, which is the folder the prohibition of 2026-08-19 requires
> ([[the-archive-gains-a-folder-per-session-inside-the-date]]). The move was 239 `git mv`s and one
> `sources:` rewrite, done before the commit; **the sentence above is the prose mention it did not
> reach**, and it is corrected here rather than in place.

**And the page counts above are a reading of one hour.** `wiki/` held **523** when that section was
written and holds **556** now — `decisions/` 295, `concepts/` 138, `proposals/` 46, `entities/` 43,
`lessons/` 18, `rules/` 16 — the difference being the pages the ingest of that same evening wrote after
the sweep. **Both numbers are true of different minutes of 2026-08-29**, which is what a count in prose
does; the folder breakdown is printed by `bash scripts/vault-catalogue.sh` and needs no copy here.

*(Compiled from `raw/handoffs/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds.md`.)*
