---
title: "The grouping defect in the dialogue extract is an S3 harness line, and every retro until then misfiles some marks"
type: decision
status: current
authority: dialogue-grouping-defect-deferral
binding: deferral
basis: human
sprint: S3
decided: 2026-08-26
created: 2026-08-26
sources: ["archive/2026-08-26/2026-08-26-the-carried-questions-are-answered-and-the-plan-is-corrected-before-it-is-built/handoffs/2026-08-26-the-carried-questions-are-answered-and-the-plan-is-corrected-before-it-is-built.md", "scripts/session-dialogue.py"]
tags: [harness, process, testing]
---

# The ruling, 2026-08-26

*(the owner selected it, against fixing it in the same session.)*

**The attention-list grouping defect in `scripts/session-dialogue.py` becomes a named S3 harness
line.** It is not repaired today.

**The reason he chose the deferral:** the script has a **52-case selftest** in
`scripts/session-dialogue-selftest.py`, and the repair moves with it. That is a change with a test
surface, not a one-line edit ([[the-session-dialogue-extract]]).

# The defect

**The list groups by *filed block* rather than by line.** A block's section heading is taken from its
first record, and every other record in that block lands underneath it.

**Measured on the session of 2026-08-26**: four `miss:` records filed under `## measure` and one
under `## decision`.

# The consequence of not doing it

**Every retro until the repair lands misfiles some of its own marks**, and a reader auditing by
section undercounts. The kind counts printed for a session are wrong in a way nothing announces
([[the-retro-reads-the-marks-and-does-not-replace-them]]).

# Rejected

**Rejected: fixing it now**, on the cost above.

# He said «чиним» and it was not built — 2026-08-29

**owner:** «чиним» — S3 item 27, the grouping defect.

**That ratifies the term rather than discharging it.** The repair was ordered and the session ran out of
itself before building it: the plan was cut to what could be built without a librarian write, and this
was not in the cut. **The deferral stands and does not archive on the ruling.**

**What it costs while it stands**: every retro until the repair misfiles some marks
([[the-session-dialogue-extract]]). The extract of 2026-08-29 was read anyway and its figures are
recorded there.

*(Compiled from `raw/handoffs/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds.md`.)*
