---
title: "The gate's frontmatter pass reads `wiki/` alone, so a page in `archive/` is validated by no schema"
type: concept
status: current
authority: gate-frontmatter-scope
basis: code
sprint: S3
created: 2026-08-28
sources: ["archive/2026-08-28/the-sprint-list-stops-lying-and-archiving-gets-a-predicate/handoffs/2026-08-28-the-sprint-list-stops-lying-and-archiving-gets-a-predicate.md", "scripts/vault-check.sh"]
tags: [vault, harness, record-schema]
---

# The property

**`scripts/vault-check.sh:84` is `find "$VAULT/wiki"`.** Nothing else feeds the frontmatter pass.

**So a page that has reached `archive/` is validated by no schema and could carry any word in its
`status:`.** That is not an oversight — `archive/` is a warehouse and is deliberately outside every
sweep, register and check here
([[the-purpose-of-archiving-is-a-cheaper-working-wiki-and-archive-is-a-warehouse]],
[[what-an-archived-page-asserts-is-frozen-and-how-it-is-found-is-live]]).

# The consequence, which corrects a ground already recorded

**`the-archiver-sets-status-archived-and-the-value-enters-the-schema-first` justifies putting the
value into the schemas by saying that a sweep writing the mark before the declaration would redden
every page it touched.** Read against the line above, that is false for a page the sweep has already
moved: nothing validates it there.

**The order that page fixes is right; the reason recorded under it is not.** The real reason arrived
on 2026-08-28 with the ruling that **the sweep continues past a refused move** — so a page can be
left **in `wiki/`** wearing the mark of a move that did not finish, and an undeclared value would
report that as a schema fault rather than as the half-finished move it is
([[the-archive-sweep-continues-past-a-refused-move-and-collects-its-refusals]]).

# What else this scope explains

**A verdict about a page in `archive/` can never fire**, so a rule written there is unreachable by
construction — the class this store has already paid for once
([[a-verdict-that-cannot-fire-is-worse-than-no-verdict]]).

**And it is why `scripts/vault-archive.sh` carries the conditional refusals rather than the
schemas.** The last moment a page's frontmatter can be judged is on its way out
([[a-conditional-requirement-is-refused-by-the-script-that-moves-the-page]]).
