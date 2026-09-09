# Vault schema

This vault is the project's compiled knowledge. Raw session journals arrive in `raw/handoffs/`;
the librarian compiles them into atomic pages under `wiki/`. Obsidian reads this directory; the
librarian writes it. **The librarian is the only writer of `wiki/`.**

## Who writes what

**The librarian is the only writer of `wiki/`**, and the clause of 2026-08-17 extends that to the
four registers — `index.md`, `tags.md`, `sprint.md`, `log.md`. That is unchanged.

**What the gate reads as its own input is the session's to write** — this file, and every
`wiki/*/_schema.yaml`. A session edits either directly and the owner reads the diff before the
commit. Neither is a divergence and neither is recorded as one.

Decided 2026-08-19, after two hand-edits of this file had each been recorded as a divergence
against a rule that did not reach it. The reason is not convenience: this file is the librarian's
own instructions and the schemas constrain what it may write, so a librarian writing them is the
one arrangement in which a change has no reader but its author. What made both of those hand-edits
safe was never the recording — it was that no librarian was running and that the change was a
`git diff` the owner read. The clause states those two properties instead of the paperwork.

**A `_schema.yaml` is still not a place to reason from the corpus.** Its header rule stands: a
field moves from `optional` to `required` when a decision says so, and the decision names the page
it is written on. Being the session's to edit changes who holds the pen, not what may be written.

## Layout

| Path | What it is |
|---|---|
| `raw/handoffs/` | session journals as they were written. **Immutable** — read, never edited |
| `wiki/decisions/` | what we chose, when, why, what we rejected, what it obliges |
| `wiki/concepts/` | how something is built and why it works that way |
| `wiki/entities/` | what exists and what it is like — modules, tools, external systems |
| `wiki/lessons/` | what we learned the hard way — failure classes, costs |
| `wiki/proposals/` | what was raised or deferred and **not built** — the idea, what it would take, and why not now. A proposal is never a record of something that exists |
| `wiki/rules/` | a rule the harness **renders** rather than a reader remembers. It carries `governs:`, naming the one destination its text is injected into, and exactly one `<!-- text -->` … `<!-- /text -->` slice marking **what travels**. Everything outside that slice — the justification, the measurements, the links — stays on the page. Rules 11 and 12 of the check read both ends |
| `archive/` | deprecated pages, and the handoffs of closed sprints |
| `index.md` | map of the territory: categories, naming, current sprint, hub pages |
| `tags.md` | the tag dictionary — definitions and aliases |
| `authority.md` | the authority dictionary — families of `authority:` slugs, what each family is the question about, and aliases. Added 2026-08-21. It exists for the same reason `tags.md` does: which slugs exist is in the tree and needs no file, but **which slugs answer the same question is nowhere and cannot be derived**. Slugs are written as plain text, never as `[[wikilinks]]` — a register that linked every page would join the link sweep and no page here could ever be an orphan again. `bash scripts/vault-authority.sh --check` compares it against the tree in both directions |
| `log.md` | the librarian's actions, and misses reported against it |
| `sprint.md` | the current sprint — goal, acceptance criteria, changes to the goal; and closed ones |
| `brief.md` | derived. Regenerated at every ingest. **Never a source** |
| `pages.base` | the list of every page — an **Obsidian base**, which is a query and not an answer: it is evaluated when you open it, so it cannot be stale and there is nothing to regenerate. Filter and group by `type`, `status`, `sprint`, `tags`, `authority`, `governs`. Only Obsidian can read it; an agent runs `bash scripts/vault-catalogue.sh`, which prints the same list |

**After writing anything under `wiki/` or `archive/`, run `bash scripts/vault-inject.sh`, then
`bash scripts/vault-check.sh`.** Rule 12 asks whether each region agrees with the page it renders
**by running the injector**, so a rule page edited and not injected leaves the gate red. There is
no catalogue step: `pages.base` is evaluated when it is opened, so a page that exists is in it the
moment it exists.

## Choosing a category

- A `decision` has a date and a rejected alternative. A `concept` has neither.
- An `entity` is a noun with properties. A `concept` is a mechanism with consequences.
- **Deferring something is still a decision** and keeps its page in `decisions/`: a date, a
  reason, and a rejected alternative ("do it now"). `proposals/` did not take that over, and the
  two are different pages that often both exist — the decision records **that** we said not now,
  the proposal carries **what** we would build. A deferral with nothing designed behind it needs
  no proposal page; a design that would otherwise survive only in a chat log does.
