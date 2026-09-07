# Job Hunt AI — working agreements

Local job-hunting tool: collects vacancies from work.ua and dou.ua into PostgreSQL,
deduplicates them, tracks the ones that disappeared, and shows them in a local web
interface of two pages behind one shell: `/vacancies`, the table where application
statuses are kept, and `/collection`, where collection is started and the search tags
are switched on and off.

Python 3.12, FastAPI, SQLAlchemy 2.0 (imperative `select()`), Jinja2, htmx 2,
PostgreSQL 17, pytest.

## The rules, and the routes into the vault

**This file is a map and a handful of rules for how to work.**

<!-- rule: the-map-in-claude-md-is-the-vault-its-librarian-and-the-sprint -->
**The vault holds the reasons.** It is the top-level directory containing a `wiki/`, and it
carries what exists, what was decided and why, how each mechanism is built, and what has burned
us. None of that is repeated here: ask it before deciding anything it may have decided already.

**It has exactly one writer.** The librarian writes `wiki/` and the registers — `index.md`,
`tags.md`, `sprint.md`, `log.md`. A session does not edit them by hand; when an answer comes back
wrong it reports the miss and lets the librarian write.

**Work belongs to a sprint, and the vault's `sprint.md` is where that sprint lives** — which one
is open, its goal, and the command each acceptance criterion is decided by. Work outside an open
sprint is work nobody agreed to. Read the contents there; they are never copied here.

<!-- /rule: the-map-in-claude-md-is-the-vault-its-librarian-and-the-sprint -->

`/vault-ask <question>` — in Russian if that is the question you have. A brief for the current
sprint arrives automatically at session start.

Everything else that governs this codebase is in the vault. The rules here are here because obeying
them late is the same as not obeying them at all.

<!-- rule: dispatch-librarians-in-parallel-only-for-reading -->
**Dispatch librarians in parallel only for reading.** A fan-out that answers questions is fine; the
moment those agents may write, they are contending. If a parallel run must be allowed to write,
re-read immediately before writing and append rather than rewrite — never hold a copy of a register
across a long turn.

<!-- /rule: dispatch-librarians-in-parallel-only-for-reading -->
<!-- rule: ask-before-weakening-or-working-around-a-rule -->
**Ask before you weaken, remove or work around any rule** — here, in the code, or in the vault.
Every recorded divergence in this project began with the rule looking unnecessary.

<!-- /rule: ask-before-weakening-or-working-around-a-rule -->
<!-- rule: a-session-ends-with-retro-then-handoff-then-ingest -->
**A session ends with** `/retro`**, then** `/handoff`**, then** `/ingest`**.** Retro interrogates the
session and resolves every open question with the owner; handoff routes what it found into the
journal; ingest compiles. The journal those write is the only thing the next session inherits —
nothing else in this repository carries what happened here. Skipping them does not lose the code,
which git has; it loses the reasons, which nothing else does.

<!-- /rule: a-session-ends-with-retro-then-handoff-then-ingest -->
<!-- rule: a-retrospective-is-a-sessions-end-not-a-sprints-ritual -->
**"Retrospective" means the end of a session.** The sprint-level ritual is a *sprint retrospective*
and is a different thing — the word meant both for three days and that ambiguity put two live,
contradictory answers in the vault about when `/ingest` runs.

<!-- /rule: a-retrospective-is-a-sessions-end-not-a-sprints-ritual -->
<!-- rule: speak-the-feedback-in-the-turn-and-the-hook-files-it -->
**When the vault answers wrong — or anything else worth recording goes wrong — say it in your reply
in that same turn**, inside a fenced `VAULT-FEEDBACK` block. **You never write**
`.superpowers/sdd/vault-feedback.md` **yourself.** A hook on `MessageDisplay` lifts the block out of
your message and files it, which is what makes the channel usable in plan mode, where a session
cannot write a file at all.

```VAULT-FEEDBACK
- miss: what the vault failed to supply, and where that surfaced
- measure: a number, with what it does and does not mean
- decision: what was decided, by whom, and against what - naming which shape it is:
  the owner said it, the owner selected it, or the session understood it
- harness: a decided change to the files that instruct an agent
```

A `VAULT-FEEDBACK` fence nested inside another fence is an example and is ignored, so the block
above files nothing. `/handoff` drains the file into `Feedback to the librarian` and `/ingest` files
each line under the kind it names. **Recording is not arguing**: it costs a line, and whether the
corpus changes is the owner's call, later.

<!-- /rule: speak-the-feedback-in-the-turn-and-the-hook-files-it -->

**If you cannot dispatch an agent** — you are one — read the vault by hand:

```
rg -i "<the russian word>" job_hunt_ai_vault/tags.md    # the aliases, and the English term
rg -il "<term>" job_hunt_ai_vault/wiki                  # then the pages
```

