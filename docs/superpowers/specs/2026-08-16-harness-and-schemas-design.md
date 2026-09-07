# Harness compiled from rules, and a schema per record type

Status: **in design.** Written during the session of 2026-08-16, as the decisions were taken,
so that they survive the session rather than the context window. Nothing here is built.

Two parts, taken in this order by the owner: the harness first, the schemas second.

## Part 1 — the harness is compiled, not maintained

Settled in conversation on 2026-08-16.

| # | Decided | Ground |
|---|---|---|
| 1 | **No symlinks.** | Measured: `core.symlinks=false` in this repo and `ln -s` yields a copy. A committed symlink checks out as a text file holding the target path, so `CLAUDE.md` would contain one line of path and no instructions. It would also hard-code the vault's directory name, which nothing may do |
| 2 | `context: fork` **exists** and is used for `/ingest`. | Documented. A forked skill is a subagent: it has no access to conversation history, which makes the handoff's self-sufficiency a precondition rather than a preference |
| 3 | **A harness change is recorded the moment it is decided**, as a marked line in `.superpowers/sdd/vault-feedback.md`. | No classifier anywhere. A classifier detects presence and cannot detect absence, so a missed rule would be unbounded |
| 4 | **The handoff carries a harness section of its own.** | `/ingest` cuts on the section boundary. Cutting on a marker inside prose would be the classifier again, re-entering through the back door |
| 5 | **The librarian keeps its monopoly on the wiki** and writes both the decision and the rule page. The steward is scripts that run after it. | Two unattended writers already lost a write once (2026-08-14, `tags.md`); a lost update leaves no trace in `git diff`. Sequencing costs nothing because the steward's work is a script |
| 6 | **The retrospective report is transient** and never enters `raw/`. | It is testimony known in advance to be corrected by the grill that follows it. Committing both would leave the vault two accounts of one session and no rule for which wins |
| 7 | **The gate runs at SessionStart**, reports into the brief, and has a manual entry point. | The brief is the junction between the store and a working session, and the hook is already there |
| 8 | **Marked regions**, not whole-file rendering. The file owns the skeleton, the pages own the text. `settings.json` is rendered whole. | `SKILL.md` and `AGENT.md` are procedures, not projections of knowledge; moving them into the wiki would move the copy problem rather than solve it. Region order is given by where the markers already sit, which answers the ordering objection to many small pages |
| 9 | **`asserts:` is a closed set of predicates with a flat, line-oriented syntax.** | The pages are written unattended, so an arbitrary shell predicate would let the store execute what an agent wrote. Flat because there is no YAML parser: PyYAML is absent and the stdlib has none |
| 10 | **A rule carries `governs:`, never `authority:`.** | A rule does not answer a question, it issues an instruction. Sharing the slug with its decision would make rule 3 print a contradiction on every normal decision-rule pair |
| 11 | **`/ingest`: one dispatch, sources compiled one at a time inside it.** | The measurement the cadence decision rests on only holds for a single dispatch. "One at a time" stays true of compilation and stops being true of dispatch |
| 12 | **Regions are marked up gradually**, starting with `.claude/skills/ingest/SKILL.md` and the repository's `CLAUDE.md`. | Both have recorded divergences already. Marking everything up front is the same cost as reading the corpus by eye, which this project has already refused |

### The three divergences found while designing this

All three are the class the design exists to prevent, and all three were found by a human — or an
agent — reading two files side by side. They are recorded in `vault-feedback.md`.

1. `.claude/skills/ingest/SKILL.md` says *never batch several handoffs*; the decision of 2026-08-16
   says the opposite. The skill's last commit predates the decision.
