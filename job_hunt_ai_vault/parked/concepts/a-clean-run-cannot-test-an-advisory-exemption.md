---
title: "A clean-run assertion cannot test an advisory exemption, so the absent-case is the instrument"
type: concept
status: current
authority: advisory-exemption-testing
basis: code
sprint: S2
created: 2026-08-18
sources: ["archive/2026-08-18/2026-08-18-the-filename-half-lands-and-the-escape-hatch-falls/handoffs/2026-08-18-the-filename-half-lands-and-the-escape-hatch-falls.md", "scripts/vault-check-selftest.sh"]
tags: [testing, harness, vault]
---

# What `run_clean` asserts, and why that is not enough here

`run_clean` asserts two things: the run exits 0, and it prints an `ok` line. **An advisory changes
neither** — it is a bare `echo` and the script's exit status never sees it
([[the-filename-verdict-is-an-advisory-while-the-title-verdict-is-red]]).

**So a broken exemption would print its slug and still pass.** The case would be green while the
check it guards was wrong in exactly the direction the case exists to detect: a page that must not
be named being named.

**Every non-firing case for the filename half is `run_case_absent` instead**, which asserts that a
particular string is not in the output — and the reason is written beside them in the file rather
than left to be rediscovered.

# The general form

**An assertion that is insensitive to the channel the behaviour uses proves nothing about it.** The
severity of a verdict decides which assertion is available: a red verdict can be tested by the exit
code, an advisory can only be tested by reading the output.

This is the same class as a verdict that cannot fire
([[a-verdict-that-cannot-fire-is-worse-than-no-verdict]]) and as a check that passed for the wrong
reason ([[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]]) — in all three the instrument
returns the answer it was going to return whatever the subject did.

**It also fixes what a new case is worth.** Of the five cases added with the filename half, **one
discriminates**: it reported MISSED against the old check, which is the only reason the mechanism is
known to be new. The other four assert absence and pass against the old code as well
([[reverting-the-code-tells-you-whether-a-test-tests-anything]]).
