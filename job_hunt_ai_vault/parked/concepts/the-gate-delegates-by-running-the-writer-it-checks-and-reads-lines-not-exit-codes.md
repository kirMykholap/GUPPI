---
title: "The gate delegates by running the writer it checks, and reads its lines rather than its exit code"
type: concept
status: current
authority: gate-delegation-reading
basis: code
sprint: S3
created: 2026-08-26
sources: ["archive/2026-08-26/2026-08-26-the-harness-half-is-built-and-the-owner-rules-how-the-vault-empties-itself/handoffs/2026-08-26-the-harness-half-is-built-and-the-owner-rules-how-the-vault-empties-itself.md", "scripts/vault-check.sh", "scripts/vault-measure.py"]
tags: [vault, harness, testing]
---

# One shape, three rules

**Rules 12, 13 and 15 of `scripts/vault-check.sh` all ask their question by running the script that
owns the thing they check** — the injector, the authority tool, and from 2026-08-26
`scripts/vault-measure.py`. Each shares the same three moves: a `missing file:` note when the script
is absent, a good sentence that is discarded, and every other line becoming a note.

**Rule 15 appeared on 2026-08-26** and asks `vault-measure.py --check`. Its number is 15 and not 14
even though 14 is due for retirement, because a retired rule number is never reused
([[a-retired-rule-number-is-never-reused]], [[the-alphabet-test-behind-the-owner-block-advisory-is-overturned]]).

# Why the lines and not the exit code

**The exit codes fork across this repository's own scripts.** `vault-measure.py` follows
`scripts/vault-archive.sh` in using exit 2 for a **refusal** and also for a **usage error**, while
the gate, catalogue, coverage and authority scripts use 2 for a usage error alone.

**The fork is real, so a rule that read the code would be tied to whichever side a later change
lands on.** Reading lines makes the rule depend on what the script *says*, which is the part its own
selftest pins, rather than on a convention two halves of the repository do not share
([[an-exit-code-read-through-a-pipe-belongs-to-the-last-stage]]).

# What this costs, measured in the gate rather than on the script

**0.28 s per gate run**, three runs each way on 2026-08-26: with rule 15, 20.20 / 20.44 / 20.46 s;
without it, 19.92 / 20.13 / 20.25 s. Over the suite's roughly 171 gate runs that is about
**50 seconds**, against the four minutes estimated beforehand from rule 13's 1.5 s.

**The script timed alone reads 0.124 s and understates the delta by more than half**, because it
omits the interpreter search and the process the gate spawns
([[a-cost-measured-on-a-script-is-not-the-cost-it-adds-to-what-runs-it]]).

# Where a measure region is reached from, and where it is not

**Rule 11 walks the harness sweep alone** — both `CLAUDE.md` files and every markdown file under
`.claude/` — and it learned to recognise a measure marker on 2026-08-26. **So a measure region
inside a `wiki/` page is reached by rule 15 and by nothing else.** The two rules do not overlap and
neither covers the other's population.