2. The vault's `CLAUDE.md` documents the contradiction check as `rg "^authority:" wiki -o | sort |
   uniq -d`. Without a capture group that prints the literal `authority:` once per match, so it
   reports a spurious duplicate whenever two pages carry the field and never compares the slugs.
   `vault-check.sh` rule 3 implements it correctly, so only the documentation is false.
3. `claude-md-can-lose-an-assertion-but-cannot-strand-a-page` says *four instances* in prose and
   lists five rows in the table beneath it.

## Part 2 — a schema per record type

Open. Recorded as each field is settled.

### The test a field has to pass

**A field is required only when something reads it and fails without it.** Everything else is
optional, or is documentation and must say so. The ground is this project's own acceptance model:
every criterion names the command that decides it, and a required field nothing reads can be wrong
forever.

### Settled

- **`basis`** stays, and its five values become an enumeration the check validates. It is the only
  field conflict resolution rests on — a page on `human` outranks one on `inference` — and today
  `basis: banana` passes.
- **`authority` needs a register**, the shape of `tags.md`: the questions already claimed, consulted
  before a new one is minted. Its absence is why 133 pages carry 133 unique slugs. With a register
  the field becomes rare rather than universal, and the check moves from after the fact to the
  moment of writing.
- **`proposals` carry no `authority`, and that is correct rather than accidental.** Two competing
  proposals about one problem are legitimate; flagging them as a contradiction would be wrong.

### The core: seven fields, plus `updated`

The test was refined by the data. **A field earns its place when (a) something reads it and fails
without it, or (b) it independently restates a fact the tree already asserts, so a disagreement
catches a writer's error.** (b) is a checksum, not duplication: `status` and `type` agree with their
folder on every page of the corpus and always have, which means the checksum has never fired — not
that it is idle.

| field | the question it answers | why it stays |
|---|---|---|
| `title` | what does this page say, in one line, in a search result | read by the catalogue, the librarian, the owner. Its own rule — a title carries no measurable quantity — is unchecked, and eight titles fail it |
| `type` | which category is this | (b) — catches a page filed into the wrong folder by an unattended writer |
| `status` | is this page live or retired | (a) rule 3 collects `authority` from `current` pages only; and (b) against `archive/`. **(a) holds only while `archive/` is scanned** |
| `created` | when did this page appear | the weakest case: git records it better, and batched ingest widens the gap between writing and committing. Kept, and owed a sanity check — not in the future, not before the first commit |
| `sources` | what does this rest on, and where is it checked | the most earned of the six. It already caught a real failure: seventeen pages citing a stale prefix after a rename |
| `tags` | what is this about | the only field with complete machinery — dictionary, aliases, an obligation to consult before minting. That machinery is the model for the `authority` register |
| `sprint` | which sprint did this page come from — **origin, never membership** | no consumer but the catalogue's printer. Kept and **labelled documentation in the schema**, because a field with no consumer that looks like an index eventually becomes one, and then a query for the current sprint returns only recent knowledge |
| `updated` | when was this page last touched | **stamped by a script from the diff. No obligation on any writer.** See below |

### What `updated` is for, and what it is not

Its role is larger than "did this file ever change": it is the left-hand side of the check this
vault has named, measured and never built. `fidelity-to-a-source-and-fidelity-to-the-tree` records
*fidelity to the tree: checked by **nothing***, and **six pages measured on 2026-08-15 as describing
what the repository no longer does**. Rule 11 proves a cited path exists, never that the file still
holds the claim.

The instrument needs no new input:

```
for each page:  d = updated (else created)
                for each source that is a live file of the tree:
                    if that file's last commit is newer than d  ->  the page is SUSPECT
