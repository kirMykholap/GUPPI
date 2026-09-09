---
title: "A tag cannot be deleted, only disabled — soft deletion is deferred"
type: decision
status: current
authority: tag-deletion
binding: deferral
basis: human
sprint: S0
decided: 2026-08-06
created: 2026-08-13
sources: ["archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md"]
tags: [tag-model, collection]
---

# A tag cannot be deleted, only disabled

`jobhunt tag remove` **refuses**, and names how many `profile_vacancy_tags` links a cascade would
carry off. The chip row on «Вакансии» is built from those links: deleting a tag means erasing the
history of *what found this*.

**The only route today is `tag disable`.** The refusal is loud and names its replacement, which is
why this is deferred rather than urgent.

## What being deferred costs

Half of the «показать вакансии, у которых нет тега фильтра» checkbox is empty. The half meant for
tags that have **ceased** to be collection tags has nothing to show, because there is no way to
cease being one while deletion is refused.

The checkbox is not useless, though: it shows orphans — pairs with no link at all — and those do
occur. See [[orphan-pairs-never-deactivate]] and [[tags-set-marker]].

## Two counts that differ and are both right

The refusal names **52** links while the «IT Director» chip shows **51** rows. **The difference is
one deactivated pair: the refusal counts links, the chip counts *active* pairs.**

Written down because a future reader comparing the two numbers would reasonably suspect one of them
of being wrong, and would go looking for a bug that is not there.

## The real fix, when it comes

A "deleted" flag on the tag instead of `DELETE`. Until then, adding and removing tags from the
browser is *further away* rather than nearer — a browser button for removal would need soft
deletion first.
