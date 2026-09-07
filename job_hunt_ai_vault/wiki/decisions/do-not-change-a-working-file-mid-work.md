---
title: "Do not change a working file mid-work, and this session did"
type: decision
status: current
authority: mid-work-file-changes
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-20
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock/handoffs/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock.md", ".claude/hooks/vault-path.ps1", ".claude/hooks/check-the-journal.ps1"]
tags: [process, harness, agents]
---

# DIVERGENCE, 2026-08-20 — recorded rather than kept as a quiet exception

**What happened.** While building the librarian lock, `Find-Bash` was moved out of
`.claude/hooks/check-the-journal.ps1` into `.claude/hooks/vault-path.ps1` — **unasked, and outside
the stated scope** — so the new hook could call it.

**Why it looked unnecessary to ask.** The alternative was a second copy of one discovery idiom, and
this store already records four copies of the vault-discovery idiom as a defect
([[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]]).

**The rejected alternative is: copy the function and leave the other file alone.**

## The owner's ruling has two halves and they point in different directions

**The practice is refused.** Do not change a working file mid-work. The rule that already covers it
is `CLAUDE.md`'s — ask before you weaken, remove or work around any rule — and its neighbour on
scope ([[narrowing-a-scope-notifies-and-widening-it-asks]]).

**The change itself stays**, because reverting it costs a second definition of a rule that must not
have two. Two discovery rules that can disagree are worse than either of them.

## Why "it was the better change" is not a defence

It was the better change and it is still a divergence. The cost of the practice is not the quality
of any one edit: it is that a file somebody else is depending on moved without their knowing, and
the reviewer of the day's diff has to discover it. **Recorded as a divergence rather than kept as a
quiet exception** is the whole of the repair
([[a-wrong-record-is-acceptable-and-an-invisible-one-is-not]]).

**The same move is also where a fact about code was assumed rather than checked**
([[a-fact-about-code-was-generalised-from-its-neighbour]]).

# It recurred the next day, in the most literal form the phrase has — 2026-08-20

**`scripts/vault-check-selftest.sh` was edited while bash was executing it.** The run collapsed
mid-suite with missing result files, **and the failure looked like a suite defect**
([[a-shell-script-was-edited-while-bash-was-executing-it]], [[failing-loudly-with-the-wrong-diagnosis]]).

**Bash reads a script incrementally**, so an edit lands in the middle of a program still being read
and the interpreter continues into bytes that were never there when it started.

**What the recurrence says about the rule's boundary:** the file was not being *worked on* by
anyone, it was being *run*, and *working file* did not read as covering that. The property that
matters is whether **anything** is holding the file open — and in this repository `bash script.sh`
is the cheapest way to be that something. The rule is not rewritten here; the instance is recorded
against it one day after it was written, which is the evidence for whichever wording the owner
prefers.

## A neighbouring shape, 2026-08-22: the file was not being worked on, it was being read

**A file read only in part was overwritten whole**, and the owner had a note in the part that was
never read ([[a-file-read-in-part-was-overwritten-whole]]). **The rule above does not reach it** —
nothing about that file was mid-work, and no scope was widened; the writer simply believed it knew a
file it had seen a window of.

**It is recorded beside this page because the repair is the same one**: touch the span, not the
file. The owner ruled it a lesson rather than a guard, so it is a rule an agent keeps and not a
mechanism that enforces one ([[knowing-a-rule-is-not-a-mechanism]]).
