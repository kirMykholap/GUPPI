---
session: 2026-08-15
sprint: S1
commits: 42f7a56..cfaa25e
---

# Handoff — 2026-08-15

The session opened on 2026-08-14 and crossed midnight; everything written after that carries
2026-08-15, which is why the sprint record, the pages and this journal disagree with the commit
dates on the first two commits. The dates are right; the session is one.

## 1. State

**Done.** S1 was opened — the first sprint this project has ever declared — and its four acceptance
criteria were written at the opening, each naming the command that decides it. Both of the owner's
notes are compiled, so **all six sources in `raw/` report INGEST COMPLETE** for the first time
(332, 33, 46, 59, 91, 31 units): criterion 2 is met, and met by its own command rather than by
anybody's word. The unit rule was fixed. The catalogue was built and generated. A fifth category
was added. The first `/vault-lint` in this vault's life was run over 108 pages.

**Not done.** Criterion 1 is not met: the audit ran and every finding is recorded with an outcome,
but **six outcomes are "owed to the owner"** and a finding without a fix or a `decisions/` page is
the criterion unmet. Criterion 3 (the three tag advisories) now has its evidence and no decision.
Criterion 4 is the owner's and its question changed shape today — see §3.

**In flight: nothing.** The tree is clean at `cfaa25e`, `vault-check.sh` green.

**Checks.** `bash scripts/vault-check.sh` — ok, three standing advisories (`vault` 42, `process`
40, `testing` 26 of 108). `bash scripts/vault-check-selftest.sh` — **61 of 61, 0 missed**, up from
55; measured wall-clock **201s**, of which about 43s is the catalogue regeneration this session
added (43 wrapper cases times 1.0s measured). `vault-coverage.sh` over all six sources — INGEST
COMPLETE on every one. **`pytest` and `ruff` were not run, and correctly so: `src/` and `tests/`
were not touched at any point today.** No browser walk, for the same reason.

**Next step.** The six decisions in §6, then `/ingest`. Nothing else is queued, and the product has
had no work since 2026-08-12.

## 2. Entities

**Appeared.**

- **`scripts/vault-catalogue.sh`** — generates `catalogue.md` from the frontmatter of every page in
  `wiki/` and `archive/`; five columns per row, grouped by category, counts produced by the run
  that produces the rows. `--write` saves. **1.0s over 108 pages**: all of a section's pages go
  through one `awk`, after a first version at one `awk` per file cost the selftest minutes.
- **`catalogue.md`** — a fifth top-level artefact beside `index.md`, `tags.md`, `sprint.md`,
  `log.md`, `brief.md`. Derived, never typed.
- **`wiki/proposals/`** — the fifth category: what was raised or designed and never built.
- **Rule 9 of `vault-check.sh`** — the catalogue is what the generator produces or the gate is red.
  The script now names five `wiki/` folders; failing conditions 17 to 18.
- **Five new selftest cases** — three for the category, two for the catalogue; the empty-vault
  fixture learned the fifth directory. 55 to 61 cases.

**Changed.** `vault-units.sh` counts a paragraph written flush under a heading. The vault's
`CLAUDE.md` carries the new category, the catalogue row, and the obligation to regenerate after any
write under `wiki/` or `archive/`. `/ingest` gained step 1b (an intention is filed in `proposals/`)
and the catalogue regeneration in step 10. The corpus went **96 to 111 pages**, 108 in `wiki/` and
3 in `archive/`.

**Taken out of service.** `the-wiki-has-no-tasks-folder` and
`the-language-rule-applies-only-to-new-work`, both to `archive/` with `superseded_by:` — in both
cases because the page's *title* carried the claim that changed, and a title cannot be edited into
truth without leaving a grep landing on a page that lies.

## 3. Decisions

All the owner's, all 2026-08-15 unless stated.

- **The catalogue is generated, not maintained.** He reaffirmed the ask his notes made twice —
  «автоматически обновляемый каталог всех страниц» — and asked the question that settled it: could
  a script do it. **This resolved the contradiction** marked the day before on two pages: the
  argument the map rests on is that a second copy diverges, and it does not reach a copy nobody
  types. Rejected: leaving the ask refused. Obliges: `--write` after every write to the corpus, and
  the catalogue staying **out of the link set** for ever.
- **Filenames carry no category prefix.** Rejected: `[category]-[short-description].md`, which his
  instructions note asked for. Reasons his: the category is already written by the folder and by
  `type:`; the filename is search surface; renaming would break every wikilink and `sources:`
  entry.
