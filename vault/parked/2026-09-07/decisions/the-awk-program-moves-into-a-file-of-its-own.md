---
title: "The awk program moves into a file of its own and is called with `awk -f`, and not today"
type: decision
status: current
authority: awk-program-home
binding: deferral
basis: human
sprint: S3
decided: 2026-08-30
created: 2026-08-30
target_kind: action
target: the-gates-awk-program-is-called-with-awk-f
sources: ["archive/2026-08-30/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md", "scripts/vault-check.sh"]
tags: [vault, harness, testing]
---

# Context

**The frontmatter pass of `scripts/vault-check.sh` is an awk program written inside a single-quoted
shell string and handed to `xargs` as one argument.** That shape produced two failures on 2026-08-30,
an hour apart and from one comment block: an apostrophe closed the quote and broke the gate loudly,
and 1.7 KB of comments pushed the argument past a size limit and stopped the gate checking **without
turning it red** ([[the-gate-can-stop-checking-and-go-on-exiting-zero]]).

**The headroom is under four kilobytes and unmeasured**: 79,149 bytes now, 82,425 known to fail, and
the exact ceiling somewhere between.

# The question

**Does the program move into a file called with `awk -f`, or does the gate keep the embedded form and
rely on the new stderr case to catch the next overflow?**

# How it works after

**It moves, and not on 2026-08-30.** Ratified and deferred the same day, with no sprint named.

**Until it lands, every comment written inside those quotes spends a budget nobody can see**, and the
repair that is in place is the selftest case asserting the gate writes nothing to stderr — which
catches the overflow after it happens rather than removing it.

**One thing was done immediately and is not the deferral**: the reasoning that stood inside the
program was moved outside the quotes, into a shell comment above the call. A comment inside the
program costs space at a limit; outside it costs nothing.

# Recommendation

**Move it.** Living with the headroom means trusting a single case to catch a failure whose only
symptom reads as a corpus fault, on a file that grows every time a verdict is added. `awk -f` removes
both failure modes at once — the program stops being a shell string, so an apostrophe is ordinary text
and the size limit does not apply.

**Rejected: living with the headroom and relying on the new stderr case.** The alternatives were the
session's own framing.

# Ratification

**owner selected, 2026-08-30: «выносим, но не сегодня».** He chose the session's recommendation
against the alternative it had put beside it.

# What it waits on, and where the measurement lives

**There is a decided-and-unbuilt page waiting for this subject.**
[[the-vault-scripts-page-stays-a-hub-and-the-gate-and-its-suite-get-subject-pages]] ruled that the
gate gets an entity page of its own; none exists, and `vault-scripts` is still the only hub. **When it
does, the headroom measurement belongs on it.**

*(Compiled from `raw/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md`.)*
