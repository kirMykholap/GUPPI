---
title: "`scripts/` joins `make style`, and only the check half of it"
type: decision
status: current
authority: makefile-targets
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-31
created: 2026-08-31
target_kind: action
target: makefile-style-runs-ruff-check-over-src-tests-and-scripts
sources: ["archive/2026-08-31/2026-08-31-the-families-become-rules/handoffs/2026-08-31-the-families-become-rules.md", "Makefile"]
tags: [harness, testing, process]
---

# Context

**`make style` ran `ruff` over `src` and `tests` only**, and `scripts/` holds the vault's whole
machinery — the gate, the injector, the archiver, the catalogue, the measure writer and now two
generators. **It had never been linted by anything.**

**The occasion was two new files.** `scripts/build-families-table.py` and
`scripts/build-family-rules.py` produced 21 findings the target could not see, and the folder as a
whole produced **10 more**: four `subprocess-run-without-check`, two `call-date-today`, one unused
import, one implicit string concatenation, one enumerate-for-loop, one open-alias. Two were
auto-fixable.

# The question

**Does `scripts/` join `make style`, and does the format half join with the check half?**

# How it works after

**`style` becomes `ruff check src tests scripts`.** The ten findings were fixed before the widening
landed, so the target was green the first time it ran wide: the four `subprocess.run` calls got an
explicit `check=False` with the reason written on each, the two `date.today()` calls were kept as the
**local** date under a `noqa` — every date in this store is a calendar day of the owner's rather than an
instant — and the remaining four were repaired outright.

**`ruff format --check scripts` is deliberately not added.** It would fail on six existing files, and
reformatting scripts nobody is reviewing belongs in a diff someone reads. **So `style` now checks a
wider set than it formats**, and that asymmetry is the decision rather than an oversight.

**What that leaves open and unscheduled:** the six files' formatting drift is invisible and unmeasured,
and adding the format half is a separate change. **It is not a ratified deferral** — nobody has agreed
to leave it — and it is named in the brief on that footing.

# Recommendation

**Widen the check half now, with the cost measured first.** The session put the ten findings to him
before asking, which is the shape a question about work takes here.

**Rejected: adding `ruff format --check scripts` in the same change.**

**Rejected: leaving the folder unlinted**, which had already let 21 findings ship in files written the
same day.

# Ratification

**owner selected, 2026-08-31: «Да, добавляем».**

*(Compiled from `raw/handoffs/2026-08-31-the-families-become-rules.md`.)*
