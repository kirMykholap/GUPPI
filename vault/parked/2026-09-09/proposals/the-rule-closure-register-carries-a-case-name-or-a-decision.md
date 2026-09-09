---
title: "The rule-closure register: a field in `wiki/rules/` carrying a case name or a decision"
type: proposal
status: current
authority: rule-closure-register-design
basis: inference
sprint: S3
created: 2026-08-25
decided_by: [[the-rule-closure-register-is-deferred-and-its-design-is-complete]]
sources: ["archive/2026-08-25/2026-08-25-the-twelve-items-are-decided-and-the-owner-names-what-the-discussion-costs/handoffs/2026-08-25-the-twelve-items-are-decided-and-the-owner-names-what-the-discussion-costs.md", "scripts/vault-check-selftest.sh", "job_hunt_ai_vault/wiki/rules/_schema.yaml"]
tags: [vault, record-schema, testing]
---

# What it would be

**A `closed_by:` field in `wiki/rules/`, one entry per rule page, naming how that rule's instrument
obligation is closed.** Two spellings and no more:

- **`case:<name>`** — a selftest case, verified against the suite's own `--list` output
  ([[the-case-list-is-swept-from-the-file-because-some-cases-have-no-dispatcher]]);
- **a wikilink** — a decision page saying why no instrument is possible, verified as a
  `current` page whose `type` is `decision`, the shape `decided_by:` already has
  ([[decided-by-is-a-field-of-its-own-and-not-a-line-in-sources]]).

**The owner's own watch is the second spelling, not a third.** He watches the ask-before-weakening
rule himself, and that is a decision page saying what closes it
([[the-ask-before-weakening-rule-gets-a-claude-rules-file-and-the-owner-as-its-watcher]]).

# The order it would be built in, and the order is the design

**Declared optional, back-filled across every page in `wiki/rules/`, then promoted to required — and
the promotion is the acceptance test for the fill.** Required first reddens the gate, and
`lock-the-librarian.ps1` reads a red gate as a refusal to dispatch, locking out the only writer who
could fill the field ([[a-lock-on-a-red-tree-hides-the-health-of-what-it-guards]]). That order has
been applied here before, to `basis`, `authority`, `binding` and `decided_by:`.

# Why a register rather than a self-declaring field

**A field that declares no instrument is possible is the `quantity:` shape**, and it was minted and
withdrawn here because two of its declarations were false while they stood and nothing mechanical
caught either ([[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]]).

**A pointer is not a declaration.** It names where the answer is and the gate verifies that it
resolves. **The session drew that line wrongly first**, rejecting the field and then reversing inside
two messages ([[the-rule-closure-register-is-deferred-and-its-design-is-complete]]).

# What is open

- **Whether a rule may carry more than one closure.** Nothing here says what a page with a case *and*
  a decision means.
- **The mapping from a rule to the case that tests it exists nowhere in the tree and cannot be
  derived.** No selftest case in `scripts/vault-check-selftest.sh` or `scripts/hook-selftest.ps1`
  names a real rule slug — the fixtures are synthetic, `probe-rule` and `whole-rule`. **That is the
  same ground `authority.md` rests on**: what is derivable needs no register, and this is not
  derivable.

# What it would oblige

**Acceptance criterion 1 of S3 gains a decider that counts every way a rule closes**, which is what
it lacks today ([[the-instrument-criterion-closes-more-ways-than-its-decider-counts]]).
