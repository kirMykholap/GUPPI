---
title: "The librarian prints each criterion's decider output at the ingest, and it goes into the brief"
type: decision
status: current
authority: criterion-reporting-at-ingest
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-23
created: 2026-08-23
sources: ["archive/2026-08-23/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands/handoffs/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands.md", "job_hunt_ai_vault/sprint.md", ".claude/agents/vault-librarian.md"]
tags: [vault, process, harness]
---

# The design, and it is the owner's

**At every ingest the librarian runs the command each acceptance criterion names and prints its
output — the output, never a judgement.** That printout goes into `brief.md`, so the state of the
criteria is the first thing the next session reads instead of something it has to excavate.

**His addition of the brief is the load-bearing half.** Printing the readings into a report nobody
opens again would have changed nothing; putting them at the front of the next session is what makes
the criteria visible between the day they are written and the day the sprint closes.

# What it fixes is a real gap, measured on the day it was designed

**The librarian reported state in enormous detail all day and no criterion was read.** Four
dispatches wrote long entries into `log.md`, every one of them naming commands and exit codes, and
not one of them left an answer to *where does criterion 3 stand*. The report is too long for
"done or not" to fall out of it.

# It does not touch the prohibition on judging the goal

**His first proposal was different**: the librarian would read the criteria and rewrite `sprint.md`
accordingly. He withdrew it once the session named the standing prohibition — the party doing the
work does not judge whether the work is done, and closing a sprint is the owner's
([[a-sprint-closes-on-its-goal]], [[the-librarian-writes-unattended]]).

**So the boundary is exactly where it was**: the librarian may run a command and copy what it says;
it may not say what that means. A decider's output is an observation and a criterion's status is a
verdict, and only the first crosses into the brief.

# What it obliges, and it is not built

- **`.claude/agents/vault-librarian.md` and whatever generates `brief.md` are the files to
  change**, and both are harness files a session writes rather than the librarian.
- **Until it lands, an ingest reports the readings it happened to take** and says which criteria it
  did not run a command for. A criterion whose decider costs half an hour is named as not run rather
  than guessed at.
- **A criterion whose decider does not exist cannot be printed**, which is the same hole criterion 1
  has from the other end ([[the-instrument-criterion-closes-more-ways-than-its-decider-counts]]).

# Deferred a second time — 2026-08-24

> **owner:** it moves to the next session.

**It was named at the start of that session with «можем обсудить» and never discussed.** The
conversation he opened it for did not happen, and the item was carried at the retro.

**Consequence: the *Sprint* section of the brief is written by hand for a third consecutive
session.** Nothing about the reasoning above changes and nothing here re-argues it.

# Deferred again, 2026-08-25 — and the obstacle is measured for the first time

> **owner:** «Предлагаю зафиксировать что есть и отложить обсуждение на следующую сессию.»

**Consequence, stated rather than implied: the brief's *Sprint* section is hand-written for a fourth
consecutive session.**

**The obstacle was never named before and it is a price, not a design gap.** Two of S3's four
acceptance criteria are decided by a 38-minute suite — criterion 1 by `vault-check-selftest.sh` and
`hook-selftest.ps1`, criterion 2 by `vault-archive.sh` plus a case in the same suite. Criteria 3 and 4
cost seconds. **So a brief printing every decider's output at every ingest pays about forty minutes per
ingest.**

**This page records what is not built and the files to change, and nowhere recorded what running it
would cost.** That is the gap this note closes.

**The shape the session proposed, and it is not ratified**: fresh output for the cheap deciders, and
for the suite the last reading with its date plus whether any script has changed since. **Whether a
script changed is a `git diff` rather than a judgement**, so the librarian would not be choosing
([[a-printed-register-cannot-drift-and-a-maintained-one-always-has]]).

**It is a deferral repeated again**, and by the rule agreed the same day it now owes the sprint it
happens in, or a refusal ([[a-repeated-deferral-names-the-sprint-it-happens-in-or-is-refused]]).

# It names S3 — 2026-08-26

> **owner:** «Да, называем обеим S3»

**This item and the gate's flag fork both name S3 as the sprint they happen in**
([[the-gate-flag-fork-is-recorded-and-nothing-is-built]]). That discharges the obligation the section
above reports as outstanding: a repeated deferral names its sprint or is refused, and this one now
names it.

**It owes a line in `sprint.md`**, and it has one from the ingest of this date. **Nothing else about
the item changed** — it is still unbuilt, the files to change are still the two named above, and the
forty-minute figure still stands unratified.
