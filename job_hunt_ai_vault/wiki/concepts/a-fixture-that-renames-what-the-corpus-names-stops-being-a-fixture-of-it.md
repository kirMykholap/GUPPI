---
title: "A fixture that renames what the corpus names by name stops being a fixture of that corpus"
type: concept
status: current
authority: fixture-renames-its-subject
basis: code
sprint: S2
created: 2026-08-19
sources: ["archive/2026-08-19/2026-08-19-the-gate-checked-itself-against-a-decoy-and-the-guard-objection-fell/handoffs/2026-08-19-the-gate-checked-itself-against-a-decoy-and-the-guard-objection-fell.md", "scripts/vault-check-selftest.sh"]
tags: [testing, harness, vault]
---

# The mechanism, in the order it ran

`scripts/vault-check-selftest.sh` built its pristine sandbox with
`cp -r "$REPO/$VAULT_DIR" "$PRISTINE/vault_copy"` — a sandbox **whose whole job is to be the
repository**, with the vault under a different name.

1. **The corpus cites paths from the repository root**, and eleven of those citations point inside the
   vault itself ([[the-corpus-names-the-vault-directory-and-a-rename-is-a-rewrite]]).
2. Under the renamed copy **none of them resolved**, so the `sources:` placeholder loop did what it is
   for and materialised them — including `job_hunt_ai_vault/wiki/decisions/_schema.yaml`, as an empty
   file.
3. **A directory holding a `wiki/` is the whole of what vault discovery looks for**
   ([[the-vault-directory]]). The placeholder tree had just become one.
4. The decoy **sorted before `vault_copy`** — discovery takes `sort | head -1` — and won every case.

**Reading: `caught 24, missed 96`**, against `caught 120, missed 0` six commits earlier.

# Why it is worse than an ordinary broken fixture

**The failure is silent and it runs in the direction of the sandbox looking fine.** Everything the
decoy breaks is reported as an **ordinary red on the case under test** — `CLAUDE.md:65` *"not a marker
alone on its line"*, `marked regions cover 0 of 14` — so a reader attributes each one to the mutation
the case just made. There is no line anywhere saying *the check examined the wrong directory*.

**And it does not arrive with the fixture.** It arrived when the corpus first cited a path inside the
vault, which happened in an unrelated ingest on 2026-08-19 and was invisible to everyone involved.
That is the general shape: **a fixture is written against the corpus of the day it is written**
([[a-fixture-must-materialise-what-the-subject-reads]]).

# The invariant

**A sandbox that is supposed to be the repository must be the repository, name for name.** Anything it
renames is an assertion that nothing depends on that name — an assertion nobody wrote down, nothing
checks, and the corpus is free to falsify at any time by citing it.

**The repair is to stop renaming, not to redirect the subject at the copy**
([[the-selftest-sandbox-is-a-mirror-rather-than-a-renamed-copy]]). Pointing the check at the copy with
`VAULT=` would have restored the green by removing discovery from 118 of 120 cases.

**Readings, in order, all 2026-08-19:** `24/96` with the schemas as committed, the baseline;
**`86/34`** with the `governs:` loop moved ahead of the placeholder loop
([[a-destination-that-is-also-a-citation-loses-to-whichever-loop-runs-first]]); **`119/1`** with the
sandbox mirroring the repository's vault directory name. The remaining one is
[[the-renamed-vault-case-is-graded-on-the-question-it-asks]] and is a corpus finding rather than a
suite defect.
