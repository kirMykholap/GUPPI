---
title: "`index.md` is for whoever reads the vault and the vault's `CLAUDE.md` for whoever writes it"
type: decision
status: current
authority: index-and-schema-roles
binding: prohibition
basis: human
sprint: S1
decided: 2026-08-16
created: 2026-08-16
sources: ["archive/2026-08-16/2026-08-16-the-structure-questioned/handoffs/2026-08-16-the-structure-questioned.md", "index.md", "CLAUDE.md", "sprint.md"]
tags: [vault, retrieval]
---

# Two files, two readers, and the split is by reader

**The vault's `CLAUDE.md` is for whoever writes a page** — the schema, the fields, supersession,
contradictions, what does not belong here.

**`index.md` is for whoever reads one** — hub pages, and nothing else.

That is the whole of the decision, taken by the owner on 2026-08-16. It does not repeal
[[the-index-is-a-map-not-a-catalogue]] or [[index-md-stays-at-the-vault-root]]; it says which of
the two audiences the map serves, which those pages left open, and it makes the duplication below a
defect rather than a convenience.

## The duplication to remove, measured rather than asserted

| what is duplicated | where |
|---|---|
| the categories table | both files, near-verbatim |
| the naming rule | both files |
| the current sprint | `index.md`, while `sprint.md` declares itself the only place it lives |

**Cross-links between the two stay; copies do not.** A copy is the failure the store exists to
prevent, and it has already produced three stale claims that lived only in a `CLAUDE.md`
([[claude-md-can-lose-an-assertion-but-cannot-strand-a-page]]).

## Not executed, and that is deliberate

Rewriting `index.md` down to hubs is deferred: it is finding #3 of
[[the-audits-findings-are-owed-to-the-owner]], where the reason is that trimming a map is
deleting text and the map's shape is the owner's. The cost of waiting is that the map keeps three
copies of what `CLAUDE.md` and `sprint.md` own — one row of
[[structure-work-agreed-and-not-executed]].

# Narrowed on 2026-08-31: a flat list of the rules served by lookup

**"Hub pages, and nothing else" is narrowed by one exception**, and `index.md` now carries a section
listing every `wiki/rules/` page delivered under `render: authority`, with its slug, one row each.

**owner selected, 2026-08-31: «понял. Да, можно».** Put to him as the cheaper of two ways to keep the
new pages out of the orphan verdict; the alternative was writing a link into each of about 290
decisions before they moved.

**The mechanical reason, which is the whole of it.** A rule under `render: authority` renders into no
file and nothing in the tree cites it on the day it is created, so rules 4 and 5 of the gate report
every one of them as an orphan. **The linked set is built from `wiki/`, `archive/`, `index.md`,
`tags.md` and `sprint.md`** — of those, only `index.md` is a place a list of them can honestly live.

**The narrowing is bounded to that class and to nothing else.** It is a list of pages that cannot be
reached any other way, not a licence to catalogue. `pages.base` and `bash scripts/vault-catalogue.sh`
remain what answers "what pages exist" ([[the-index-is-a-map-not-a-catalogue]]).

**The exception was predicted here and it is worth saying so.** The concept above records hub rows
going from none to thirteen and says *"each is defensible on its own, which is how this failure always
arrives"*. **This one is defensible on its own too.** It is taken anyway, on his word, with the
prediction named rather than forgotten.

*(Extended at the ingest of `raw/handoffs/2026-08-31-the-families-become-rules.md`.)*
