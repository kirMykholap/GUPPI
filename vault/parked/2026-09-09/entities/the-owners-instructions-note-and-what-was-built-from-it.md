---
title: "The owner's instructions note is design intent, and this is what was built from each line of it"
type: entity
status: current
authority: owners-design-intent
basis: human
sprint: S1
created: 2026-08-14
sources: ["raw/notes/2026-08-13-owners-note-second-brain-instructions.md", "raw/notes/2026-08-13-owners-note-second-brain-info.md", "docs/superpowers/specs/2026-08-13-second-brain-design.md", "scripts/vault-check.sh"]
tags: [vault, process]
---

# The note that specified this vault before it existed

`raw/notes/2026-08-13-owners-note-second-brain-instructions.md`. Sixty lines, written by the owner
in Russian, titled *«Project Librarian: LLM Wiki Configuration»* and ending with an instruction to
its reader: **create `CLAUDE.md` at the root of your Obsidian vault and paste this text into it.**
That file exists — the vault's own `CLAUDE.md` is this note's descendant — and it is longer, because
several of the note's rules were changed on the way and several more were added.

**Everything in it is written in the present tense about a store that did not exist yet.** It is an
instruction, never an observation, and it is the only kind of source in `raw/` of which that is
true: the handoffs are testimony about a working tree. Reading it as a record produces pages that
describe mechanisms nobody built —
[[an-intent-note-compiled-as-testimony-describes-things-nobody-built]].

Its bracketed numbers — `[7, 12-14]`, `[23, 26, 34, 35]` — cite the external source set it was
compiled from, the method described at <https://www.aibyaakash.com/p/karpathy-second-brain>. **They
resolve to nothing in this repository and must not be chased as line references.**

It is one of two. The other, `raw/notes/2026-08-13-owners-note-second-brain-info.md`, is the method
note and is **still uncompiled**. Why the vault exists at all is
[[the-handoff-splits-into-a-handoff-and-a-knowledge-base]].

*(That paragraph was true until 2026-08-15.)* **The method note is now compiled too** —
[[the-owners-method-note-and-what-was-built-from-it]] — and reading the two side by side found
that **they disagree with each other on five points**, three of which are rows in the table below:
the category set, the `type:` enum and the filename rule. On each of them the build followed the
other note. The accounting here stands; what it lacked was the second witness.

## What became of each instruction

Compiled 2026-08-14; the line numbers are in the sidecar beside the note. "Built" means the
mechanism is on disk and can be read today; "unbuilt" means it is not, whatever the note says.

