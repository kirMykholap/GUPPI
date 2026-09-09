---
title: "A truncated report hides the line it was run for"
type: lesson
status: archived
authority: truncated-report
basis: measurement
sprint: S3
created: 2026-08-23
sources: ["archive/2026-08-23/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands/handoffs/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands.md", "scripts/vault-check-selftest.sh"]
tags: [testing, process, harness]
---

# The incident, 2026-08-23

**`bash scripts/vault-check-selftest.sh | tail -25` was run on a suite that had `missed 1`.** The
suite prints each MISSED case **with its detail** — which case, and what the gate said instead of
what was expected — and those lines are in the body of the report, not at its end. The tail showed
the totals and cut the diagnosis.

**What it left was a choice between two bad options**: re-run the suite blind, at half an hour, or
reason about the failure from the fixture helpers without ever seeing what the gate actually
printed.

**The same command hid the exit code as well**, which is a second failure of the same invocation
and has its own page ([[an-exit-code-read-through-a-pipe-belongs-to-the-last-stage]]).

# Why the tail is the wrong end of this particular report

**A suite's summary is at the end and its evidence is in the middle.** Every design that prints
`caught N, missed M` last puts the interesting lines furthest from the tail — so the more useful
the run, the more of it a fixed-size tail throws away.

**And the cost is asymmetric.** Keeping the whole output costs some scrollback. Losing it costs
another full run of a suite whose wall clock is measured in tens of minutes
([[the-gates-cost-grows-with-the-corpus-and-rule-pages-are-the-minor-term]]).

# What to do instead

**Write the run to a file and read the file.** `> out.txt 2>&1`, then `grep` it for MISSED, then
read around the hits. The exit code is then the command's own and the evidence survives the
question you did not think to ask first.

**`grep` for the verdict rather than slicing by line count**, when a filter is wanted at all: the
number of lines a report needs is a property of what went wrong, and it is not known before the run.

# The `grep` half of the advice above went false, and it cost two defects — 2026-08-26

**The closing line of this page recommends grepping for the verdict rather than slicing by line
count. That is not enough, and this session paid for it twice in one day.**

**A filtered reading of a check is not a reading of it.** Every run of every check that session was
piped through `grep`, and both defects the session shipped were on the console and outside the
filter:

- **`scripts/hook-selftest.ps1` printed argument-binding errors** for five cases that never ran, and
  the score line said `caught 169, missed 0`
  ([[a-statement-starting-with-a-bare-word-is-a-command-call-in-powershell]]);
- **the hang printed nothing at all**, which no filter can show, and the run was read as finished
  because the grep produced no MISSED line
  ([[a-command-in-a-make-recipe-hangs-while-it-inherits-standard-input]]).

**A grep encodes what you already suspect.** Slicing by line count throws away lines by position and
a filter throws them away by hypothesis, which is worse in the one case that matters: the defect you
did not think to look for.

**The half of the advice that stands is the file.** Write the run to a file, then filter the file as
often as you like — the evidence survives the question you did not ask first, and the exit code is
the command's own ([[an-exit-code-read-through-a-pipe-belongs-to-the-last-stage]]).

**`scripts/vault-check-selftest.sh` prints this caution about its own filter and a reader filtering
by hand had none**, which is the asymmetry worth naming: the tools here warn about narrowing and
nothing warns a human doing it at the prompt.
