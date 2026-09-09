---
title: "The cleanup verdict names which delivery a family gets, and the session sets it for the owner to ratify as a block"
type: decision
status: current
authority: family-verdict-kinds
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-31
created: 2026-08-31
target_kind: action
target: docs-vault-cleanup-verdicts-md-carries-one-line-per-family
sources: ["archive/2026-08-31/2026-08-31-the-families-become-rules/handoffs/2026-08-31-the-families-become-rules.md", "docs/vault-cleanup-verdicts.md", "docs/vault-cleanup-families.md", "scripts/build-families-table.py"]
tags: [vault, process, record-schema]
---

# Context

**The cleanup table's legend had two values — живое and мёртвое — and they predate the ruling that
split the delivery in two.** Once a `render: authority` rule serves the vault alone and everything
outside it is delivered by rendering into a named file
([[the-hook-matches-the-exact-slug-and-resolves-nothing-through-the-register]]), a family is not simply
alive or dead: it is addressed to one delivery or the other, or to neither.

**The design said the owner writes the verdicts.**
[[the-prohibition-families-become-rule-pages-served-by-a-hook]] states that the judgement half *"is not
the librarian's"*, and `brief.md` and `sprint.md` said the same in prose. **The session read it as
already settled the other way**, off [[the-retro-list-is-worked-by-the-session-with-items-carved-out-for-the-owner]]
and its neighbour, and set the verdicts itself.

# The question

**What does a family's verdict name, how many values does it take, and who writes them?**

# How it works after

**It names the delivery, and the third value is not "dead".**

| verdict | what it means | what happens to its decisions |
|---|---|---|
| `vault-facing` | the text is addressed to the vault's own pages | one page under `render: authority`; the decisions are **released** to `archive/` |
| `harness-facing` | the text belongs in a harness or product file | nothing is built yet; the decisions **stay** in `wiki/decisions/` |
| `none` | the family produces no rule at all | the decisions **stay** |

**Only `vault-facing` releases anything.** The repeal frees a prohibition once the family rule carrying
its clause exists, and the other two verdicts produce no such rule.

**The test applied, in one sentence:** would somebody touching a vault page that carries a slug of this
family need this text? If instead it instructs a session, an agent, a script or the product, it reaches
its reader by being rendered into that file and is `harness-facing`.

**The session sets them and brings them as one block**, named family by family with its count, as
enumerated prose in chat. **The owner ratifies or corrects.** The reading that this was already decided
is now decided, so the next session does not have to infer it from two pages against the prose of two
registers.

**They live in `docs/vault-cleanup-verdicts.md`, a file of their own**, because
`docs/vault-cleanup-families.md` is generated and overwritten whole — a verdict written into the table
would be destroyed by the next regeneration, and a generator recovering one by parsing its own previous
output breaks silently. **That half is the session's own recommendation and he did not answer it**, and
it is filed at that strength rather than promoted.

# Recommendation

**A verdict that names the delivery.** The session's own, and its ground is that the two-valued legend
cannot express a family whose text is real and whose delivery is not built.

**Rejected: the two-valued legend**, which would have filed the harness-facing families as dead.

**Rejected: a copy of the verdicts inside `wiki/`.** A page duplicating a `docs/` file line for line is
the drifting list this store repairs by deletion ([[a-copy-of-a-list-drifts]]).

# Ratification

**owner selected, 2026-08-31: «принимается».** Given against the session's block of 53 verdicts — 18
`vault-facing` holding 131 prohibitions, 35 `harness-facing` holding 164, and `none` used nowhere —
shown as enumerated prose with the two borderline calls named by the session itself.

**The shape of the verdict is the session's understanding and is filed as that.** It follows from his
ruling on the two deliveries rather than from a sentence of his about verdicts.

# What is unguarded, and named rather than deferred

**Nothing checks that `docs/vault-cleanup-verdicts.md` still matches `job_hunt_ai_vault/authority.md`.**
A renamed family would silently lose its verdict and the generator would print an empty one. **That is
the shape this store repairs by deletion rather than by discipline** ([[a-copy-of-a-list-drifts]]), and
it is raised in the brief rather than filed as a ratified deferral, because nobody has agreed to leave
it.

**And the table this feeds was itself short by two rows on its first run**, because its generator keyed
on a field that had stopped being unique the day before
([[a-mapping-written-against-a-repealed-invariant-loses-rows-silently]]) — so the verdicts were set
against a reading that had to be checked by hand before it could be trusted.

*(Compiled from `raw/handoffs/2026-08-31-the-families-become-rules.md`.)*
