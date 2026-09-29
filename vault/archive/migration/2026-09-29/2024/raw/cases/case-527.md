## Case 527 — A glossary row passes when its page says what the term is

> **context:**
> The glossary is the `## Terms` table of `entity-glossary`. Each row holds a term, a one-line meaning and a `where` link to the live page that defines the term. `uv run guppi glossary` renders the table into `vault/wiki/glossary.md`, and `/hi` loads it. `estimate-glossary-terms-defined` promises that each `where` page "defines the term of the row". The reading at the `/hi` of this session, after the librarian's run 1c196e8 that applied case 520, failed on three rows. `rule-hook-registry` does not say what a hook is. The Retro row puts the short defer under `## Retro` in the Spec, but `rule-retro` puts it under `## Deferred`, and so does `case-schema.md`. `rule-harness` does not say what the harness is. Only `case-schema.md`, the Render of `rule-case-protocol`, says it.
> The readings also do not agree on what "defines" means. The reading of session 1753 (L4) failed five rows and accepted the others. A strict pass in this session found eighteen rows whose page defines the term but leaves out some claim of the meaning. One example is Handoff, whose page `rule-handoff` never names `guppi gate`. The pass reported each of these as a claim the page leaves out, not as a claim the page contradicts. `lesson-glossary-one-where-for-a-term-many-schemas-define` shows the cost of the strict reading: a meaning cut down to its one `where` page becomes narrower than the truth.
> In one round the person accepted every recommendation, in their words: "OK, I agree".
> - A row passes when its page says what the term is and nothing in the meaning contradicts that page. Details may rest on other pages.
> - This reading goes into the Criterion, which is replaced whole in 527.2.
> - Hook and Harness get their definitions from a new sentence in the Purpose of their `where` pages.
> - The sentence of `rule-retro` on who writes the short defer stays out of this Case.
>
> Pre-spec found two faults in the ratified text. This answer fixes both.
> - Case 531.1 of this session replaces the Render of `rule-retro` whole. After it, Retro writes no short defer, and the sentence that puts one under `## Deferred` is gone. 531.1 also rewrites the Retro row around the words that 527.1 changes, and its pairs match the row before and after 527.1. After both Cases, the row says that a short defer stands only at the close of Plan Mode, under `## Deferred` in the Spec. That rests on `case-schema.md`, which puts a short defer under the `## Deferred` heading of the plan file. So 527.1 now names `case-schema.md` for this line, not `rule-retro`. The contradiction on who writes a Retro defer goes away with 531.1.
> - The first text of the `rule-harness` sentence listed a closed set of files. That list left out `guppi.toml`, which `rule-guppi-config` renders and whose rule the same Purpose counts. It also left out `vault/wiki/where-to-stop.md`, which Case 531.7 renders from `rules/`. The sentence and the row Harness now define the harness as the files that `guppi render` writes from the pages of `rules/`, and they name some of those files as examples. A new rendered file then needs no change to the row.
>
> What `case-guppi` found in the frame:
> - `estimate-harness-pipeline` reads the Purpose of `rule-harness`. It reads only the three rules, the order of `make lint` and the rules outside any pipeline. The new sentence makes none of that false, so the Estimate is not named.
> - `estimate-hook-registry-rendered` reads the render of `.claude/settings.json`. The Purpose of `rule-hook-registry` is outside its `## Render`, so the file does not change.
> - The Estimates of `rule-glossary` read the render, the check and the ticks, not these rows.
> - The Purpose of `entity-glossary` calls `where` "the live page that defines it". That stays true under the new reading.
> - The near backlog item `rule-page-generation` is deferred by case 469, which is about a supersede of an archived Decision. This Case does not touch it.
>
> The check of the answer notes that one line of the old Criterion is not carried word for word. The change is on purpose. The old line was "Each row names in `where` a `[[slug]]` of a live page, and that page defines the term of the row." In 527.2 it ends "that page says what the term of the row is", which is the reading the person chose. The new `＋` and `－` lines say that a contradiction fails a row and that a claim the page leaves out does not. The line on a term in two rows and the `－` line on the terms that are not rows are carried word for word.
> The open `read` line of this Estimate in the 1753 Spec closes at the librarian's run. The reading of this session ticks it, because `generate` ticks the lines of a slug in every live Spec of `raw/` (case 326). The Case creates no page, so no vault query was run. Not done: the eighteen rows keep the claims their pages leave out.

> **problem:**
> Three rows of the glossary link to a page that does not say what the term is, or that contradicts the row. The Criterion of `estimate-glossary-terms-defined` does not say how strictly "defines the term" reads, so two readings of one table counted different rows as failed.

> **recommend:**
> Read "defines" as "says what the term is, and does not contradict the row", and write that reading into the Criterion. Add one sentence each to the Purpose of `rule-hook-registry` and `rule-harness`, so that they say what a hook and the harness are. Define the harness by what `guppi render` writes, so the definition does not go stale when a new file is rendered. Correct the heading in the Retro row. The strict reading was rejected: every claim of a row would have to stand on its one `where` page, which cuts meanings below the truth, as the lesson of session 1753 records.