- **`index.md` stays at the vault root.** Rejected: `wiki/index.md`, which both notes ask for. His
  reason, verbatim: *it is a part for the agent, not the knowledge base.*
- **A proposal is a folder, not a status.** He asked for a status like «предложено»/«отложено» to
  answer *what did we plan and never do*. Rejected in favour of a folder, and the reason is this
  project's own scar tissue: a `status:` field asks to be read carefully, a folder makes the
  mistake structurally impossible, and intent has twice been compiled here as though it were a
  record of something built. Obliges: `status` stays two-valued, and **deferral remains a
  decision** — `decisions/` records *that* we said not now, `proposals/` carries *what* we would
  build.
- **English is the rule; the Russian past is deferred, not exempt.** The "new work only" rule had
  become a standing exemption over **10947 Cyrillic lines in 107 files** (tests 4916, docs 3740,
  src 2044, templates 228, scripts 19). The product UI keeps its Russian permanently on separate
  ground. Nothing is mass-translated *now*, and that is a deferral with a reason rather than a
  boundary with a date.
- **The paragraph was deleted deliberately.** The ingest of 2026-08-14 read the disappearance of
  the language rule from `CLAUDE.md` as a loss and revived it as a page. The owner said today that
  he removed it by hand. This changes criterion 4 of the sprint: the question is no longer only
  "what catches a rule lost in a cut" but "what tells a loss from a deletion", and **an
  `elsewhere:CLAUDE.md` verdict cannot answer either on its own**. Nine such verdicts exist.
- **Process, mine, stated for the record:** the audit was split from the writing into its own
  dispatch, because an audit run before the writes would have examined a corpus that was about to
  change. It cost one extra fixed part, about 15 minutes.

## 4. How it is built

- **The unit rule's third defeating shape.** `vault-units.sh` documents two — a file with no blank
  lines, an unclosed fence — and had a third open: a paragraph opens "after a blank line", and a
  heading reset that flag, so text flush against its heading was invisible to the denominator. The
  fix is `blank = 1` on the heading rule. **Priced before it was applied**: +2 units across all six
  sources, both in one note, one of them already verdicted by hand. A bullet is deliberately not
  treated this way — a line under a bullet is that bullet's continuation, not a claim.
- **Staleness is asked by regenerating, never by mtime.** Rule 9 regenerates the catalogue and
  diffs. A checkout rewrites mtimes, and the first staleness check in this project fired on every
  clone for exactly that reason.
- **The catalogue must never join the link set.** An orphan is a page nothing links to; the
  catalogue links to everything. Had it joined the registers rule 5 reads, the orphan rule would
  have kept running, kept passing, and proved nothing. The register list is an allowlist, so the
  catalogue is excluded by absence — and a selftest case plants an orphan, **regenerates the
  catalogue so that it does link to it**, and still demands the orphan be reported.
- **A rule that touches every page makes every unrelated test fragile.** Adding rule 9 failed 14
  selftest cases at once, none of them about the catalogue: any mutation makes it stale. The
  wrappers regenerate after the mutation, which is the same courtesy the source placeholders
  already receive, and the catalogue's own two cases deliberately do not use the wrappers.
- **Fidelity to a source and fidelity to the tree are different properties.** The audit sampled ten
  of the most-cited pages against the lines their sidecars name: ten of ten still say what the
  source said. Six pages said what the repository no longer does. Only the first has ever been
  checked here, and no script checks either.

## 5. Lessons

- **Two sources read as one lose the disagreement between them.** One page had merged the owner's
  two notes into a single reading: its list is true of the pair and stated by neither. They
  disagree on five points and the build followed the method note on all five. The bill is dated —
  the filename prefix was recorded on 2026-08-14 as "diverged, by nobody's recorded decision" while
  the owner's own prefix-free example sat in the uncompiled file, cited in three pages' `sources:`.
- **A commit-stamped number survives; a present-tense one drifts.** Six stated counts had moved:
  "N at `<commit>`" was right every time, "it is now N" wrong every time. And **five of the six
  understated** — a corpus grows and a copied number does not, so a stale count usually leaves its
  argument *stronger* than the page claims. That is why nothing breaks and nobody looks. The
  register on the lesson page went from six instances to twelve.
- **A live page can argue from a deprecated one, and no rule catches it.** A link into `archive/`
  resolves perfectly. Found by reading, in the first audit.
