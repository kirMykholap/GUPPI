---
title: "The hook's `authority:` branch is not written, and the `Read` matcher is downstream of it"
type: decision
status: current
authority: serve-the-rule-authority-branch
binding: deferral
basis: code
sprint: S3
decided: 2026-08-30
created: 2026-08-30
target_kind: action
target: serve-the-rule-ps1-matches-on-authority-and-is-registered-on-read
sources: ["archive/2026-08-30/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md", ".claude/hooks/serve-the-rule.ps1"]
tags: [harness, vault, agents]
---

# Context

**`.claude/hooks/serve-the-rule.ps1` was designed with two matchers**: by path, reading `governs:`,
for harness files that carry no frontmatter; and by `authority:`, for pages under `wiki/`, which is
the half described as covering "580 pages no mechanism reached before"
([[the-rule-server-hook]]).

**The journal of the day it was built records the second half as "implemented and dormant", waiting
only on a `Read` matcher.** That is what the file's own header says as well.

**Read off the code: it is not implemented.** `$slug` is assigned at line 123 and never read again;
the only match is a path equality test against `governs:` at line 145, and the record it appends
carries `Kind = 'governs'`. There is no second branch.

# The question

**What is actually owed before a rule found by its slug reaches anybody?**

# How it works after

**Two things are owed and they are ordered.**

1. **The `authority:` matching branch is written.** Without it a page under `render: authority` cannot
   be served by any matcher the hook has, because the only one it has keys on the field such a page is
   forbidden to carry
   ([[a-rule-under-render-authority-is-written-into-no-file-and-found-by-its-slug]]).
2. **The `Read` matcher is registered, and the path silence is reconsidered with it.** The hook exits
   at line 86 for every path under `wiki/` and `archive/` and for the six registers — a silence
   written to keep it quiet during an ingest. **As it stands that silence swallows the whole
   `authority:` half**, whose subject is exactly those pages, so wiring `Read` today would deliver
   nothing.

**What is measured and what is not.** Read frequency per session has never been measured by anyone,
and it is the most frequent tool call there is. The write path fires **71 to 108** times a session at
**750–930 ms** each. The 99 ms and 141 ms figures the design was priced on are void — taken without
stdin ([[a-process-is-measured-with-the-stdin-it-will-have]]).

**No sprint is named.**

# Recommendation

**Record the correction with the deferral rather than beside it.** The deferral as the journal states
it — *the `Read` matcher* — is the smaller half and it is downstream. A reader acting on the journal's
version would wire a matcher onto a branch that does not exist and observe nothing, which reads as
the mechanism working and finding no rules.

**And the `render: authority` value now fails the admission test its own schema comment asserts it
passes** — a value with a reader from the day it was minted. The gate reads it in three places; the
delivery does not exist. **That is the same defect `status: repealed` was minted with**
([[a-rule-with-no-instrument-behind-it-is-a-rule-a-fixture-can-violate-for-a-week]]), on the same day,
and nothing live said so.

**Rejected: wiring the `Read` matcher first**, and rejected: recording the deferral in the journal's
own words.

# Ratification

**The owner deferred the `Read` matcher, 2026-08-30**, to its own decision after a measurement rather
than accepting an unbounded multiplier on a cost he had been quoted. **The correction below it is the
librarian's, read off the file**, and it changes what the deferral is rather than whether it stands.

# Both owed items were built on 2026-08-31, and the measurement that closed the second falsified this page's own premise

**The two things this deferral ordered are done, in the order it ordered them.** The `authority:`
matching branch was written first; the `Read` matcher was registered after it, and the path silence was
reconsidered with it and split by mode
([[the-hook-matches-the-exact-slug-and-resolves-nothing-through-the-register]], [[the-rule-server-hook]]).

**The clause that priced the deferral is false, and it is the interesting half.** This page says *"Read
frequency per session has never been measured by anyone, and it is the most frequent tool call there
is."* Counted across every transcript this project has: **Bash 5088, Edit 1102, Read 490, Agent 395,
Write 392, Grep 49.** `Read` is the **fourth**, and about a third of the `Edit|Write` path, because this
repository reads with `cat` and `grep` rather than with the tool. The clause is `basis: code` and the
new figure is `basis: measurement`, so there is no rank conflict to settle — the sentence is simply
wrong and is dated here rather than struck.

**The deferral's own precondition is what produced the number that retired it.** The owner deferred the
matcher pending a measurement rather than accept an unbounded multiplier on a cost he had been quoted;
the measurement came back an order smaller than the premise, and the item closed on it. **Registering
the matcher adds about a third to a hook that already fires 71 to 108 times a session** — and the
per-call cost fell rather than rose, at 389–478 ms on the write path and 392–450 ms on the read path
with 36 rule pages ([[a-process-is-measured-with-the-stdin-it-will-have]]).

**This page does not leave `wiki/decisions/` on that account.** It carries `target_kind: action`, and a
decision with an action target waits for `wiki/tasks/`
([[no-decision-with-an-action-target-can-close-until-tasks-exist]]). What the archiver does with it is
the archiver's; nothing is marked here.

*(Compiled from `raw/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md`, whose `Entities` section states the opposite and is left as it was written, and extended at the ingest of `raw/handoffs/2026-08-31-the-families-become-rules.md`.)*