### Case 527.1 — The rows Hook, Harness and Retro match their pages

> **given:**
> `entity-glossary` — the page whose `## Terms` table this Case changes
> **＋** `vault/wiki/glossary.md` — the render of the table, grouped by the parent MOC of `where`
> **＋** `rule-glossary` — the guard: one link per `where` cell, a live page, no term twice
> **＋** `rule-hook-registry` — the `where` page of Hook, whose Purpose gains what a hook is
> **＋** `rule-harness` — the `where` page of Harness, whose Purpose gains what the harness is
> **＋** `rule-render-harness` — the renderer `guppi render`, which writes the files of the harness from the pages of `rules/`
> **＋** `rule-case-protocol` — its Render `case-schema.md` puts a short defer under the `## Deferred` heading of the Spec

> **when:**
> `uv run guppi glossary` renders `vault/wiki/glossary.md` from the `## Terms` table of `entity-glossary` at the librarian's run, and a reader follows the `where` link of the rows Hook, Harness and Retro.

> **then:**
> The Purpose of `rule-hook-registry` says what a hook is, and the row Hook stands as it is.
> **＋** The Purpose of `rule-harness` says that the harness is the files that `guppi render` writes from the pages of `rules/`, and the row Harness says the same.
> **＋** The row Retro puts the short defer under `## Deferred` in the Spec, as `case-schema.md` does.
> **－** The other rows of the table of `entity-glossary` do not change.
> **－** The Render of `rule-hook-registry` does not change.

> **tasks:**
> - [ ] update `entity-glossary`
>   - old: `` | Harness | Hooks, agents, skills rendered from `rules/` pages | [[rule-harness]] | ``
>   - new: `` | Harness | The files that `guppi render` writes from the pages of `rules/`, such as `.claude/settings.json` with its hooks, the skills and agents, `CLAUDE.md`, `case-schema.md` and `guppi.toml` | [[rule-harness]] | ``
>   - old: `` under `## Retro` in the Spec ``
>   - new: `` under `## Deferred` in the Spec ``
>   - change: `the row Harness defines the harness as the files guppi render writes from rules/; the row Retro puts the short defer under ## Deferred, as case-schema.md does (case 527.1)`
> - [ ] update `rule-hook-registry`
>   - old: `Prevents a hook from being registered by hand, outside a ratified decision.`
>   - new: `` Prevents a hook from being registered by hand, outside a ratified decision. A hook is a script that Claude Code runs when an event of the session fires, such as `Stop` or `PreToolUse`; the Rule page behind it names the script in `implementation_ref`. ``
>   - change: `the Purpose says what a hook is (case 527.1)`
> - [ ] update `rule-harness`
>   - old: `Prevents the tools of the harness from drifting apart from the pages that describe them.`
>   - new: `` Prevents the tools of the harness from drifting apart from the pages that describe them. The harness is the files that `guppi render` writes from the pages of `rules/`, such as `.claude/settings.json` with its hooks, the skills and agents under `.claude/`, `CLAUDE.md`, `case-schema.md` and `guppi.toml`. ``
>   - change: `the Purpose says what the harness is: the files guppi render writes from the pages of rules/ (case 527.1)`
> - [ ] `uv run guppi glossary`

> **ratification:**
> ```
> - decision[case 527.1][update][entity-glossary]{ref:entity-glossary}
> - decision[case 527.1][update][rule-hook-registry]{ref:rule-hook-registry}
> - decision[case 527.1][update][rule-harness]{ref:rule-harness}
> ```

### Case 527.2 — The glossary check reads whether the page says what the term is

> **given:**
> `estimate-glossary-terms-defined` — the promise on the rows of the glossary; its Criterion is replaced whole
> **＋** `entity-glossary` — the page whose `## Terms` table the Estimate reads
> **＋** `rule-glossary` — the guard whose script `uv run guppi glossary` reads the table
> **＋** `rule-lint` — the rule of `guppi lint`, which reads the same table

> **when:**
> `uv run guppi glossary` reads the `## Terms` table of `entity-glossary` at the librarian's run, and `guppi lint` and a reader read the same table.

> **then:**
> Each row names in `where` a `[[slug]]` of a live page, and that page says what the term of the row is.
> **＋** No claim of the meaning of a row contradicts its `where` page.
> **＋** No term stands in two rows.
> **－** A row does not fail because its `where` page leaves out a claim of its meaning.
> **－** The terms that the Purpose of `entity-glossary` names as not rows, C4 model, Delegate and the retired terms, stand in no row.

> **tasks:**
> - [ ] update `estimate-glossary-terms-defined`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the where page says what the term is and contradicts no claim of the row; a claim it leaves out does not fail the row (case 527.2)`
> - [ ] read `estimate-glossary-terms-defined` — by hand in a later session after the librarian's run: the table of `vault/wiki/glossary.md` against each `where` page, and `make lint`

> **ratification:**
> ```
> - decision[case 527.2][update][estimate-glossary-terms-defined]{ref:entity-glossary}
> ```
