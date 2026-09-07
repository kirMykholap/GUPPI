# Second brain — a vault, a librarian, and a generated brief

**Date:** 2026-08-13
**Status:** design agreed with the owner, including the vault layout.

Part I settles what we are building and why, and how the pieces operate. Part II settles the
store itself: categories, page schema, index, tags, the handoff template, and sprints.

---

# Part I — Why, and how it operates

## 1. The problem

`docs/HANDOFF.md` is 1289 lines, 129 KB, and every session reads all of it before it can
start. The owner's diagnosis on 2026-08-12 was that it had become a knowledge base wearing a
handoff's name.

The obvious reading — that this is a token cost — is wrong, and getting it wrong would have
led us to build the wrong thing. 129 KB is roughly 35–40k tokens, about 4% of a 1M window.
Expensive, not fatal. What is fatal is that **a fact on line 900 is functionally invisible**:
it is read and not seen. This file has contradicted itself three times, each occasion
recorded in its own §7. The disease is attention and single truth, not volume.

That matters for the design: "offload to a vault and leave a navigator" treats the symptom.
Offloading makes a fact *more* invisible, not less — now it is out of the room as well as out
of sight.

## 2. Four goals, and why their order is not a preference

1. **Cheap session start.** Read 3 KB instead of 129.
2. **Knowledge neither lost nor divergent.** A decision taken in slice 2 is found in slice 6
   and is not re-litigated.
3. **Query by topic, not by file.** "I am rewriting the view in React — what helps, what
   gets in the way?" answered with a short synthesis.
4. **Reusable infrastructure.** Install into a new project, get the working system.

Asked which one hurts most, the owner answered that all four had happened and none dominates.
That is itself the diagnosis: **the project's documentation currently has none of the
properties required of it.** This is "change the method", not "patch the file".

The order is forced by dependency rather than by importance: 3 stands on 2 (a librarian over
an incoherent corpus returns incoherent answers), and 4 stands on all of them.

**Goals 1 and 2 pull against each other, and that tension is the centre of the design.**
(1) wants knowledge *hidden* — less loaded. (2) wants nothing lost and nothing contradictory —
and you cannot see that two pages disagree if you only ever load one. Hiding is precisely the
mechanism that makes divergence possible; `HANDOFF` diverged not despite its size but because
of it.

**Goal 3 is therefore not a layer on top of 1 and 2. It is the resolution of the conflict
between them.** The librarian is the only reader that sees the corpus whole, and it sees it
with a fresh context every time. It is what lets us hide without losing.

Consequence: **phase 1 must contain 1+2+3.** The cheap option — "split `HANDOFF` by hand in
half a day" — is off the table. Without a librarian the split makes things worse: the
knowledge has not vanished, but it has become invisible.

## 3. Non-goals

- **Not a replacement for `CLAUDE.md`.** See §17 for exactly which rules stay there.
- **Not a replacement for code and tests** as the truth about code.
- **Not classical RAG.** Retrieval will eventually exist — see below — but it runs over
  *compiled* pages, never over raw chunks. Knowledge is synthesised at ingest and compounds
  between sessions; retrieval only chooses which compiled pages to open.
- **Vectors are not in phase 1** — deferred rather than rejected. See below.

## 3a. Vectors — planned, deferred, and cheap to add later

Two claims in an earlier draft of this document were too strong, and are corrected here.

**The token argument holds for the main context and not for the librarian's.** The main session
receives an answer of 500–1500 tokens either way, and vectors do not change that. The
librarian's own context is different: grep returns paths and matching lines, and the cost then
lies in the pages it *opens* — including the ones a word matched by accident. Better ranking
means fewer wasted opens.

But the librarian's tokens are the cheap ones: an isolated context that is thrown away. The
scarce resource is the main session's, and vectors do not touch it. **The stronger argument is
therefore not cost but quality — a librarian that reads forty pages answers worse than one that
reads five.** That is the same attention failure which motivated this whole design, one floor
down.

**The maintenance surface is also smaller than the earlier draft claimed.** At a few hundred
pages there is no vector database: a numpy array and a cosine computed in full is instant. The
index does not go stale either, because `/ingest` knows exactly which pages it wrote and
re-embeds only those. The real cost is the model and its dependency — a local embedder, since
the owner works from a subscription and no API — and that cost lands hardest on **phase 2**: a
plugin needing a local model installs far less easily than one needing `ripgrep`, which every
machine already has.

### Why they are still deferred

Not because they buy little, but because there is nothing yet to tune them on.

1. **The corpus does not exist.** At thirty pages grep with tags is genuinely sufficient, and
   vectors would be optimising nothing.
