---
title: "The sprint close reviews the repeal decisions as a set"
type: decision
status: archived
authority: repeal-decision-review-cadence
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-30
created: 2026-08-30
target_kind: action
target: the-sprint-close-reviews-the-repeal-decisions
sources: ["archive/2026-08-30/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form/handoffs/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form.md", ".claude/skills/sprint/SKILL.md"]
tags: [vault, process, harness]
---

# Context

**A `target_kind: repeal` decision never leaves `wiki/decisions/`.** `scripts/vault-archive.sh`
refuses to release one absolutely, because once the page it cancelled reaches `archive/` that decision
is the only live carrier of the fact that the thing no longer exists
([[a-cancelled-page-takes-a-status-of-its-own]]).

**So the folder now has a class of page that only grows**, by design rather than by neglect. Nothing
reads it as a set.

# The question

**What stops a permanently-live class from becoming a pile nobody looks at?**

# How it works after

**`.claude/skills/sprint/SKILL.md` gains a mandatory step at the sprint close: review the decisions
carrying `target_kind: repeal` as a set.** The catalogue of what was cancelled is a command over those
live decisions rather than a maintained file, so the step is a reading and not a write.

# Recommendation

**A review step rather than an archival route.** Giving repeal decisions a way out would remove the
only live carrier of the absence, which is the whole reason they stay.

# Ratification

**The owner said it**, on 2026-08-30: «Это норамльно на первое время, но добавить обязательный пункт
обсудить архивацию таких страниц перед закрытием спринта». He then selected it again by approving the
plan of the same day.

**Not built.**

*(Compiled from `raw/handoffs/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form.md`.)*
