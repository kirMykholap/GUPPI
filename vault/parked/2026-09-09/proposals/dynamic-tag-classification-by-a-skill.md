---
title: "A skill that classifies the tags after the fact, instead of policing them as they are minted"
type: proposal
status: current
authority: tag-classification-skill
basis: human
sprint: S1
created: 2026-08-15
sources: ["tags.md", "scripts/vault-check.sh", "CLAUDE.md"]
decided_by: [[the-audits-findings-are-owed-to-the-owner]]
tags: [vault, retrieval]
---

# Let the tags appear, and group them afterwards

**The owner's design, 2026-08-15.** In his shape, not the librarian's:

> Tags appear freely as work happens; that is inevitable and not a defect. A separate skill then
> looks only at the files' tags and tries to group them — match new tags against old ones, prepare
> aliases the way `tags.md` already does, and watch for concept drift. We do not police which tags
> an agent adds or how it classifies; we look at the result. If it is unsatisfying, the librarian
> is asked, the tag skill runs, improvements are applied. The main limiter is a number past which
> the tag count clearly needs review.

The inversion is the point: today the discipline is at the moment of minting — consult `tags.md`,
reuse if something fits, record the rejected word as an alias
([[aliases-carry-the-question-across-languages]]). That rule is cheap for the writer and it depends
entirely on the writer having read the dictionary. **This proposal keeps it and stops relying on
it**, by making the periodic pass the thing that produces the classification.

## What the session adds, as constraints rather than opinions

- **No ML library, because no new dependencies is a project rule** — and none is needed, because
  **the classifier is already paid for.** The reader of this vault is a language model, and 17 tag
  names against 108 page titles is a size a model groups better than embeddings would, precisely
  across the Russian/English boundary where a vector search over this corpus is weakest
  ([[vectors-are-deferred-not-rejected]]: what a vector buys here is finding a page, and the
  recall gap this corpus actually has is vocabulary, which is a dictionary problem).
- **Smart Connections and Dataview are Obsidian plugins.** Fine as the owner's own view of his own
  vault, and **nothing in the project may depend on them**: an agent reads this store with `rg` and
  wikilinks and has no Obsidian at all ([[the-vault-directory]] — the same reason nothing may depend
  on the vault's directory name). A grouping that exists only inside a plugin is invisible to every
  reader the vault was built for.
- **Concept drift is checkable here, and cheaply**, because every tag carries a **definition** in
  `tags.md` and not only a name. Drift is *the pages carrying a tag no longer matching that tag's
  definition* — a judgement, not a script, and `/vault-lint` already asks for it. Without the
  definitions there would be nothing to drift from, which is why the dictionary is not a second
  copy of the frontmatter.
- **The limiter already exists**, as the advisory in `vault-check.sh`: a tag on more than 20 pages
  prints a line and does not fail the run. `tags.md` states the band slightly differently — "more
  than ~15–20 pages" — so there are already two numbers for one rule. **What is missing is not the
  threshold. It is that the threshold prints a line nobody acts on**, instead of triggering the
  skill.

  *(Corrected 2026-08-16; the bullet is kept as it was written. **There is one number now, and it
  is measured inside a folder** — the advisory prints when a tag selects more than ten pages in one
  folder of `wiki/`, `tags.md` states the same rule in the same words, and `archive/` is not
  measured ([[the-folder-is-the-first-narrowing]]). The half of this bullet that still stands is
  the load-bearing one: **the threshold still prints a line rather than triggering the skill.**
  Five lines print at `2036d98`, and each is now named by
  [[the-dense-tags-are-not-split-and-the-standing-advisories-are-named-here]] — named is not the same as acted on,
  so the complaint this proposal is built around is intact.)*

## Measured 2026-08-15, after this session's own writes

```
rg -N -I "^tags: \[" "$VAULT/wiki" | sed 's/^tags: \[//; s/\]$//' | tr ',' '\n' | tr -d ' ' \
  | sort | uniq -c | sort -rn
```

**17 tags, 108 pages in `wiki/`, 235 tag assignments** — 2.18 per page, against a schema that
allows 2 to 4. The one-liner above reads only the inline spelling of `tags:`, which is what every
page in this corpus uses today; `vault-check.sh` reads the block spelling too, because Obsidian's
property editor emits it.

| tag | pages | |
|---|---|---|
| `vault` | 42 | over the threshold |
| `process` | 40 | over the threshold |
| `testing` | 26 | over the threshold |
| `data` | 19 | |
| `collection` | 18 | |
| `web` | 13 | |
| `architecture`, `agents` | 11 each | |
| `retrieval`, `htmx`, `filters` | 9–10 each | |
| `tag-model`, `schema`, `deactivation`, `batches` | 5 each | |
| `frontend` | 4 | |
| `profile` | 3 | |

**Tags grow faster than the corpus.** `vault` stood at **31 of 95 pages on 2026-08-14**
([[lint-waits-for-an-open-sprint]], [[aliases-carry-the-question-across-languages]]) and is **42 of
108** a day later: the corpus grew by 14%, the tag by 35%. That is the shape of the problem — the
subject a store writes most about is itself, and the tag that classifies nothing is the one every
page qualifies for.

## The strata inside each of the three, measured 2026-08-15

Acceptance criterion 3 of S1 asks for a **decision**, and this is the evidence gathered for it. The
finding under all three numbers is the same: **each is several subjects sharing a word, not one
subject that grew.**

- **`vault` 42 — four strata that barely overlap.** The store's *shape* (categories, folders,
  filenames, index, catalogue, statuses — 12 pages); the *session loop* (handoff → ingest →
  verdicts → brief → hook — 14, and **25 of the 42 also carry `process`**, which is where that
  loop really lives); the *tooling and the agent* (scripts, librarian, hooks, parallelism — 8);
  and *provenance failures* (7). **The cut that pays is shape-versus-loop**, and the `process`
  overlap has already half-made it.
