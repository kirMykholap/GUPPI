---
title: "Testing a `SessionStart` hook by feeding it a payload has live side effects, and it rotated the real ledger"
type: lesson
status: archived
authority: hook-probe-side-effects
basis: code
sprint: S3
created: 2026-08-24
sources: ["archive/2026-08-24/2026-08-24-the-feedback-line-is-spoken-and-the-floor-under-a-session-is-read/handoffs/2026-08-24-the-feedback-line-is-spoken-and-the-floor-under-a-session-is-read.md", ".claude/hooks/session-brief.ps1", ".superpowers/sdd/pre-task-ledger.tsv"]
tags: [harness, testing, process]
---

# What happened, 2026-08-24

**A probe fed `session-brief.ps1` a hand-written payload with a made-up `session_id`.** The hook did
what it always does: `Invoke-LedgerRotation` on `source: startup`, and `Set-SessionStamp` on any
`session_id`.

**So the live `pre-task-ledger.tsv` was rotated away and the session was restamped as
`test-sid-0001`.** The five real rows were put back by hand and the spurious rotation file removed
([[the-pre-task-ledger]], [[one-ledger-is-the-record-the-heartbeat-and-the-permission-mode]]).

# It was broken before this session, and that is the part worth keeping

**The hook has behaved this way since it was written, and nothing anywhere says so.** No comment in
the file, no line in the hook register, nothing in the selftest. The next person testing that hook
by hand will do exactly the same thing.

**The general shape: a hook is a program with side effects, and running it is not observing it.**
The measurement harness that exists — `scripts/hook-selftest.ps1` — runs hooks against a sandbox for
this reason; the failure happens the moment somebody steps outside it to "just check something"
([[a-hook-is-measured-from-powershell-or-not-at-all]],
[[the-selftest-works-in-its-own-fixture-and-never-in-the-corpus]]).

# Why the damage was quiet

**A rotation looks like a normal end-of-day event and leaves a plausible file.** Nothing compares
the ledger's contents against what the session actually did, so the loss is invisible to every
instrument here — the same direction of failure this store keeps recording
([[an-instrument-that-fails-towards-nothing-to-do]]).

# What is not done

**Nothing warns about it.** The repair was manual and the hazard stands; naming it here is the whole
of what this ingest did about it.

# It reproduced exactly, in the session that read this page and quoted it back — 2026-08-26

**A probe of `.claude/hooks/catch-the-feedback.ps1` was run against the repository copy rather than
a sandbox** and filed a fabricated record — `- decision: the owner said it - «де»` — into
`.superpowers/sdd/vault-feedback.md`.

**It was caught at the drain and dropped rather than compiled**, because it is a test payload and
not testimony. **Filing it would have put four Cyrillic letters in the owner's mouth**
([[a-block-attributed-to-the-owner-is-written-in-his-own-russian]]).

**The recurrence happened in the session that read this lesson and quoted it back the same hour**,
which is the whole point of writing it down and is also the evidence that writing it down was not
enough ([[knowing-a-rule-is-not-a-mechanism]]).

**It is the second measured instance of the class, and the class now has a proposal**
([[a-register-of-what-each-hook-writes-when-it-is-probed]]). The collector called that proposal its
weakest of five; this instance is the second data point it was short of.
