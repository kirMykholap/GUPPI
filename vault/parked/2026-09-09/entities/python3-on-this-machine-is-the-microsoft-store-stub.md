---
title: "`python3` on this machine is the Microsoft Store stub, and it hangs rather than failing"
type: entity
status: current
authority: python3-store-stub
basis: measurement
sprint: S3
created: 2026-08-26
sources: ["archive/2026-08-26/2026-08-26-the-gate-hangs-on-a-store-stub-and-the-checks-get-their-names/handoffs/2026-08-26-the-gate-hangs-on-a-store-stub-and-the-checks-get-their-names.md", "scripts/vault-check.sh"]
tags: [external, harness, testing]
---

# What it is

**`python3` here is not an interpreter.** It resolves to
`AppData/Local/Microsoft/WindowsApps/python3`, an app-execution alias for
`PythonSoftwareFoundation.PythonManager`.

**It neither answers nor exits.** It is not *present but broken* — it produces no output, no error and
no exit code.

**The working interpreter is `python`**, at `/c/Python314/python`.

# What it cost

**It hung rule 15 of `scripts/vault-check.sh` for an hour on 2026-08-26.** The rule's probe chose the
first candidate that **existed** rather than the first that **worked**, and `command -v python3`
succeeds on the stub ([[an-interpreter-probe-must-choose-what-works-rather-than-what-exists]]).

**A timeout does not help.** `timeout 15 python3 -c "print(1)"` had not returned after 90 seconds:
an MSYS signal does not reach a native Windows process
([[an-msys-signal-does-not-reach-a-native-windows-process]]).

# What was done about it

**A candidate resolving under `WindowsApps` is skipped without being run.** The order of candidates is
unchanged and behaviour on a machine without the stub is identical.

**Gate afterwards: 21.5 s, exit 0, `VAULT-CHECK: ok`** on a 682-file corpus. The recorded cost of rule
15 on this machine was 20.2 s, so 21.5 s is the norm and not a remainder of the problem.

# Why this is an entity and not only a lesson

**It is a noun on this machine with properties that will bite anything else that probes for an
interpreter** — the smoke runner, `vault-measure.py`'s callers, any future rule that shells out.
The class of it belongs to [[windows-console-encoding]] and [[claude-code-config-loading]]: facts
about this host that no amount of correct shell writing avoids.