- A `proposal` is never a record of something that exists. It says what it would take, what is
  open, and what it would oblige. It is `current` while it stands — so the page's own history
  answers "what did we plan and never do", which is the question the category was added for
  (owner, 2026-08-15).
  **A refused proposal moves to `archive/` and takes `status: refused`** (owner, 2026-08-23):
  «отклоненный proposal - уходит в архив и получает status "refused"». **The value is minted** —
  `wiki/proposals/_schema.yaml` declares it, and it is red in every other folder.
  **It carries no `superseded_by:`** (owner, 2026-08-23, in the session after the one that ruled
  the sentence above). A refusal is a *cause*; `superseded_by:` is a relation between two pages
  asserting one claim differently, which a refusal and the proposal it refused do not. The clause
  this replaced said it did carry one, on the ground that a refusal has a successor asserting the
  same claim the other way — that ground is now struck rather than left standing.
  **What it carries instead is `decided_by:`**, naming the decision that refused it, and
  `scripts/vault-archive.sh` refuses to release the page without one. The requirement is
  conditional on the status and no per-folder schema can state a conditional, which is why the
  refusal lives in the script and not in the YAML — the same shape as `paths` under
  `render: whole`.
  **An implemented one also moves to `archive/`, and carries neither** (owner, 2026-08-23). It
  goes with `status: implemented`, and the live page recording what was built cites it. It is not
  `deprecated`, because a retired page was replaced for going false and an implemented proposal
  was never false; and `superseded_by:` is a relation for a *changed claim*, which the pages
  recording what exists do not make — they assert something else
  ([[an-implemented-proposal-moves-to-archive-and-the-successor-carries-its-claim]]).
  **`archive/` is history and `wiki/` is the source of truth**, so what leaves direct view is
  reached through the successor that carries its claim. That reverses the ruling of 2026-08-22,
  under which a built proposal stayed here.
  **A page does not leave without a live page naming it** — `scripts/vault-archive.sh` refuses,
  because nothing in `archive/` is checked, swept or read by `/pre-task`, so a page nothing
  points at has left the store rather than been filed in it.
  **`built` is the third status and is not minted yet**: it means the design is complete and the
  task list written, ready to implement with no code yet, and its test is that task list — which
  waits on `wiki/tasks/`, deferred to S4
  ([[implemented-joins-the-legal-status-values-and-the-status-block-enters-every-schema]]).
- A `rule` is the only category whose text is **written to be rendered somewhere else**. Everything
  else here is read by a reader who came looking; a rule reaches the file it governs whether anyone
  came looking or not. That is why it names a destination and why it is a folder rather than a
  status: the guarantee is about where the text ends up, not about how mature it is. The decision
  that a rule exists still lives in `decisions/`; the rule carries the text that decision obliges.
- A measurement is not a page. The number lives on the `lessons/` page it justifies, marked
  `basis: measurement`. A bare number without its conclusion is useless; a conclusion without its
  number is unfalsifiable.

## Page schema

One entity or one decision per file. `kebab-case` filenames, descriptive — **the filename is part
of the search surface**, because retrieval is `ripgrep` plus links.

