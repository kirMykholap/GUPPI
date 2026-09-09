---
title: "`concepts/` are non-functional requirements and `entities/` are functional, and only there is a shared slug required"
type: decision
status: archived
authority: concepts-entities-taxonomy
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-30
created: 2026-08-30
target_kind: action
target: the-two-schema-headers-state-the-concept-entity-taxonomy
sources: ["archive/2026-08-30/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md", "job_hunt_ai_vault/CLAUDE.md", "job_hunt_ai_vault/wiki/concepts/_schema.yaml", "job_hunt_ai_vault/wiki/entities/_schema.yaml"]
tags: [vault, record-schema, process]
---

# Context

**`wiki/concepts/` holds 142 pages and `wiki/entities/` holds 45**, and the owner named the imbalance
as the thing he objects to: *«сейчас явный перекос в сторону concepts, но я не вижу смысла в этом»*.

**Neither folder has an archival criterion**, deferred explicitly on 2026-08-28
([[entities-and-concepts-get-no-archival-criterion-today]]), and asked for one again on 2026-08-30 he
refused to name it.

**Measured the same day, as a proxy:** 126 of 142 `concepts/` and 43 of 45 `entities/` carry no
product tag — 169 pages of 187 outside the product. The test is by tag and is not a judgement about
contents.

**Files this touches:** `job_hunt_ai_vault/wiki/concepts/_schema.yaml`,
`job_hunt_ai_vault/wiki/entities/_schema.yaml`, `job_hunt_ai_vault/CLAUDE.md`,
`docs/vault-cleanup-families.md`.

# The question

**What distinguishes a `concepts/` page from an `entities/` page, and what is the exit criterion for
each folder?**

# How it works after

**`concepts/` are non-functional requirements. `entities/` are functional requirements.** That is the
test the next sweep walks by.

**One `authority:` slug is permitted and required on the pair, and only there.** A concept and an
entity answering the same question carry the same slug, which is what makes the two halves of one
subject findable together.

**No exit criterion is named for either folder**, deliberately: he declined to give one on the ground
that the two are a small part of the store today.

**This ruling is written in no file.** Its destination was agreed — a decision page, which is this
one, **plus a line in the header of both `_schema.yaml` files**. **The schema half is the session's to
write, not the librarian's**: those files are what the gate reads as its own input
([[what-the-gate-reads-as-its-own-input-is-the-sessions-to-write]]), and this page makes no claim that
they have changed. It is owed.

**The `required` half of the pair does not switch on with this.** Twenty-two families hold concepts
with no entity — 54 pages — so requiring the pair on the first run reddens all of them
([[the-required-half-of-paired-authority-waits-on-the-taxonomy]]).

# Recommendation

**Write the decision and leave the schema headers to the session.** Ratified in words on 2026-08-30
and present in no schema, no verdict and no page, this ruling was the largest unwritten thing the day
produced, and the sweep that follows walks by it. A ruling that exists only in a chat log is a ruling
the next session cannot obey.

**Rejected: waiting for the exit criterion.** He declined to give one and the taxonomy is usable
without it.

# Ratification

**owner, 2026-08-30:** «критерий выхода для entities/ и concepts/ я не назову. Это сейчас малая часть
vault. Но я точно хочу сделать так, чтобы concepts были про нефункциональные требования, а entitie -
про функциональные требования. Только здесь разрешен и требуется одинаковый authority. Потому что
сейчас явный перекос в сторону concepts, но я не вижу смысла в этом.»

**Found by reading the session extract whole, and it was in no feedback mark.**

# It disagrees with two live statements, and neither disagreement is settled

> [!NOTE] RAISED, NOT RESOLVED — different `authority:` slugs in both cases, so rule 3 of the gate
> cannot see either and no `CONTRADICTION` block is legal.

**Against the folder test that is live in the vault's own `CLAUDE.md`.** That file says *"An `entity`
is a noun with properties. A `concept` is a mechanism with consequences"*, and
[[the-clause-that-concepts-describes-the-product-is-struck]] (`concepts-scope-clause`) says explicitly
that this line *"is the one below it, and it is untouched"* — it survived the strike of 2026-08-23 as
the thing the folder rule actually rests on.

**Functional versus non-functional is a different predicate.** `session-hooks`, `docker-desktop` and
`windows-console-encoding` are nouns with properties and are functional requirements of nothing.
**Whether the new taxonomy replaces that test or stands beside it is not stated and must be**, or the
sweep of 187 pages walks by two tests that disagree.

**Against the per-type slug permission ruled the same day.**
[[authority-uniqueness-becomes-a-per-type-question]] (`authority-per-type-uniqueness`) says any two
pages of different types **may and should** share a slug. This page says a shared slug is permitted
*only* in the concept/entity pair. A reading that reconciles them exists — *required* only here,
*permitted* everywhere — but it is the librarian's inference and is not what either sentence says.

*(Compiled from `raw/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md`.)*
