# Who reads the vault

**Status: design, ratified 2026-08-30, not built.** Kept in `docs/` as the worked example of what a
full proposal looks like before the librarian compiles it into `wiki/proposals/`.

Five actors, one writer. What each is given, what each returns, and what finally retires a decision.
Written after the sweep of 2026-08-29 took a third of `wiki/` and changed which of these questions
still have answers.

Figures are read from the tree on 2026-08-30. `wiki/` holds 556 live pages: `decisions/` 295,
`concepts/` 138, `proposals/` 46, `entities/` 43, `lessons/` 18, `rules/` 16. Of the 295 decisions,
263 are `prohibition` and 32 `deferral`; none is a `divergence`, because the sweep took every one.

## The rule everything else follows

**Nobody but the librarian writes.** Not `wiki/`, not the four registers. Everything else in this
design reads and returns.

That is not a limit to route around — it is the property the review model rests on. The review that
replaced asking permission belongs to the caller, never to the party being reviewed
([[the-librarian-writes-unattended]]). A reading agent that could also write would be countersigning
its own testimony, and so would a librarian that judged its own reading before writing it down.

**So the second rule is the first one applied to judgement: the verdict and the pen are held by
different parties.** That is why the reading agents exist at all, and it is a better ground than the
size of any folder — it does not go stale when the folder grows or shrinks.

## The five actors

| Actor | What it is |
|---|---|
| **the session** | Plans, writes code, runs the checks, reads the diff, commits. Never writes the vault. Holds the conversation with the owner, which is the only place a ruling is made. |
| **`vault-librarian`** | Knows how to search the vault and how to write it, and carries no goal of its own — the goal arrives from the ritual or the caller. Gains `Agent` in its `tools:` line, dispatches its own readers, waits, writes, and returns once. |
| **`vault-ask`** | The single search entry point, forked. Finds and reports; writes nothing. Everyone uses it, the librarian included, so the reading rules are explained in one place instead of rendered into every agent that happens to read. |
| **decisions census** | Reads `wiki/decisions/` whole and returns one row per page. Writes nothing. |
| **lessons collector** | Reads `wiki/lessons/`, groups the lessons by meaning, and returns a draft proposal per group with the lessons each group would retire. Writes nothing. |

## Who calls whom

**At an ingest — one dispatch.** The session hands `/ingest` the journal to the librarian. The
librarian dispatches the decisions census and the lessons collector, both reading only, waits for
their verdicts, writes what they found, and **returns once**. The session then reads the diff and
commits ([[the-librarian-dispatches-its-own-reading-agents-and-returns-once]]).

**On demand — no ritual.** Any caller with a question reaches `vault-ask`, which returns an answer,
its sources, and what the vault does not have.

The librarian is the only actor that writes. Every dispatch leaving it goes to something that reads
and comes back — including, once `vault-ask` is the one way in, its own searching.

## What each is given, and what comes back

A forked skill has **no conversation history** — its own text is the whole prompt. Everything the
caller wants it to know travels as arguments, and what is not passed does not exist. That is the
contract, not an obstacle, and it is the line of this design most likely to be got wrong in the
building.

| Reader | Given | Returns |
|---|---|---|
| `vault-ask` | The question, and the caller's plan or context — explicitly, as arguments | A synthesis, its sources, and *what is not in the vault* — the section that says a decision is still free to make |
| decisions census | `wiki/decisions/`, and the five verdicts it is allowed to return | One row per page: slug, `binding:`, verdict, and the evidence for it |
| lessons collector | `wiki/lessons/`, and the proposals that already exist | Groups by meaning, one draft proposal per group, and the lessons each group would retire |

## The five verdicts

| Verdict | What it says | Could a script say it? |
|---|---|---|
| `stands` | The constraint is still true and nothing else carries it. It stays. | No — it is a claim about the world, not about the tree |
| `carried` | A live page already carries this claim. Name it, and the librarian writes `decided_by:` there and `processed` here. | Partly — grep finds the page only where the wording matches |
| `false` | The claim is no longer true. Name the successor, or say plainly that none exists yet. | No |
| `topic` | A deferral with no design behind it. It is a subject we have not discussed, not a decision — it belongs on the frontier. | No |
| `contradicts <slug>` | This page disagrees with another live page filed under a **different** authority. | No — and this is the instrument the store does not have |

**Why `contradicts` is the whole argument.** Rule 3 of the gate already catches two `current` pages
claiming the same `authority:`. It is blind the moment two pages disagree under *different* slugs,
because there is nothing to compare. The vault has two recorded instances of exactly that shape,
neither can legally be marked as a contradiction, and the brief has reported the class in four
consecutive editions with no instrument behind it. That is a job no script will ever do, and it is
what makes this a separate reader rather than a grep.

## What retires a decision

A decision is an atomic working instrument: it points at the creation or the change of a page, and it
is spent once that page exists and names it back. That is not a proposal — it is already the sweep's
`decided_by:` criterion, and 44 of the 66 decisions archived on 2026-08-29 left exactly that way.

| Shape | Points at | Retires when | Today |
|---|---|---|---|
| `prohibition` | a rule in `wiki/rules/` | the rule names it in `decided_by:` | works — 16 of 263 |
| `deferral`, designed | a proposal | the proposal names it | 0 of 32 |
| `deferral`, undesigned | nothing — it is a topic | it leaves `decisions/` for the frontier list | not built |
| ratification | the rule it signs off | the rule names it | works |
| repeal | its successor page | `deprecated` + `superseded_by:`, then archive | half-checked |
| creation | an entity or a concept | that page names it in `decided_by:` | field is illegal there |
| `action` | a task | the task closes | S4 |

