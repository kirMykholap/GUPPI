---
title: "A register of what each hook writes when it is probed, and the collector flagged it as its own weakest"
type: proposal
status: current
authority: hook-side-effect-register
basis: inference
sprint: S3
created: 2026-08-26
decided_by: [[the-lessons-collector-is-a-reading-dispatch-and-the-librarian-writes-what-it-returns]]
sources: ["archive/2026-08-26/2026-08-26-the-harness-half-is-built-and-the-owner-rules-how-the-vault-empties-itself/handoffs/2026-08-26-the-harness-half-is-built-and-the-owner-rules-how-the-vault-empties-itself.md", ".claude/hooks/catch-the-feedback.ps1"]
tags: [harness, testing, process]
---

# What it would be

**A register naming, per hook, what it writes when it runs** — which file, under what condition, and
whether a probe against the repository copy touches live state. It would be read before anyone feeds
a hook a payload by hand.

# The evidence, and it is two measured instances

**A `SessionStart` probe rotated the real ledger**
([[testing-a-session-start-hook-with-a-made-up-payload-has-live-side-effects]]).

**And on 2026-08-26 a probe of `catch-the-feedback.ps1` was run against the repository copy rather
than a sandbox and filed a fabricated record** — `- decision: the owner said it - «де»` — into
`.superpowers/sdd/vault-feedback.md`. It was dropped at the drain rather than compiled, because it
is a test payload and not testimony; filing it would have put four Cyrillic letters in the owner's
mouth ([[a-block-attributed-to-the-owner-is-written-in-his-own-russian]]).

**That second instance happened in the session that read the first lesson and quoted it back the
same hour.** Knowing the rule did not stop it ([[knowing-a-rule-is-not-a-mechanism]]).

# Why the collector called it the weakest of its five

**One measured loss at the time it was drafted, and three neighbours the check does not cover.** A
register is a document, not an instrument: nothing verifies it, nothing updates it when a hook gains
a write, and this store has a standing verdict that a maintained list always drifts
([[a-printed-register-cannot-drift-and-a-maintained-one-always-has]],
[[a-copied-list-drifts-and-a-sweep-cannot]]).

**The second instance strengthens the case for the class and not for this form.**

# What is open, and one alternative is probably better

- **A generated register beats a written one.** What a hook writes is in its source; a sweep for
  write calls per hook file would be a printed register rather than a maintained one.
- **A sandbox for hook probes** would remove the failure instead of documenting it — the same shape
  as the plant-and-revert helper ([[a-plant-and-revert-helper-for-the-real-tree]]).
- **Neither is designed**, and this proposal is filed as it stands rather than replaced by the
  better idea it points at.

# Its `decided_by:` will need re-pointing

**It names the decision that created the collector**, because no per-topic ruling exists for it. The
field moves the day the owner rules on this proposal.