2. **We do not yet know how the questions get asked**, and that governs the model and the
   granularity. Building the index now would set those guesses in concrete.
3. **The miss log (§9) is the data** that makes the eventual choice something other than a guess.

**Deferring costs nothing, because the layout is already vector-ready.** One entity per page
makes a page the ideal chunk: no splitting strategy is required, one vector per page over
`title` + `tags` + body. That fell out of the atomicity rule for free.

### Vectors and tags are not alternatives

They answer different questions, and the difference decides where each belongs.

- A **vector** answers *what resembles this question* — ranked, approximate, and **with no
  boundary**. You get top-k and cannot know whether k was enough.
- A **tag** answers *what belongs to this class* — exact, enumerable, **complete**.

We have a query that needs completeness: `/pre-task` asks "does my plan contradict anything?".
A ranked partial answer is dangerous there — the decision the plan violates may rank twelfth
when k is eight, and the agent proceeds believing nothing conflicts.

**The rule: vectors search, tags guarantee.** "What exists on this subject" is a vector
question; "am I breaking anything" is enumeration by tag and category.

One honest concession: **§13's aliases are a poor man's embedding.** They exist so that a
question asked in Russian reaches an English page, and a multilingual model does that better and
without a dictionary. When vectors arrive the aliases lose much of their purpose — while tag
definitions and the split rule lose none, because those are about the discipline of
classification rather than about search.

## 4. Two phases

**Phase 1, in this repository.** The vault, the librarian, its entry points, the hooks, and the
journal discipline. It is judged here, on a real corpus, by a real session start.

**Phase 2, a separate project.** Extract what survived into an installable plugin. What travels
is the *machinery* — the librarian, the entry points, the hooks, the conventions, the four
categories. What stays is this project's vault, which is its knowledge and belongs to it.

Building the plugin first was considered and rejected. The vault convention would have to be
designed with no corpus in hand: "what is a page", "what goes in the index", "what does a
contradiction look like" would all be answered by guessing. Infrastructure is extracted from a
working instance, not designed for a hypothetical one. Phase 1 also pays this week; phase 2
pays some day.

## 5. Three artefacts, three owners

| Artefact | Written by | Rules |
|---|---|---|
| **Journal** (handoff) | the session, at its end | appended to; never edited after the fact |
| **Vault** | the librarian, at ingest | edited under the single-truth rules of §6 |
| **Brief** | the librarian, at the end of a session | **derived. Never a source** |

The last row is a hard rule. If the brief is wrong, the fix goes into the vault or into the
librarian — **never into the brief**. A hand-edited brief that survives a session is immediate
divergence, which is the failure §7 of the old handoff is about.

The journal is a log. If the librarian disagrees with it, that disagreement lives on a vault
page or as a new line in `log.md`; the record of what the session believed stays as written.
Otherwise we lose the ability to find out where the session was wrong.

**Ingest sits between the journal and the brief and is not optional.** Without it knowledge
would travel journal → brief and settle only in a derived artefact, and within three sessions
briefs would be paraphrasing briefs.

## 6. The librarian

**One agent, two entry points — not two skills.** The two modes share nearly everything and
differ only in their trigger and the shape of their answer. Duplicated instructions diverge:
that would be the divergence failure reproduced inside the component whose job is to prevent it.

**Shared, in the agent definition.** The definition is thin and points at `vault/CLAUDE.md` as
the single source for the rules of the store — the rules must not exist in two places.

- how to search: grep first, then follow `[[links]]` from the hits (§12);
- answer with **synthesis, never a dump**;
- always return the list of pages used. An answer that cannot be checked is not an answer;
- always report the **negative space**: what the vault does *not* have on the topic. "No
  decisions were recorded about the visual layer" tells the caller it is free to decide — and
  that the decision must be recorded. Without it, "no constraints" is indistinguishable from
  "the librarian did not find them";
- record a miss in `log.md` when one is reported (§9).

**Different, in the two thin entry points:**

| | Mode 1 — sprint brief | Mode 2 — answer on a topic |
|---|---|---|
| Trigger | no topic given | topic given |
| Caller | generated at session end, `cat` at session start | mid-work, by the owner **or by an agent** |
| Answer | state of the current sprint: goal, done, not done, what must not be broken, what to watch | direct answer + sources + negative space |

Mode 2's answer follows the categories in their natural order, which is also the order of §14's
handoff sections — one sequence to remember, not two:

> pages like this already exist (`entities/`) → these decisions were already taken
> (`decisions/`) → the mechanism works like this (`concepts/`) → do not attempt X, it leads to
> Y, use Z (`lessons/`)

