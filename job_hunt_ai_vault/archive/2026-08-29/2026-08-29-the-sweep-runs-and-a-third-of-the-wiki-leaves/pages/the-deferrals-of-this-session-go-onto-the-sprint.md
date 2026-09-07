---
title: "The unstarted work of 2026-08-20 goes onto `sprint.md` rather than into a brief"
type: decision
status: archived
authority: session-deferrals
basis: human
binding: deferral
sprint: S2
decided: 2026-08-20
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock/handoffs/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock.md", "sprint.md"]
tags: [vault, process, agents]
---

# Deferred 2026-08-20, and the destination is the point

**Rejected: leaving any of them in the brief's *next* list.** A brief is derived and regenerated at
every ingest, so an item living only there is re-asserted by a document nobody is accountable to
and falls out the first time attention goes elsewhere — with no artefact recording that it did
([[the-record-schema-sweep-and-the-trim-candidates-go-onto-the-sprint]],
[[the-growth-signal-is-the-brief]]).

| deferred | the consequence of not doing it |
|---|---|
| **the `render:` default removal** — named by the owner this session, never started; `render` is in neither block of `wiki/concepts/_schema.yaml` | **the default is a trap for the next concept page written**, and the change is three moves in one order, one of them code ([[render-is-reinstated-and-required-now-that-another-mode-has-a-writer]]) |
| **the prose-path detector** — named by the owner this session, never started | three `wiki/` pages still name `.claude/agents/vault-librarian.md` five days after the file moved, and **nothing reports it** ([[a-path-detector-for-prose-references]]) |
| **the English translation of `tests/integration/test_migrations.py`** — 206 Cyrillic lines of 951 | **the file is mixed-language by this session's hand**, eight English lines above them ([[the-english-rule-is-forward-only-and-the-unit-is-the-file]]) |
| **per-session rotation of `log.md`** — raised by the owner and explicitly not built | `log.md` keeps growing ([[log-md-rotates-per-session-into-the-dated-archive]]) |
| **the scout design for cutting the ingest's wall clock** — measured, not built | the ingest stays one long round trip ([[read-only-scouts-one-per-folder-ahead-of-the-librarian]]) |
| **whether `ask-the-vault.ps1` fires for a subagent's writes** — documented, not verified | **an existing guard's reach is believed rather than known** ([[hooks-in-the-settings-file-apply-inside-subagents]]) |
| **that the librarian lock fires at all** — hooks are read at session start, so nothing in the session that built it could show it | **a lock that is silently absent looks exactly like a lock with nothing to say** ([[the-librarian-lock-hook]]) |

## The last two are not deferrals in the same sense

They are **unverified claims**, not unstarted work. Each has an acceptance test that costs one move
after a restart, and each is on this list so that the interval between *built* and *proved* is a
written interval rather than an assumption.

**No ordering is decided here.** `sprint.md`'s *next* line is where the order is read from, and it
is the owner's ([[a-sprint-closes-on-its-goal]]).

# The second session of 2026-08-20 deferred another list, on the same policy

**Same destination, same reason.** These are on `sprint.md`, not in a brief.

| deferred | the consequence of not doing it |
|---|---|
| **the prose-path detector**, sprint item 2 — untouched; it gained a measurement and nothing else | the corpus carries five wrong references and **the gate reports none of them**: it saw four of nine and was blind to five ([[a-path-detector-for-prose-references]]) |
| **the run of the migration tests**, owed against a condition rather than a date | a narrow claim stands until somebody runs them, and a narrow claim read as a broad one is how a hole ships inside verified work ([[a-deferred-check-must-be-run-when-its-condition-arrives]], [[a-hole-was-shipped-in-work-already-reported-as-verified]]) |
| **the green-gate selftest case** on a red tree | the next person to run the suite on a red tree reads a broken lock ([[the-green-gate-selftest-case-is-deferred-and-the-fixture-repair-cannot-reach-it]]) |
| **whether the `values:` copy becomes a rule** | the next field admitted to a second folder rediscovers it, or does not ([[the-legal-value-list-lives-in-each-folders-schema]]) |
| **whether [[product-work-does-not-interleave-into-the-vault-sprint]] needs a clarifying line** | the page is not wrong and the owner read it as contradicting a vault task, which is the evidence ([[a-librarian-answer-that-stops-at-the-agent-boundary-is-not-an-answer-the-owner-has]]) |
| **whether the scouts proposal is re-priced** on today's dispatch measurements | its per-dispatch floor is argued against the ingest's cost, and a narrow dispatch is already cheaper ([[read-only-scouts-one-per-folder-ahead-of-the-librarian]], [[a-cost-figure-attached-to-the-wrong-unit-discourages-the-thing-it-prices]]) |
| **migration warning language** — `0008` prints English, `0004`–`0007` print Russian | what an owner sees running `alembic downgrade` is two languages depending on the revision ([[the-language-of-a-migration-warning-is-unsettled]]) |

**Two alarms are carried untouched rather than deferred**: the `raw/`-emptying hazard's open half —
whether the same shape sits elsewhere in that plan, which nobody has looked at
([[failing-loudly-with-the-wrong-diagnosis]]) — and the gate's cost, which is on the *raised and
explicitly not built* list ([[the-gates-cost-grows-with-the-corpus-and-rule-pages-are-the-minor-term]]).

**The three items this page listed as unstarted are closed**: the `render:` default removal, in all
three moves ([[an-absent-render-is-red-on-a-page-that-renders]]); the English translation
([[the-migration-test-translation-stands-with-its-remaining-cyrillic]]); and both unverified claims,
which were acceptance tests rather than work
([[a-tree-broken-for-a-real-reason-is-a-better-fixture-than-a-planted-offender]]). **The prose-path
detector and `log.md` rotation are not.**

# The destination held and the conversations still did not happen — 2026-08-21

**Three items the owner deferred to the session of 2026-08-21 by name moved into a fourth
consecutive session** — the seventh S2 criterion, a machine-readable format for the registers, and
the fog finding. **Each was on `sprint.md`, exactly where this decision put it.**

**So the destination is not the failing half, and this page is not weakened by it.** What the ruling
protects against — an item living only in a regenerated brief and falling out with no artefact — did
not happen: there is an artefact, it says the same thing it said yesterday, and nobody read it at
the moment it mattered.

**The pattern is recorded as its own lesson rather than as a defect in this decision**
([[a-conversation-the-owner-scheduled-is-displaced-by-the-work-beside-it]]).

*(Compiled from `raw/handoffs/2026-08-21-the-mechanisms-are-wired-and-a-pre-task-changes-the-work.md`.)*

# It reaches an unbuilt plan as well as an unstarted item — 2026-08-26

**The owner selected it**: the committed plan's unbuilt half goes into `sprint.md` **line by line**,
rather than into a second plan document, **because the plan already exists and is committed**
([[the-plan-is-committed-and-the-execution-moves-to-a-session-of-its-own]]).

**Nine items, each a line**: B1, B4, C1, C2, C3, D, E4, E5 and `vault-measure.py --refresh`. **Two
of them are addressed elsewhere and the sprint line says so** — B1's second half is aimed at the
wrong rule page, and D's deletion of a stated count is discharged by a move on the hub
([[the-vault-scripts-page-stays-a-hub-and-the-gate-and-its-suite-get-subject-pages]]).

**The rejected alternative was a second plan document.** Two plans for one body of work is a copy,
and this store repairs a copy by not making it
([[a-copied-list-drifts-and-a-sweep-cannot]]).
