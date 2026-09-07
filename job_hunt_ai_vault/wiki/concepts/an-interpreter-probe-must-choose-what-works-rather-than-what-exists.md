---
title: "An interpreter probe must choose what works rather than what exists, and a hanging candidate falls outside the reasoning that excused a broken one"
type: concept
status: current
authority: interpreter-probe-selection
basis: code
sprint: S3
created: 2026-08-26
sources: ["archive/2026-08-26/2026-08-26-the-gate-hangs-on-a-store-stub-and-the-checks-get-their-names/handoffs/2026-08-26-the-gate-hangs-on-a-store-stub-and-the-checks-get-their-names.md", "scripts/vault-check.sh"]
tags: [harness, testing, external]
---

# The shape that hung

```
for measure_candidate in python3 python py; do command -v "$measure_candidate" && break; done
```

**`command -v` answers *does this name resolve*, and the rule needed *does this run Python*.** On this
machine `python3` resolves to the Microsoft Store stub
([[python3-on-this-machine-is-the-microsoft-store-stub]]), so the probe picked it, ran it, and the
gate never returned.

# The reasoning above the rule provided for the wrong failure

**Rule 15's own comment provides for an interpreter that is *"present but broken"***, on the ground
that whatever such an interpreter writes fails to match the good sentence and becomes a note rather
than a verdict.

**That holds for an interpreter that returns.** A hanging one writes nothing: there is no note, no
verdict and no end. **The excuse covered the case where the failure produces output, and the failure
that happened produces none.**

# The guard has to stand before the run, not around it

**A timeout wrapper cannot save a probe from a process it cannot kill.** `timeout 15 python3 -c` did
not return in 90 seconds ([[an-msys-signal-does-not-reach-a-native-windows-process]]).

**So the repair is a path test rather than a timeout**: a candidate resolving under `WindowsApps` is
skipped **without being run**.

# The general form

**A probe that tests for existence and needs behaviour is a check that passes for the wrong reason**
([[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]]). Where behaviour cannot be tested
safely — because testing it is the dangerous act — the guard is a property of the candidate that can
be read without running it.

**And a defence written for "it might be broken" is not a defence against "it might not answer".**
Those are different failures and only one of them has an output to inspect
([[a-background-job-with-buffered-output-cannot-be-told-from-a-dead-one]]).
