---
title: "An implemented proposal moves to `archive/`, and the successor page carries its claim"
type: decision
status: archived
authority: built-proposal-disposition
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-23
created: 2026-08-23
sources: ["sprint.md", "scripts/vault-archive.sh", "job_hunt_ai_vault/CLAUDE.md"]
tags: [vault, process, harness]
supersedes: "[[a-built-proposal-stays-in-proposals-with-a-built-mark]]"
---

# The ruling, 2026-08-23, and it reverses the one taken the day before

**The owner overturned his own prohibition of 2026-08-22.** Yesterday a built proposal was to stay
in `wiki/proposals/` and the move to `archive/` was refused
([[a-built-proposal-stays-in-proposals-with-a-built-mark]], now `deprecated`). Today the move is
what happens, and the ground he gave for it is a statement about what `archive/` **is**:

> **owner: Архив - это способ убрать из прямой видимости то, что уже содержит вики. Вики -
> источник истины, а архив - история, как она была(правильная или нет). Если мы внедряем proposal -
> значит появится concept или entity, tasks и прочее. Proposal в таком случае уезжает в архив, а не
> удаляется и ссылка на него остается в новом документе. Он просто исчезает из прямого видения.
> Логика что "архив сохраняет одно занчение - старница больше не верна" - неправильная. Архив -
> это история.**

**What the block settles, read out rather than paraphrased away:**

- **`archive/` is history, not a verdict.** It holds a page as it was, *правильная или нет* — right
  or wrong. Being there says nothing about whether the page was ever true.
- **`wiki/` is the source of truth**, and `archive/` is the way something the wiki already carries
  leaves direct view.
- **Implementing a proposal produces other pages** — a `concept` or an `entity`, tasks, and the
  rest. Those are what the wiki then carries.
- **The proposal goes to the archive, is not deleted, and the link to it stays in the new
  document.** It disappears from direct view and from nowhere else.

# The mark that yesterday's ruling deferred splits in two

**The corpus knows one word, `built`, and it has meant one thing: the thing described now exists in
code.** As of this date there are two marks, not one, and writing that down is the whole point of
this section — without it the store carries one word for two states and every reader has to guess
which is meant.

**owner selected: B — the mark splits, and `status` on a proposal carries three states,
`current` → `built` → `implemented`.** Chosen against **A — the single mark, read as *the thing
described now exists in code***, which is the reading the corpus held until today.

| state | what it says | where the page lives |
|---|---|---|
| `current` | it stands, and nobody has executed it | `wiki/proposals/` |
| `built` | the design is complete and the task list is written; it is ready to implement, and there is no code yet | `wiki/proposals/` |
| `implemented` | it is realised, the pages recording what was built exist, and it leaves direct view | `archive/` |

**The wording of the option is this session's and the choice is his.** He answered a rendered menu
with a letter, so the ruling ranks as his and the sentence carrying it ranks as the session's; it is
not a quotation and is not written as one
([[the-retro-records-a-ruling-chosen-from-a-menu-and-ratifies-decisions-not-utterances]]).

## Only `implemented` lands now

**owner selected: only `implemented` now** — chosen against landing both marks in the same change.
It closes the defect that was named, and it is checkable. **`built` arrives with tasks and gets its
test then.**

**That line is a selection and not his prose.** The text he chose was this session's own
recommendation returned to it as an option; it is written here as a label, unsigned and unquoted,
for the reason the shape exists at all
([[the-retro-records-a-ruling-chosen-from-a-menu-and-ratifies-decisions-not-utterances]]).

**The reason `built` cannot land yet is that its test needs a task list**, and `wiki/tasks/` does
not exist: the folder set is closed against it, and both the category and the tick-who-writes
question are deferred to S4 ([[the-folder-set-is-closed-and-tasks-is-not-in-it]]). A mark whose
definition is *the task list is written* cannot be decided by anything while there is nowhere for a
task list to be. His own sentence above names `tasks` among what implementing a proposal produces,
which is the same dependency seen from the other end.

**So the three-state model is decided and the middle state is not yet legal anywhere.** That is a
deliberate gap and not an oversight:
[[implemented-joins-the-legal-status-values-and-the-status-block-enters-every-schema]] admits the
third value and admits only that one.

# The safety condition, and it is a precondition rather than a habit

