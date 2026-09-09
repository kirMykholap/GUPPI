---
title: "The catalogue was built after all, and it is generated — which is what the argument against it never covered"
type: decision
status: deprecated
authority: catalogue-generation
basis: human
sprint: S1
decided: 2026-08-15
created: 2026-08-15
sources: ["raw/notes/2026-08-13-owners-note-second-brain-instructions.md", "raw/notes/2026-08-13-owners-note-second-brain-info.md", "scripts/vault-catalogue.sh", "scripts/vault-check.sh"]
tags: [vault, retrieval]
superseded_by: [[the-page-list-is-a-query-not-a-generated-file]]
---

# Both artefacts exist: the map is a map, and the catalogue is the list

> [!WARNING] DEPRECATED 2026-08-17
> **The conclusion survived; the mechanism did not.** `catalogue.md` is deleted, rule 9 of
> `vault-check.sh` is retired, and the list of every page is `pages.base` - an Obsidian base, which
> is a query and therefore cannot be stale at all ([[pages-base]]). The successor is
> [[the-page-list-is-a-query-not-a-generated-file]], and it keeps everything this page argued:
> both artefacts exist, `index.md` stays a map, and the old objection reaches only a catalogue
> somebody maintains. **owner, 2026-08-17: use Bases.** Read this page for *why there is a list at
> all* and for the byte-identical regeneration of 2026-08-15, which was the cheap proof after an
> audit and is a thing the query cannot do. Everything it says about `--write`, rule 9 and the link
> register describes a file that no longer exists.

**Decided by the owner on 2026-08-15**, and it resolves the contradiction that stood on
[[the-index-is-a-map-not-a-catalogue]] and
[[the-owners-instructions-note-and-what-was-built-from-it]] from 2026-08-14. He reaffirmed what
both his notes asked for — «автоматически обновляемый каталог всех страниц» — and asked the
question that settled it: **could a script do it?** It can.

- `scripts/vault-catalogue.sh` generates `catalogue.md` from the frontmatter of every page in
  `wiki/` and `archive/`: one row per page — name, title, `status`, `sprint`, tags — grouped by
  category, with the counts produced by the same run that produces the rows.
- **Rule 9 of `vault-check.sh` fails while that file differs from what the script produces.** It
  compares by regenerating and diffing, never by mtime, because a checkout rewrites mtimes and the
  first staleness check in this project fired on every clone for exactly that reason.
- Written by `bash scripts/vault-catalogue.sh --write`, which the vault's `CLAUDE.md` now requires
  after any write under `wiki/` or `archive/`. Shipped in `b58ec48`.

**Why the old argument does not reach it.** The map was chosen because *a second copy of what the
files already say diverges*, and because a hand-kept table of a thousand pages becomes the problem
it was meant to solve. Both are true of a catalogue somebody maintains. **Neither is true of one
nobody types**: it cannot drift from the frontmatter it is derived from, because it is regenerated
from it and a gate fails while it is not.

**Rejected: keeping only the map.** That was the position of 2026-08-13, taken by the designer and
marked `basis: inference` for that reason, and it declined a `basis: human` ask. Also rejected: a
catalogue maintained by the librarian, which is the version both objections above actually
describe.

## The one dangerous thing about it, and what holds it

**`catalogue.md` links to every page in the vault.** The register that rule 5 reads for
reachability is an allowlist of exactly `index.md`, `tags.md` and `sprint.md`, and **the catalogue
is deliberately absent from it**. If it were added, the orphan rule would keep running, keep
passing, and prove nothing ever again — and an orphan matters here because a page reachable only
by an exact grep hit is a page a Russian question never finds
([[aliases-carry-the-question-across-languages]]).

That exclusion is not a comment: the selftest case named **«the catalogue does not rescue an
orphan»** plants an orphan, regenerates the catalogue so that it does link to the planted page, and
still expects the orphan reported. The suite is **61 of 61, 0 missed, measured 2026-08-15**
([[vault-scripts]]). *(This sentence said "case 58" and "58 of 58" earlier the same day. The case
is named rather than numbered from 2026-08-15: an ordinal moves whenever a case is inserted above
it — it was the 58th of 58 that morning and is the 50th of 61 by the evening — and a number that
renumbers itself is the failure on [[a-stated-count-drifts-from-the-list-it-heads]] with a moving
target underneath it. The name is stable and greppable in the script.)*

## What each of the two is now for

| | answers | how it stays true |
|---|---|---|
| `index.md` | *where do I start* — categories, the naming rule, the current sprint, hub pages | edited by hand, and only when the map itself changes |
| `catalogue.md` | *what is there at all* | regenerated; rule 9 fails while it is not what the script produces |

Retrieval is still `ripgrep` first and the links out of whatever it finds — the catalogue does not
change that and is not an entry point for a topic query. It answers the one question grep cannot:
the whole list. **`index.md` keeps its shape and its place** ([[index-md-stays-at-the-vault-root]]).

## The first regeneration after an audit was byte-identical

**2026-08-15**, immediately after the first `/vault-lint` rewrote **sixteen** pages under `wiki/`:
`bash scripts/vault-catalogue.sh --write` produced a file identical to the committed one, byte for
byte. That is the quiet proof the audit changed no `title`, `status`, `sprint` or `tags` line
anywhere — sixteen pages of prose edited and not one row of the catalogue moved.

It is worth recording because it is the **cheap** proof. Establishing the same thing by reading
sixteen diffs is a review; establishing it from a derived file that is regenerated from exactly
those five fields is a diff of nothing. A generated artefact is an assertion about its inputs, and
this is the first time this one paid ([[the-audit-is-dispatched-after-the-writes]]).

## Who resolved it, and why that mattered

The librarian marks a contradiction and never chooses; the owner is the only party that may
resolve one ([[the-librarian-writes-unattended]]). This one stood for one day, marked on both
pages, and was settled by the person whose note raised it — by building the third option neither
page had considered.
