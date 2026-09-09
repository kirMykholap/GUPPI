---
title: "`Add-Content -Encoding UTF8` writes a BOM in front of the first field of the first row"
type: lesson
status: archived
authority: powershell-append-bom
basis: measurement
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact/handoffs/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact.md", ".claude/hooks/pre-task-state.ps1"]
tags: [harness, process, testing]
---

# The defect, 2026-08-20

**In Windows PowerShell 5.1, `Add-Content -Encoding UTF8` emits a byte-order mark**, and on a file
created by that call it lands in front of the very first field of the very first row.

**Here that field is the timestamp the plan path compares** — lexically, on a fixed-width format
([[the-pre-task-state-machine-has-a-flag-for-the-plan-and-a-flag-for-the-write]]). A mark in front
of it makes the first row of a ledger sort and compare unlike every row after it.

**`AppendAllText` with a `UTF8Encoding` constructed as false emits none**, on creation or on append,
and that is what the ledger writer uses ([[the-pre-task-ledger]]).

# Why this keeps happening here

**This repository has met the encoding boundary from several sides already** — a `.ps1` read in the
ANSI codepage without a BOM, a CRLF defeating an anchored match, a `\r` making a check find nothing
([[windows-console-encoding]], [[line-endings-make-git-status-overstate-what-changed]]).

**The generalisation is about invisible leading bytes, not about PowerShell.** A file's first byte
is the one no reader prints and every parser reads. Where a format's meaning is positional — a
first field, an anchored pattern, a fixed-width timestamp — the failure is confined to the first
record, which is exactly where a spot check looks least.
