---
title: "The archive sweep reports a refusal, and the gate stays silent about placement"
type: decision
status: archived
authority: archive-sweep-reporting
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-25
created: 2026-08-25
sources: ["archive/2026-08-25/2026-08-25-the-twelve-items-are-decided-and-the-owner-names-what-the-discussion-costs/handoffs/2026-08-25-the-twelve-items-are-decided-and-the-owner-names-what-the-discussion-costs.md", "scripts/vault-archive.sh", ".claude/skills/vault-lint/SKILL.md"]
tags: [vault, harness, process]
---

# The ruling, 2026-08-25

> **owner:** «твоя рекомендация принимается»

**A page the sweep cannot move is reported by the sweep, at `/vault-lint`, with a non-zero exit and
counts of what moved and what was refused.** The sweep lives inside `scripts/vault-archive.sh`, where
the ruling of 2026-08-24 put it ([[the-archive-mover-is-a-sweep-inside-the-archive-script-at-the-lint-stage]]).

**`scripts/vault-check.sh` says nothing about placement.** A page sitting in the wrong folder is not
a gate verdict.

**Rejected: red in the gate**, on the deadlock this repository has already built once — a red gate is
read by `lock-the-librarian.ps1` as a refusal to dispatch, locking out the only writer who could move
the page ([[a-lock-on-a-red-tree-hides-the-health-of-what-it-guards]]). **Rejected: a standing
advisory**, which is the alarm class this session is removing
([[an-alarm-that-fires-when-nothing-is-wrong-is-one-you-learn-not-to-read]]).

# The first run is measured before it exists

**Read off the `status:` lines in `wiki/`: two pages carry a status obliging a move, both
`status: implemented` and both in `proposals/`** — `a-style-rule-for-the-prose-a-session-writes` and
`a-verdict-pairing-the-idea-status-with-a-named-decision`. **`deprecated` is zero and `refused` is
zero.**

**Both pass the archive precondition** — cited by six and four live pages — so the sweep's first run
moves both and refuses nothing. **So the refusal path is unexercised on the day it was designed**,
and that is a property of the corpus rather than of the design
([[a-new-verdict-is-proved-in-the-real-tree-because-the-check-cannot-see-a-sandbox]]).

# The hand-written divergence beside it names one page and there are two

**`a-verdict-pairing-the-idea-status-with-a-named-decision` took `status: implemented` in the same
session and its breach is recorded nowhere**
([[divergence-an-implemented-proposal-stays-in-the-proposals-folder-because-nothing-moves-it]]). **A
hand-written divergence records what somebody noticed**, which is the argument for the sweep rather
than an argument about that page.

# Not done

**No sweep exists.** `scripts/vault-archive.sh` moves only what it is given as an argument and
searches for nothing.
