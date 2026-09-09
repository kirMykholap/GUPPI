---
title: "The `Links:` field and the script that would have filled it are refused, on the owner's reading of his own graph"
type: decision
status: archived
authority: links-field-refusal
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-30
created: 2026-08-30
target_kind: proposal
target: links-is-filled-by-a-script-from-the-bodys-wikilinks
sources: ["archive/2026-08-30/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md", "job_hunt_ai_vault/wiki/proposals/links-is-filled-by-a-script-from-the-bodys-wikilinks.md", "job_hunt_ai_vault/wiki/concepts/_schema.yaml"]
tags: [vault, record-schema, retrieval]
---

# Context

**`Links:` was admitted to all six `_schema.yaml` files on 2026-08-23** to carry a page's own body
`[[wikilinks]]` in its frontmatter, so a reader could walk the graph without opening the page. It was
to be filled by a script rather than by an agent.

**The script was never written and no page ever carried the field** — zero under `wiki/` and zero
under `archive/`, measured on the day it was removed.

**One exchange before the ruling the session had recommended building the script**, and had ordered it
run every session under `/vault-lint` before the archiver.

**Files this touches:** all six `job_hunt_ai_vault/wiki/*/_schema.yaml`,
`job_hunt_ai_vault/wiki/proposals/links-is-filled-by-a-script-from-the-bodys-wikilinks.md`.

# The question

**Is the script built, or are the script and the field both refused?**

# How it works after

**Both are refused. `Links:` is removed from all six schemas and the key is legal nowhere**, with a
dated note left where the block stood. Removing it reddens nothing, because nothing carried it.

**The proposal takes `status: refused` and carries `decided_by:` naming this page**, which is what
`scripts/vault-archive.sh` reads before releasing it. **The decision that admitted the field moved
into its `sources:`** rather than being dropped
([[a-decided-by-target-in-the-archive-is-kept-and-becomes-a-lesson-candidate]]).

**Why the field bought nobody anything, and it is two readers rather than one.** The owner found the
first half by looking at his own vault: **Obsidian builds its graph from the `[[wikilinks]]` in the
body**, so edges already run to pages linked in prose and the field cached nothing for him. The
session verified that and added the second: **an agent gets a page's outgoing links with one grep over
that one file, without loading it**, and its inbound links with one grep over `wiki/`.

**What replaced the third thing it was reaching for** — *what else answers this question* — is a
shared `authority:` slug across types, obtained with no field and no script
([[a-slug-shared-across-types-is-the-graph-the-links-field-would-have-cached]]).

**The page is still in `wiki/proposals/` and is owed a move to `archive/`.** A refused proposal
belongs there; the archiver is what moves it and sets its mark, and it has not run.

# Recommendation

**Refuse both.** The session had recommended the opposite one exchange earlier and was wrong for a
reason worth keeping: it recommended caching a derived property without checking where the two readers
already got it from. **A cache is justified by a reader who cannot compute the thing more cheaply, and
neither reader here was that.**

**Rejected: building the script and keeping the field**, which was the session's own recommendation.

# Ratification

**owner, 2026-08-30:** «Я не согласен с тем, что графа нет как ты пишешь. В obsidian есть граф прямо
сейчас и я вижу ребра, которые ведут на страницу, ссылка на которую в прозе а не в "Links". Если это
так работает, то тогда строить скрипт для поля Links не имеет смысла, ровно как и это поле.»

# The pointer this page repairs

**`decided_by:` on the refused proposal named
[[the-cleanup-suspends-the-rules-that-would-refuse-it]] until this ingest.** That decision repeals four
rules and says nothing about `Links:`; it was the nearest decision that existed, and the archiver
requires the field to be filled before it will release a refused proposal. **The pointer now names the
decision that actually refused the page**, which is this one.

*(Compiled from `raw/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md`.)*
