---
title: "A cancelled page takes a status of its own, and the deprecated refusal stays unconditional"
type: decision
status: archived
authority: repealed-status-mint
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-30
created: 2026-08-30
target_kind: action
target: mint-the-repealed-status-and-its-release-route
sources: ["archive/2026-08-30/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form/handoffs/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form.md", "wiki/rules/_schema.yaml", "scripts/vault-archive.sh"]
tags: [vault, record-schema, process]
---

# Context

**A cancelled page could not leave `wiki/` at all.** `deprecated` is the only status obliging a page
to leave, and `scripts/vault-archive.sh` refuses to release a `deprecated` page without a live
successor named in `superseded_by:`
([[a-deprecated-page-needs-a-live-successor-named-in-superseded-by-before-it-may-leave]]) — the
strongest test in the script, chosen deliberately because nothing in `archive/` is swept, checked or
read by `/pre-task`, so a page nothing points at has **left** the store rather than been filed in it.

**A cancellation has no successor and can have none.** The owner ruled that on 2026-08-30, overturning
the ruling of the day before that a repeal is recorded by supersession: «Вчерашнее решение, что отмена
записывается через supersession - неверная. Если мы отменяем, то мы не можем заменить это
чем-либо. Значит отмена должна быть подкреплена descision и только».

**So under `deprecated` alone such a page had two outcomes and both are wrong**: it sits in `wiki/`
carrying a claim that is false, or it is given an invented successor.

# The question

**Does the `deprecated` refusal become conditional, or does a cancellation get a status of its own?**

# How it works after

**A status of its own: `repealed`.** It is minted the way `implemented` and `archived` were, and it is
**legal in `wiki/rules/` alone** — narrower than the plan's *all six*, and one of the five forks the
session resolved without asking.

**`scripts/vault-archive.sh` releases such a page on `decided_by:`** naming a repeal decision, instead
of on `superseded_by:`, and forbids it a `superseded_by:` at all.

**The refusal for a `deprecated` page without a live successor is untouched and stays absolute.** That
is the whole point of a second value rather than a condition: making the first route depend on a field
a page could simply omit would weaken the strongest test this store has.

**And the decision behind a repeal never leaves.** Once the cancelled page reaches `archive/`, that
decision is the only live carrier of the fact that the thing is gone
([[a-decision-declares-its-target-and-the-handshake-closes-it]]).

# Recommendation

**A second value with its own precondition**, against widening the existing route. The session put
both and recommended this one.

# Ratification

**The owner said it**: «Case 2.2: Я принимаю вариант А».

**Built on 2026-08-30.** `wiki/rules/_schema.yaml` declares the value; the archiver has the release
route; and the gate's `retired` verdict learned the third mark with a message of its own — which was
**not** in the plan and was caught while writing the fixture
([[a-rule-with-no-instrument-behind-it-is-a-rule-a-fixture-can-violate-for-a-week]]).

*(Compiled from `raw/handoffs/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form.md`.)*
