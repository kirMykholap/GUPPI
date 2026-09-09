---
title: "Measure before optimising, and count the right thing: the cost was processes per page, not pages"
type: lesson
status: archived
authority: injector-cost-model
basis: measurement
sprint: S2
created: 2026-08-18
sources: ["archive/2026-08-18/2026-08-18-the-marker-carries-its-type-and-the-gate-was-blind/handoffs/2026-08-18-the-marker-carries-its-type-and-the-gate-was-blind.md", "scripts/vault-inject.sh"]
tags: [harness, testing, vault]
---

# What was expected, and what was measured

**Expected:** widening the injector's walk from 9 pages to 258 would dominate the cost, and the
deferred `awk` rewrite was its precondition.

**Measured 2026-08-18 on this machine, three runs each:**

| Run | Wide walk | Old `wiki/rules/` walk |
|---|---|---|
| `vault-inject.sh --check` | **1837 ms** | **1898 ms** |
| `vault-check.sh` | **5258 ms** | **5168 ms** |

**The wider walk came out faster than the narrow one.** The old figure reproduces the 1.98 s already
on the record, so the two measurements are comparable
([[the-selftest-cost-scales-with-the-rule-pages-it-renders]]).

**The pre-filter costs 113 ms** — `grep -l '^governs:'` over the whole glob — and the real cost was
never the page count at all.

# Where the time actually was

**A first draft that used `basename`, `dirname` and `sed` per page spent 1.48 s of 2.28 s on process
spawns alone — about 40 ms per process on this platform.** Parameter expansion removed all of it.

> **The thing to count when this loop gets slower is PROCESSES PER PAGE, not pages.**

**What this revises:** the deferred *"one `awk` pass over all rule pages instead of two processes
each"* is still worth having ([[what-the-harness-build-waits-on]]) — but it was filed as a
precondition for the wider walk, and it was not one. The two are independent, and the reason the
`awk` idea helps is the same reason measured here: it removes processes.

# Why the wrong unit was chosen in the first place

**Pages are the visible quantity.** The walk is written as a loop over pages, the change was
described as "9 to 258", and 28× is a number that sounds like an answer. Processes per page is
invisible in the source — it is a property of what each iteration *calls*, not of what it iterates
over.

**This is the same shape as a count that names the wrong set**
([[a-stated-count-drifts-from-the-list-it-heads]],
[[the-evidence-was-not-wrong-the-instrument-was-too-coarse]]): the arithmetic was right and the
denominator was not the one that governed the cost. **Measurement settled what argument could not**,
again ([[measurement-settled-what-argument-could-not]]).

# Two numbers from the same session, and why both are on the record

The selftest ran **106 caught, 0 missed** mid-session and **107, 0** at the end, up from 99. **Wall
clock was not timed**, so the 8m04s figure stands unrevised rather than being restated from memory —
a number is re-measured or it is left alone ([[an-unsourced-number-is-dropped-not-chosen]]).

# The per-spawn figure was re-measured on 2026-08-24, and the old one is in a comment that reasons from it

**A process spawn costs about 19 ms here, not the 40 ms written into `scripts/vault-inject.sh` on
2026-08-18.** Read off a paired change: five spawns per page were removed across sixteen selected
pages — eighty spawns — and the first reading returned 1.55 s.

**The unit is still the right one.** What moved is the constant, and this page's whole argument is
that the constant belongs to the platform rather than to the work: it was measured once, written
into a comment, and reasoned from for six days.

**Where the rest of the injector's saving came from**: `status:` and `render:` are now read in one
`awk` pass instead of one `awk` plus a `sed | head | sed`, and `governs_targets()` lost the
`sed | head -1 |` in front of its `awk` for an anchored match that exits early. **The parser's four
rules were not retyped** — only the plumbing in front of them moved, because that function is the
second of three readers of `governs:` in the repository.

**The paired reading: the injector went from 6.19/6.26/6.34 s to 3.45–3.71 s, and the gate from
17.2 s to 15.3 s** ([[a-control-nothing-touched-separates-a-change-from-the-machine]]).