```yaml
---
title: "The batch finaliser has exactly one owner"
type: concept              # decision | concept | entity | lesson | proposal | rule
                           # — must match the folder
status: current            # current | deprecated
authority: batch-finalisation   # the question this page alone answers. REQUIRED in every folder
                                # but wiki/rules/, where it is forbidden: a rule answers with
                                # governs: below. Optional until 2026-08-21, when it became the
                                # index a claim is looked up in before a page is written
governs: .claude/skills/ingest/SKILL.md
                           # rules only, and required. NOT unique across rules: the owner
                           # removed that on 2026-08-17, because a file carries as many
                           # regions as it has rules and four of them share CLAUDE.md. The
                           # destination this rule's text is rendered into, written as a path
                           # FROM THE REPOSITORY ROOT and resolved against nothing else - unlike
                           # sources:, which tries both roots, because this one is a file the
                           # injector writes and a path meaning two files renders into the wrong
                           # one. A rule answers with this and never with authority:, or the
                           # decision it states and the rule stating it would share a slug and
                           # read as a contradiction
basis: code                # human | code | measurement | external | inference
sprint: S1                 # where it came from, NOT what it belongs to
decided: 2026-08-12        # decisions only: when it was taken. The slice date where
                           # the source records only the slice
created: 2026-08-13
sources: ["[[handoff-2026-08-13]]", "docs/superpowers/plans/2026-08-06-shell-and-two-pages.md"]
                           # what this was compiled FROM. Provenance, paths or links, any number
decided_by: [[the-decision-that-caused-this-page]]
                           # proposals/ and rules/ ONLY, and required in rules/ once every page
                           # there carries one. The decision that CAUSED this page: exactly one,
                           # always a [[wikilink]], always a page whose type is decision - the gate
                           # reddens any other target, and the link sweep already reports one that
                           # resolves to nothing. Absent everywhere else, where the causing page is
                           # named in sources: like any other material
Links: ["[[a-page-the-body-mentions]]"]
                           # the body's wikilinks, legal in all six and written BY A SCRIPT. Never
                           # by hand, and nothing is ever added to sources: to make a link countable
tags: [collection, batches]
supersedes: [[old-page]]        # on a successor only
superseded_by: [[new-page]]     # on a retired page only
---
```

### `status` and supersession

**The legal values live in each folder's `_schema.yaml`, under `values:`, and nowhere else.** They
were hardcoded in `scripts/vault-check.sh` until 2026-08-23; the gate is the reader, not the
register. Read them from the six files rather than from here. Two folders differ from the rest and
the difference is the point: `wiki/proposals/` carries the maturity values as well, and every one
of them is red in any other folder, which is the protection rather than an oversight
([[implemented-joins-the-legal-status-values-and-the-status-block-enters-every-schema]]).

**Only `deprecated` obliges a page to leave `wiki/` on sight**, and the gate says so. It was
replaced because it went false, so there is nothing to wait for.

**`implemented` opens a state rather than closing one** (owner, 2026-08-23). A page takes the mark
and **stays here** while it is tested for having someone who points at it; it moves only once it
passes, and its citations are rewritten on the way. So a page carrying `implemented` inside
`wiki/` is legitimate and expected, and the gate judges it not at all. A verdict reddening it was
written on 2026-08-23 and removed the same day, on that correction: the mark was read as an
address when it is a stage.

Supersession is a **relation**, not a status. When a page is replaced:

1. write the successor with `status: current` and `supersedes: [[old-page]]`;
2. set the old page to `status: deprecated`, add `superseded_by: [[new-page]]`;
3. move the old page into `archive/`.

**An implemented proposal is not a supersession and does not use those three steps.** It takes
`status: implemented`, stays here until something names it, and then moves — with no
`superseded_by:` and no successor claiming to replace it. What it needs instead is a live page
that names it, and `scripts/vault-archive.sh` refuses the move without one. **The refusal is the
test**: while it fails, the page waits here rather than being wrong.

**A title corrected in place is not a supersession** (owner, 2026-08-17). Supersession is for a
changed *claim*. Here the filename is the identity - it is the search surface and it is what every
wikilink resolves to - so striking a stale number out of a title moves no address and strands
nothing, while superseding on a title change would mean a page is identified by its title, which is
not how anything here addresses a page. **Renaming the file is the other operation** and it is not
this one: it moves an address, so it needs the rewriter-and-detector pair before it is attempted.

**The link is written in both directions on purpose.** Obsidian shows a human the backlink, but
the librarian greps: a deprecated page that does not name its successor is a dead end.

**Nothing is ever deleted.** An entity taken out of service — a module cut, a tool replaced — is
deprecated, not removed. "Why did we move away from X" is a legitimate question six months later.

### `authority`

The question a page is the **sole** answer to **within its own type** — a slug, not an enum. Two
`current` pages **of one type** carrying the same value are a contradiction; two of different types
are legal and expected, and the shared slug is the route a reader walks — proposal to decision to
concept or entity to rule (owner, 2026-08-30,
[[authority-uniqueness-becomes-a-per-type-question]]). Rule 3 of the gate compares within a type and
is the mechanical form of this sentence.