**A proposal may reach `archive/` only when at least one live `wiki/` page cites it.** Without that
citation the knowledge leaves the wiki and nothing carries it: the successor his sentence promises —
*ссылка на него остается в новом документе* — is the entire mechanism by which an archived proposal
is still reachable, and an archived page nothing points at is reachable by an exact grep and by
nothing else.

**This becomes a precondition inside `scripts/vault-archive.sh`, and it is not built.** It is
criterion 2 of S3, decided by the script refusing with exit 2 and by a selftest case carrying it
([[vault-archive-sh]],
[[the-archive-script-gains-a-pages-kind-and-a-retired-page-is-dated-by-its-session]]). **Until it
lands the condition binds a writer and is enforced by nobody.** Stated here as the decision it is,
and not as a claim about the tree.

# `superseded_by:` is still the wrong relation, and that finding survives the reversal

**Yesterday's ruling was right about the relation and wrong about the disposition.** A built
proposal has no successor asserting the same claim differently — a concept page describing the
injector does not say differently what the proposal for an injector said; it says a different thing
about a different subject. That argument is untouched by today's reversal and is carried forward.

**What replaces the relation is the pair his sentence names**: the page carries
`status: implemented`, and a live page cites it. Neither is a supersession, so an implemented
proposal is not marked `deprecated` and is given no `superseded_by:`. *(This paragraph is the
librarian's reading of his sentence rather than a second ruling — he named the citation and the
archive, and the status word came from the menu.)*

**The refused case is unchanged and was never in dispute.** A refusal has a successor asserting the
same claim the other way, so a refused proposal is `deprecated` with `superseded_by:` and moves to
`archive/` — the ordinary supersession, exactly as the vault's own `CLAUDE.md` describes it.

# The rejected alternative, argued and lost

**Rejected: that `archive/` should keep one meaning — *the page is no longer true*.** It was
recommended to him in those terms and he refused it in the block above: *«Логика что "архив
сохраняет одно занчение - старница больше не верна" - неправильная. Архив - это история.»*

**The recommendation had a real argument behind it and the argument is recorded, not buried.** An
archived page leaves almost every instrument this store has:

- **rules 2, 3, 6, 7 and 14 of `bash scripts/vault-check.sh`** build their page set from
  `$VAULT/wiki` alone, so frontmatter, duplicate `authority`, tags and the owner-quote advisory stop
  seeing it;
- **`bash scripts/vault-inject.sh`** sweeps `wiki/*/*.md`, so nothing there can ever render;
- **`bash scripts/vault-authority.sh`** builds its corpus from `$VAULT/wiki`, so the page leaves the
  index a claim is looked up in before a page is written
  ([[no-new-entity-where-an-existing-one-can-carry-the-claim]]);
- **`/pre-task` drops `## archive` outright**, as retired text, so no plan is ever checked against
  it ([[the-pre-task-agent]]).

**His answer dissolves that objection rather than denying it.** Every item on the list is a cost
paid by a reader who needs what the archived page holds — and after implementation nobody does: the
concept or entity that was built is what carries the claim, and it sits in `wiki/`, where every one
of those instruments reads. The proposal is history of how the design looked before it was executed.
**The objection was against archiving a page somebody still needs, and the safety condition above is
exactly the test for that.**

**A link into `archive/` resolves and reads perfectly, which is the same property from the other
side and is a known hazard in its own right** ([[a-live-page-can-argue-from-a-deprecated-one]],
[[what-an-archived-page-asserts-is-frozen-and-how-it-is-found-is-live]]).

# What the reversal costs and what it buys

**It buys back the folder's own query.** `rg -l "^status: current" wiki/proposals` was the answer to
*what did we plan and never do*, and it is the reason the category exists at all
([[proposals-are-a-folder-not-a-status]]). Yesterday's ruling left a built proposal `current` in
that folder, so the query over-reported by design. Today an implemented one is gone from the folder,
and a `built` one will be distinguishable inside it once that mark lands.

**It costs the retirement procedure a special case.** The vault's `CLAUDE.md` describes a
three-step supersession — successor, deprecate, move — plus the fourth step that removes the slug
from `authority.md` ([[retiring-a-page-removes-its-slug-from-the-authority-register]]). An
implemented proposal takes the move without the first two steps, which is a path through the
procedure that the procedure does not yet describe.

