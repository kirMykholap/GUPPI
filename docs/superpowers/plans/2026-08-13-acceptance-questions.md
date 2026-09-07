# Acceptance questions for the librarian

Phase 1 passes if the librarian answers these correctly and completely **while the main session
never reads the vault**.

The expected answers below were written from `docs/HANDOFF.md` **before the librarian was asked
anything**. That is the whole point: they cover the category the owner's own review loop cannot —
*what was missing and you had forgotten* — precisely because the answer is known in advance and
therefore cannot be graded by whether it merely sounds plausible.

> **A caveat about who runs them.** Run in the session that built the vault, these prove less than
> they should: that session knows what is in the corpus. The librarian itself is honest — it is a
> subagent with a fresh context that has to find everything — but the grading is not blind.
> **The stronger run is a fresh session**, and the owner is the right person to make it.

---

## Q1 — Why does the batch finaliser have exactly one owner, and what breaks if a second is added?

**Expected.** A batch's normal end is written by `run_profile` and nobody else; two owners would
disagree about the end time and the status. The only other closers exist for a process that can no
longer speak for itself — the startup sweep and the staleness rule, both in `ingest/batches.py` —
and they cannot disagree because `finish_batch` is scoped to `status='running'`: the first verdict
wins. A crashed run closes as `interrupted`, never `finished`.

**Bonus, if it finds it:** the sweep closes only `started_by='web'` batches, because a CLI batch
lives in another process and may still be running.

## Q2 — What does an agent round trip cost, and where does that number come from?

**Expected.** 5 to 35 minutes, measured on slice 3, which cost a session of eight to ten hours;
seven tasks at three or four trips each is the session, and fix waves were the most expensive step
(35 minutes for one, 30 for a task later thrown away).

**The half that matters most:** the figure describes **implementer** trips — agents that write code
and run tests. It does not describe every subagent call; a librarian call is tens of seconds. An
answer that gives the number without its boundary is **incomplete**, because that is precisely how
the number was misapplied once already.

## Q3 — What has already been decided about JavaScript, and why was the rule narrowed?

**Expected.** Own JavaScript is allowed where it cannot show a wrong list — decided 2026-08-12,
replacing "no JavaScript of our own beyond htmx and the theme toggle". The line is what the code can
affect: presentation and interaction no query depends on is allowed; anything participating in
*which rows are on screen* is not.

**The honest reason, and an answer without it is incomplete:** of the four silent defects slice 3
found, three were plain test-coverage gaps any architecture would have had; only the stale-chips one
was htmx-shaped. The real cost is that no test here executes JavaScript, and a JS runner would mean
npm.

**Bonus:** the AST test that would pin this boundary is not written yet.

## Q4 — I am rewriting the view in React. What in the documentation helps, and what gets in the way?

**Expected.** The decision already exists and is listed as one not to relitigate: **the stack stays
htmx, and React arrives as islands only when a screen's state must live in a tab rather than in the
database** — the resume editor and the AI interview qualify, matching with live re-ranking does not.
A filter change costs 5.9 ms against a 250 ms debounce, and server cost is bounded by `PAGE_SIZE`
while client cost grows with the total.

Also relevant: no table library leaves a server-rendered `<table>` (all seven verified by
downloading them); the JavaScript policy above; the per-page swap-target invariant; no npm; and no
test here executes JavaScript.

**It must also report the negative space** — nothing has been recorded about a wholesale framework
migration, so that decision is open and would have to be written down.

## Q5 — <the owner's own question>

_Open. The four above were drafted by the party that already knows what the file contains; his will
be more honest._

---

## Results — 2026-08-13, proxy run

Run through a fresh-context agent instructed to read `.claude/agents/vault-librarian.md` and follow
it. **The main session did not read the vault.** Not the full test: `.claude/agents/` is loaded at
session start, so the agent was not registered and could not be dispatched by name — see
[[claude-code-config-loading]]. Registration is untested until a fresh session; the corpus and the
instructions are not.

| | Verdict | Notes |
|---|---|---|
| **Q1** batch finaliser | **PASS**, with the bonus | Found every expected element including `started_by='web'`. Went further: the page is `basis: code`, so it checked `ingest/batches.py:164,204` — and found a fact the vault does **not** carry, that `finish_batch` also closes dangling `ParseRun` rows |
| **Q2** round-trip cost | **PASS** | Number, provenance and — the half that matters — the boundary: implementer trips only, a librarian call is tens of seconds |
| **Q3** JavaScript, asked in Russian | **PASS**, with the bonus | Including the honest reason (3 of 4 defects were coverage gaps) and the unwritten AST test |
| **Q4** React, asked in Russian | **PASS** | Named the island rule and its one condition, and correctly concluded that «весь внешний вид» falls **outside** it — then read the schema well enough to say that proceeding means superseding a page whose `authority` is a sole claim |

