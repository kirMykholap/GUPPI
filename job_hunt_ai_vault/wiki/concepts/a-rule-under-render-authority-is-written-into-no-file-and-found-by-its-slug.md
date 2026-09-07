---
title: "A rule under `render: authority` is written into no file and found by its slug"
type: concept
status: current
authority: lookup-rule-delivery
basis: code
sprint: S3
created: 2026-08-30
sources: ["archive/2026-08-30/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md", "job_hunt_ai_vault/wiki/rules/_schema.yaml", "scripts/vault-check.sh", ".claude/hooks/serve-the-rule.ps1"]
tags: [harness, vault, record-schema]
---

# The mode

**`render:` took a third value on 2026-08-30 and it is the first one that renders nothing.** A rule
page under `render: authority` is injected into no file at all. It carries an `authority:` slug and
**no** `governs:`, and a hook is supposed to find it at the moment a file that slug answers for is
touched.

| `render:` | where the text goes | what the page carries |
|---|---|---|
| `region` | a paired marker inside a file with a life of its own | `governs:`, one `<!-- text -->` slice |
| `whole` | a generated file the injector owns end to end | `governs:`, `paths:` |
| `authority` | **nowhere** — it is fetched | `authority:`, no `governs:`, no slice |

**`authority:` became legal in `wiki/rules/` in the same change**, having been forbidden there since
2026-08-21. The old ground was that a rule answering with a slug would collide with the decision
stating it; that ground went when rule 3 of the gate narrowed to comparing slugs **within a type**
([[authority-uniqueness-becomes-a-per-type-question]]).

# The condition lives in the gate, because a per-folder schema cannot state it

**`governs:` moved from `required:` to `optional:` in `wiki/rules/_schema.yaml`.** It is required in
practice for the two rendering modes and forbidden for this one, and no `_schema.yaml` can say
*required unless another field says otherwise*. So the `nogoverns` verdict reads `render:` before it
fires. **That is the arrangement `paths:` already had**, in the other direction
([[a-conditional-requirement-is-refused-by-the-script-that-moves-the-page]],
[[paths-is-required-where-it-is-read-and-nowhere-else]]).

**Two verdicts of its own keep the mode from being a per-page waiver:**

- `authoritygoverns` — a lookup rule that also names a destination is red.
- `authoritynoslug` — a lookup rule with no slug to be found by is red.

# The value has a writer and a reader — except that it does not, yet

**The admission test this store applies after minting `status: repealed` with no reader is that a
value has both from the day it exists.** The schema comment for `render: authority` asserts it passes:
*"the gate branches on it in three places and the hook is what delivers it."*

**Read off the code on 2026-08-30, the delivery half is not there.**
`.claude/hooks/serve-the-rule.ps1` parses `authority:` into a variable at line 123 and **never reads
it again**. Its only match is a path equality test against `governs:` at line 145, and the single
record it appends carries `Kind = 'governs'`. There is no second branch.

**So a page under `render: authority` cannot be served by that hook on any matcher**, because the only
matcher it has keys on the field such a page is forbidden to carry. **And the hook exits silently for
every path under `wiki/` and `archive/` and for the six registers**, so even once a branch exists and
a `Read` matcher is wired, the half described as covering "580 pages no mechanism reached before"
reaches none of them as the silence is written today.

**Zero pages carry `render: authority` today** — fifteen `region`, two `whole` — so nothing is
mis-delivered while this stands. The gate half is real and fires; the delivery half is owed
([[the-hooks-authority-branch-is-not-written-and-the-read-matcher-is-downstream]]).

**This paragraph is `basis: code` and the journal that occasioned it says the branch is
"implemented and dormant".** The code is the stronger source and it is what is recorded here.

# Why a third mode rather than a seventh folder

**The folder set is closed and a rule is still what this is** — text written to reach a reader who did
not come looking ([[the-folder-set-is-closed-and-tasks-is-not-in-it]]). What changed is the carrier,
and the carrier is exactly what `render:` names. A fourth route also joins the delivery table on
[[a-rule-reaches-a-session-by-several-routes-and-only-one-transition-had-a-gate]], which is where the
gate on moving a rule to conditional delivery reads it.

# The delivery half exists now, and the section above it is dated rather than struck — 2026-08-31

**Everything under *The value has a writer and a reader — except that it does not, yet* was true on
2026-08-30 and is false from 2026-08-31.** It is left standing because it is the record of a value
minted without the delivery its own schema comment claimed for it, which is a shape this store keeps.

**What the hook does now, read off `.claude/hooks/serve-the-rule.ps1`.** It reads `render:` and
`tool_name`, neither of which it read before. A page whose `render:` is `authority` is matched on the
`authority:` slug of the file being touched, **by string equality, with nothing resolved through
`job_hunt_ai_vault/authority.md`** — a hash lookup rather than a walk, and the family register is not a
runtime dependency ([[the-hook-matches-the-exact-slug-and-resolves-nothing-through-the-register]]).
`paths:` is gone from the file entirely.

**The silence is scoped by mode as well as by path, and that is what gives the half an occasion to
fire.** Silent on `Edit|Write` inside `wiki/`, speaking on `Read` there, silent in `archive/` and on
the six registers in both directions, and ending the run at once on a `Read` outside the vault, so each
half fires on one mode. **A slug exists only under `wiki/`, which is exactly where the write path is
silent** — with writes alone this half would have had no occasion at all. `.claude/settings.json`
registers the hook on `Read`, and that registration is what makes it reachable.

**The count in the paragraph above has moved.** It read *"Zero pages carry `render: authority` today —
fifteen `region`, two `whole`"*. On 2026-08-31 `wiki/rules/` holds 36 pages: **19 under
`render: authority`**, and the region and whole counts are unchanged at seventeen between them.

**The mode is delivered and its coverage is a separate number.** Fourteen of the nineteen carry a slug
that a live `concepts/` or `entities/` page also carries; five do not, and a rule matching a read of
itself is worth nothing ([[the-convergence-pass-over-the-live-non-decision-pages]]).

*(Compiled from `raw/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md`, and extended at the ingest of `raw/handoffs/2026-08-31-the-families-become-rules.md`.)*