The sprint boundary is what keeps mode 1 from growing (§15). A brief scoped to the project in
general must cover everything plausible and would become `HANDOFF` again.

### Write rules

The librarian **writes the vault itself and does not ask permission.** Review is post-hoc, via
the log and the diff. Three mechanisms make that review real:

1. **Git is the audit log.** The vault is in the repository; each ingest is a commit, and
   `git diff` says *what* changed, mechanically. The librarian's own log says *why*. A
   self-reported log alone would be testimony of the same kind we already decided not to fully
   trust in the journal. A disagreement between log and diff is itself a finding.
2. **It never deletes text.** It appends, or it deprecates a page and creates its successor
   (§11). **No fact can vanish silently, because there is nowhere for it to go.** The dangerous
   act was never a new page — a new page is at worst clutter — it is an edit that quietly eats
   a paragraph. This also shrinks review from "read everything" to "read the deprecations", of
   which there will be nought to two per session.
3. **It does not resolve an `authority` conflict.** If two `current` pages claim the same
   question, it marks both with a `> [!CAUTION] CONTRADICTION` block and raises it in the
   brief. Asking the owner in chat is welcome but is not sufficient: an answer given in chat
   leaves no artefact. The marking is the artefact; the question is a courtesy.

The same division applies to sprints (§15): the librarian observes and reports, the owner
decides. It does not close a sprint for the same reason it does not resolve a contradiction —
both are judgements about the project rather than about the store.

### What it knows

The librarian is a subagent with an isolated context: **it did not watch the session.**
Everything it knows about one is the journal plus, later, the task-tracker diff — testimony and
evidence. The journal's quality therefore bounds everything downstream, which makes writing it
a load-bearing operation rather than a courtesy, and makes §14's template load-bearing with it.

## 7. The loop

**End of session:** the session writes the journal → the librarian ingests journal (+ task diff)
into the vault → the librarian generates `vault/brief.md`.

**Start of session:** a `SessionStart` hook `cat`s the brief. Mode 1 arrives mechanically, not
because somebody remembered to ask.

Generation belongs at the **end** for two reasons, neither of which is speed:

- **you are still in context and can see the brief lie.** At the start you have no way to know
  what was left out — that is the blind spot of the owner's own review loop (§9);
- **`cat` is deterministic.** It does not fail, does not answer differently to the same input,
  and costs nothing. Generation at start is one more thing that can break before the first
  line is typed.

A regenerate command covers the case where the vault changed outside a session.

> A correction made during the design conversation, recorded so the reasoning is not reused
> wrongly: the **5–35 minute** round-trip figure in `CLAUDE.md` describes *implementer* trips
> that write code and run tests. A librarian call — grep, read a dozen pages, write 2–3 KB — is
> tens of seconds. The end-of-session choice does not rest on that number.

A `SessionStart` hook is a shell command whose stdout is injected; it cannot summon a subagent
by itself. The alternatives were a headless `claude -p` run or an injected instruction that
costs a round trip inside the session. `cat` of a pre-generated file avoids both.

**A session can die without writing a journal** — context exhausted, a crash, an abandoned run.
The next brief would then be built on stale data, and that must be *visible*: `/ingest` records
"no handoff for session N" in the log, and the brief says so in its first line. A silently
inherited old brief is the worst of the available outcomes.

## 8. The task tracker — the boundary is stubbed, not wired

The owner plans to adopt **beads** as the task tracker; it is not installed yet. Phase 1 is
**ready for it, not dependent on it**: the brief has a place for "active unblocked tasks", left
empty or filled by hand until beads exists, and connected later at one point. Phase 1 therefore
does not block on a separate piece of work with its own open questions.

Two rules for when it arrives:

- **The brief quotes `bd` output; it never restates it.** A paraphrased task list diverges from
  the real one at the first closed task.
- **The task diff is evidence; the journal is testimony.** The diff is mechanical and cannot
  lie; the journal is written by whoever was tired at the end of a session. When they disagree
  — the journal calls a task done, the tracker shows it open — that is a finding to raise, not
  a discrepancy to smooth over.

The tracker owns task *state*. The vault owns what we *learned* from a task. This is why there
is no `tasks/` category in §10: a page carrying a task's status would be a second owner of a
fact the tracker already owns.

Beads is developer tooling and does not ship inside the application, so the `CLAUDE.md` rule
"add no new dependencies" — which is about what the product depends on — is not violated.
Recorded here so that nobody trips over the rule later.

## 9. How we will know it worked

**The owner's loop, primary.** Open a session; if something is missing, fix the librarian.