**The unqualified version stood here until 2026-08-31 and is corrected rather than deleted**, because
it was true from 2026-08-21 until the day the type-crossing chain was ratified, and every page
written under it was written correctly. What made it change is the cleanup: a family rule inherits
the slug of the decision it discharged, and under the old sentence the pair would have read as a
contradiction.

Found mechanically:

```
rg --no-filename "^authority:" wiki | sort | uniq -d
```

*Corrected 2026-08-17.* This line used to read `rg "^authority:" wiki -o | ...`, and `-o` prints
only the matched part — the literal string `authority:`, identically on every page — so `uniq -d`
reported a duplicate whenever the corpus had two pages with the field at all, and never compared a
slug to a slug. **It was false and it failed nothing**, because rule 3 of `vault-check.sh` does the
real comparison and does it correctly, over `current` pages only
([[a-command-that-is-false-only-in-its-documentation-fails-nothing]]). The line above is the
illustration; the check is the authority, and it is the check that has a selftest.

#### It is required, and it stopped being a label on 2026-08-21

**`authority:` is required on every page outside `wiki/rules/`, where it stays forbidden** — a rule
answers with `governs:`, and the two on one page would make the decision and the rule stating it
share a slug. It used to be optional and *"pages that do not claim sole ownership of a question
simply omit it"*; that sentence is gone, and what replaced it is a job rather than a rank.

**The job is the intake valve.** `/ingest` had none: a unit of knowledge became a page by default,
and the corpus reached 479 pages in nine days with 27 retirements against it. The admission rule the
owner set that day — [[no-new-entity-where-an-existing-one-can-carry-the-claim]] — is decided by
looking a candidate up, and **an index a page may omit is an index with holes in it**. The holes are
invisible in the worst direction: a lookup that returns nothing reads exactly like a question nobody
has answered yet.

**It was optional in `concepts/` for four hours on the day it was decided, and that exception is
gone rather than moved.** A `concepts/` page could carry `governs:`, and
[[authority-beside-governs-is-forbidden-on-any-page]] made those two pages required and forbidden at
once — a condition no per-folder schema can express. The owner removed what the condition ranged
over rather than the condition: **a page that renders its text into another file is a rule**, by the
folder set's own definition, so both pages moved into `wiki/rules/` and `governs:` left `concepts/`
with them ([[governs-is-a-property-of-wiki-rules-alone]]). `authority:` is now required in every
folder but `wiki/rules/`, with no exception anywhere.

**Looking up is what the field is for**, and the commands are
`bash scripts/vault-authority.sh --near <slug>` for the family a candidate belongs to and
`bash scripts/vault-catalogue.sh` for `authority` and `title` across the whole corpus in one pass.
That pass is the wide half of the reading rule: **the ten-page ceiling is about opening a page, never
about searching for one.**

### `binding`

**Decisions only, and required there.** What the decision does to a reader who is about to work.

| value | what it means | how a plan check reads it |
|---|---|---|
| `prohibition` | it may not be done; lifting it is a conversation with the owner, never a session's call | a hard constraint, enumerated in full |
| `deferral` | not now — doing it later is what was intended | context: this is already designed, do not invent it again |
| `divergence` | how a rule was already broken | context; it teaches and forbids nothing |

**The folder held three different things and answered as one.** How many of each there are is
printed by `bash scripts/vault-authority.sh --binding` and is deliberately not written here. The
sentence that stood in this place was measured on 2026-08-21 across the 189 pages `decisions/` then
held, and a session of 2026-08-23 read it as a statement about today - which is what a number in
prose does: it goes false without saying so, and it is repaired by deleting the copy rather than by
correcting it ([[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]],
[[the-region-coverage-figure-is-dated-where-it-stands]]). A plan checked against `decisions/` got
back a list of *relevant* pages where it needed a list of what *stops* it, and the difference is
the whole use of the answer.

**An absent value reads as `prohibition`.** The field is required, so this is not a default the
schema permits — it is what the reader assumes while the corpus is being marked up, and it is the
safe direction. A deferral misread as a prohibition costs a question; a prohibition misread as a
deferral costs the constraint.

**`divergence` is the only value a script can verify** — the title begins with `DIVERGENCE:` — and
`bash scripts/vault-authority.sh --binding` verifies exactly that and counts the other two for a
human to compare against what he expects. The other two are judgements, which is why the reader's
default is the strict one.

### Titles and filenames

**Not a field, and named here because its absence is load-bearing.**

