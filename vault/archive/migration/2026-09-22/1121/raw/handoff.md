# Handoff — 2026-09-22, Slice 3f themes 4–6 and the pipeline defects

## Notes from memory

The person pushed back twice on where the atomicity rule should live, and the pushback was
right both times. First place proposed was `rule-entities-schema`, which holds Entities
only; second was the Purpose of `rule-page-schemas`, which is wider but still about pages
while the rule is also about a Case. The settled answer came from `rule-language` and
`rule-agent-writing`: a rule that cannot be checked in substance can still be a Rule if its
guard is that its text stands in the file the agent reads and does not drift from the page.
So `rule-atomicity` is `enforcement: render`, `render_mode: partial`, spliced into
`case-schema.md`, and `rule-case-protocol` becomes a MOC of one child. The one-child MOC is
legal by the precedent of `rule-claude-md` between cases 272.2 and 272.3, but if pre-spec or
lint ever judges a MOC by a count of children, this is the page that will show it.

The person also asked whether an explicit edge should record "page A leans on rule B". The
answer was no, because case 305 of the previous session ratified that a rule constrains a
case and never another rule, and a `cites` field would be a supersede of that plus a
judgment on each of the 37 existing rule-to-rule mentions. That reasoning is worth keeping:
the reuse work in the Backlog is Entity → Entity, not Rule → Rule.

The reuse discussion ended in three Backlog notes (case 319), not in Cases. The person wants
them taken up next session. The honest boundary is written into the third note: a new module
written beside an existing one in another file is caught by the vault query alone, never by
a script.

Case 322 defers Slice 3b for the nineteenth time. It has been deferred since case 29.

One decision carries a caveat I could not remove: `estimate-documentation-completes` is read
`failed`. The 0014 librarian read lines 52–64 of its own ledger while counting entries, and
its frame forbids reading the ledger at all. The brief of 0014 reported it honestly. No fix
is ratified; the next Plan Mode should decide whether the frame's wording is wrong or the
run was.

## Direct instructions to the librarian

Check first, before `generate`: several pages are touched by more than one Case of this Spec
and the `replace` anchors depend on the order of application. `rule-prespec` is written by
310.6, 314.2, 317 and 320; `rule-case-protocol` by 317, 318 and 320; `rule-skill-hi` by
310.5, 314.1 and 318; `entity-glossary` by 317, 318, 321 and 323; `entity-sprint-migration`
by 310.2, 318, 319, 320, 321 and 323. In particular 314.2's `old` was rewritten during
pre-spec to anchor on the tail that 310.6 writes — if 310.6 fails, 314.2 fails after it.
Case 321 writes the whole `## Milestones` section of the sprint page, which discards the
earlier `replace` pairs of 310.2 and 320 on that section by design; those pairs must still
hit, or `generate` will fail them.

`entity-sprint-migration` ends with six Estimates, not four: 310.3 and 320 each create one
with `ref: entity-sprint-migration`. Case 323 rewrites the Purpose so it names no number.

Nothing in this Spec creates a page whose slug an existing page carries; `ask-guppi` checked
all eleven new slugs at pre-spec and every one was free, live and archived.

`vault/wiki/index.md` was deleted by hand in Work Mode, before the page updates. Between the
deletion and your `generate`, `guppi lint` reports one extra `ref` finding —
`rules/rule-case-protocol: ref: body names index` — which 318's `replace` removes. If it
survives your run, 318's pair did not hit.

The two lessons of this session share a family with `lesson-reword-pairs-signed-before-the-places-were-read`:
`lesson-replace-anchors-overlap-in-one-spec` is the second occurrence of anchors written
without reading the place. Judge whether that is an Insight.

## What actually got done

Ratified: 21 Cases, 308.1 through 323, plus the defer 322. Cases 310.1 and 310.4 were
superseded in the session by 313 and 320 and left the Spec.

Code landed in five scripts and their tests, commit `bfe18d9` on `migration`:
`guppi/lint.py` gained `check_layout` (315); `guppi/sprint.py` takes every wikilink before
the first " — " as the pages of an item and renders a note without a tick (313);
`guppi/prespec.py` accepts the closer `sprint`, binds a sprint line to an `update` of the
sprint page and refuses any item carrying `file` (310.6, 314.2, 320); `guppi/materialize.py`
lifts a create whole when the unit changes that category's schema rule, moves a folded
reading on a supersede, and lost `RULE_CLASS`, `rule_class_path` and the `category: file`
route (308.2, 309, 320); `guppi/generate.py` ticks every `read` line of a slug in the first
Spec that holds one and lost the Rule-class branch (312, 320). `make test` 548 passed, 2
skipped; `make style` clean.

`vault/wiki/index.md` is deleted.

Sixteen readings were written: fifteen `passed`, one `failed`
(`estimate-documentation-completes`).

Not done, and why: every page of the vault — that is your run. Eight readings whose moment
has not come — `estimate-hi-writes-frontier` (the next `/hi`), `estimate-harness-pipeline`,
`estimate-sprint-migration-rule-class-files-dissolved`, `estimate-atomicity-rendered`,
`estimate-sprint-migration-index-dissolved`, `estimate-case-protocol-ledger-line-form`,
`estimate-case-protocol-case-form`, `estimate-generate-fails-alone` (all after your run, by
their `method`), and `estimate-session-phases-in-order` (after your commit). The by-hand
check of 308.1 — that `entity-glossary` carries `rules: ["[[rule-glossary]]"]` — also waits
for your cascade. Slice 3b was not taken.

One open question for the next Plan Mode, from Retro: the `## Work` lines of the Frontier
were closed `· work` before their work was done, because `/pre-spec` refuses an open line
and the readings happen in Work Mode, after it. The form allows it; the moment of closing
and the moment of the work have come apart.