**Its blind spot, and the second half.** That loop catches only what was missing *and you knew
it*. It cannot catch what was missing and you had forgotten — which is exactly the category
that has bitten this project three times: the rule existed, was written down, nobody saw it,
and the session confidently went the wrong way with nobody flinching. So: when something bites
*mid*-session — a rule broken, a settled decision re-litigated — that is a librarian defect.

**Who records a miss.** Not the working agent, directly: a second writer into the vault would
destroy the single ownership the whole design rests on. The miss goes into the session journal,
§14's section 7, and `/ingest` transfers it to `log.md`. The writer stays single, and the
template guarantees the question is *asked* at the end of every session rather than when
somebody remembers. **That list is the only real test data this system will ever have**, and it
is also the evidence for or against vectors.

**A one-time gate.** Five to seven acceptance questions whose answers are currently buried in
`HANDOFF` and which both the owner and the assistant already know — they cover the "forgotten"
category precisely because the answer is known in advance. Phase 1 passes if the librarian
answers them correctly and completely while the main session never reads the vault. That single
test exercises all three goals at once: (1) it did not read, (2) the answer is single and
uncontradicted, (3) the topic query works.

Drafted so far:

- Why does the batch finaliser have exactly one owner, and what breaks if a second is added?
- What does an agent round trip cost, and where does that number come from?
- What has already been decided about JavaScript in this project, and why was the rule narrowed?
- I am rewriting the view in React — what in the documentation helps, and what gets in the way?

---

# Part II — The vault

## 10. Layout and the four categories

```
vault/
  CLAUDE.md          # the schema — the single source for the rules of the store
  index.md           # map of the territory (§12)
  tags.md            # the tag dictionary (§13)
  log.md             # librarian's actions, and recorded misses
  brief.md           # derived; regenerated at each session end
  raw/handoffs/      # immutable session journals (§14)
  wiki/
    decisions/
    concepts/
    entities/
    lessons/
  archive/           # deprecated pages; closed sprints' handoffs
```

Three layers, after the source method: **raw** is truth as it arrived and is immutable; **wiki**
is compiled knowledge and only the librarian writes it; **`vault/CLAUDE.md`** is the schema.

### The four categories

An earlier draft had a separate `invariants/`. It was dropped on purpose: **a decision and the
rule it produced are the same fact at two moments of its life.** "Own JavaScript is allowed
where it cannot show a wrong list" is both a decision (taken 2026-08-12, replacing an older
rule) and an invariant (what you must now obey). Two folders would put one fact in two places
on day one.

But not every invariant grew from a decision — "PostgreSQL's `now()` is constant within a
transaction" was chosen by nobody. That difference is the useful one, because it says what you
are allowed to do: **a decision can be overturned; a fact about PostgreSQL cannot.**

| Folder | The question it answers | What overturns it |
|---|---|---|
| `decisions/` | what we **chose**, when, why, what we rejected, what it now obliges | a new decision |
| `concepts/` | how it is **built** and why it works that way — mechanisms, invariants, consequences | new knowledge |
| `entities/` | what **exists** and what it is like — modules, tools, external systems | the subject itself changing |
| `lessons/` | what we learned **the hard way** — classes of failure, costs, "not like that again" | experience |

**Discriminators, so filing is not a guess:**

- `concepts` describes the **product**; `lessons` describes **us, working on the product**.
- A `decision` has a date and a rejected alternative. A `concept` has neither.
- An `entity` is a noun with properties. A `concept` is a mechanism with consequences.

**Two categories that were considered and folded in:**

- **Deferred limitations** ("we are not doing X now; the consequence is Y") are `decisions/`.
  Deferring is a choice, with a date, a reason, and a rejected alternative — "do it now".
- **Measurements** are not a folder. A number lives on the `lessons/` page it justifies and is
  marked `basis: measurement`. A bare number without its conclusion is useless; a conclusion
  without its number is unfalsifiable. Separating them harms both.

All four are generic — every project has what was chosen, how it is built, what exists, and what
burned us — so the list itself travels to phase 2.

## 11. The page schema

One entity or one decision per file. `kebab-case` names, descriptive, because **the filename is
part of the search surface** (§12).

```yaml
---
title: "The batch finaliser has exactly one owner"
type: concept              # decision | concept | entity | lesson
status: current            # current | deprecated
authority: batch-finalisation      # the question this page alone answers; optional
basis: code                # human | code | measurement | external | inference
sprint: S3                 # where it came from, NOT what it belongs to
created: 2026-08-13
sources: ["[[handoff-2026-08-13]]", "docs/superpowers/plans/2026-08-06-shell-and-two-pages.md"]
tags: [collection, batches]
supersedes: [[old-page]]           # on the successor
superseded_by: [[new-page]]        # on the retired page
---
```