**A title carries no measurable quantity, and neither does the filename** - unconditional in both
halves, and rule 10 of `vault-check.sh` enforces both. The title verdict is red; the filename
verdict is an advisory, because a filename is an address and repairing one moves every inbound
link, both registers and `log.md`. Name what is counted instead of counting it
([[a-title-names-what-is-counted-instead-of-counting-it]]).

**There is no way for a page to declare itself exempt.** A `quantity:` field carried that
declaration from 2026-08-17 until it was withdrawn on 2026-08-18, and the pages holding it were
retitled the same week ([[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]]). A
number that genuinely cannot drift - a status code, a rule's address, the reading of one past day -
still leaves the title. **Two of those declarations were false while they stood**, and neither was
found by anything mechanical: a declaration silences the one instrument that would have caught it
drifting, which is the argument against ever minting another field of this shape.

**So a word entering the predicate is a promise that the word is always a count.** While a page
could declare itself, a word only had to be usually one - a false positive cost a line of
frontmatter. With no appeal, a false positive is paid for by rewriting correct prose, which is a
real price and is why the list is short.

**Two boundaries, both closed on 2026-08-19 rather than left open.** The rule's subject is
`title:` and the filename, and it **never reads the body**: those two strings are what this store
addresses and retrieves by, so a false title is asserted to a reader who has not opened the page,
while a false subheading is contradicted by the list underneath it in the same glance. Measured
before the ruling: 201 counting headings across 128 of 308 pages, which is the argument - a list
of them would have to be extended by every page written afterwards
([[the-no-quantity-rule-reads-the-title-and-the-filename-and-never-the-body]]).

**And a title's length is unbounded, deliberately.** Naming what is counted instead of counting it
costs characters - `criterion 6` became `the criterion that every governed file carries a region` -
and the longest title went 143 to 175 bytes on the same page. A limit would charge that price back
to correct prose, and a long title cannot go false the way a counted one can
([[the-length-of-a-title-is-unbounded-and-no-check-measures-it]]).

Exempt, each because it is not a count: a code span - how this corpus writes identifiers, though
never a rule number, which it writes in prose; an ISO date, a fixed boundary; a digit glued to a
letter, since `cp1252` is a name; and the words *one* and *first*, both measured rather than
assumed - every title using either used it as a pronoun, a position or an invariant, and never as
a count that could drift.
### `basis`

What the page rests on. It ranks conflicts without the librarian overstepping: a page on
`inference` cannot argue with a page on `human`; a page on `code` loses to the code itself.

| value | meaning |
|---|---|
| `human` | the owner decided it in conversation |
| `code` | it follows from code and tests, and is verifiable by reading them |
| `measurement` | a number obtained by measuring |
| `external` | an article, vendor documentation, upstream behaviour |
| `inference` | the librarian concluded it. The weakest; re-check before relying on it |

### `sprint`

**Origin, not membership.** A page about batch finalisation is not "sprint 3's" — it is timeless
and merely entered the vault in sprint 3. If the field meant membership, a query about the
current sprint would return only recent knowledge and older invariants would be forgotten.

## Tags

Categories are static and few — *what kind* of knowledge. Tags are dynamic and many — *what it is
about*. A page has exactly one category (its folder) and **2–4 tags**. A page with ten tags is not
classified, it is smeared.

**Consult `tags.md` before minting a new tag.** If an existing tag fits, use it. When you consider
a new tag and reject it in favour of an existing one, **record the rejected word as an alias** —
it is what a future grep will hit, and it is how a question asked in Russian reaches an English
page.

## Contradictions

If two `current` pages **of the same type** claim the same `authority`, mark **both** with

```markdown
> [!CAUTION] CONTRADICTION
> Also claimed by [[other-page]]. Unresolved.
```

and raise it in the brief. **Do not choose a winner.** Deciding which of two rules is the real one
is a judgement about the project, not about the store. Asking the owner in chat is welcome but is
not sufficient: an answer given in chat leaves no artefact. The marking is the artefact.

## What does not belong here

- Rules that are *enforced* by tests, or that must be obeyed before anyone would think to ask —
  those stay in the repository's own `CLAUDE.md`.
- Task status. The task tracker owns that. The vault owns what we *learned* from a task.
- Anything git already records better: file lists, diffs, commit history.
