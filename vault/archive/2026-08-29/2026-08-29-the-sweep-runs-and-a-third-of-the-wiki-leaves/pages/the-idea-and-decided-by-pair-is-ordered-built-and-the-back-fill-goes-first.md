---
title: "The `idea` and `decided_by:` pair is ordered built, and the back-fill goes first"
type: decision
status: archived
authority: idea-decided-by-pairing
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-23
created: 2026-08-23
sources: ["archive/2026-08-23/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands/handoffs/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands.md", "job_hunt_ai_vault/wiki/proposals/_schema.yaml", "scripts/vault-check.sh"]
tags: [record-schema, vault, harness]
---

# The ruling, at the retro of the second session of 2026-08-23

> **owner: нужно построить**

**A verdict pairing `status: idea` with `decided_by:` is to be built.** The design is
[[a-verdict-pairing-the-idea-status-with-a-named-decision]].

# It is a reversal, and both halves belong on this page

**The session built the pair from his own sentence and then dropped it the same hour.** Its two
arguments are recorded in `wiki/proposals/_schema.yaml` as the reason no such verdict exists:

- **it would make `status` mean *authorisation* where his ruling of 2026-08-17 makes it mean
  *maturity*** ([[an-idea-is-a-proposal-with-an-immature-status]]) — a fully designed proposal that
  no decision produced would have to assert an immaturity it does not have, and a half-thought one
  produced by a deferral decision could not be an `idea` at all;
- **the verdict would redden every page in `wiki/proposals/` on the day it landed**, because none
  of them carries the field.

**The objection was raised twice and overruled twice.** It is kept here rather than dropped: the
reasoning is what the session that builds the pair has to answer, and the schema comment recording
it is now stale in its conclusion and accurate in its argument.

# The ordering is part of the item, and it is not optional

**The verdict must follow the back-fill of `decided_by:` across `wiki/proposals/`, never precede
it.** Landing first reddens the gate on every page in the folder at once, and
`lock-the-librarian.ps1` reads a red gate as a refusal to dispatch — locking out the only writer
permitted to do the work that would clear it
([[a-lock-on-a-red-tree-hides-the-health-of-what-it-guards]], [[the-librarian-lock-hook]]).

**The same order was already forced twice**, on `authority:` and on `basis:`, and it is written
down: legal and optional, then the back-fill, then promote
([[the-unknown-key-verdict-orders-a-schema-change-ahead-of-the-page-that-uses-the-field]]).

# The back-fill is the blocking item and it is measured

**Read off the tree on 2026-08-23, at the ingest of this journal:**
`bash scripts/vault-check.sh --lint` names every page in `wiki/proposals/` and `wiki/rules/`
carrying no `decided_by:`, and every page it names is a `proposals/` page — the rules folder is
full. That count is the work this ruling waits on
([[decided-by-is-legal-in-proposals-and-rules-and-required-in-rules]]).

**Nothing here fills it.** The back-fill is a judgement about which decision caused each proposal,
one page at a time, and it is a session's item rather than a sweep's — the same shape as the
`wiki/rules/` fill, where four of fifteen pages stated their own cause in prose and the rest had to
be argued ([[the-ask-before-weakening-rule-is-ratified-after-being-enforced-without-a-decision]]).

# The verdict is ordered built on 2026-08-24, and the standing objection was resolved rather than overruled a third time

**The owner selected "build it", after seeing both recorded objections for the first time.** The
first of them — that `status:` reports maturity and an unauthorised proposal is not immature — he
answered in his own terms rather than setting aside:

> **owner: не вижу противоречий. status отображает зрелость - все верно. idea - незрелый.
> implemented - максимально зрелый, так как реализован, а механичсеки(скриптами) подкреплен полем
> decided_by. current - в процессе созревания. ТАкже механически подкреплен decided_by. Полностью
> продуманный замысел, который никто не заказывал - idea. У него нет поля decided_by, он родился
> потому что так захотелось пользователю.**

**So a fully designed proposal nobody ordered is immature in the sense the field means**: it has no
decision behind it, and `decided_by:` is the mechanical support the other two values carry.

**The ordering above is untouched: back-fill first, verdict second.** The back-fill's method was
decided the same day — read off each page's `sources:`, never swept
([[the-decided-by-back-fill-is-read-off-each-page-and-never-swept]]).

**Neither half is built.** The verdict is ordered and the back-fill is specified; the tree carries
neither, and a `/pre-task` corrected the plan's description of the deferral from *an override of a
prohibition* to **a deferral of the verdict** — the ordering this page forbids was never in question
([[a-plan-can-be-factually-wrong-about-the-tree-and-the-pre-task-is-what-reads-the-tree]]).
