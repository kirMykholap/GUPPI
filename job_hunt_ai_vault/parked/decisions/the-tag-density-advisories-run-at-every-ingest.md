---
title: "The tag-density advisories run at every ingest, and the owner ruled with the reason against it in front of him"
type: decision
status: current
authority: advisory-cadence
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-21
created: 2026-08-21
sources: ["archive/2026-08-21/2026-08-21-the-mechanisms-are-wired-and-a-pre-task-changes-the-work/handoffs/2026-08-21-the-mechanisms-are-wired-and-a-pre-task-changes-the-work.md", ".claude/skills/ingest/SKILL.md", "scripts/vault-check.sh"]
tags: [vault, retrieval, process]
---

# The ruling, 2026-08-21

> **owner: механическую часть следует повесить на ingest.**

**`/ingest` now calls `bash scripts/vault-check.sh --lint` and a coverage pass over every source in
`raw/`, as step 11.** Neither call can fail the step; what they print is reported and the judgements
they feed — split a tag, or leave it — stay the owner's, made at `/vault-lint`.

**This overturns the decision of 2026-08-20 that moved those lines behind the flag**, and **the
reason recorded there is not refuted**: an always-firing advisory stops being read, and this store
has four separate costs of one on the record ([[the-tag-density-advisories-move-behind-lint]],
[[the-dense-tags-are-not-split-and-the-standing-advisories-are-named-here]],
[[an-alarm-that-fires-when-nothing-is-wrong-is-one-you-learn-not-to-read]]).

# What changed is the standing of the figures, not the argument about them

**They became a finding rather than background.** `vault` selects **124 of 193** pages in
`decisions/`, `process` 106, `harness` 98, against a threshold of ten. A tag carried by 64% of a
folder classifies nothing, and **a finding nobody sees is worse than one they tire of.**

**The mechanism the earlier decision built is untouched.** The flag still exists, the bare run still
prints only what is about that run, and the exit code is still identical with and without it
([[severity-in-the-gate-is-decidable-which-is-what-lets-a-flag-be-safe]]). What moved is **who
calls it**: `/vault-lint` was the only caller, and is not any more.

**`/vault-lint` is defined per sprint and had therefore never run against this corpus**
([[lint-waits-for-an-open-sprint]]). That is the gap the ruling closes: the channel was correct and
its only consumer was a ritual with no cadence.

# The half that is not contested

**The coverage loop over every source in `raw/` is a different instrument.** It reads every source
rather than the one being compiled, so it reports an ingest left unfinished on an earlier day — and
on the day it was wired it found `15 verdicts are not verdicts` in the 2026-08-12 journal
([[handoff-retires-only-when-every-unit-has-a-verdict]], [[a-denominator-is-walked-off-the-input-list]]).

# What it obliges

**The advisory now prints every session until the tag verdict is given**, which is by construction
the shape the 2026-08-20 decision was avoiding. **If it is ever answered the call costs 11 s and
prints nothing** — so the cost of the cadence is bounded and the cost of the silence is not.
