---
title: "A control nothing touched separates a change from the machine, and the suite's wall clock is not the instrument"
type: lesson
status: archived
authority: drift-control
basis: measurement
sprint: S3
created: 2026-08-24
sources: ["archive/2026-08-24/2026-08-24-the-suite-learns-to-list-itself-and-every-proposal-names-its-cause/handoffs/2026-08-24-the-suite-learns-to-list-itself-and-every-proposal-names-its-cause.md", "scripts/vault-authority.sh", "scripts/vault-check.sh"]
tags: [testing, harness, vault]
---

# The measurement, 2026-08-24

**`scripts/vault-authority.sh` was not edited all session and drifted from 1.18–1.38 s to
1.52–1.98 s.** Over the same interval the gate, on identical code, went from 15.02/15.39/15.42 s to
21.21/21.46/24.87 s — about forty per cent.

**The machine moved by a third inside one session.** Without that control, the session's own
thirty-eight-minute suite run would have been published as a regression caused by its work.

# What the control makes sayable, and what it does not

**The only defensible claim about what the work bought is the paired gate reading: 17.2 → 15.3 s,
about eleven per cent.** Three runs each way, taken back to back in a quiet window.

**The suite's wall clock is not comparable across the session.** It ran at 37m44s against 34m08s
previously, and two things differ besides the code: the corpus grew, and the machine slowed. **That
figure must not be quoted as a regression.**

# Why the suite is the wrong instrument for a change of this size

**One point costs thirty-eight minutes, the machine drifts by a third inside a session, and the
effect being looked for is 1.9 s.** No number of runs at that price separates the signal from the
room.

**The instrument that works is the gate**, at three readings a minute, **with a control beside it
that nothing touched.** That pairing is what turns a reading into a comparison
([[a-measurement-taken-while-other-work-runs-against-the-same-disk-measures-nothing]]).

# The other way a reading of this work came out meaningless

**A copy of the injector timed from a scratch directory finished in 0.8 s and had done nothing**
([[measuring-a-copy-of-a-script-placed-somewhere-else-measures-nothing]]). **Both failures produce a
number that looks like good news**, which is why a control and an assertion inside the harness are
the same defence from two directions.
