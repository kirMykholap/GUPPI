---
title: "A target that covers part of a repository reports clean about that part, and says nothing about the rest"
type: lesson
status: current
authority: partial-target-clean-report
basis: measurement
sprint: S3
created: 2026-08-31
sources: ["archive/2026-08-31/2026-08-31-the-families-become-rules/handoffs/2026-08-31-the-families-become-rules.md", "Makefile", "scripts/build-family-rules.py"]
tags: [testing, harness, process]
---

# The incident, 2026-08-31

**`make style` ran `ruff` over `src` and `tests` only, and reported clean all day.** Two new files
written into `scripts/` that morning carried **21 findings** the target could not see. The folder as a
whole carried **10 more**, none of which had ever been looked at by anything.

**`scripts/` is not a corner of this repository.** It holds the gate, the injector, the archiver, the
catalogue, the measure writer and the two generators — the machinery every ritual here runs on.

# The class

**A green target is a claim about its own scope and about nothing else, and the scope is invisible in
the output.** `make style` printed the same word — nothing — whether the unchecked folder was empty or
held thirty-one findings. **The reader supplies the scope from memory**, and memory says "the linter
passed".

**Coverage of a checker is not measured by anything here.** The gate has `--lint` advisories about the
corpus, the suite counts its own cases, and no instrument anywhere answers *which paths does this
target actually read*. That question was answered by a person noticing that two new files were in a
folder whose name was not in the target.

# What follows

**When a target is widened, the widening is the finding, not the fix.** Ten pre-existing findings in a
folder nobody had linted is the measurement worth writing down; the four-line `Makefile` change is not.

**A partial target's scope belongs in the entity that describes it.** [[the-makefile]] states what each
target runs, and it was false about `style` for the hours between the change and this ingest — which is
the ordinary risk of an entity that describes a file.

**Widening the check half does not widen the format half, and saying so is part of the record.**
`ruff format --check scripts` was deliberately not added, so `style` now checks a wider set than it
formats ([[scripts-joins-make-style-and-only-the-check-half]]). **An asymmetry nobody wrote down is
indistinguishable from an oversight.**

*(Compiled from `raw/handoffs/2026-08-31-the-families-become-rules.md`.)*