**`status` has two values, and supersession is a relation rather than a status.** When a page is
replaced: the successor is written `current` with `supersedes:`, the old page becomes
`deprecated` with `superseded_by:` and moves to `archive/`. **The link is written in both
directions on purpose** — Obsidian shows a human the backlink, but the librarian greps, and a
deprecated page whose successor is not named on it is a dead end that would require scanning the
whole wiki to escape.

**Nothing is ever deleted.** An entity taken out of service — a module cut, a tool replaced — is
deprecated, not removed. "Why did we move away from X" is a legitimate question six months later
and must have an answer.

**`authority` is the question a page is the sole answer to** — a slug, not an enum. Two `current`
pages carrying the same value *are* a contradiction, and one found mechanically:

```
rg "^authority:" vault/wiki -o | sort | uniq -d
```

That is what gives `/lint` teeth. Pages that do not claim sole ownership of a question simply
have no `authority`.

**`basis` is what the page rests on**, and it ranks conflicts without the librarian overstepping:
a page on `inference` cannot argue with a page on `human`; a page on `code` loses to the code
itself. The librarian presents the ranking; the owner still decides.

**`sprint` means origin, not membership.** A `concepts/` page about batch finalisation is not
"sprint 3's" — it is timeless, and merely entered the vault in sprint 3. If the field meant
membership, a query about the current sprint would return only recent knowledge and the librarian
would start forgetting older invariants — which is goal 2 breaking. The sprint brief is therefore
built from *state plus what changed this sprint*, never from "pages belonging to this sprint".

`type` duplicates the folder. That is tolerated for machine-readability, and `/lint` asserts the
two agree — a file in `entities/` with `type: decision` is a defect.

## 12. The index is a map, not a catalogue

An earlier draft made `index.md` a table with one row per page, carrying `authority` and
`status`. It was withdrawn for two reasons: at a thousand pages that table becomes the problem it
was meant to solve, and — more fundamental — **it is a second copy of what the files already
say, and second copies diverge.** `/lint` can derive the same answer with the grep above.
Deriving is cheaper than maintaining.

**Finding pages is grep, then links.** The librarian greps the vault for the question's terms,
gets paths and matching lines, and opens the hits. That costs the size of the *query*, not the
size of the corpus, and does not grow. Then it follows `[[links]]` from what it found: **it does
not need to find every relevant page, only one, and walk from there.** This is what makes
wikilinks load-bearing rather than decorative, and why `/lint` hunts orphans — a page nobody
links to is invisible to everything except an exact grep hit.

`index.md` therefore holds what grep cannot supply, and it does not grow with the corpus:

- which categories exist and what belongs in each;
- the naming convention, so grep lands;
- where the current sprint's boundary is;
- links to a few **hub pages** — entry points into large subjects.

A hundred new pages do not lengthen it. A fifth category would, and categories appear about once
a year.

**The cost, stated honestly:** grep finds only what shares vocabulary with the question. Ask
about "внешний вид" when the page is called `vacancy-table-layout` and you miss. Three things
carry that weight — filenames, the tag dictionary's aliases (§13), and links — and all three are
now structural rather than cosmetic.

## 13. The tag dictionary

Categories are static and few — *what kind* of knowledge. Tags are dynamic and many — *what it is
about*. Orthogonal: a page has exactly one category, its folder, and several tags.

Tags are assigned at ingest, and the rule that keeps them from proliferating is
**consult before minting**: the librarian reads a source, sees something about pages, checks
`tags.md`, finds `page`, and uses it instead of inventing `pages` or `ui-page`.

```yaml
- tag: page
  definition: a page of the application's web interface (/vacancies, /collection) — not a wiki page
  aliases: [страница, screen, view, ui-page]
  since: 2026-08-13
```

**The definition is why the dictionary is not a second copy of the tags.** It cannot be derived
from the files, and without it a librarian arriving with a fresh context will within a month
attach `page` to a wiki page, a results page and a vacancy card alike.

**Aliases are where the dictionary pays for itself twice.** When the librarian considers a new
tag and *rejects* it in favour of an existing one, the rejected word is a synonym worth keeping —
it is what a future grep will hit. This matters especially here, where the corpus is half Russian
and half English: a question asked in Russian lands on an alias and leads to English pages. That
is the recall gap that motivated vectors, closed by one line — and it is the one part of the
dictionary a multilingual embedding would eventually supersede (§3a). The definitions and the
split rule it would not: those are discipline, not search.