```

One `git log --name-only` pass dates every file at once. **Coverage is 91 pages of 142**; the other
51 cite only the immutable `raw/` and are invisible to it, although a page compiled from a journal
can go stale against the code exactly as any other can. That is a limit, not an omission.

**`updated` does not clear a suspicion.** Stamped by a script, it means bytes moved, not that anyone
re-read the sources — so a typo fix would clear a suspicion silently, in the dangerous direction.
The suspicion is a **finding, and a finding carries an outcome**, which is how every other finding
in this project is closed (S1 criterion 1). The acknowledgement is deliberate and written; the date
is automatic and carries no weight it cannot hold.

Two mechanics: the stamper compares content **excluding its own line**, or it re-triggers on itself;
and the write ritual becomes **stamp -> catalogue -> check**, because stamping modifies files and
rule 9 would otherwise fail on the catalogue the stamp just invalidated.

### Per type, above the core

**`decisions`**

- **`decided` stays.** Only 8 decision pages of 58 carry the date in their H1, so for fifty of them
  the field is the sole carrier and git cannot recover it — git dates the writing, not the deciding.
  Batched ingest widens that gap: dropping the field would make every decision of a sprint look
  taken on the day of its retrospective. Owed a check: `decided <= created`.
- **`supersedes` stays, and gains a symmetry rule.** The schema requires the link in both
  directions and explains why — *a deprecated page that does not name its successor is a dead end* —
  and **nothing checks it**. `A supersedes B` with `B` silent passes today, which breaks the chain
  the field exists to keep.

**`proposals`** — left as it stands, **with a mark to revisit**. The defect is recorded rather than
fixed: there are two statuses and a proposal has three states, so `deprecated` cannot distinguish
*built* from *refused* — which is the question the category was created to answer.

**`lessons`, `concepts`** — nothing above the core.

**`rules`** — `governs:` (required, unique: two rules rendering into one region is a contradiction)
and `asserts:` (optional). `governs` keeps the harness **saying** what the vault holds; `asserts`
keeps the tree **being** what the rule claims.

**`entities` — the codebase, the harness, the pipeline and the tests get pages.** Today all fifteen
describe tooling and environment and **none describes the application**, while `src/jobhunt/` is 42
files under five packages with 40 test files.

The recorded objection is serious: a module map has no source in `raw/`, which is the same ground
`tasks/` was refused on, and a hand-maintained map is exactly the `CLAUDE.md` block that went stale
within an hour of a file move. **Both are answered by the two mechanisms designed above, and neither
would answer alone:** `asserts:` catches the structure moving, and `sources:` plus the staleness
detector flags the prose when the code it describes gets a commit. For pages about the application
that detector's coverage is total, because their sources are code.

Three bounds so it stays a map rather than a second codebase: **one page per package, not per
file**; **written when that area is worked on**, never as one cartography pass; and **no coverage
numbers** — name the test files, which `asserts:` can check, because a stated count drifts from the
list it heads.

**Sequenced after `asserts:` and the detector exist.** Before them it is a second "Where things
are", and it would rot on schedule.

## Part 3 — what `raw/` is for, and where artefacts live

**Measured, and the measurement decides it:** the journal of 2026-08-16 is **75 units** and cost a
15-29 minute dispatch. A spec is 175-289 units; a plan is 354-525. `docs/superpowers/` holds 16 644
lines of plans against 2 488 lines across all six journals — roughly **ten times the present ingest
workload**, and every unit owes a verdict.

**The principle: `raw/` holds testimony, not artefacts.** A journal is testimony; a retrospective
and its grill are testimony; **a spec and a plan are artefacts — an instruction that was executed.**
Testimony is compiled. Artefacts are frozen and cited.

The mechanical proof is S1's own criterion 2 — *every source in `raw/` reports `INGEST COMPLETE`*.
A spec placed there breaks that criterion by construction, because it will never earn 289 verdicts.

**Freezing is what artefacts actually need.** Thirteen pages cite
`docs/superpowers/specs/2026-08-13-second-brain-design.md`, a **mutable** file: a citation into a
moving target rots silently, which is the fidelity-to-the-tree gap. Moving an artefact into a dated
folder at the end of its session turns it into a stable address, with nothing compiled.

### Four folders, one meaning each

| folder | its single meaning | between sessions |
|---|---|---|
| `raw/` | inbox of testimony awaiting compilation | **empty** |
| `sessions/<session date>/` | one session's whole record: journal, sidecar, specs, plans | grows |
| `wiki/` | compiled knowledge | — |
| `archive/` | **only** retired wiki pages | — |

An empty `raw/` is the owner's stated want, verbatim: the uncompiled set becomes visible by looking
rather than by running `vault-coverage.sh` over every file. And `archive/` regains a single meaning,
which retires stale claim #3 by making it inapplicable rather than by editing it.

**Dated by session**, not by sprint and not by compilation: batching separates those three, and the
boundary worth reading is the day's.

**The long-run shape is that nothing moves at all** — the skill writes the artefact into
`sessions/<date>/` from the start, since the date is known while it is being written. That dissolves
the "when is a half-finished plan archived" question rather than answering it. A move is the
interim, needed only until the skills are rewritten.

**Telling the spec-writing skill where to write is the first real use of the harness mechanism** —
a line in `vault-feedback.md`, a rule page, `governs:` on the skill file, a rendered region, the
gate. Work that was queued anyway, not an exercise.

### The migration, which is one wave and not two

115 of 124 pages cite `raw/` in `sources:`; 13 cite a spec under `docs/superpowers/`. Both are the
same job: a mechanical rewrite over `sources:`, where the detector is complete, plus a read of prose
mentions, where no detector exists. Filenames already carry their dates, so every target folder is
derivable without a judgement. Leaving the artefacts in place would preserve a mutable location that
thirteen pages depend on, which is the rot this whole design exists to remove.

### The folder, decided

**`archive/<session date>/`**, not a separate `sessions/`. The owner's ground: one entry point for
a search by date. The cost accepted with it is that `archive/` carries session records beside
retired pages — and it is paid down by dating the retired pages too, by the date they were retired,
so the folder means one thing again: **everything that left the working set on that day.**

**The sixteen artefacts under `docs/superpowers/` migrate** in the same wave as the 115 `raw/`
citations.

## What is still open

Blocking construction:

1. **The handoff template.** Now load-bearing: `/ingest` cuts on section boundaries, so the sections
   must be identical in every journal. The harness section and the retrospective's human section
   both land here.
2. **The closed predicate set for `asserts:`** — four are sketched; the full set and the rule for
   growing it are not agreed.
3. **The rules for marked regions**, including which of them may be exempt from *no region -> red*.

Half-designed:

4. **The `authority` register** — agreed in principle, on the model of `tags.md`. Where it lives,
   who writes it, whether it is generated, and what the librarian owes before minting a slug are all
   open.
5. **Mechanising the title rule** — eight titles carry a measurable quantity and nothing checks it.

Untouched:

6. **A home for ideas** — S2's second blocking question. An idea is pre-design and `proposals/`
   holds designs.
7. **The gates at session start** — parked by the owner as not a priority; routing stays manual.

Sequencing:

8. **Closing S1 and opening S2.** Two of the four questions blocking S2 are answered by this
   design: `rules` is a sixth folder in `wiki/`, and the move of `raw/` into a dated archive is
   designed whole. The remaining two are the home for ideas, and whether product work interleaves.
   S1's tail — *a check that fires, or a written decision that there will be none* — is met by a
   check now designed, if the owner reads "a working answer" as not requiring it to be built.

## Part 4 — the handoff template

Five journals follow the present template heading for heading, so the form works. What changes is
what the design above requires of it.

**It lives at `.claude/templates/handoff.md`.** Not in `raw/`, which is now an inbox that is empty
between sessions and where the template was already an exception the coverage script had to skip.
Both skills — the retrospective and the handoff — **point at it** rather than carry a copy; a
pointer is checkable and a copy is not.

**The section-set check reads the list from the template**, never from a hard-coded copy: change the
template and what journals owe changes with it, with no second place to remember. The same shape as
`catalogue.md` — regenerate and compare, rather than compare against a list someone wrote down.

**Numbers are dropped; the cut is by heading text.** The numbers already coupled the template to the
harness — `/ingest` says in so many words that *section 7* goes to `log.md` — so inserting a section
meant renumbering everything that referred to a number. A name does not move.

**One new section, `Harness`, and it goes last.** Everything above it is an account of the session;
it is a work queue, and the two are different genres. It carries the marked lines drained from
`vault-feedback.md`, and `/ingest` cuts it on the section boundary.

**The owner's corrections are a marked token in place, not a section of their own.** Sections do not
map onto folders one for one in any case — `State` is journal wholesale, `Deferred` goes to
`proposals/`, `Feedback to the librarian` to `log.md`, `Anything else` nowhere — so a section would
have bought no consistency. A marker written by a human is authorship, not classification, and it
keeps the correction beside the claim it corrects instead of ten sections away behind a reference.
The librarian is told that a marked unit is the owner's testimony and overrides its neighbour; the
`basis: human` it earns lands on whichever page the unit reaches, and the field keeps exactly the
meaning it already had.

**`Anything else worth keeping` stays, with its default written down:** its units are `skip:` unless
the librarian finds them a category. A catch-all is more honest than forcing a classification, but a
verdict chosen by taste is a hole in *there is no fifth option*.

**The template gets a rule in the check:** a journal in the inbox carries the exact heading set the
template declares. Until now the template was advice; with the cut running on headings, a renamed or
missing one breaks the compilation silently, which is this project's signature failure.

### The shape

```
---
session: YYYY-MM-DD
sprint: S0
commits: <first>..<last>          # or "none"
---

# Handoff — YYYY-MM-DD

## State
## Entities
## Decisions
## How it is built
## Lessons
## Deferred
## Feedback to the librarian
## Anything else worth keeping
## Harness
```
