---
title: "The owner's method note is the why under the instructions, and this is what was built from each line of it"
type: entity
status: current
authority: owners-method-note
basis: human
sprint: S1
created: 2026-08-15
sources: ["raw/notes/2026-08-13-owners-note-second-brain-info.md", "raw/notes/2026-08-13-owners-note-second-brain-instructions.md", "scripts/vault-check.sh", "scripts/vault-catalogue.sh"]
tags: [vault, process]
---

# The second of the owner's two notes, and the last source in `raw/` to be compiled

`raw/notes/2026-08-13-owners-note-second-brain-info.md`, titled *«Концепция Системы: Obsidian
Second Brain как Скомпилированное Хранилище Знаний»* and naming «методология Карпати» as its
method. Compiled 2026-08-15, line by line; the sidecar beside it carries the verdicts.

Where [[the-owners-instructions-note-and-what-was-built-from-it]] is a configuration to be pasted
into a `CLAUDE.md`, **this one is the reasoning under it**: the philosophy, the three layers, the
workflow, the technical standards and the sprint cycle. The two were written the same day by the
same person and **they do not agree with each other**, which is the finding below.

**It is intent, not testimony** — present tense about a store that did not exist —
[[an-intent-note-compiled-as-testimony-describes-things-nobody-built]]. It is also written with no
markdown headings and no blank lines at all: `vault-units.sh` therefore makes every line a unit,
including the stray `.` and `:` lines a paste out of a chat left behind. **Ninety-one units, of
which twenty-nine are a full stop or a colon alone on a line** — measured with
`grep -cE '^[.:]$'`, and they are the reason the sidecar carries forty `skip:` verdicts.

## What became of each part of the method

"Built" means the mechanism is on disk and can be read today; "unbuilt" means it is not, whatever
the note says.

| The note asks for | What became of it |
|---|---|
| Obsidian as the reader/IDE, Claude Code as the librarian agent with direct filesystem access | **built** — [[the-vault-directory]], [[vault-librarian]] |
| **compilation rather than RAG**: knowledge is «вплавляется» into an existing structure by synthesis, not retrieved afresh from raw chunks; an agent writes it for an agent to read | **built, and it is the frame the retrieval decisions hang off** — [[the-vault-is-compiled-not-retrieved]] |
| three layers: `raw/` as truth, `wiki/` as compiled knowledge, `CLAUDE.md` as the constitution | **built, and there are four things rather than three.** `brief.md`, the artefact the loop actually delivers, is absent from this note entirely, and the constitution is two files — [[journal-vault-brief-each-artefact-has-one-owner]], [[claude-md-is-a-map-and-four-rules]] |
| `raw/` holds the md files produced during development **and** each sprint's handoff | **diverged.** `raw/` holds session journals and these two notes and nothing else; plans and specs live in `docs/superpowers/` and are cited from there in `sources:`. Nothing accumulates in `raw/` while a slice runs |
| `raw/` immutable, the librarian reading and never writing there | **built**, and rule 8 of `vault-check.sh` is the only structural rule that reaches inside it |
| `wiki/`: atomic notes, one entity = one file | **built**, in the vault's `CLAUDE.md`, in those words |
| `wiki/entities/` — modules, tools, people; `wiki/concepts/` — ideas, technical decisions, terms; `wiki/decisions/` — the decision log | **built**, and `concepts/` is asked for **only here**: the instructions note has no such folder and asks instead for a `tasks/` this note never mentions ([[the-wiki-has-no-tasks-folder]], retired 2026-08-15 in favour of [[the-wiki-has-five-folders-and-tasks-is-not-one]]). `lessons/` was added by the build and neither note has it, and so was `proposals/` on 2026-08-15 ([[proposals-are-a-folder-not-a-status]]) |
| `decisions/` as the register a plan is checked against before work starts | **built, and it is `/pre-task`** — the librarian enumerates the frontmatter of every `decisions/` page rather than the developer agent reading the folder ([[one-librarian-behind-every-caller]]) |
| `wiki/index.md` — an automatically updated catalogue of every page | **now built, in two pieces, and neither sits at that path.** The catalogue is generated from frontmatter ([[the-catalogue-is-generated-not-maintained]]); the map keeps the name `index.md` and stays at the vault root ([[index-md-stays-at-the-vault-root]], [[the-index-is-a-map-not-a-catalogue]]) |
| `CLAUDE.md` as the constitution: naming schemes, the YAML schema, conflict handling, archiving rules | **built**, and split in two — the vault's own holds the schema, the repository's is a map and four rules |
| a strict handoff at the end of every session **or sprint**, and `/ingest` launched by hand | **built with the weaker half dropped**: a session ends with `/handoff` then `/ingest`, and there is no sprint-sized handoff at all — [[journal-vault-brief-each-artefact-has-one-owner]], [[the-handoff-template-maps-onto-the-categories]] |
| `/ingest`: read the handoff, distribute it into atomic files in `wiki/`, cross-link, update `index.md` and `log.md` | **redefined.** "Distribute it" became units with verdicts, because *«has this been processed completely»* had to be a question a script can answer — [[ingest-is-units-and-verdicts]], [[the-verdict-is-the-write]]. `log.md` at every ingest; `index.md` only when the map itself changes |
| never delete history: mark `status: deprecated`, record the reason, move the file to `archive/` | **built**, with the reverse link `supersedes:` added — a retired page that does not name its successor is a dead end — and rule 7 fails a deprecated page still sitting in `wiki/` |
| `/lint` once per sprint: contradictions between pages, orphan pages, broken links, **and missing conceptual pages** | **three of the four went mechanical and run on every write** — rules 3, 5 and 4 of `vault-check.sh`. **"Missing conceptual pages" is unbuilt**, and it is a *different* fourth item from the one the instructions note asked for; neither exists — [[lint-waits-for-an-open-sprint]] |
| standardised YAML frontmatter on every file in `wiki/`, for machine readability | **built and enforced** by rule 2, and outgrown: `basis`, `authority`, `sprint`, `decided` and the two supersession fields were added |
| `type: decision \| concept \| entity` | **built, plus `lesson`.** This note's enum is the one that survived; the instructions note spells the third value `task` |
| `status: active \| deprecated` | **diverged.** `active` is spelled `current`, and no page has ever carried `active` |
| `tags: [проект, архитектура]` — the tags themselves in Russian | **diverged, and deliberately.** Tags are English words, 2 to 4 per page, and a Russian question reaches them through the alias list — [[aliases-carry-the-question-across-languages]] |
| filenames in kebab-case, formed by the agent, *«например, `auth-module-redesign.md`»* | **built** — and **the example carries no category prefix**, which is the practice, and it contradicts the other note's `[category]-[short-description].md`: [[filenames-carry-no-category-prefix]] |
| git as version control, *«рекомендуется делать коммиты после каждого ингеста»* so an ingest can be undone | **built as practice and enforced by nothing.** Every ingest so far is its own commit, and `log.md` beside `git diff` is what makes unattended writing reviewable ([[the-librarian-writes-unattended]]) — but no skill, hook or check requires the commit |
| the sprint cycle: an active phase accumulating files in `raw/`, a retrospective, compilation, archiving | **half built.** A sprint is declared explicitly and closes on its goal ([[a-sprint-closes-on-its-goal]]); the handoff is written at the end of every session rather than at the retrospective; and nothing accumulates in `raw/` during the active phase |
| archiving: the session's intermediate files leave and only the synthesised result stays in the base | **rejected by measurement.** 31 pages cited `raw/handoffs/…` in `sources:`, so the first close would have turned the check red on all 31 — **95 of 111 re-measured 2026-08-15** — [[a-sprint-closes-on-its-goal]] |