**The counterweight — a tag can also fail by growing.** A librarian told not to invent will
attach `page` to everything faintly page-shaped until `tag:page` returns forty pages and
classifies nothing. `/lint` therefore flags:

- a tag on more than ~15–20 pages — a split candidate, raised to the owner;
- a tag registered but used nowhere — dead, remove;
- two tags with near-identical definitions — merge candidates, one becomes the other's alias.

Norm: **2–4 tags per page.** A page with ten tags is not classified, it is smeared.

## 14. The handoff template

The handoff is the **only channel** from a session to the librarian, which did not watch it.
Its sections therefore mirror the categories, so that ingest is filing rather than
interpretation, and in the same order as mode 2's answer (§6) — one sequence to remember.

```markdown
---
session: 2026-08-13
sprint: S4
commits: e872992..HEAD
---

## 1. State                     → the brief. Never compiled into the wiki
Done / not done / in flight / next step. Checks: tests (how many), ruff, browser walk

## 2. Entities                  → entities/
Appeared | changed | taken out of service (and why)

## 3. Decisions                 → decisions/
What we chose | what we rejected | why | what it now obliges

## 4. How it is built           → concepts/
Mechanisms understood or corrected. Invariants and their consequences

## 5. Lessons                   → lessons/
What burned us. With the number, if there is one

## 6. Deferred                  → decisions/ (deferring is a decision)
What we are not doing now | the consequence of not doing it

## 7. Feedback to the librarian → log.md
What the brief failed to supply / contradictions noticed in the docs / questions for the owner

## 8. Anything else worth keeping
```

Three halves living by different rules: **§1 is state** — perishable, feeds the brief, never
enters the wiki, and is a lie within a sprint. **§2–6 are knowledge** — compiled, permanent.
**§7 is feedback about the machinery**, not about the project.

**An empty section is a legal answer**, but the section must be present, so the question is asked
at the end of every session. Nobody misses the "what the brief failed to supply" section on their
own; it has to be asked.

Two details carry weight:

- **`commits:` in the header.** The handoff is testimony, git is evidence. With the range, the
  librarian or `/lint` can check that the session reported what it actually did.
- **§2 is about entities, not files.** Docker, htmx, PostgreSQL, the `web/data` package — the
  list of touched files is git's job, and git does it better. Without this note the section
  degenerates into a retelling of the diff.

**§8 is the template's own improvement mechanism.** A strict template determines what gets
noticed: something learned that fits no section goes unwritten, not because it is unimportant but
because there is nowhere to put it. The free-form section catches it — and if it fills up
regularly, that is the signal that the template is missing a section, and which one.

## 15. Sprints

**All work happens inside a sprint, and a sprint is declared explicitly.** A goal, milestones,
tasks, then a retrospective, conclusions, improvements — and the next sprint. Declaration is
explicit rather than derived from merges or slices because "sprint" must mean what the owner
intends, not what happened to coincide with a branch: this very design conversation is not a
slice and yields a great deal of knowledge.

**A goal is written as a checkable statement, with 2–4 acceptance criteria, at the moment the
sprint opens.** "Improve collection" cannot be checked. "Collection starts from the browser and
its progress is visible" can be, by looking. The criteria are written at the opening
deliberately: at the end you are motivated to close, and only criteria fixed in advance are
honest. This project already has an instance — the visual slice's single criterion was
*"has the owner started opening `/vacancies`"*.

**Closure is decided on the goal, not on an empty backlog.** Requiring every task closed makes
the sprint a consequence of the backlog rather than a frame for it, and leaves only two
outcomes: closing tasks for form's sake, or a sprint that never ends. Leftover work is carried
over or dropped — and **dropping is a decision with a reason**, so it becomes a `decisions/`
page. That is precisely the payoff the owner wanted from the archive: at the retrospective you
can see not only what was done but *what you stopped doing and why*, which today is lost in
silence.

**Who does what.** The librarian reports — "goal of S4: …; 7 of 9 epics closed; two open" — and
records the closure once it is declared. **It never closes a sprint**, for the same reason it
never resolves an `authority` conflict: both are judgements about the project.

### The growth signal

Sprints exist so that the brief does not grow. A sprint running for two months would hand back
`HANDOFF` under a new name, so something must bound it — but a calendar time-box is the wrong
instrument. Its value in team Scrum is forecasting and cadence, neither of which applies to one
person working evenings; the one thing it would give — a forced retrospective — we already get
from a per-session handoff.

