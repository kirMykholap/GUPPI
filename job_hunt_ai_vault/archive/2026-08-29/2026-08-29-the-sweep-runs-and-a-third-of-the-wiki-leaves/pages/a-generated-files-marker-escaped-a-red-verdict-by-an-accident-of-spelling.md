---
title: "A generated file's marker escaped a red verdict by an accident of spelling"
type: lesson
status: archived
authority: marker-net-spelling-accident
basis: measurement
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-19/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery/handoffs/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery.md", "scripts/vault-check.sh", ".claude/rules/ast-boundaries.md"]
tags: [harness, testing, vault]
---

# What was found

**Rule 11 of `vault-check.sh` carries a malformed-marker net**, and the generated file's marker —
`<!-- vault-inject: generated from rule: … - do not edit -->` — **fell through it by luck.**

**The net wants `[a-zA-Z]+` before the colon, and `vault-inject` carries a hyphen.** A marker spelled
`<!-- generated: … -->` would have matched the net's shape, failed its strict reading, and **reddened
the gate on every generated file**.

**The net now recognises the marker by a rule that means it**, rather than by not matching it.

# Why a lucky pass is a defect

**The verdict was correct and the reason was not**, which this store already has a rule for
([[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]]). Nothing would have announced the
change: the day somebody renames the injector, or spells a marker without a hyphen, the gate goes
red on a file that is perfectly correct — and the diagnosis would start at the file rather than at
the net.

**A marker is detected loosely and judged strictly** ([[a-marker-is-detected-loosely-and-judged-strictly]]),
and the whole point of the loose half is that a nearly-right marker is **caught** rather than
ignored. A marker that is legitimate and does not match the loose pattern is the same failure from
the other side: the net has a hole shaped like a spelling.

# The habit

**When a new marker is minted, run it past the net that judges markers** and confirm which branch it
lands in — deliberately, not by observing that the gate stayed green
([[a-new-verdict-is-proved-in-the-real-tree-because-the-check-cannot-see-a-sandbox]]).