## The two notes disagree with each other, and it cost a day

They were written the same day by the same person, and on five points they say different things:

| | instructions note | method note | what was built |
|---|---|---|---|
| categories | `entities`, `decisions`, `tasks` | `entities`, `concepts`, `decisions` | `entities`, `concepts`, `decisions`, `lessons` |
| the `type:` enum | `entity`, `decision`, `task` | `decision`, `concept`, `entity` | plus `lesson`, minus `task` |
| filenames | `[category]-[short-description].md` | `auth-module-redesign.md` | no prefix — [[filenames-carry-no-category-prefix]] |
| frontmatter | no `tags:` field at all | `tags:`, spelled in Russian | `tags:`, in English, 2 to 4 |
| `/lint`'s fourth check | reconcile `entities/` against `decisions/` | find the missing conceptual pages | neither |

**On every one of them the build followed this note rather than the other**, and on the filename
rule that mattered: the row was recorded on 2026-08-14 as *«diverged, by nobody's recorded
decision»* while the evidence that the owner had also written a prefix-free example sat in this
file, cited in the `sources:` of three pages and read by nobody line by line. The lesson is
[[summarised-sources-lose-the-disagreement-between-them]].

## What the pages that already cited it had got right, and what they had not

Three pages carried this note in `sources:` before it was compiled.

- **[[the-index-is-a-map-not-a-catalogue]] — survives verbatim.** It says both notes ask for
  «автоматически обновляемый каталог всех страниц»; they do, in exactly those words, at line 31
  here and line 14 there. Nothing later in this note argues for a map, as that page claims.
- **[[the-handoff-splits-into-a-handoff-and-a-knowledge-base]] — accurate as a union, misleading
  as a list.** Its summary of "what they ask for" merges the two notes into one bullet list —
  «(`entities/`, `concepts/`, `decisions/`, plus a `tasks/`)», "kebab-case filenames" — and no
  single note said either of those things. The merge is where the disagreements above went.
- **[[the-owners-instructions-note-and-what-was-built-from-it]] — its own accounting stands.**
  This note adds a second witness to several of its rows and overturns none.

## What the note does not say

Nothing about **coverage** — no notion that "has this document been compiled in full" should be a
question a script can answer. Nothing about the **brief**, which is the artefact the whole loop
delivers. Nothing about `basis` or `authority`, so under this note's schema there would have been
no way to rank two sources that disagree — which is exactly what the table above had to do. And
nothing about **how a question asked in Russian reaches a page written in English**: its own
example spells the tags in Russian and stops there.