**So the measure is the size of the brief itself.** It is the disease rather than a proxy for it:
an overgrown sprint is visible as an overgrown brief. The librarian generates the brief anyway
and knows its size for free; when it exceeds the threshold it says so in the brief's own first
line — *"S4 has run 11 sessions, brief is 6.2 KB against a threshold of 4.5 — is the goal still
one goal?"*, with the threshold being whatever calibration below has produced — as a question,
never a verdict. Splitting, narrowing or closing is the owner's call.

**The threshold is calibrated, not invented.** An earlier draft named 4 KB outright; that number
was made up. The procedure instead:

- **Sprint 1 collects data and raises no alarm.** The librarian records the brief's size in
  `log.md` every session.
- **At sprint 1's retrospective** we have the growth curve and, more importantly, the owner's
  answer to one question: *"did the brief get long?"* That answer is the ground truth; size is
  only its proxy, and only the owner knows when he began skimming rather than reading.
- **From sprint 2** the threshold is 3–4× the size he called comfortable.

An alternative was considered — baseline from brief #1, alarm at 4× — and rejected: the first
brief of a sprint is abnormally small because almost nothing has happened yet, not because it is
healthy. With a 0.4 KB baseline a healthy brief would trip the alarm by the third session, and an
alarm that always fires stops being read.

Secondary counters the librarian can grep and show alongside — sessions in the sprint, new pages,
**how many times the goal changed** — help explain *why* the brief swelled. The alarm is the
brief's size; those are context.

## 16. Where it lives, and what is in git

`vault/` sits at the repository root and is **entirely tracked** — `raw/`, `wiki/`, `archive/`,
`index.md`, `log.md`, `tags.md`, `brief.md`. Git is the librarian's audit log and a commit after
each ingest is the undo; neither works for anything outside git. The brief is tracked too, though
derived, because its size over time is the measurement §15 depends on.

`raw/handoffs/` grows without bound, and that is harmless: **nothing reads it in bulk.** Ingest
opens the one new file. Unbounded growth only hurts where something is read as a batch, and by
construction nothing here is.

`.superpowers/sdd/` stays git-ignored as it is today. Agent diffs and reports are one session's
working material; only the conclusions drawn from them enter the vault.

## 17. What `CLAUDE.md` keeps

Most of `CLAUDE.md` moves, but not all of it, and the line is **not** "rule stays, reasoning
goes".

> **A rule stays in `CLAUDE.md` if it must be obeyed at a moment when nobody would think to ask.**

Stays: the **language** rule, which governs every line written and never announces itself; the
**commands**; **"add no new dependencies"**, which fires while you are thinking about anything
else; **how a slice is executed**, which governs the shape of the session itself; and the **map
of the five AST boundary tests**, which is exactly the "where to look" that `CLAUDE.md` becomes.

Moves: **all the "why"**. Why the batch finaliser has one owner, why the `<script>` strip in the
htmx invariant is load-bearing, why the JavaScript rule was narrowed, why `tags_set` exists at
all. These are `concepts/` and `decisions/`, and they are fetched exactly when the subject is
touched.

The test: the language rule cannot be moved — a session would break it on its first line, before
it could occur to anyone to ask. The batch rule can — it is only broken while touching batches,
and touching batches is when you ask.

## 18. Workflows

| Command | When | What it does |
|---|---|---|
| `/ingest` | manually, at session end | splits the source into units and gives every one a verdict (§18a); creates and retires pages per §11; updates `index.md` and `tags.md`; writes `log.md`; **generates `brief.md` as its last step** |
| `/lint` | once per sprint | **unfinished ingests — any raw document with units that carry no verdict**; duplicate `authority` among `current` pages; orphans; broken links; `type` disagreeing with folder; dead, oversized and near-duplicate tags; index drift |
| `/pre-task` | before starting a task | **a mode-2 librarian call**, not a bulk read |

`/pre-task` as originally drafted required the working agent to read `index.md` and *every*
`active` file in `decisions/`. That is goal 1 defeated through a side door: the decisions register
grows monotonically and is never pruned, the read lands in the *main* context, and it happens
before every task. It is a librarian call instead — the agent submits its plan, the librarian
reads the decisions in its own context and returns what conflicts and what helps. Same guarantee,
bounded cost.

Mode 2 also needs a trigger the agent cannot forget. `PreToolUse` prompt injection matched on
rule-bearing paths — `CLAUDE.md`, vault pages — is narrow on purpose: all three recorded
divergences looked like "the rule seemed unnecessary".

## 18a. Ingest is units and verdicts, and it is checkable

Added 2026-08-13, during execution, at the owner's insistence and correctly. The earlier wording
described ingest as "read the handoff and file its sections" — which is a wish rather than an
operation. It cannot be checked, it only works for documents written to our own template, and it
gave no answer at all to the question the owner actually asked: **how do I know a document has
been turned into knowledge completely?**

