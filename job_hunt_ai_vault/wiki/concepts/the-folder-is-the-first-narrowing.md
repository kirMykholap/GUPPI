---
title: "Narrowing comes before the grep, and the folder is the first narrowing"
type: concept
status: current
authority: retrieval-narrowing
basis: measurement
sprint: S1
created: 2026-08-16
sources: [".claude/agents/vault-librarian.md", ".claude/agents/pre-task.md", "scripts/vault-check.sh", "tags.md"]
tags: [retrieval, vault]
---

# A full-text grep over this corpus is already too wide

Retrieval here is grep plus the links out of whatever it found
([[the-index-is-a-map-not-a-catalogue]]), and that description leaves out the step which now does
most of the work: **choosing what to grep over.** Measured at `2036d98`, over 118 pages in `wiki/`:

| the widest net | what it returns |
|---|---|
| `rg -il vault "$VAULT/wiki"` | **116 of 118** pages |
| `rg -il check "$VAULT/wiki"` | **84 of 118** pages |
| `tags: vault` over `wiki/` | **51 of 118** pages |
| `tags: vault` inside `concepts/` | **11 of 32** |

A search that returns nearly the corpus has not searched. The tag was the answer to that once and
has stopped being one on its own: 51 at `2036d98` is five times what a reader can open for one
question.

## The order, and why the folder comes first

1. **the folder**, when the question names its kind;
2. **the filenames** — `rg --files "$DIR" | rg -i "<term>"`. They are written to be searched, which
   is why they carry no category prefix ([[filenames-carry-no-category-prefix]]);
3. **the tag**, looked up in `tags.md` first so the Russian word reaches the English one
   ([[aliases-carry-the-question-across-languages]]);
4. **full text**, last, and only if those found nothing.

| the question | the folder |
|---|---|
| what was decided about X, what may I not do | `decisions/` |
| how does X work, why is it built that way | `concepts/` |
| what burned us, what went wrong | `lessons/` |
| what exists, and what is it like | `entities/` |
| what did we plan and never do | `proposals/` |

**The folder is the cheapest narrowing there is**, and it is the only one already written down for
every page: a page's folder is also its `type:`, and rule 4 of `vault-check.sh` fails while the two
disagree ([[vault-scripts]]). Nothing has to be maintained for it to keep working, and it cannot go
stale the way a count or a threshold can.

**The five folders had been a classification no search used.** They decided where a page was
written and how an answer was ordered — `entities/` → `decisions/` → `concepts/` → `lessons/`
([[one-librarian-behind-every-caller]]) — while all three greps ran over `wiki/` whole. `/pre-task`
was the exception and had been doing folder-first alone since it was written: it enumerates
frontmatter across **every** `decisions/` page and opens only the ones the titles implicate.

## The folder narrows the denominator; the tag narrows inside it

The two steps do different work and neither replaces the other. At `2036d98`, `rg -il vault` inside
`decisions/` matches **47 of 47** — the folder alone buys nothing against a word that appears
everywhere — while `tags: vault` inside `decisions/` selects **19**. Vocabulary is not
classification, and the tag is the only one of the two that was applied by a reader deciding what a
page is about.

## A guessed folder is a silent miss

This is the cost, and it is the reason the rule stops where it does. A grep in the wrong folder
returns nothing and looks exactly like a grep in the right folder over a corpus that has no answer:
**the page exists, the search is clean, and nothing reports that you looked in the wrong half.**
Every other failure of retrieval here is at least loud.

So the folder is applied **only when the question names its kind**, and a question that does not
name one searches `wiki/` whole. That is the same shape as the ten-page ceiling: bound the reading
where a partial answer is safe, never where it is dangerous ([[one-librarian-behind-every-caller]]).

## What else changed with it

The split advisory in `vault-check.sh` is measured inside one folder rather than over the corpus,
against the reader's ceiling of ten — the same ten this page's caveat is scoped by, and the reason
one absolute count could not do the job:
[[the-dense-tags-are-not-split-and-the-standing-advisories-are-named-here]].

## The whole funnel, as the owner and the session settled it in conversation — 2026-08-21

**The order, end to end:** the question's words → the aliases in `tags.md` and `authority.md` → the
**family** a slug belongs to → `title` and `authority` across the corpus **in one command** → open at
most ten pages → one hop along the wikilinks, reading titles only.

**Stages 1–2 are what this page already describes.** What 2026-08-21 added is the middle: a family
is a question's worth of pages rather than a word's worth
([[authority-becomes-the-index-and-is-required-outside-rules]]), and
`bash scripts/vault-catalogue.sh` prints `authority` and `title` for the whole store in a single pass
of frontmatter ([[vault-scripts]]).

**The ten-page ceiling is about *opening* a page and never about searching for one.** That
distinction was already written into the librarian's own definition, and nothing was delivering the
wide half it licenses — a sweep of every page's frontmatter costs one command and reads no bodies.

**Being built is not being delivered.** No skill or agent names either instrument, so the funnel
reaches nobody as a procedure; that half is a proposal and is deliberately not built
([[the-reading-funnel-is-delivered-as-a-procedure]]).

*(Compiled from `raw/handoffs/2026-08-21-a-claim-is-looked-up-before-a-page-is-written.md`.)*

## The `/pre-task` citation is repointed, and the folder-first claim survived the move — 2026-08-22

**`sources:` cited `.claude/skills/pre-task/SKILL.md` and now cites `.claude/agents/pre-task.md`.**
The skill was deleted on this date, when the ritual became an agent
([[the-pre-task-becomes-an-agent-and-the-ritual-is-enforced]]), and rule 5 of the gate requires every
repository path in `sources:` to resolve — a citation to a file that is not there reads as provenance
and is not ([[vault-scripts]]). **The address moves and the history stays readable**: the sentence
above about `/pre-task` was compiled while the skill existed.

**What this page cites it for survived, and in the wider form this page's own funnel section asked
for.** The clause *`/pre-task` was the exception and had been doing folder-first alone* is carried by
the agent, which drops `lessons/` and `archive/`, keeps `concepts/`, `entities/`, `proposals/` and
`rules/` whole, and reduces `decisions/` to `binding: prohibition`
([[the-pre-task-enumeration-covers-every-folder-but-lessons]]).

**One sentence above is contradicted by its own new source, and is dated rather than rewritten.**
*"No skill or agent names either instrument"* was already overtaken on 2026-08-21, when phase 1
became `bash scripts/vault-catalogue.sh`; today that call sits in an agent definition, so the
catalogue **is** named by a reader. **`bash scripts/vault-authority.sh --near` still is not**, and the
funnel as an ordered procedure still reaches nobody — which is the half
[[the-reading-funnel-is-delivered-as-a-procedure]] holds and which is still not built.
