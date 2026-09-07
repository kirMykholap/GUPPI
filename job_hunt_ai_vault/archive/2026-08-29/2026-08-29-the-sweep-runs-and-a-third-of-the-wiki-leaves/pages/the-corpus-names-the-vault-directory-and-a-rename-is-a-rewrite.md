---
title: "The corpus cites the vault by its literal directory name, so renaming it is a rewrite and nothing had recorded that"
type: lesson
status: archived
authority: vault-name-citations
basis: measurement
sprint: S2
created: 2026-08-19
sources: ["archive/2026-08-19/2026-08-19-the-gate-checked-itself-against-a-decoy-and-the-guard-objection-fell/handoffs/2026-08-19-the-gate-checked-itself-against-a-decoy-and-the-guard-objection-fell.md", "scripts/vault-check-selftest.sh"]
tags: [vault, retrieval, testing]
---

# Measured 2026-08-19, and it was surfaced by a fixture rather than by a rename

**Eleven citations in the corpus spell the vault's directory name.** They are `sources:` entries written
as paths from the repository root, and they point **inside the vault itself**:

| where | how many |
|---|---|
| `job_hunt_ai_vault/CLAUDE.md` | six |
| `job_hunt_ai_vault/wiki/decisions/_schema.yaml` | two |
| `sprint.md`, `index.md`, `pages.base`, one each | three |

Spread over eleven pages, one citation each. *(The journal this is compiled from says nine; measured at
`bade6c9`, `git grep -l '^sources:.*job_hunt_ai_vault/'` over `wiki/` and `archive/` returns eleven
files and the per-destination breakdown above reproduces exactly. The page count is corrected here
rather than compiled.)* **The check prints them the moment the name stops matching** — with the sandbox
no longer renaming the vault, `run_clean "the vault is renamed"` fails and prints eleven lines of
`sources names a path that does not exist: job_hunt_ai_vault/...`
([[the-renamed-vault-case-is-graded-on-the-question-it-asks]]).

# What this does and does not contradict

**Discovery is name-independent and space-safe, and that half is proved in the same output**: the check
found `a vault with spaces` and named it in every message ([[the-vault-directory]]).

**What is not free is the corpus.** The owner fixed the directory's name on 2026-08-17 and licensed
`governs:` to depend on it; **`sources:` was never licensed and depends on it anyway**, because a path
from the repository root into the vault has no other spelling. So the constraint *nothing may depend on
the name* is false of the corpus today, and was false before anyone decided anything about it.

**It was green on placeholders and not on truth**: under the old `vault_copy` rename, those citations
resolved against empty files the sandbox itself had created
([[a-test-can-be-green-on-placeholders-its-own-setup-created]]).

# The class it belongs to

**This is [[moving-raw-into-a-dated-archive]] again at a smaller size** — 115 of 124 pages cite `raw/`
there, eleven citations here — and it belongs beside [[a-rewriter-must-be-paired-with-a-detector]]: a
rename that moves an address needs a rewriter, and a rewriter needs a detector that says whether it
finished.

**The detector already exists for this one.** Rule 5b prints every unresolved `sources:` path, so the
sweep is `sed` plus a gate run, and the cost is known rather than estimated
([[a-page-rename-is-sed-and-verify]]).

**What the vault gains from writing it down is that the rename stops being free.** Nothing had recorded
it, so the next person to act on *the name is the owner's to change* would have discovered it from a red
gate.
