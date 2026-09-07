---
title: "An MSYS signal does not reach a native Windows process, which is why a timeout wrapper fails here and so does a job stop"
type: concept
status: current
authority: msys-signal-reach
basis: measurement
sprint: S3
created: 2026-08-26
sources: ["archive/2026-08-26/2026-08-26-the-gate-hangs-on-a-store-stub-and-the-checks-get-their-names/handoffs/2026-08-26-the-gate-hangs-on-a-store-stub-and-the-checks-get-their-names.md"]
tags: [external, harness, testing]
---

# The property

**A signal sent from the MSYS side — by `timeout`, by `kill`, by a tracked job's stop — reaches the
MSYS process and not the native Windows process it launched.** The wrapper returns or reports
success, and the thing it meant to stop is still running.

# The measurements of that property, taken on one day

**A timeout did not bound a hung probe.** `timeout 15 python3 -c "print(1)"` had not returned after
**90 seconds** measured from outside, against a Store stub that answers nothing
([[python3-on-this-machine-is-the-microsoft-store-stub]]).

**A background job stop did not stop the tree.** After `TaskStop` on `vault-check-selftest.sh`,
**33 processes survived in the suite's process group**; `kill -9` on the MSYS PIDs left **eight**
alive, each with a live Windows child. Only `taskkill //PID <winpid> //F //T` reached them.

# What follows for anything built here

**A guard must refuse before it runs, not wrap what it runs**
([[an-interpreter-probe-must-choose-what-works-rather-than-what-exists]]).

**And a background run cannot be assumed dead because it was stopped.** Liveness on this host is a
process count, not the return of the stop command
([[a-background-job-with-buffered-output-cannot-be-told-from-a-dead-one]]).

**This is another member of the host-facts family** — the things about this machine that no amount of
correct shell writing avoids ([[windows-console-encoding]],
[[a-path-is-resolved-by-the-program-that-opens-it-not-by-the-shell-that-launched-it]]).
