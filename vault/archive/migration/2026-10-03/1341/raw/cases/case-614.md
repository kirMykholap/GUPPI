## Case 614 — A test Entity that sets off waiting readings

> **context:**
> The person asked this session to close as many waiting readings as it can. A reading checks a promise at the moment the promise describes, and most open readings wait because that moment has not come since their Criterion was set. The person chose a test Entity as one way to bring some of those moments. The person chose to set off the other moments on purpose when the session decides to, not from a plan; examples are a `/carry` that is not needed, or a ledger line the hook refuses. Those other moments change no page, so they stay outside this Case. Nothing is broken on purpose to get a send-back from `rule-case-check`.
>
> This Case creates `entity-reading-probe` with no `ref`, and its purpose is close to the purpose of `entity-glossary`. That is the moment `estimate-plan-mode-verified` waits for: a `create` without a `ref` whose purpose an index line already carries, named in the `context` before ratification. This paragraph is that naming. The index line of `entities/entity-glossary.md` reads "The terms of GUPPI, one row each with its meaning and the page that defines it; the source of glossary.md". The test page repeats that meaning on purpose, and its purpose says it is a test page.
>
> At the librarian's run, the index check of `rule-index-check` compares the `create` with the entities index lines once more. It may merge a `create` into an `update` of the page that already holds the thing, or keep the entry and mark it `near`. This Case expects the entry to be kept with `near: entity-glossary` and not merged, because the page says it is a test page and not the source of `glossary.md`. That is the moment of the `near` clause of `estimate-index-check-merges`, which has never been exercised. Its Criterion stands, and a reading at the next `/hi` takes it from the report of the run.
>
> The page also holds an invented word, `quillwort`, and its replacement, `bramblewort`. A Case of the next session will replace the first word with the second by `reword`, which is the moment `estimate-generate-rewords` waits for. The same Case will then delete the page. The word change and the delete cannot run in this session (case 614, Q5). The check of pairs in `guppi/prespec.py` loads only the pages on disk, so a `reword` on a page that the same Spec creates gets the finding "a reword pair hits no live page". The docstring of the same file says the anchor is judged "against the page as the Spec leaves it". That gap stays as it is, and this Case does not fix it. Nothing in this Case schedules the Case of the next session.
>
> The person chose that the next session deletes the page. The delete must also come before any close of the sprint, because `estimate-sprint-migration-lint-clean` needs `make lint` to exit 0 at that close, and the live test page keeps lint red.
>
> The vault query of `.claude/agents/ask-guppi.md` ran here: the Grep `^(purpose|deferred_by):` over `vault/wiki/rules/` and over `vault/wiki/entities/`. The entities index printed four pages: `entity-sprint`, `entity-sprint-migration`, `entity-guppi` and `entity-glossary`. None is a test page, and `entity-glossary` is near, as above. The rules that bear on this Case are `rule-ask`, `rule-entities-schema` and `rule-index-check`. `rule-ask` asks for the query before a `create` without a `ref`. It stands `draft` with `deferred_by` `decision-case-553`, whose Problem is that the two agents that read the vault for a Case follow different rules on Decision pages. That does not touch this Case, which reads no Decision page. The Grep `reading-probe|quillwort|bramblewort` (case-insensitive) over `vault/` printed three files, all raw files of this session: `vault/raw/2026-10-03/event_log.md`, `vault/raw/2026-10-03/1341/ledger.md` and `vault/raw/2026-10-03/1341/cases/case-614.md`. No page under `vault/wiki/` or `vault/archive/` holds the slug or either word. The tags `workflow` and `librarian` exist in `vault/wiki/tags.md`.
>
> Two sentences of the frame do not fit the test page, and both stand, because the page lives for one session and the next session archives it. First, `rule-entities-schema` defines an Entity as a thing the developer builds, and the test page is not one. Second, while the page is live, `guppi lint` reports two findings on it:
> - `schema`, because a `Leaf` requires `parent` and a `create` with no `ref` gets none;
> - `orphan`, because no other live page names it in its frontmatter, and `check_orphans` of `guppi/lint.py` does not read the `create` list of a Decision page.
>
> Those are the findings that the Criteria of `estimate-entities-schema-checked` and `estimate-lint-finds-a-broken-link` promise for such a page, so both Criteria stand. A live reading of either Estimate taken while the page is live should count these findings as the test page, not as a defect.
>
> Done means `estimate-plan-mode-verified` reads this Case and its showing, and `estimate-index-check-merges` reads the report of the librarian's run. Both Criteria stand, because this Case is the moment each describes. `estimate-generate-writes` already checks how `guppi generate` writes a `create`, and its Criterion stands too. This Case creates no Estimate and replaces no Criterion. No Case of this session is related.