**A source is split into units mechanically.** A unit is one claim: a heading, a table row, or a
paragraph or bullet that opens in bold. That is the granularity such documents are written at.

**Every unit gets exactly one verdict**, recorded in a sidecar beside the immutable source —
`<source>.coverage.tsv`, so that `raw/` stays untouched:

| verdict | meaning |
|---|---|
| `page:<name>` | compiled into that wiki page |
| `journal` | session state, not knowledge — stays in `raw/`, never enters the wiki |
| `elsewhere:<where>` | belongs to `CLAUDE.md`, the code, or the task tracker |
| `skip:<reason>` | deliberately not compiled, and why |

**There is no fifth option.** "Is this document fully processed?" becomes "are there units with no
verdict?", which is mechanical and general — it works on the next document as well as this one.

### Coverage and fidelity are different checks with different costs

**Coverage — nothing was dropped.** Mechanical, 100% required. It works *only* because the
denominator is generated by a script. If the party that accounts for the units also decides what
the units are, a forgotten section never appears on the list and its absence is invisible. That is
exactly how §1 of the old handoff was lost on the first pass, and how the loss went unnoticed while
the ingest log claimed §1 had been read.

**Fidelity — what was compiled says what the source said.** **No script can check this.** The
Critical found in task 2 — a page describing behaviour that a later slice had replaced — would
pass coverage without a murmur: the page exists and its identifiers match.

Fidelity is checked by **sampling** (the sidecar records the source line, so ten random pairs
opened side by side take ten minutes and give a real verdict) and by the **acceptance questions**
of §9. A review agent is worth its cost only when a whole document moves.

## 19. Still deferred

- How sprint declaration is wired into the workflow mechanically — who prompts for it, and where
  the sprint's own record lives.
- Installing beads, and the migration of the existing `HANDOFF` into the vault. Both are plan
  matters rather than open design.
- The brief's exact section layout.

## 20. Open

- **One acceptance question from the owner** (§9). His will be more honest than the four drafted
  by the party that already knows what the file contains.

## 21. Decisions, so they are not re-litigated

| Decision | Why |
|---|---|
| Two phases; the plugin is extracted, not designed first | a convention designed without a corpus is guesswork |
| The librarian is in phase 1, not later | it is the resolution of the 1-vs-2 conflict, not an optimisation |
| Vectors deferred, not rejected | there is nothing to tune them on until a corpus exists; the layout is already vector-ready, so adding them later is cheap |
| Tags survive the arrival of vectors | a vector ranks without a boundary, and `/pre-task` needs completeness rather than a top-k |
| One agent, two entry points | duplicated instructions diverge |
| The librarian writes the vault unattended | owner's call; detection replaces permission, made real by git, no-delete, and the conflict carve-out |
| Never delete text; deprecate and archive | removes the whole class of silent loss and shrinks review to deprecations |
| The brief is generated at the end of a session | you are still in context to see it lie, and `cat` is deterministic |
| Ready for beads, not dependent on it | phase 1 must not block on a separate piece of work |
| Four categories, no `invariants/`, no `tasks/` | a decision and its rule are one fact; task state belongs to the tracker |
| `index.md` is a map, not a per-page table | a per-page table is a second copy, and it grows; grep plus links does not |
| Supersession links written both ways | the librarian greps; a deprecated page must name its successor |
| `sprint:` means origin, not membership | membership would make the librarian forget older knowledge |
| Sprints closed on the goal, not an empty backlog | otherwise the sprint is a consequence of the backlog and never ends |
| The growth alarm measures the brief, not counters | the brief's size is the disease itself, not a proxy |
| The threshold is measured in sprint 1, not set now | the project's other numbers are all measured; a made-up one would be false precision |
| Ingest is units with verdicts, not "read and file" | "fully processed" has to be answerable mechanically, on any document and not only ours; and the denominator must be generated by a script, or a forgotten section is invisible |
| Coverage and fidelity are separate checks | coverage is free and mandatory; fidelity needs sampling or known answers, and no script can supply it |

## Reference

The method is the one described at <https://www.aibyaakash.com/p/karpathy-second-brain>: a raw
folder, an AI-maintained wiki with an index, a schema document, single-source ingestion rather
than batch, and an append-only log — knowledge that compounds between sessions instead of being
retrieved afresh at each query.

The owner's two working notes, `docs/second-brain-info.md` and `docs/second-brain-instructions.md`,
were the starting point for Part II. They are source material rather than documentation and belong
in `raw/` — they will make a fitting first ingest.
