---
type: decision
case: "1010"
status: current
children: ["[[decision-case-1010.1]]", "[[decision-case-1010.2]]", "[[decision-case-1010.3]]"]
origin: raw/2026-11-02/2035/ledger.md#case-1010
sprint: plugin
created: 2026-11-02
tags: [hooks, harness, workflow, case-build, session]
---

## Problem

The note of names can send `case-guppi` hundreds of notes for one Case, because it takes the modules a task only imports for files it changes, and because a name that hundreds of texts hold gives one note per file.

## Recommend

- **Narrow the note now or wait for a real one**
  - Recommended: (a) narrow now, from the probe, since the probe ran the hook's own functions over the live files.
  - Answer: (a), narrow now.
- **Which paths of a task line count as changed files**
  - Recommended: (a) only the first code span, when it is a path; a task that changes two files takes two task lines.
  - Answer: (a).
- **What the note does with a name that many files hold**
  - Recommended: (a) one note for a broad name, a name that more than 20 files hold.
  - Answer: (a), more than 20 files.
- **How the Case splits and what checks each part**
  - Recommended: (a) three parts, each with its own check: the first code span, the note of a broad name with a new Estimate, and the answer of `case-guppi`.
  - Answer: (a).

## History

- 2026-11-02 created · raw/2026-11-02/2035/ledger.md#case-1010
