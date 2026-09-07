---
title: "The selftest's sandbox is fixed by making it a faithful mirror, not by pointing the check at its copy"
type: decision
status: current
authority: selftest-sandbox-fidelity
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-19
created: 2026-08-19
sources: ["archive/2026-08-19/2026-08-19-the-gate-checked-itself-against-a-decoy-and-the-guard-objection-fell/handoffs/2026-08-19-the-gate-checked-itself-against-a-decoy-and-the-guard-objection-fell.md", "scripts/vault-check-selftest.sh"]
tags: [testing, harness, vault]
---

# The fork, 2026-08-19

The sandbox copied the vault to `vault_copy`, and that rename is what broke the suite
([[a-fixture-that-renames-what-the-corpus-names-stops-being-a-fixture-of-it]]). Two repairs were
available.

**Taken: make the sandbox mirror the repository**, copying the vault under the name it has.

**Rejected: export `VAULT=` for every case except the two rename cases** — five lines against roughly
seventy. *Why:* it removes the ambiguity by **stopping the suite exercising discovery in all but two
of its cases**, which is working around a sandbox that is not a faithful mirror instead of making it
one. Discovery is a thing the check does on every real run, and a suite that stubs it out has
narrowed what it proves in order to go green.

# What it obliges

**The sandbox is a mirror, so anything the corpus names by name resolves in it.** That is the property
the repair buys, and it is the one to check the next time a fixture is written: **the sandbox's job is
to be the repository, and every deviation from that is an assertion nobody wrote down.**

**Discovery keeps the two cases it already had** — `a vault with spaces` and `the vault is renamed` —
so the mirror does not cost the coverage the rejected option was meant to preserve.

**The ordering fix is kept on its own merits** and is not part of this decision
([[a-destination-that-is-also-a-citation-loses-to-whichever-loop-runs-first]]). It was published first
as *the* cause and was not one
([[the-first-published-diagnosis-can-be-a-real-defect-and-still-not-the-cause]]).