**The successor inherits the archived proposal's `authority:` slug**, so the question it answered
still has an answer in the register and the fourth step does not fire. Where the successor is a page
that already exists, the slug moves onto it; where several pages record what was built, the one that
answers the proposal's question takes it. **This page is itself that shape**: it carries
`authority: built-proposal-disposition`, inherited from the page it supersedes, and no second slug
was minted beside it.

# What is not decided here

- **The proposals already retired to `archive/` under the rule of 2026-08-18.** About thirty pages
  left `wiki/` before yesterday, and nothing in his words says whether any of them comes back. It
  was not decided yesterday either.
- **Whether a refused proposal gets a mark of its own.** He named `built` and `implemented`.
- **How `built` is tested.** It arrives with tasks and gets its test then, which is S4.
- **Whether the vault's own `CLAUDE.md` states this procedure, and in what words.** That file is
  the session's to write and not the librarian's
  ([[what-the-gate-reads-as-its-own-input-is-the-sessions-to-write]]), and its clause about a built
  proposal still reads as it did yesterday.

# He confirmed the librarian's reading in his own words, and it is no longer an inference — 2026-08-23

**The section above says the pairing of `status: implemented` with a citation is *"the librarian's
reading of his sentence rather than a second ruling"*. He then said it himself:**

> **owner: да, библиотекарь правильно понял. внедрённый proposal уезжает без deprecated и без
> superseded_by: — только status: implemented плюс ссылка из живого преемника.**

**So that paragraph's caveat is discharged and the paragraph is not edited.** What was an inference
from his sentence is now his sentence. The clause of that section — *"the status word came from the
menu"* — still stands as written, because it does.

# The mark opens a state, and the orphan test is what closes it — 2026-08-23

**The safety condition above is stated as a rule binding a writer. He restated it as a property of
the mark, and the difference is where the page lives while it waits:**

> **owner: метка несет показатель, что ее должны проверить (наверно lint или кто-то еще) явялется
> ли файл сиротой. Если ниодно запись не ссылается на запись с меткой "implemented" - Значит это
> ошибка. Любая запись с меткой "implemented" должна иметь того, кто на нее ссылается, хотя бы
> одного.**

> **owner: запись с меткой "implemented" лежит в wiki до тех пор, пока она не проверится на
> сиротство. Как только она проходит этот тест - запись отправляется в архив, и сама ссылка на нее
> переписывается у всех, кто на нее ссылался.**

**Three things follow that the section above does not say:**

1. **A page carrying `implemented` inside `wiki/` is legitimate and expected.** It is where the page
   waits while the test is pending, not a violation.
2. **The mark carries an obligation on somebody else** — a lint, or whatever runs it: *any* page
   marked `implemented` must have at least one page pointing at it, and none is an error.
3. **The citations are rewritten on the way out**, by the party that moves it, so a link that
   pointed into `wiki/` points into `archive/` afterwards. `scripts/vault-archive.sh` rewrites
   `sources:` lines and nothing else, so the wikilinks in prose are rewritten by nobody
   ([[vault-archive-sh]], [[a-path-detector-for-prose-references]]) — and a `[[wikilink]]` resolves
   by filename anywhere under `wiki/` or `archive/`, so those need no rewriting to keep working.

**This corrected a verdict the session had already built.** A gate verdict named `realised` had made
`status: implemented` inside `wiki/` red; it was removed the same day on this correction, and the
reusable half of it — a mark that opens a state is not a mark that names a place — is
[[a-mark-that-opens-a-state-is-not-a-mark-that-names-a-place]]. **The gate judges the mark not at
all.**

## The advisory the mark needs, and it is not built

**Nothing lists the pages waiting in `implemented`.** The consequence is precise: **a page that will
never pass the orphan test looks exactly like one that has not been tested yet**, and the state
carries no clock. His own words name the shape — *наверно lint или кто-то еще* — and put it outside
the gate, which is where the ruling above already puts it.

**The refusal inside `scripts/vault-archive.sh` is the test and not the advisory.** It answers *may
this page move now* at the moment somebody tries; it never volunteers *these four pages have been
waiting since Tuesday* ([[the-tag-density-advisories-move-behind-lint]]).
