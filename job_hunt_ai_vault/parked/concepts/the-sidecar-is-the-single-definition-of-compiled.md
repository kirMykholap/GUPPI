---
title: "The sidecar is the single definition of *compiled*, and every reader that asks the question asks it the same way"
type: concept
status: current
authority: compiled-definition
basis: code
sprint: S2
created: 2026-08-21
sources: ["archive/2026-08-20/2026-08-20-the-ingest-picks-by-sidecar-and-the-owner-cannot-see-the-harness/handoffs/2026-08-20-the-ingest-picks-by-sidecar-and-the-owner-cannot-see-the-harness.md", ".claude/hooks/session-brief.ps1", "scripts/vault-check.sh", ".claude/skills/ingest/SKILL.md"]
tags: [vault, harness, process]
---

# What *compiled* means here

**A handoff is compiled when `<name>.coverage.tsv` sits beside it.** That file is written by the
ingest that gave every unit of the journal a verdict, so its existence is the ingest's own
signature ([[ingest-is-units-and-verdicts]]).

# The readers, and that they agree is the point

| reader | the question it asks |
|---|---|
| `.claude/hooks/session-brief.ps1` | is there an uncompiled journal to warn the new session about |
| rule 8 of `scripts/vault-check.sh` | should this journal's form be judged at all |
| `/ingest` | which source am I compiling |

**The last of the three joined on 2026-08-20** and the first two had used the sidecar since
2026-08-17 ([[the-ingest-chooses-its-source-by-the-sidecar]]).

**One definition read by three mechanisms is worth more than three that happen to agree.** Each of
these is written in a different language — PowerShell, bash, prose in a skill file — and the only
thing they share is a filename rule. That is cheap enough to keep true.

# Why it beats the ordering it replaced

**It is a file-existence test, and no ordering can break it.** The date prefix it replaced orders
sessions only while there is one a day: with two journals of 2026-08-16 both compiled, a
`Sort-Object Name -Descending` returned the *earlier* of the two and the brief's staleness alarm
fired on a journal that had been ingested hours before ([[session-hooks]]).

**It also names *which* journals are uncompiled instead of naming one**, which is what lets the
ingest take several oldest-first inside one dispatch
([[ingest-runs-after-handoff-at-the-end-of-a-session]]).

# What it does not say

**It says nothing about fidelity.** A sidecar proves every unit was accounted for; it cannot prove a
unit was transcribed correctly, and a page describing behaviour a later slice replaced passes with
its identifiers intact ([[fidelity-to-a-source-and-fidelity-to-the-tree]]).

**The sidecar's name is load-bearing.** `vault-coverage.sh` falls back to evidence mode when it
finds no sidecar under the exact name, and evidence mode is a first pass reporting a fraction — a
report of *0 of 33 evidenced* is not a pass, which is why that mode exits non-zero
([[vault-scripts]]).
