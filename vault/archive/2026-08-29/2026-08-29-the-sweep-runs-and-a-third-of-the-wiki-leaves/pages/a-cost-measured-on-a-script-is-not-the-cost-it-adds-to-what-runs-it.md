---
title: "A cost measured on a script is not the cost it adds to the thing that runs it"
type: lesson
status: archived
authority: delegated-cost-measurement
basis: measurement
sprint: S3
created: 2026-08-26
sources: ["archive/2026-08-26/2026-08-26-the-harness-half-is-built-and-the-owner-rules-how-the-vault-empties-itself/handoffs/2026-08-26-the-harness-half-is-built-and-the-owner-rules-how-the-vault-empties-itself.md", "scripts/vault-check.sh", "scripts/vault-measure.py"]
tags: [harness, testing, vault]
---

# The two readings, 2026-08-26

**`uv run python scripts/vault-measure.py --check` alone: 0.124 s.**

**The delta it adds to `bash scripts/vault-check.sh`: 0.28 s** — three runs each way, with it
20.20 / 20.44 / 20.46 s and without it 19.92 / 20.13 / 20.25 s.

**More than double**, because the standalone figure omits the interpreter search and the process the
gate spawns. **The smaller figure had already been written into the file as the answer** before the
gate was ever timed.

# What the number was used for, and how far the estimate was out

**The owner was asked to accept "roughly four minutes" over the suite**, extrapolated from rule 13's
1.5 s. **The measured cost is about 50 seconds** over the suite's roughly 171 gate runs — the
estimate was eight times too high, in the direction that asks for permission the work did not need
([[the-gate-rule-is-built-before-the-scanner-exclusion-and-the-cost-is-accepted]]).

# The rule this leaves

**Measure a delegated cost inside its caller, with a control, or do not quote it.** Timing the
delegate alone answers a different question — what the process costs once it exists — and the caller
pays for creating it.

**And a control run is what separates the change from the machine**: the same session read the gate
at 20.2 s against the 15.3 s the corpus records, **measured without rule 15 as well**, so the drift
belongs to the machine and not to the change ([[a-control-nothing-touched-separates-a-change-from-the-machine]],
[[the-suite-gets-a-scanner-exclusion-before-a-narrowed-gate]]).
