---
title: "A script must not be edited while it is running, because bash reads it lazily by byte offset"
type: lesson
status: current
authority: editing-a-running-script
basis: code
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock/handoffs/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock.md", "scripts/vault-check-selftest.sh"]
tags: [process, harness, testing]
---

# The mechanism, which is what makes it non-obvious

**Bash reads a script lazily, by byte offset.** It does not load the file and then run it; it
returns to the file for the next command, at the offset it left off at.

**So appending a comment to a backgrounded suite shifted everything below that point**, the
interpreter resumed **inside a line**, and the run failed at line 1212 — **a line the edit never
touched**.

`bash -n` passed afterwards, which is what identified the cause: a file that parses clean and a run
that died on a syntax error can only be a file that changed underneath the run.

# Why it is easy to walk into

**The edit looked unrelated to the run.** It was a comment, above the region being executed, in a
suite that had been backgrounded precisely so that other work could continue. Every one of those is
a reason it felt safe.

# The rule

**Background a long run and the file is frozen until it finishes**, or copy the script and edit the
copy. This is not a style preference: there is no edit to a running bash script that is safe,
because the danger is the byte offset rather than the semantics.

# It also produced a second failure, downstream

The wrapper measuring that run reported *no misses* about a suite that executed no case
([[an-assertion-inside-a-measurement-harness-catches-a-broken-instrument]]). **Two failures from
one edit, and the second one is the sort that gets believed.**

# The negative half, added 2026-08-30, because a wider claim was filed and was false

**Editing a repository file while `scripts/vault-check-selftest.sh` runs is SAFE.** A feedback line
filed earlier on 2026-08-30 said the opposite — that repository edits during a run give different
cases different versions — and **that line is false and is corrected here rather than carried.**

**The suite snapshots the tree once into `$PRISTINE` at line 165 and every case copies from that**, so
what a case sees is fixed the moment the run starts.

**What is unsafe is exactly and only this page's own claim**: editing the **suite file itself**, which
`bash` reads incrementally as it executes.

**The overstatement would have cost a future session working time** — it forbids editing anything
during a run, which is most of what a session does while a twenty-second gate is in flight. **A hazard
stated too widely is a hazard nobody can work around correctly**, and it is worth as much care as
stating one too narrowly.

*(Extended 2026-08-30 from `raw/handoffs/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form.md`.)*