## Two gaps this model exposes

**A decision that built something can never retire.** `decided_by:` is legal only in `proposals/` and
`rules/`, so a decision whose product was an entity or a concept has nothing to discharge against and
stays in the folder forever. `entities/` and `concepts/` hold 181 of the 556 live pages and have no
exit criterion of their own — the same hole seen from the other side. The repair is to make the field
legal and **optional** there; required is a separate decision, taken after a back-fill, because made
required today 181 pages redden at once, and the store's own rule moves a field from optional to
required only when a decision says so.

**A repeal is only checked when it wears the right status.** `scripts/vault-archive.sh:239` refuses
to move a page marked `deprecated` that names no `superseded_by:`. The sweep writes
`status: archived` instead — so a repeal taken by the `decided_by:` criterion is never asked for its
successor at all. Two of 241 archived pages carry the field, and both were set by hand during the
ingest. For 237 of them the absence is correct: a decision that was *spent* is not superseded. What
nothing distinguishes is **spent from repealed** at the moment of the move, and only the second owes
a successor. The mechanism exists and is right; what is missing is the question being asked.

## What this costs, and what nobody has measured

Every figure below is a **flat** dispatch from a main session. Nested dispatch — the librarian
running its own readers — has never been measured in this repository, so the arithmetic for the
design above does not exist yet.

| Reading | Tokens | Wall clock | Note |
|---|---|---|---|
| `/ingest`, one journal | 271,465 | 34m08s | 151 tool calls |
| `/ingest`, one journal | 277,722 | 34m56s | 128 tool calls |
| lessons collector, only real run | 388,649 | 17m23s | over 182 pages; the folder now holds 18 |
| `/pre-task`, eleven items | 185,319 | 11m19s | 71 shortlisted, 38 opened |

**The cost tracks tool calls, not file sizes.** Across the five recorded ingests carrying both
figures, tokens per tool call sit between **1,552 and 2,170** — a factor of 1.4 — while the totals
span a factor of 1.8 and the call counts a factor of 2.4. The spend is the accumulated context
re-sent at every call, not any single large read.

That is the argument for this whole design: moving reading into an isolated context takes calls out
of the writer's loop. It is also why nobody can quote the net yet — two of the five points invert,
and the relation is not proven linear.

## Not decided here

- **The census's cadence.** Every ingest, on demand, or a cheap pass each session and a whole one at
  the sprint's close.
- **Whether the forked `vault-ask` replaces the librarian's own searching or sits beside it.**
  Replacing it is the clean version and costs a round trip on every lookup.
- **Whether a deferral carries the condition of its own return as a field.** The store says a
  deferral leaves "on the arrival of its term", and no page anywhere records what any given term is.
- **Where the frontier list lives** once undesigned deferrals stop being pages in `decisions/`.
- **`action`, and the task folder behind it.** Deferred to S4 by the owner; the exit condition is a
  task, and tasks do not exist yet.

## What blocks the build, read from the tree on 2026-08-30

**Buildable now.** `Agent` in the librarian's `tools:` line, one word. The two new agent files, which
nothing governs. The `/ingest` rewiring, in a file this session has already edited.

> **Corrected 2026-08-31, and the sentence it replaces is named rather than silently dropped.** This
> paragraph used to list `decided_by` added to the `optional:` block of `wiki/entities/_schema.yaml`
> and `wiki/concepts/_schema.yaml` as buildable. **The owner ruled the opposite on 2026-08-23**:
> `decided_by:` is legal in `wiki/proposals/` and `wiki/rules/` and in no other folder, on the causal
> chain he stated — a decision produces a proposal or a rule and nothing else, and anything further
> down names what it descends from in `sources:`
> ([[decided-by-is-legal-in-proposals-and-rules-and-required-in-rules]]). A key behaves differently
> from a legal value here, which is why the narrowing is safe rather than merely permitted: the gate
> reddens a page carrying a key that appears in neither block of its schema, so a folder left out
> refuses rather than waves through. Writing the field into those two schemas would have made it
> legal where it is forbidden.

**Blocked, and each names what would unblock it.**

1. **`vault-ask` cannot simply be forked.** The skill carries a rendered rule region,
   `speak-the-feedback-in-the-turn-and-the-hook-files-it`, whose text is addressed to **the caller**:
   *say it in your reply in that same turn*, and a hook lifts the block out of the message. Under
   `context: fork` the SKILL.md becomes the *forked agent's* prompt, so that region would instruct
   the fork to speak a feedback block no hook will read and no caller will see. Removing it means
   changing the rule page's `governs:` list, and rule pages are the librarian's. **Unblocked by a
   librarian write, not by a session edit.**
2. **The `topic` verdict has no destination.** Where the frontier list lives is not decided, so the
   census would return a verdict nobody can act on. **Unblocked by naming the destination.**
3. **`decided-by-is-legal-in-proposals-and-rules-and-required-in-rules` has to be overturned.** The
   owner ruled it on 2026-08-30; the decision page recording that is the librarian's, at the next
   `/ingest`. The schema may change first, but until the page lands the corpus disagrees with itself.
4. **The repeal check needs a way to tell spent from repealed**, and nothing carries that mark today.
   **Unblocked by a field, or by the repeal going through `deprecated` as the supersession procedure
   already says it should.**

**And the cost, which is not a blocker but is the day.** A new legal field in two folders changes
what the gate accepts, so `scripts/vault-check-selftest.sh` owes new cases; a whole run is 194 cases
in 29 minutes, and `make smoke` is about four.
