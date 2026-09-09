---
title: "The compaction probe runs after the ingest, and the AST rule's move waits on it"
type: decision
status: current
authority: compaction-probe-sequencing
binding: deferral
basis: human
sprint: S2
decided: 2026-08-19
created: 2026-08-19
sources: ["archive/2026-08-19/2026-08-19-the-corpus-stops-counting-and-the-gate-learns-its-keys/handoffs/2026-08-19-the-corpus-stops-counting-and-the-gate-learns-its-keys.md", "archive/2026-08-20/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock/specs/RUNBOOK.md"]
tags: [harness, agents, testing]
---

# Deferred 2026-08-19, and the ordering is the reason

**The last of the probe's questions — after `/compact`, does `Edit` demand a re-read — is not run,
and it is sequenced after `/ingest`.**

It needs `/compact`, and **compaction before the ingest risks the journal to buy a measurement about
a proposed refactor.** The journal is the only thing the next session inherits
([[journal-vault-brief-each-artefact-has-one-owner]]); the measurement is about whether a rule
delivered on a read survives a compacted context, which decides the wiring of a move that has not
happened. **A risk to the record against a fact about a proposal is not a trade this project makes.**

**Rejected: running it earlier in the session, before the ritual.** That is the same trade with the
order disguised — the ritual would then run in a compacted context, which is the state it was written
not to depend on.

# What it costs to not do it

**The probe directory stands.** Five artefacts stay in the tree — the rules file, the target, the
runbook, the hook and the settings block — and clearing them is what the last probe is owed
([[the-conditional-delivery-probe]]).

**Region coverage stays at `1 of 14`** rather than returning to `1 of 13`, because `.claude/rules/`
holds the probe file and the governed set is swept rather than listed
([[the-governed-set-is-swept-and-markdown-by-property]],
[[the-governed-denominator-may-grow-and-the-criterion-stays-a-file-count]]).

**And the AST rule's move stays blocked.** This is the correction of a claim made earlier the same
session: the subagent probe passed and *"the move is unblocked"* was said, but **that probe was
never the only gate.** The compaction probe's own stated consequence decides whether the re-read
re-triggers the rule, and that is the case the move most depends on
([[the-ast-rule-moves-to-prove-the-mechanism]],
[[a-scoped-rule-fires-on-a-read-and-an-edit-implies-one]],
[[what-reaches-a-subagent-a-scoped-rule-does-and-an-html-comment-does-not]]).

# What it needs, written down so the next session does not re-derive it

`/compact`, then **an edit attempt on `probe/probe-target.md` without reading it first**. If `Edit`
demands a re-read, the compaction question closes: the re-read re-triggers the rule and delivery
survives compaction. The runbook holds the full method, and it is read with the caveat that reading
it contaminates the reader
([[a-runbook-that-carries-the-nonce-cannot-be-read-by-what-it-measures]]).

# It ran, and the answer is the one the move most feared — 2026-08-19

**The sequencing was carried out as decided and the probe ran after the ingest.** Its answer: **the Edit
proceeds without a re-read.** The compaction question does not close on its own — the scoped rule is
dropped by `/compact`, the Edit tool's read gate is session-scoped and survives it, and the edit lands
with no rule in context and no signal that one is missing
([[what-survives-a-compaction-is-whatever-has-something-that-runs-it-again]]).

**So the blocker on the AST move changed rather than lifted.** It was this probe; the probe is answered;
**it is now the guard** ([[the-guard-is-not-built-and-the-ast-move-now-waits-on-it]],
[[a-guard-branch-in-the-edit-hook-delivers-a-path-scoped-rule]]).

**This page's own correction stands vindicated.** It said the subagent probe *"was never the only gate"*
and that this one decides the case the move most depends on. It did, and it decided against.
