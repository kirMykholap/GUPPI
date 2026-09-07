---
title: "A schema obligation is applied to the suite's own fixtures in the same change that mints it"
type: proposal
status: current
authority: fixture-conformance-sweep
basis: code
sprint: S3
created: 2026-08-30
sources: ["job_hunt_ai_vault/raw/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md", "scripts/vault-check-selftest.sh", "job_hunt_ai_vault/wiki/decisions/_schema.yaml"]
tags: [testing, vault, harness]
---

# What it would be

**Two cheap checks over `scripts/vault-check-selftest.sh`, both run as part of minting an obligation
rather than after the suite goes red.**

1. **A fixture-conformance grep.** When a field or a section becomes required for some `type:` or
   `target_kind:`, grep the suite for every fixture carrying that value and confirm each satisfies
   the new obligation. One grep, before the change is committed.
2. **A positional-dependency ban in fixtures.** No case appends to the end of a file and then asserts
   about what is last in it. A fixture that needs a line in a block inserts it under that block's
   heading.

# The two incidents

**A fixture pinned to the end of the file expired when a block was added below it.**
`lc_key_not_allowed` appended its line to the end of `wiki/decisions/_schema.yaml` and depended on
`required_from:` being the last block. A block added below took the line. **The case stopped testing
its subject without going red**: it reported the wrong reason, and the suite still called it a miss
only because the message did not match. Repaired by inserting under the heading.

**A new obligatory section reddened the suite's own fixtures and nobody looked.** Making
`# The rule text` mandatory for `target_kind: rule` broke one of the two fixtures in the suite
carrying that value. **The check that would have found it costs one grep and was not run.**

# The group they make

**Both are the suite failing as a corpus rather than as a set of assertions.** A fixture is a tiny
store this project would refuse, and a rule reaching into it says something true about the store
rather than something incidental ([[a-rule-over-every-page-makes-every-test-fragile]], wave two).
**One expires silently and one reddens; neither is caught by reading the assertions.**

# What the store already says, and what is added

**[[a-rule-with-no-instrument-behind-it-is-a-rule-a-fixture-can-violate-for-a-week]] says the first
instrument for a rule should be expected to go red, and that when it does the fixture is the suspect
before the check is.** That is the right disposition and it is a disposition — it tells a reader what
to think once the suite is already red.

**What is added is the moment and the cost.** The grep runs when the obligation is minted, before
anything is red, and it costs one command. The page above says *expect red*; this says *the red is
avoidable and here is what avoids it*.

**And the positional half is not on that page at all.** A fixture depending on file order is not a
missing instrument — it is a fixture that will silently stop being about its subject, which is the
class [[a-test-can-be-green-on-placeholders-its-own-setup-created]] names for a different cause.

# What it would take

- The grep, written into whatever performs a schema change — the ritual, not a reviewer's memory.
- One pass over the existing fixtures for end-of-file appends, and a repair for each.
- A selftest case is **not** obviously the right instrument here: the subject is the suite itself, and
  a case about the suite inside the suite is the shape this store has already been burned by
  ([[a-selftest-case-can-pin-the-announcement-while-the-thing-it-announces-is-broken]]).

# What is open

- **Where the grep lives.** A schema change is the session's to make, so this cannot live in the
  librarian's ritual ([[what-the-gate-reads-as-its-own-input-is-the-sessions-to-write]]).
- **Whether the positional ban is checkable at all**, or is a convention with a review behind it. A
  fixture that appends is not syntactically distinct from one that inserts.
- **How many fixtures carry a positional dependency today.** Unmeasured, and the number decides
  whether this is a sweep or a note.

# What it would oblige

**Minting an obligation acquires a step.** It is one grep and it is paid at the moment the obligation
is decided, which is the moment somebody already has the field's meaning in front of them.