- **My own two measurements lied today, in opposite directions.** `grep -P` with a Cyrillic range
  reported **zero** matches in a repository holding eleven thousand such lines — the flag is
  unsupported in this environment and the failure is silent and green. And I counted eight AST
  boundary tests by globbing a name, where one was the shared helper `_ast_boundary.py`; the page's
  "seven" was right and my correction was wrong. **A measurement that agrees with no expectation
  deserves a second instrument before it is quoted.**
- **The audit's own arithmetic drifted by one** — its report said +320 where the tree says +321,
  inside the audit of numbers drifting from their lists. The finding declining to end.
- **The staleness hook fired for real for the first time**, on resume: *6 commits have landed since
  36e9e4c*. It counts from the commit that carries the brief, not from the brief's own stamp, and
  the count was exact.

## 6. Deferred

**Six findings from the audit are owed to the owner**, and each is deferred with a reason:

- **Two retitles** — `/lint has never run` (it has) and `two staleness checks` (there are three).
  Retitling is supersession, and the librarian refused to do it inside the run that falsified them,
  because that would erase why the deferral existed. Consequence: two current pages carry titles
  that are false today.
- **The three tag advisories** (criterion 3). Evidence gathered: `vault` 42 is four strata with 25
  overlapping `process`; `process` 40 gives up an `environment` tag most cheaply (5 pages);
  `testing` 26 splits on *accounting*, not on the vault/product line already rejected on
  2026-08-13; and `batches` is a strict subset of `collection`, selecting nothing new. **Tags grow
  at 35% against the corpus's 14%.** Consequence: an advisory that stands for a fourth day stops
  being read.
- **`index.md` is obeying its rule and failing anyway** — no per-page rows, and 4.2x growth against
  the corpus's 3.7x: thirteen hub rows each defensible alone, and two paragraphs restating other
  pages instead of linking them, in the file whose founding argument is that second copies diverge.
  Trimming a map is deleting text and the map's shape is the owner's. Consequence: the failure
  arrives by prose instead of by rows.
- **`.gitattributes` pins only `*.sh`**, so 52 of 111 pages are CRLF and 59 LF. The `git status`
  overstatement is not an event but the standing state. Consequence of fixing: one commit that
  rewrites 59 files and nothing else. Consequence of not: every session reads `git status` twice.
- **Three proposals that do not exist**: reconciling `entities/` against `decisions/` (asked for by
  the owner's note, built by nothing), a check for missing conceptual pages, and a rule comparing a
  stated count against the list it heads. All three currently live as clauses inside other pages.
- **`.claude/skills/vault-lint/SKILL.md` does not know about the fifth category** or about the
  `> [!NOTE] CONTRADICTION — RESOLVED` shape used today.

**Also deferred:** the selftest's 201s (the one-`awk`-per-run optimisation would return about 30s
of it); the module map, the CLI and the data model, which are uncompiled and **have no source in
`raw/` to be compiled from** — that is the finding, not the gap; and the English migration itself.

## 7. Feedback to the librarian

- measure: first end-to-end measurement of an ingest, 2026-08-14. One `vault-librarian` dispatch
  compiling `raw/notes/...-instructions.md` (38 lines from vault-units.sh, 29 counted units, 43
  sidecar lines) reported by the harness as `subagent_tokens: 144119`, `duration_ms: 924804`
  (15m25s), `tool_uses: 66`. Produced 3 pages, 5 updates, 1 CONTRADICTION. The composition of
  `subagent_tokens` is still undocumented, so it is recorded as observed and not converted to a
  rate or to money. Until now only single librarian *questions* had numbers (3-8 min each); an
  ingest is a different class of work and this is its first figure.
- lint: `vault-units.sh` misses one shape of document, and it is the third of a family the script
  was written to close. A paragraph is counted when it follows a blank line, and a file with no
  blank lines at all is handled explicitly - but a **heading sets `blank = 0`**, so a paragraph
  written directly under a heading, with no blank line between, is invisible to the denominator.
  Measured 2026-08-14 across all six sources: the one-line fix (`blank = 1` on the heading rule)
  adds **+2 units in total**, both in the instructions note - line 4, already verdicted by hand,
  and line 55, which is not. So the whole cost of closing it is one line of awk and one verdict,
  and no closed source goes red. Found on the first document that was not written from our own
  template, which is what a limitation of this kind waits for.
  *(An earlier version of this entry said prose was uncounted and a prose document would have a
  denominator near zero. That was wrong on both halves and is corrected here: paragraph openers
  are counted, and the no-blank-lines shape is handled in the script by name.)*
