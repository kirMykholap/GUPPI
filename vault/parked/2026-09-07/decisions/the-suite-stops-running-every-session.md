---
title: "The suite stops running every session, and runs at a sprint's close or in a rare case"
type: decision
status: current
authority: retro-suite-launch
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-26
created: 2026-08-26
supersedes: "[[the-selftest-suite-runs-in-the-background-while-the-retro-proceeds]]"
sources: ["archive/2026-08-26/2026-08-26-the-gate-hangs-on-a-store-stub-and-the-checks-get-their-names/handoffs/2026-08-26-the-gate-hangs-on-a-store-stub-and-the-checks-get-their-names.md", ".claude/skills/retro/SKILL.md", "scripts/vault-check-selftest.sh"]
tags: [testing, harness, process]
---

# The ruling, 2026-08-26, in his own words

> **owner:** «Перестаем постоянно использовать. Как и говорили ранее - только в очень редких случаях
> или при закрытии спринта.»

**The full selftest suite comes out of the per-session loop.** It runs at a sprint's close, or in a
rare case somebody names.

**This replaces the permanent step-0 launch decided earlier the same day**
([[the-selftest-suite-runs-in-the-background-while-the-retro-proceeds]]). That decision was about
*not serialising the suite against the retro conversation*, which was right; what it assumed is that
the suite runs every session at all.

# The cadence now agrees with the criterion instead of fighting it

**Criterion 1 of S3 is read off `missed 0`, and a criterion is read at a sprint's close** — which is
exactly when the full run now happens. The arrangement it replaces produced a number every session
and read it at the close.

# The evidence against the every-session run is the day it was overturned

**The suite ran 56 minutes without finishing and was killed.** Its number was never read. **The one
thing it accomplished was starving the gate that `/handoff` must run**, which cost an hour of
diagnosis pointed at the wrong cause
([[a-trace-answered-in-ninety-seconds-what-an-hour-of-process-archaeology-did-not]]).

# What it leaves without cover, and it is named

**Between sprint closes nothing mechanical checks the gate's rules**, until the smoke runner exists
([[the-smoke-runner-is-built-first-thing-next-session]]). **The rule 15 repair of this same day landed
with no selftest case**, and the suite that would carry it now runs once a sprint
([[a-defect-one-day-old-outlived-the-selftest-that-shipped-with-it]]).

# Rejected

**Rejected: keeping the every-session run.** The reading above is what it produced on the day it was
decided.
