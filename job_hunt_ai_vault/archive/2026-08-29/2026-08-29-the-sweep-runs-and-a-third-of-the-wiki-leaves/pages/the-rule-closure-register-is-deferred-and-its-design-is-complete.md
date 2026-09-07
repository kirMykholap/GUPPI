---
title: "The rule-closure register is deferred, and its design is complete"
type: decision
status: archived
authority: rule-closure-mark-deferral
binding: deferral
basis: human
sprint: S3
decided: 2026-08-25
created: 2026-08-25
sources: ["archive/2026-08-25/2026-08-25-the-twelve-items-are-decided-and-the-owner-names-what-the-discussion-costs/handoffs/2026-08-25-the-twelve-items-are-decided-and-the-owner-names-what-the-discussion-costs.md", "scripts/vault-check-selftest.sh", "scripts/session-dialogue-selftest.py"]
tags: [vault, harness, testing]
---

# What is deferred, 2026-08-25

**The register that says how each rule page closes its instrument obligation is not built**, and the
design behind it is finished rather than sketched
([[the-rule-closure-register-carries-a-case-name-or-a-decision]]).

**Rejected: doing it now.** The session was cut at the plan and the execution moved to a session of
its own ([[the-plan-is-committed-and-the-execution-moves-to-a-session-of-its-own]]).

**Estimated at an hour and a half to two hours**, which is a projection and not a measurement
([[a-projection-is-published-with-its-instrument-or-not-at-all]]).

# The consequence of not doing it

**Acceptance criterion 1 of S3 still has no decider that counts every way a rule can close.** The
decider names two selftest suites and reports `missed 0`; the criterion closes three ways
([[the-instrument-criterion-closes-more-ways-than-its-decider-counts]]).

**And the decider does not name every suite that exists.** `scripts/session-dialogue-selftest.py`
holds 32 cases and is invisible to it, so a Python instrument's cases cannot close anything today.

# The distinction the session drew wrongly on the way here

**It rejected a frontmatter field as *the shape of the withdrawn `quantity:` field* and then reversed
itself inside two messages.** The difference it landed on: `quantity:` declared an **exemption from a
check**, while a closure pointer names **where the answer is** and the gate verifies that the pointer
resolves — which is the accepted shape of `decided_by:`
([[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]],
[[decided-by-is-a-field-of-its-own-and-not-a-line-in-sources]]).

**Nothing in the vault draws that line**, and it is recorded here because the next session will meet
it again.