- **`process` 40 — its cheapest split is an `environment` tag.** It would take 3 pages from
  `process` (`docker-desktop`, `windows-console-encoding`, `app-restart-required`, which are facts
  about the machine and land here only because there is no better bucket) and pull
  `claude-code-config-loading` and `playwright-mcp` in from elsewhere: **5 pages for one word.**
- **`testing` 26 — the split that fits is *accounting*, not the vault/product line.** Coverage,
  verdicts, counts and units are 5 pages; the vault/product cut was already considered on
  2026-08-13 and refused on a ground that still holds, that `vault-check.sh` fails a build for the
  same reason `pytest` does.
- **`batches` is a strict subset of `collection`** and selects nothing new — a merge candidate
  rather than a split one, and the only one of the four findings that would make the dictionary
  smaller.

**Consequence of leaving all three, stated as a cost rather than a nag: an advisory that stands
for a fourth day stops being read.** That is the same failure as an alarm that always fires, and it
is the reason the threshold prints instead of failing.

**The precedent is in the dictionary and it worked**: `collection` reached **17 of 29 pages**, "had
stopped classifying", and was split — bookkeeping to `batches`, judgement to `deactivation`, field
rules to `data`. `web` was narrowed at **22 of 56** by the same reasoning. Both were done by hand,
in a pass someone decided to make.

**Measured per folder on 2026-08-16, this section's plan was refuted before it was applied.** The
strata above were gathered as evidence for splitting three tags *corpus-wide*, and the per-folder
table at `2036d98` shows why that would have been the wrong cut: **`testing` is 5 of 47 pages in
`decisions/`**, ten percent and doing its job, and useless only in `lessons/` at 13 of 19;
`process` is 4 of 32 in `concepts/`. Two of the three tags accused here are useless in exactly one
folder each. **The unit of a split is therefore a tag inside a folder** — `testing` in `lessons/`,
never `testing` — and the owner's decision of that day was to split none of them and name the
standing lines instead ([[the-dense-tags-are-not-split-and-the-standing-advisories-are-named-here]]).

**None of the strata work is discarded by that.** The shape-versus-loop cut for `vault`, the
`environment` tag for `process` and the *accounting* cut for `testing` are exactly the split
candidates this proposal's skill would bring to the owner; what the per-folder reading adds is
*which line each of them would close*, and that `process`'s cheapest split touches none of the five.
The counts in the table above — 42, 40 and 26 of 108 — are the 2026-08-15 reading over the whole
corpus and are kept as such; they are no longer what any threshold is measured against.

## What it would take

1. **A skill whose input is only the frontmatter and the dictionary** — every page's `tags:`, its
   title and its folder, plus the definitions in `tags.md`. Deliberately not the page bodies: the
   proposal is to classify the classification, and a skill that reads 108 pages is a `/vault-lint`
   run, which already exists and costs what it costs.
2. **Four outputs, each a proposal and not an edit**: split candidates with a suggested cut;
   merge candidates — two definitions that no longer distinguish anything; missing aliases,
   including the Russian ones, which is the rule above run in bulk; and a drift list — pages whose
   subject no longer matches the definition of a tag they carry.
3. **A trigger.** The advisory line in `vault-check.sh` names the skill, or the ingest that pushes
   a tag over the threshold says so in `log.md`. An advisory that fires every run and cannot be
   acted upon is one you learn not to read, which is stated in the script itself.
4. **Application by the owner's call.** Re-tagging pages a session never touched is not the
   librarian's to do unattended ([[the-librarian-writes-unattended]],
   [[lint-waits-for-an-open-sprint]]).

## What is open

- **The limiter's number**, and there are two of them today: `>20` in the script, `~15–20` in
  `tags.md`. Whichever survives, three tags are already over it and have been for two days.
  *(Closed 2026-08-16: **there is one**, ten pages inside one folder of `wiki/`, and the script and
  `tags.md` now state it in the same words. Ten is not a new number — it is the reader's ceiling,
  already written into the librarian's definition, which is why it does not move when the corpus
  does. What the closure did **not** do is reduce the standing lines: **five at `2036d98`**, against
  the three counted here.)*
- **Whether the skill may write `tags.md` itself.** Adding an alias is additive and nearly free;
  splitting a tag rewrites frontmatter across dozens of pages and is a different act entirely.
- **When it runs** — at every ingest, or at the retrospective. The retrospective is where
  `/vault-lint` waits, and a tag pass that runs every ingest will report the same three tags every
  time until someone acts.
- **Whether a split is even the right answer for `vault`.** The alternative nobody has argued is
  that a store writing about itself is normal and the threshold should be per-tag rather than
  global.

## What it would oblige

A tag split changes pages this proposal's own author did not write, so the day it is accepted it
also needs the thing `collection`'s split had: **the old word kept as an alias**, so that a
question asked in the vocabulary of the tag that no longer exists still lands
([[aliases-carry-the-question-across-languages]]).

**A sibling proposal attacks the same problem from the other end and was also not taken**:
[[an-alias-may-point-at-a-page-not-only-at-a-tag]] would stop the mechanism that inflates the big
tags — an alias must attach to a tag today, so every recall fix widens the widest tag — while this
one re-cuts the tags that are already wide. They are complementary and neither is a substitute for
the other: that proposal plugs the leak, this one drains.

**Nothing here is decided.** The design is the owner's; the constraints are the session's; there is
no decision page behind it and no date ([[proposals-are-a-folder-not-a-status]]).