- lint: the librarian's own report miscounted its sidecar - `page:` 28 and `skip:` 10 reported
  against 27 and 11 measured by `cut -f2 | sort | uniq -c`. Harmless here because the sidecar is
  the artefact and the script reads it, not the report. Recorded because it is another instance of
  [[a-stated-count-drifts-from-the-list-it-heads]], this time inside the agent that maintains the
  page saying so, which is where the rule is least likely to be applied to itself.
- lint: the vault's own `CLAUDE.md` describes `archive/` as "deprecated pages, and the handoffs of
  closed sprints". Handoffs never move there and never will: 31 pages cite `raw/handoffs/...` in
  `sources:`, so the first close would turn the check red on all 31, and that was measured before
  the idea was ever run - [[a-sprint-closes-on-its-goal]]. The schema file is not a wiki page, so
  no rule and no check compares it against the decisions it contradicts, and this is the second
  time a claim living only in a `CLAUDE.md` has gone stale without anything noticing.
- measure: second ingest figure, 2026-08-15. One `vault-librarian` dispatch carrying three tasks -
  compile the 91-unit method note, write one verdict owed by the unit-rule fix, and record three
  owner decisions - reported by the harness as `subagent_tokens: 183809`, `duration_ms: 1765573`
  (29m26s), `tool_uses: 103`. Produced 6 pages, 8 updated, 3 registers, one contradiction resolved.
  With the first figure (29 units, 15m25s, 144119 tokens, 66 tool uses) there are now two points:
  roughly three times the units for twice the wall-clock, so the fixed cost of a dispatch is a
  large share of a small one. Both are single dispatches, and neither says anything about what a
  dispatch carrying one task costs. Composition of `subagent_tokens` is still undocumented.
- measure: third and fourth librarian figures, 2026-08-15. A **writing-only** dispatch - four
  tasks, no source compiled - `subagent_tokens: 125348`, `duration_ms: 866283` (14m26s),
  `tool_uses: 58`, producing 5 pages, 2 supersessions, 6 updates. The **first `/vault-lint` ever**,
  over 108 pages: `subagent_tokens: 232794`, `duration_ms: 1593781` (26m34s), `tool_uses: 131`, 13
  findings, 16 pages fixed. Four dispatches today total 85m51s and 686070 subagent tokens. The four
  points say the fixed cost dominates a small dispatch and that an audit costs about what a large
  ingest does.
- lint: the `archive/` entry above quotes "31 pages cite `raw/handoffs/...`". The audit of
  2026-08-15 measured **95 of 111** and fixed that number on the four pages carrying it. The entry
  is left as written because it is testimony about what was believed at the time; the correction
  belongs beside it, not inside it - which is the same rule `raw/` lives by.

**Questions for the owner**, beyond the six deferred findings: whether criterion 4 of S1 still
means what it did, now that the paragraph turns out to have been deleted on purpose.

## 8. Anything else worth keeping

**Four librarian dispatches were measured today** — 15m25s, 29m26s, 14m26s, 26m34s; 144119,
183809, 125348 and 232794 `subagent_tokens`; 66, 103, 58 and 131 tool uses. **85m51s and 686070
tokens in one session.** Before today the only figures in this project were for single librarian
*questions*, 3 to 8 minutes each, and a page warned that the implementer-trip number must not be
applied to a retrieval agent. There are now four points for the writing class of work.

**The review half of the ingest skill earned its keep three times.** Each dispatch was checked
against `git diff`, the registers and a fidelity sample rather than against its own report: the
first miscounted its sidecar by one in each direction, the fourth was off by one insertion, and the
third *corrected two figures in the brief it was handed* rather than repeating them — 217 tag
assignments was stale by twelve, and "35 python files" is 34 plus `app.css`. It also refused to
write a number that no source records and no measurement can now recover.

**The catalogue's first regeneration after the audit was byte-identical**, which is the quiet proof
that the audit changed no frontmatter — sixteen pages rewritten and not one `title`, `status`,
`sprint` or `tags` line among them.

**`brief.md` was deliberately untouched all session.** Its `ingested:` field is compared by the
hook against the newest *journal* by name, so a brief regenerated from a note would have fired a
false alarm; it is regenerated by the `/ingest` that follows this file.