| The note asks for | What became of it |
|---|---|
| a compiled knowledge base; Claude Code as its librarian; atomic pages out of raw handoffs | **built** — [[journal-vault-brief-each-artefact-has-one-owner]], [[vault-librarian]] |
| goal: accumulate context, **exclude contradictions**, ready the base for developer agents | **built, except the verb.** The store does not eliminate a contradiction; it marks both pages and refuses to choose, because choosing is a judgement about the project — [[the-librarian-writes-unattended]] |
| `raw/handoffs/` immutable | **built**, and rule 8 of `vault-check.sh` is the only structural rule that reaches inside `raw/`: it fails a journal that has dropped one of its eight sections |
| `wiki/` written by the agent only | **built as a convention, not as a lock.** The guard hook cannot tell who is writing, and two librarians in parallel broke it once: [[parallel-librarians-break-the-one-writer-property]] |
| `wiki/entities/`, `wiki/decisions/` | **built** |
| `wiki/tasks/` — status and detail of this sprint's tasks and past ones | **unbuilt, deliberately** — [[the-wiki-has-no-tasks-folder]], retired 2026-08-15 in favour of [[the-wiki-has-five-folders-and-tasks-is-not-one]]: the set is five now, and `tasks/` is refused on the same two grounds |
| `wiki/index.md`, an automatically updated catalogue of every page | **decided both ways on 2026-08-15, and no longer a divergence.** The catalogue was built and is *generated* — [[the-catalogue-is-generated-not-maintained]]; `index.md` stays a map and stays at the vault root — [[the-index-is-a-map-not-a-catalogue]], [[index-md-stays-at-the-vault-root]]. *(This row read "unbuilt, twice over" until then, and the block below carried `> [!CAUTION] CONTRADICTION`.)* |
| `log.md`, a chronological journal of the librarian's actions | **built**, and it is half of what makes unattended writing reviewable: `git diff` says what changed, `log.md` says why |
| `archive/` for deprecated pages **and finished handoffs** | **half built.** Retired pages move there; handoffs never do, and that was measured before it was ever run — [[a-sprint-closes-on-its-goal]] |
| atomicity: one entity or one decision per file | **built**, in the vault's `CLAUDE.md`, in those words |
| filenames `[category]-[short-description].md` | **rejected by the owner on 2026-08-15** — [[filenames-carry-no-category-prefix]]. No page carries a prefix; the category is the folder and the `type:` field, so a prefix is a third copy, and a name beginning with a word a third of the corpus shares is worse to grep. *(This row read "diverged, by nobody's recorded decision" until then — and the counter-evidence, his own prefix-free example in the method note, was in `sources:` the whole time: [[summarised-sources-lose-the-disagreement-between-them]].)* |
| frontmatter: `title`, `type`, `status: active`, `created`, `sources` | **built and outgrown.** `type` gained `concept` and `lesson` and lost `task`; **`active` is spelled `current`**; `basis`, `authority`, `sprint`, `decided`, `tags` and the two supersession fields were added. All of it is enforced by `vault-check.sh` rule 2 |
| `[[wikilinks]]` between pages | **built and load-bearing** — a broken link and an orphan page are both hard failures, because an exact grep is the one retrieval path known to fail across languages |
| on a conflict: mark `> [!CAUTION] CONTRADICTION` **and ask the owner** | **the marking is built; the asking was dropped.** An answer given in chat leaves no artefact, so the marking *is* the artefact and the brief raises it — [[the-librarian-writes-unattended]] |
| `/ingest`, run by hand when a handoff appears: read it, update `wiki/`, supersede, update `index.md` and `log.md` | **built, with a firmer trigger and a different body.** A session *ends* with `/handoff` then `/ingest`; "update the wiki" was replaced by units with verdicts — [[ingest-is-units-and-verdicts]]; the strict template it reads is [[the-handoff-template-maps-onto-the-categories]]; supersession gained the reverse link `supersedes:`; `index.md` is touched only when the map itself changes |
| `/lint` at the end of a sprint: orphans, stale `status`, `entities/` reconciled against `decisions/` | **built, and never once run** — [[lint-waits-for-an-open-sprint]]. Orphans and the status vocabulary went mechanical instead, into `vault-check.sh` on every write. **The third check does not exist**: `/vault-lint`'s six items do not include reconciling `entities/` against `decisions/`, and nothing else does it. The method note's list has a fourth item of its own — *«отсутствие необходимых концептуальных страниц»* — and that one is not built either ([[the-owners-method-note-and-what-was-built-from-it]]) |
| `/pre-task`: the developer agent reads `index.md` and every `active` file in `decisions/` | **built differently.** The agent dispatches the librarian instead of reading the vault itself, and the librarian enumerates the frontmatter of *every* `decisions/` page and opens only what the titles implicate — [[one-librarian-behind-every-caller]]. Followed literally today it would return nothing: `index.md` lists no pages |
| sprint closure: a final `/ingest`, then this sprint's handoffs into `archive/sprints/sprint-N/` | **the first is built stronger** — an ingest closes every session, not every sprint. **The second was rejected by measurement**: 31 pages cited `raw/handoffs/…` in `sources:`, so the first close would have turned the check red on all 31 — **95 of 111 re-measured 2026-08-15** — [[a-sprint-closes-on-its-goal]] |

> [!NOTE] CONTRADICTION — RESOLVED 2026-08-15 BY THE OWNER
> **What stood here from 2026-08-14 to 2026-08-15**, kept because the standoff is part of the
> record: *«`index.md`: catalogue or map. This note asks for «автоматически обновляемый каталог
> всех страниц», and so does the owner's other note. [[the-index-is-a-map-not-a-catalogue]]
> declines to build one, and its own frontmatter marks that refusal `basis: inference`: the spec's
> decision table records the row without the "owner's call" attribution its neighbours carry. So a
> `human` source asks for a catalogue and an `inference` page says no. Unresolved, and not the
> librarian's to resolve. Both pages carry this block.»*
>
> **How it was settled.** The owner reaffirmed the ask and asked whether a script could satisfy it.
> It can: `scripts/vault-catalogue.sh` generates `catalogue.md` from the frontmatter of every page,
> and rule 9 of `vault-check.sh` fails while that file differs from what the script produces — so
> the objection the map was built on, that a hand-kept catalogue rots, does not apply to one nobody
> types. **Both artefacts now exist**, and the ask this row records was met rather than overruled:
> [[the-catalogue-is-generated-not-maintained]], commit `b58ec48`. The other half of the same
> phrase — the *path* `wiki/index.md` — was decided the other way and separately:
> [[index-md-stays-at-the-vault-root]].
>
> **Resolved by the owner. The librarian marked it and chose nothing**
> ([[the-librarian-writes-unattended]]), which is what the marking was for.

## What the note did not say, and it matters

There is nothing in it about **coverage** — no notion that "has this document been compiled in
full" should be a question a script can answer. That is the largest single addition the build made
to the method; it came from the owner in conversation the next day rather than from these sixty
lines ([[ingest-is-units-and-verdicts]]), and this page is one of its products.

Nothing in it about `basis` or `authority` either. Both exist to rank two sources that disagree
without the librarian overstepping — which is exactly the situation the caution above records, and
under the note's own schema there would have been no way to mark it.
