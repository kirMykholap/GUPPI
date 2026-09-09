---
title: "The selftest works in its own fixture and never reaches into the corpus for a file"
type: decision
status: current
authority: selftest-fixture-source
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-20
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock/handoffs/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock.md", "scripts/vault-check-selftest.sh"]
tags: [testing, harness, vault]
---

# Ruled 2026-08-20 by the owner, and it settles the class rather than the case

**A suite is a test environment, so it works in its own sandbox. Reaching into the working wiki for
a file is wrong on its face.**

**Rejected: making the borrowed file's presence a documented precondition**, which is what the
session first proposed. That keeps the coupling and adds a sentence.

## The case that produced it

Two cases in `scripts/vault-check-selftest.sh` appended into
`$(find "$1/$VAULT_DIR/raw/handoffs" -name '2026-*.md' | sort | head -1)`. **With `raw/handoffs/`
empty that substitution is the empty string**, the redirect prints `: No such file or directory`
and exits 0, the tree is left unmutated, and both cases report MISSED as *the mutation changed
nothing* ([[failing-loudly-with-the-wrong-diagnosis]]).

**So acceptance criterion 5 of the `raw/` migration — "`raw/` is an inbox that is empty between
sessions" — walks straight into breaking the suite that guards the migration**
([[archive-is-dated-by-session-and-holds-what-left-the-working-set]],
[[moving-raw-into-a-dated-archive]]).

## What was built

`raw_fixture` plants its own note in `raw/notes/`. **Not in `raw/handoffs/`**, which would have owed
rule 8 every section of the handoff template and gone red for its own reasons
([[the-journal-gate-hook]]). Suite after the change: `caught 133, missed 0`.

**This is the second time a fixture was found to be a fixture of the corpus rather than of itself**
([[a-fixture-that-renames-what-the-corpus-names-stops-being-a-fixture-of-it]]), which is why the
ruling is written as a class.

## One case the ruling cannot reach — named 2026-08-20

**`lock allows the librarian on a green gate`, in `scripts/hook-selftest.ps1`, runs against the real
tree on purpose.** A lock that refuses unconditionally passes every red case, and only a green tree
tells the two apart; the sandbox vault cannot be green ([[the-librarian-lock-hook]]).

**So the fixture ruling and that case's whole value point in opposite directions**, and the repair
is deferred without a known shape rather than applied
([[the-green-gate-selftest-case-is-deferred-and-the-fixture-repair-cannot-reach-it]]). **On a red
tree it prints `MISSED`, which reads as *the lock is broken*** —
[[failing-loudly-with-the-wrong-diagnosis]], met for the third time.

**This is a boundary on the ruling, not an exception to it.** Every case whose subject is the
suite's own tree is inside the ruling; the one case whose subject is *the tree being green* cannot
be.
