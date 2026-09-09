---
title: "A test can be green on placeholders rather than on truth, and the placeholders can be its own setup's"
type: lesson
status: current
authority: green-on-own-placeholders
basis: measurement
sprint: S2
created: 2026-08-19
sources: ["archive/2026-08-19/2026-08-19-the-gate-checked-itself-against-a-decoy-and-the-guard-objection-fell/handoffs/2026-08-19-the-gate-checked-itself-against-a-decoy-and-the-guard-objection-fell.md", "scripts/vault-check-selftest.sh"]
tags: [testing, harness, vault]
---

# The incident

**`run_clean "the vault is renamed"` passed for six days on nothing.** The sandbox renamed the vault to
`vault_copy`, so the eleven citations spelling `job_hunt_ai_vault/...` did not resolve — and the
`sources:` placeholder loop **created empty files at exactly those paths**. The case then asserted that
the check reports nothing, and the check reported nothing, because every path it was asked about had
just been conjured.

**Removing the rename removed the placeholders and the case failed on a true statement about the
corpus** ([[the-corpus-names-the-vault-directory-and-a-rename-is-a-rewrite]]).

# Why the ordinary defences do not see it

**The case is green, so nothing prints.** `/lint` reads output; a reviewer reads a diff; a coverage
report reads a denominator. None of them has a question shaped like *is this green load-bearing*
([[a-case-that-passes-before-the-change-tests-nothing]] is the discipline that would have, and it is
applied to **new** cases rather than to a case that has been passing).

**The placeholder loop is correct and so is the case.** Neither is a defect on its own; the green comes
from the two interacting through a third thing — the rename — that neither of them mentions.

**And the setup is the party with motive.** A fixture exists to make the subject runnable, so it fills
in whatever is missing. **Filling in what is missing is indistinguishable from fabricating the evidence**
when the subject's question is *does this path exist*
([[a-fixture-must-materialise-what-the-subject-reads]]).

# The check to make

**Ask what the setup created, and whether the assertion is about one of those things.** For a suite that
materialises paths from the corpus, every path-existence assertion is suspect by construction.

**Reverting the mutation is not enough here**
([[reverting-the-code-tells-you-whether-a-test-tests-anything]]): the case passes with and without the
mutation, and it passes for the wrong reason in both. What discriminates is removing **the setup's own
convenience**, which is what the mirror repair did
([[the-selftest-sandbox-is-a-mirror-rather-than-a-renamed-copy]]).
