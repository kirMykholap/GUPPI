---
title: "Reverting the code is how you learn whether a test tests anything"
type: lesson
status: archived
authority: revert-to-verify-a-test
basis: code
sprint: S2
created: 2026-08-18
sources: ["archive/2026-08-18/2026-08-18-the-marker-carries-its-type-and-the-gate-was-blind/handoffs/2026-08-18-the-marker-carries-its-type-and-the-gate-was-blind.md", "scripts/vault-check-selftest.sh"]
tags: [testing, harness, vault]
---

# The procedure, and the two cases it proved on 2026-08-18

**Run the new case against the *old* implementation and watch it fail.** Both selftest cases added
this session were proved that way, against the same fixture:

- **the fenced block** — the old injector answered `every rule agrees` while dropping the fence's
  contents ([[a-fenced-block-inside-a-slice-survives-into-the-destination]]);
- **the trailing blank line** — the old comparison answered `every rule agrees` while the region and
  the slice differed by one newline
  ([[a-command-substitution-strips-the-newline-a-gate-compares]]).

**Written from the specification alone, both would have passed with the defect in place.** That is
not a hypothetical: it is the recorded failure of this project's own test-writing
([[a-test-built-from-a-specification-can-pass-without-the-code]],
[[a-test-green-under-any-implementation]]).

# Why the specification is not enough, stated precisely

A specification says what the code should do. **A test written from it asserts the same thing the
code asserts, in the same words, and agrees with it for the same reasons** — including the reasons
that are wrong. The revert is the only cheap instrument that answers a different question: *does
this case distinguish the two worlds?*

**It is cheaper than it sounds.** One `git stash`, one run, one restore — seconds, against a suite
that costs 8m04s to run in full ([[the-selftest-cost-scales-with-the-rule-pages-it-renders]]).
The expensive thing is the case that was never distinguishing.

# Where it sits among the instruments this project already has

| Instrument | The question it answers |
|---|---|
| hand-probe before the suite | does the mechanism do the thing at all ([[hand-probe-a-new-mechanism-before-running-the-suite]]) |
| **revert and re-run** | **does this case notice when it stops** |
| the selftest | do the rules still catch what they were written for |
| `/vault-lint` and a human reading | is any of it *true* ([[a-gate-guarantees-agreement-never-truth]]) |

**A test that fails for its own reasons proves nothing either**
([[a-test-that-fails-for-its-own-reasons-proves-nothing]]) — the revert is what tells the two red
runs apart.

## And say which of the new cases prove nothing — 2026-08-18

**Five selftest cases arrived with the filename half of rule 10. One discriminates.** It reported
MISSED against the old check, which is the only reason the mechanism is known to be new. **The other
four assert absence and pass against the old code too** — they are exemption cases, and the old
check, which never read a filename, also printed nothing for them.

**A suite claiming five new cases prove a new mechanism would be wrong about four of them.** The
honest report names which case carried the proof, and the others are regression guards rather than
evidence. What makes the four unavoidable rather than sloppy is that an advisory exemption cannot be
tested by a clean run at all ([[a-clean-run-cannot-test-an-advisory-exemption]]).