> **problem:**
> The person wants a test Entity that sets off waiting readings. The check refuses a word change on a page that the same session creates. So this session can only create the page, with the shape that sets off `estimate-plan-mode-verified` now and the `near` clause of `estimate-index-check-merges` at the librarian's run, and that lets the next session test `estimate-generate-rewords` and then delete it.

> **recommend:**
> - **What does this Case cover?**
>   - Recommended: (a) the test Entity only. The main agent stages the other moments itself, as work that needs no decision.
>   - Answer: The test Entity only. The person will set off the other moments on purpose when the session decides to, not by a plan, for example a `/carry` the person does not need.
> - **When is the test page deleted?**
>   - Recommended: (a) create, change and delete in this session.
>   - Answer: Agreed with the recommendation.
> - **Which moments does the shape of the test page produce?**
>   - Recommended: (a) both: no parent link and a purpose that repeats an existing Entity, and an invented word for a later word change.
>   - Answer: Agreed with the recommendation.
> - **Do I break my own answers on purpose to trigger the send-backs?**
>   - Recommended: (b) all but the rebuild in another shape.
>   - Answer: Nothing is broken on purpose. The person will set off the moments on purpose, not by a plan.
> - **Where does the word change go, now that the check refuses it in this session?**
>   - Recommended: (b) create now, and do the word change and the delete in the next session.
>   - Answer: Agreed.

> **given:**
> `entity-reading-probe` — the test page this Case creates
> **＋** `entity-glossary` — the page whose purpose the test page repeats
> **＋** `rule-entities-schema` — the shape of an Entity page and what an Entity is
> **＋** `rule-ask` — the vault query before a `create` without a `ref`
> **＋** `rule-index-check` — the librarian compares a `create` with the index lines once more
> **＋** `rule-page-generation` — `guppi generate` writes the page at the librarian's run
> **＋** `rule-lint` — `guppi lint` reports a page off its schema or named by no page

> **when:**
> The librarian's run after this session does the index check of `rule-index-check` over the `create` of this Case, runs `guppi generate` over it, and then runs `guppi lint`.

> **then:**
> The index check keeps the `create` of `entity-reading-probe` and marks it `near: entity-glossary`. It does not merge the `create` into an `update` of `entity-glossary`.
> **＋** `guppi generate` writes `entity-reading-probe` as a `draft` `Leaf` with no `parent`, with a `purpose` that repeats the meaning of the `purpose` of `entity-glossary` and says the page is a test page.
> **＋** Its `## Purpose` holds the words `quillwort` and `bramblewort`, which no other live page holds.
> **＋** While the page is live, `guppi lint` reports two findings on `entity-reading-probe`: `schema` for its missing `parent`, and `orphan`.
> **－** `entity-glossary` keeps its text, and no page gets a link to `entity-reading-probe`.

> **tasks:**
> - [ ] create `entity-reading-probe`
>   - type: `entity`
>   - kind: `Leaf`
>   - purpose: `The terms of GUPPI with their meanings and the pages that define them; a test page that stages waiting readings, deleted in the next session`
>   - tags: `[workflow, librarian]`
>   - sections.Purpose: `A test page, created to set off readings that wait for their moment, and deleted by a Case of the next session before any close of the sprint. Its purpose repeats the meaning of the purpose of entity-glossary, so that the Case that creates it names that page before ratification, the moment estimate-plan-mode-verified reads, and the index check of the librarian marks it near that page, the moment estimate-index-check-merges reads. It is not the source of glossary.md. Its text holds the invented word quillwort and the word bramblewort, so that the Case of the next session can replace the first by the second across the vault, the moment estimate-generate-rewords reads, and then delete this page.`

> **ratification:**
> ```
> - decision[case 614][create][entity-reading-probe]{tags:workflow,librarian}
> ```