The corpus is English and the questions often are not, which is what the alias list is for. This
matters because every task here is reviewed by a subagent, so the readers most in need of the vault
are the ones that cannot ask it the easy way.

<!-- rule: the-suite-never-runs-against-the-production-database -->
**The test database comes from** `TEST_DATABASE_URL` (see `tests/conftest.py`) and is created
by the fixture. **Never run the suite against the production database** — the fixture builds
and drops schema, and there is no second chance.

<!-- /rule: the-suite-never-runs-against-the-production-database -->
<!-- rule: the-owner-decides-how-a-slice-is-executed -->
**How a slice is executed is the owner's decision, and it overrides any skill that says
otherwise.** Ask the vault before you start one; the skills will confidently tell you a
different thing.

<!-- /rule: the-owner-decides-how-a-slice-is-executed -->

## Language

<!-- rule: english-in-the-repository-russian-with-the-owner -->
**English for everything written into the repository**: code, identifiers, docstrings,
comments, test names, documents under `docs/`, commit messages, specs, and any
brief or report handed to a subagent.

**Russian only for chat with the owner** — and for what the owner sees while using the  
tool: the web page and CLI output are product content, not documentation, and stay in  
Russian. Status values remain English identifiers (`new`, `applied`, …).
**And the plan the owner reads in order to approve it is Russian**: it is written for him, and it
lives outside the repository.

**English technical terms are not transliterated into Cyrillic**: "vault", not «ваулт»;
"proposal", not «пропозал». They are the repository’s own vocabulary, and an identifier keeps
its own alphabet inside a Russian sentence.

<!-- /rule: english-in-the-repository-russian-with-the-owner -->

## How to write it

<!-- rule: write-plainly-name-the-source-and-say-what-is-not-done -->
- Keep the facts and remove the sales pitch.
- Name a real source or remove the claim.
- Plain language by default, never on request: short sentences, active voice, a common word over a
  term.
- Give the answer in the first sentence, then the list, and keep the reasoning below it skippable.
  No "if X then Y".
- One question per message.
- Say what is done and what is not done. Never leave the not-done implied.

<!-- /rule: write-plainly-name-the-source-and-say-what-is-not-done -->

<!-- rule: the-reply-is-a-report-answers-and-one-case -->
**Every reply opens with the frontier**, printed as a numbered list with a one-line description and a
status per item — discussed, ratified, deferred, open. It is not a summary and it is not optional:
the form held on 2026-08-30 because it was re-stated at the top of every message, and nothing else
carries it forward.

**Then the reply is three things, in this order:** what the session did since the last message; the
answers to the owner's questions; and **exactly one case**.

**A case is worked by the decision schema, all five parts and in this order:**

1. **Context** — what the thing is, how it works today, and which pages, modules and files it touches.
2. **The question** — the problem, or the fork between the options, stated so it can be answered.
3. **How it works after** — what the state is once this is decided, naming the target that receives it.
4. **Recommendation** — the session's own, with its ground.
5. **Ratification** — left for the owner, and filled with his words when he gives them.

**No case is opened until the previous one is ratified or explicitly deferred.** Two open cases is
how a session stops being answerable.

**And any question carries its context, case or not.** What the thing is, how it works today, what
would be built, the fork if there is one, and a recommendation with its ground. A clarifying question
is not exempt.

**The frontier is one concept with three carriers, and they are not interchangeable.**

- **`sprint.md` is the frontier between sessions**, and it is where a deferred item lands.
- **`brief.md` is its view at session start** — **generated** from `sprint.md`, never written by hand.
- **`grill-me` extends it** with what an interview opens.

**It is walked twice in a session** — before the plan is written, and again at the retro — and never
at the retro alone. **Every item not discussed is marked deferred**, in the chat, through the
feedback channel.

<!-- /rule: the-reply-is-a-report-answers-and-one-case -->

## Commands

**`make help` lists them.** The commands are not written out here: a list in prose goes stale
without saying so, and this one already did — it claimed the vault gate cost `~2 s` when it cost
five times that.

```
make help     # every target, with what it is for
make style    # ruff over src and tests. MUST BE CLEAN BEFORE EVERY COMMIT
make smoke    # the fast check of the whole repository, about three minutes
make test     # the product's own suite
```

`docker compose up -d --build` brings up the database and the app, and has no target: it is not a
check and nothing here decides that a target may write.

`python -m uv run ...` is an equivalent fallback and works in any shell, whatever its
PATH. The empty-state hints on `/vacancies` deliberately use that longer form.

Do not run `ruff format --check` over `docs/` or the vault — it reports noise on markdown code
blocks. Line width is 100 (`pyproject.toml`).

**Add no new dependencies** — neither Python packages nor npm. htmx already lives in
`src/jobhunt/web/static/`.
