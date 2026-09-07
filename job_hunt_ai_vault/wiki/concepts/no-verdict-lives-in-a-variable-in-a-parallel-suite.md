---
title: "No verdict lives in a variable, which is the invariant that makes a parallel suite safe"
type: concept
status: current
authority: parallel-suite-counting
basis: code
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock/handoffs/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock.md", "scripts/vault-check-selftest.sh"]
tags: [testing, harness, process]
---

# The failure this defends against, which the owner named as the worst kind

```sh
pass=$((pass + 1))      # inside a backgrounded subshell
```

**increments a copy.** The parent stays at zero, the suite prints `caught 0, missed 0` and exits 0.
**Faster, green, and checking nothing.**

That is worse than a slow suite and worse than a red one, because both of those are visible. It is
the same class as an instrument that fails towards *nothing to do*
([[an-instrument-that-fails-towards-nothing-to-do]]) and as a measurement wrapper reporting success
about a run that never executed
([[an-assertion-inside-a-measurement-harness-catches-a-broken-instrument]]).

# The invariant

**`report` writes one file per case, and the totals are counted after `wait`.** No verdict is ever
held in a shell variable that a subshell could own a copy of.

# It was proved able to fail, because a green run cannot prove it

Run against a **stubbed gate** — `vault-check.sh` replaced by `echo "VAULT-CHECK: ok"; exit 0`,
through the `SCRIPTS=` handle the script already carried — the suite reported **`caught 46, missed
84` and exited 1**, printed 84 `MISSED` lines each naming its case and carrying wanted-versus-actual
exit codes, and **its arithmetic reconciles**: 45 `CAUGHT` plus 1 `CLEAN` is the 46 it claimed.

**So the counter survived the move out of a variable, the miss path prints, and the exit code is
the score** — which is what
[[a-claim-labelled-measured-came-from-an-instrument-reporting-its-own-exit-code]] requires of this
suite.

**The same run measured the parallel floor**
([[the-parallel-floor-bounds-any-further-speedup]]), which is why it was worth building the stub
rather than reasoning about it.

# The invariant covers the verdict and not the case number — 2026-08-22

**Two cases ran, passed, and were never counted.** They were written as bare `( ... ) &` subshells
calling `report` directly, so **`next_rf` incremented inside the subshell**, the parent's case number
never moved, and the collector iterated past their report files.

**The suite printed `caught 156, missed 0`** — a clean number with two cases missing from it.

**Nothing in the suite would ever have said so.** A dropped case looks exactly like a case that was
never written: there is no file to be absent, no name to be missing, and no arithmetic inside the run
that could disagree with itself. **What found it was arithmetic from outside** — eight cases had been
added and six were reported ([[a-stated-count-drifts-from-the-list-it-heads]],
[[an-instrument-that-fails-towards-nothing-to-do]]).

**The invariant on this page held and was not enough.** No *verdict* lived in a variable; the
**allocator** did. Both are parent state, and a case that allocates its own report file inside a
subshell silently overwrites or orphans it — the same class arriving one field over.

**Repaired by giving them a runner that allocates in the parent**, which is what every other runner
here already does. **The general shape:** a green number is evidence about the cases that ran and
says nothing about the ones that did not
([[a-green-gate-can-be-no-evidence-about-the-branch-just-changed]],
[[a-denominator-is-walked-off-the-input-list]]).
