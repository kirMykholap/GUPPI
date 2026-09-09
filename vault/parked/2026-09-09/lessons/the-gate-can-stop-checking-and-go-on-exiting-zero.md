---
title: "The gate can stop checking and go on exiting zero, and its only symptom reads as a corpus fault"
type: lesson
status: current
authority: gate-silent-pass
basis: measurement
sprint: S3
created: 2026-08-30
sources: ["archive/2026-08-30/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md", "scripts/vault-check.sh", "scripts/vault-check-selftest.sh"]
tags: [vault, testing, harness]
---

# The incident, 2026-08-30

**1.7 KB of comments were added inside the awk program embedded in `scripts/vault-check.sh`, and the
frontmatter pass stopped running.** The program is passed to `xargs` as a single argument; past a
size this machine enforces, `xargs` prints

```
cannot fit single argument within argument list size limit
```

**to stderr and nothing else.** The pass produced no output, every verdict that reads frontmatter
had nothing to judge, and `vault-check.sh` went on **exiting 0**.

**The one visible symptom was all twenty registered tags reported as used on no page** — which reads
as a corpus problem and is not one. Nothing in the output said a pass had not run.

# What green meant while it lasted

**`bash scripts/vault-check-selftest.sh` in that state reported `caught 162, missed 49`.** Forty-nine
red cases passed **by default**, because the verdict that would have caught each of them was never
computed. The suite is a mutation test of the gate and it was mutating a gate that was not looking.

**Three earlier suite runs of that day were thrown away** for the same reason: they had run against a
gate that had silently stopped checking, so their numbers say nothing about anything.

# The headroom, and that nothing measured it

| reading | bytes |
|---|---|
| the program region at `0da5e96`, before this session | 78,516 |
| the program region after this session's edits | 79,149 |
| a size that fails on this machine | 82,425 |

**The exact ceiling is unmeasured and lies between the last two.** The headroom was under four
kilobytes before this session started and no instrument reported it, so every comment written inside
those quotes spends a budget nobody can see.

# What was repaired, and what is owed

**A selftest case now asserts that the gate writes nothing to stderr.** It asserts the channel is
**empty** rather than checking for a list of known messages, so it catches the next tool that fails
this way as well as this one.

**The durable repair is `awk -f`** — the program moves into a file of its own and stops being a shell
argument at all. Ratified and deferred the same day
([[the-awk-program-moves-into-a-file-of-its-own]]).

**And the reasoning that was inside the program was moved outside the quotes**, into a shell comment
above the call. A comment inside the program costs space at a limit; the same comment outside costs
nothing.

# Why nothing in this store described this class

**Every failure mode written down here is about a verdict being wrong, unreachable or too coarse.**
[[a-non-zero-exit-from-the-gate-no-longer-names-one-event]] is about telling exit 1 from exit 2;
[[the-unreachable-verdict-is-dropped-and-replaced]] is about a verdict that cannot fire. **This is the
case where the gate exits 0 and has checked nothing**, and the difference is that both of those are
visible in the output and this one is not.

**The general form**: a check that reports its own failure only on stderr, while its exit code stays
clean, is indistinguishable from a check that passed. **Read the channel, not only the code**
([[a-hook-that-observes-another-tools-run-reads-a-printed-marker-and-not-an-exit-code]]).

*(Compiled from `raw/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md`.)*
