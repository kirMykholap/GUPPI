---
title: "The approved-scope bit survives a `/compact` and not a `/clear`, by construction"
type: decision
status: current
authority: approved-scope-lifetime
binding: prohibition
basis: inference
sprint: S2
decided: 2026-08-20
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact/handoffs/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact.md", "archive/2026-08-20/2026-08-20-the-ingest-picks-by-sidecar-and-the-owner-cannot-see-the-harness/handoffs/2026-08-20-the-ingest-picks-by-sidecar-and-the-owner-cannot-see-the-harness.md", ".claude/hooks/pre-task-state.ps1"]
tags: [harness, agents, process]
---

# The behaviour, and it is not a special case

**A `/compact` keeps the session identifier and the approved scope did not change**, so the ledger
rows keyed on that identifier are still the session's and the plan path still finds a pre-task newer
than the last approved scope ([[the-pre-task-state-machine-has-a-flag-for-the-plan-and-a-flag-for-the-write]]).

**A `/clear` starts a conversation that knows nothing of the plan**, and the bit is not inherited.

**Nothing in the code says either sentence.** Both fall out of keying the ledger on `session_id` —
which is why the behaviour is worth recording as a decision: it was chosen by *not* writing a
special case, and a later reader will otherwise look for the branch that implements it.

# It rests on an unmeasured property

**Whether `session_id` survives a `/clear` has never been measured here.** If it does survive, an
approved scope reads as surviving into a context that no longer knows the plan — the failure
direction is *asking less often*, which is the wrong one for a guard.

**The repair, if the property is wrong, is one line**: a reset from the `SessionStart` hook, whose
matcher already names `clear` ([[session-hooks]]). It is deferred against the measurement rather
than against a date ([[a-deferred-check-must-be-run-when-its-condition-arrives]]).

**Rejected: measuring it before shipping.** A `/clear` is cheap to perform and expensive to arrange
inside a working session, and the consequence is bounded by a repair that is already designed.

# The repair was built the same day, and the measurement it waited on was withdrawn — 2026-08-20

**The one-line repair named above exists.** `.claude/hooks/session-brief.ps1` appends a
`session-start:<source>` row and `Read-LedgerState` resets the state on `session-start:clear`, which
closes the deferral this page opened ([[the-session-start-row-is-the-instrument-the-reset-and-the-rotation-signal]]).
**It shipped before the measurement**, which the page's own rejected alternative had allowed for:
the branch is correct under either answer, because a surviving identifier makes the reset land on a
state that is already empty.

**The measurement was then withdrawn by the owner rather than deferred against a condition.**
**owner:** «нет. снимаем, как убираем. Не делаем.» It was offered at the retro of 2026-08-20 and he
took it off the list.

**What that costs, exactly:** this page stays `basis: inference` and unmeasured. Whether
`session_id` survives a `/clear` is still unknown here, and the sentence *"nothing in the code says
either sentence"* is now half false — the `clear` half is written in code, the `compact` half is
still an absence of one. **Withdrawing it costs nothing operationally**, which is why it was
withdrawable: the branch built that night is correct either way.

**Written here so the next session does not re-offer it as owed**
([[a-deferred-check-must-be-run-when-its-condition-arrives]] does not apply — there is no condition
left to arrive).
