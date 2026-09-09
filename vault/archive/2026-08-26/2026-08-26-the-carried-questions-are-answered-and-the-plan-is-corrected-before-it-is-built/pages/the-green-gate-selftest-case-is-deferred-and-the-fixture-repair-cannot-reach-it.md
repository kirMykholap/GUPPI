---
title: "The green-gate selftest case is deferred, and the ruled fixture repair cannot reach it"
type: decision
status: deprecated
authority: green-tree-case-deferral
basis: human
binding: deferral
sprint: S2
decided: 2026-08-20
created: 2026-08-20
superseded_by: "[[the-green-gate-selftest-case-is-thrown-out-rather-than-deferred-again]]"
sources: ["archive/2026-08-20/2026-08-20-the-lock-fires-and-deadlocks-the-vaults-only-writer/handoffs/2026-08-20-the-lock-fires-and-deadlocks-the-vaults-only-writer.md", "scripts/hook-selftest.ps1"]
tags: [testing, harness, vault]
---

# Deferred 2026-08-20, and it is the deferral with no known repair

**The case:** `lock allows the librarian on a green gate`, in `scripts/hook-selftest.ps1`. **With
the real tree red it prints `MISSED`**, which reads as *the lock is broken* when the truth is *the
tree is red* ([[failing-loudly-with-the-wrong-diagnosis]]).

**It ran that way in anger this session**, because the owner's file move made the tree red for a
real reason.

## Why the ruled repair cannot simply be applied

**The repair for the sibling cases is a fixture** — a suite works in its own sandbox and never
borrows a file from the corpus ([[the-selftest-works-in-its-own-fixture-and-never-in-the-corpus]]).

**This case's entire value is that it does *not* run in a fixture.** A lock that refuses
unconditionally passes every red case and is worse than no lock; only a green tree tells the two
apart, and the sandbox vault cannot be green ([[the-librarian-lock-hook]]).

**So the repair and the case's purpose point in opposite directions**, which is what makes this a
deferral of a different kind from the others recorded the same day: **there is no known repair
shape**, not merely an unspent one.

**Rejected: applying the fixture ruling anyway**, which would delete the only case that can tell a
working lock from a lock that refuses everything.

## The consequence of not doing it

**The next person to run the suite on a red tree reads a broken lock.** The diagnosis leads away
from the cause, which is the specific harm this store has already named
([[failing-loudly-with-the-wrong-diagnosis]]) — and the case reports `MISSED` while the count reads
`70 caught, 0 missed` on a green tree, so nothing in the summary line distinguishes the two states.
