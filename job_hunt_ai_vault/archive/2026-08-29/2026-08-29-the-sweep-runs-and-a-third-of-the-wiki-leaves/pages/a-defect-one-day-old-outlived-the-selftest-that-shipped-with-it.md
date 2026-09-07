---
title: "A defect one day old outlived the selftest that shipped with it, because the suite runs where the probe happens to work"
type: lesson
status: archived
authority: same-day-defect-no-case
basis: code
sprint: S3
created: 2026-08-26
sources: ["archive/2026-08-26/2026-08-26-the-gate-hangs-on-a-store-stub-and-the-checks-get-their-names/handoffs/2026-08-26-the-gate-hangs-on-a-store-stub-and-the-checks-get-their-names.md", "scripts/vault-check.sh", "scripts/vault-measure-selftest.py"]
tags: [testing, harness, vault]
---

# The incident, 2026-08-26

**Rule 15 of `scripts/vault-check.sh` and `scripts/vault-measure.py` landed in `a03f042` with 59
selftest cases.** The next day the rule hung the gate for an hour
([[python3-on-this-machine-is-the-microsoft-store-stub]]).

**None of the 59 can see it.** The suite runs on a machine where the probe happens to pick a working
interpreter, so the failing branch is never entered
([[an-interpreter-probe-must-choose-what-works-rather-than-what-exists]]).

# The property that makes this class invisible

**The cases test what the code does; the defect is which code runs.** A probe that selects an
interpreter has a selection step, and every case runs downstream of a selection that succeeded — so
the case count says nothing about the branch
([[a-green-gate-can-be-no-evidence-about-the-branch-just-changed]],
[[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]]).

**A selftest built on the machine that has the good candidate is a fixture that depends on the
environment**, which is the defect this suite has been bitten by before from the other side
([[the-selftest-works-in-its-own-fixture-and-never-in-the-corpus]]).

# The repair landed with no case, and the suite that would carry it now runs once a sprint

**Nothing mechanical protects the fix.** The owner took the full suite out of the session loop the
same day ([[the-suite-stops-running-every-session]]), so the case — when somebody writes it — will
not be exercised until a sprint closes, unless the smoke runner takes it
([[the-smoke-runner-is-built-first-thing-next-session]]).

**That is recorded as a deferral rather than as a repair**, and it is the sharpest live instance of a
case that would have to plant its own broken candidate rather than rely on the host having one
([[a-case-that-passes-before-the-change-tests-nothing]]).

# The case exists, and it is proved in both directions — 2026-08-26

**`a store stub first on PATH is skipped unrun`, in `scripts/vault-check-selftest.sh`.** It does what
the section above says such a case would have to do: it plants its own broken candidate rather than
relying on what the host happens to have.

**Both directions were run, which is what makes it evidence rather than a green line.** Against the
current gate the case is **CAUGHT**; against a candidate copy with the `WindowsApps` guard deleted it
**MISSES**, and the diagnosis names the planted stub by the stub's own output — so the failing run
says *which* thing went wrong rather than only that something did
([[a-new-verdict-is-proved-in-the-real-tree-because-the-check-cannot-see-a-sandbox]],
[[a-case-green-before-its-mechanism-is-proved-by-removing-the-guard]]).

**The stub prints and exits; it does not hang.** A fixture that reproduced the real symptom would
hang the suite for ever the first time the guard regressed — which is the failure the case exists to
catch, so the case would take the whole suite down with the defect it found. **The property under
test is *the guard skipped this candidate unrun*, and a stub that exits proves that as well as one
that hangs** ([[a-fixture-must-materialise-what-the-subject-reads]],
[[an-msys-signal-does-not-reach-a-native-windows-process]]).

**The heading above stays as it was.** It is a true account of the day the repair landed, and this is
the next day catching up ([[the-date-of-a-correction-note-is-the-date-the-text-became-false]]).