**What the negative space found, which is the point of requiring it.** Gaps neither reviewer nor
author had noticed: no test guards the one-finaliser rule (`test_batch_write_boundary.py` guards
*which module* writes, not *how many closers* exist); the 5-minute lower bound of the round-trip
range has no named instance; reviewer trips are unmeasured, so "review is affordable" is a
judgement rather than a measurement; and the 2026-08-11 recalibration has no post-hoc data
confirming slices became faster.

**The first recorded miss, and it is word-shaped.** Both runs independently reported that `tags.md`
had no alias for JavaScript, React, фронтенд, вёрстка or внешний вид — the Russian questions landed
only because those English words appear in filenames. Closed the same day by a `frontend` tag with
eleven aliases. This is precisely the category the vector deferral said would decide the question,
and it was closed by one dictionary entry rather than by an index.

---

## Results — 2026-08-13, second run: dispatched by name, against the shortened `CLAUDE.md`

Run **after task 10**, when `docs/HANDOFF.md` had become a 27-line pointer and `CLAUDE.md` had
been reduced to rules with `[[wikilinks]]` instead of rules with explanations. Q3 and Q4 were
asked in Russian.

**The dispatch was the test this time, not only the answers.** Every earlier run was a stand-in:
`.claude/agents/` is read when a session starts, so the session that wrote the librarian could
not call it by name and told a general agent to read its definition instead. This one was
dispatched as `vault-librarian` in a session that began after the file existed. It reports that
the definition arrived as its system prompt — it opened the file only afterwards, to compare, and
found the same 96 lines and the same `tools:` list as the toolset it actually had. **Registration
is no longer untested.** Still untested: `/vault-ask` as the entry point (this was a direct
dispatch), and the writing half of the definition (this run was read-only).

| | Verdict | Notes |
|---|---|---|
| **Q1** batch finaliser | **PASS** | The rule, both cleaners, why they cannot contradict, and what breaks — plus the consequence the first run did not draw: `load_state` reads the *latest* batch, so a losing writer's status is what the user reads |
| **Q2** round-trip cost | **PASS** | Number, provenance, and both boundaries: implementer trips only, and the 5-minute end has no named instance |
| **Q3** JavaScript, in Russian | **PASS** | The narrowed rule, the honest reason, and the debt: the AST test is owed, nothing has forced it, and no own JavaScript has been written since |
| **Q4** React, in Russian | **PASS** | The island rule and its condition, what survives a rewrite (the query invariants) and what dies with the templates (the swap-target invariant, the fragment tests), and that no decision about React beyond the island condition exists — so proceeding is a new decision to be recorded |

**The confound, reported by the librarian itself and worth more than the passes.** The harness
injects `CLAUDE.md` into a subagent's context as it stood **at session start** — the long version.
So this run had the old explanations for free and cannot prove the shortened file is sufficient
on its own. What it *can* prove, and did, is the other half: it compared four moved paragraphs
against the pages that received them, line by line, and **found no page thinner than the paragraph
it replaced** — three of the four carry strictly more, including two evidence gaps that were never
in `CLAUDE.md` at all. The move was a move.

It also named the new failure mode honestly: the answer to "why" is now behind a wikilink, and an
agent that does not follow it gets a rule without its reason. Cheap for anything that can grep the
vault; impossible for anything that cannot.

**A second miss, and it is word-shaped again.** `rg -il "отображени|фронт|переписыва|вёрстк"` over
the wiki returns **zero files** — the corpus is entirely English, and a Russian question reaches it
only through `tags.md`. The `frontend` tag added after the first run carries `фронтенд`, `фронт`,
`вёрстка`, `внешний вид` and `React`, and those worked; **`отображение` is not among them**, and
neither is any word for "rewrite". The bridge holds only for vocabulary someone thought of in
advance, which is the second data point in the file that the vector question turns on.

**And a gap in the map rather than in the answer:** there is no page about React. Q4's answer had
to be assembled by walking wikilinks out of `the-stack-stays-htmx`, because `rg -il react` finds
only the two JavaScript pages and one meta page. Grep alone does not reach it.
