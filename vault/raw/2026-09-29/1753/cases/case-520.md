## Case 520 — The glossary rows point at the page that defines them

> **context:**
> The glossary is the `## Terms` table of `entity-glossary`. Each row holds a term, a one-line meaning and a `where` link to the live page that defines the term. `guppi glossary` renders the table into `vault/wiki/glossary.md`, grouped by the parent MOC of each `where` page, and `/hi` loads it. `estimate-glossary-terms-defined` promises that each `where` page defines its row. The reading at this `/hi` failed on five rows after the librarian's run d8c1f17, which applied case 515.
> - Vault links to `rule-page-schemas`, which never says what the vault is. Its meaning also reads as "one page per category".
> - Hook links to `rule-hook-registry`, but its meaning describes the ledger writer: it reads the transcript, keeps its window across midnight, and can block. Only `rule-ledger-write` says that.
> - `deferred_by` and `origin` link to `rule-page-generation`, whose body names neither field.
> - Entity / Rule (status) links to the same page, which lists neither `archived` nor "built once every Estimate passes".
>
> The `origin` meaning also says "created or deleted" and that lint greps the field. No page body says either.
>
> The person agreed with every recommendation of the round. Each changed row links to a page that states it. A clause that no such page states is cut, and it still stands on its own page, such as midnight on `rule-ledger-write`. The rows the reading accepted only loosely stay as they are: `CLAUDE.md`, `case-schema.md`, Types and Decision.
>
> Two passes of pre-spec changed the new meanings. The person agreed to cut the `deferred_by` meaning to what its page says.
> - Hook names `rule-hook-registry` in place of "this page", which in the glossary would read as `entity-glossary`. As that page says, a hook can also stand in an agent's own frontmatter, as part of that agent's Render.
> - `deferred_by` first kept "On an Entity, Rule or Insight", which `rule-rules-schema` does not state. Then it said "On a Rule", which was too narrow: `rule-entities-schema` and `rule-insights-schema` define the same field, and a live Insight carries it. The meaning now has no qualifier and opens with the Decision pages whose `defer` targets the page. That is true for all three types and is what `rule-rules-schema` states.
> - `origin` follows `rule-decisions-schema`: its case numbers, the Case file only for a Case built by `case-guppi` from session 2026-09-27/1819 on, and the pointer that is not rewritten. It opens "On a page a Case created". That is my choice over naming the Decision page alone: the Entity, Rule and Estimate schemas give the same form for a page a Case created. A Lesson points at its ledger line, and an Insight points at no ledger line. Neither is a page a Case created, so the meaning does not claim them.
>
> The Case creates no page, so no vault query was needed. The frame reads as follows. `rule-glossary` stops the write on a `where` that names no live page, so every new link must name a live page, and each one does. The Purpose of `entity-glossary` lets a term enter, change or leave by an `update` of the page with `replace` pairs, and the split of the status row does exactly that. The Criterion of `estimate-glossary-terms-defined` stands whole, because the promise does not change, only the rows. So its status is not set to `pending` here, and its reading waits for the librarian's run that renders the table. The Estimates of `rule-glossary` speak of the render, the check and the ticks, not of these rows, and are not touched.

> **problem:**
> Five rows of the glossary link to a page that does not define their term, or give a meaning that their `where` page does not state. So the promise of `estimate-glossary-terms-defined` fails, and a reader who follows the link does not find the term.

> **recommend:**
> Change the five rows by `replace` pairs on `entity-glossary`:
> - Vault links to `rule-vault-layout`, with its meaning taken from that page.
> - Hook keeps `rule-hook-registry`, and its meaning says what the registry says.
> - Entity / Rule (status) splits into Entity (status) → `rule-entities-schema` and Rule (status) → `rule-rules-schema`, as every other status row is per type.
> - `deferred_by` links to `rule-rules-schema`, the fullest statement of the field, with its meaning cut to that page.
> - `origin` links to `rule-decisions-schema`, with its meaning and case numbers taken from that page, for a page a Case created.
>
> Changing only the links and keeping the extra clauses was rejected, because the next reading would fail on the same clauses.

> **given:**
> `entity-glossary` — the page whose `## Terms` table this Case changes
> **＋** `vault/wiki/glossary.md` — the render of the table, grouped by the parent MOC of `where`
> **＋** `rule-glossary` — the guard: one link per `where` cell, a live page, no term twice
> **＋** `rule-vault-layout` — the new `where` page of Vault
> **＋** `rule-hook-registry` — the `where` page of Hook
> **＋** `rule-entities-schema` — the new `where` page of Entity (status)
> **＋** `rule-rules-schema` — the new `where` page of Rule (status) and `deferred_by`
> **＋** `rule-decisions-schema` — the new `where` page of `origin`

> **when:**
> `uv run guppi glossary` renders `vault/wiki/glossary.md` from the `## Terms` table of `entity-glossary` at the librarian's run, and a reader follows the `where` link of a row.

> **then:**
> The row Vault names `rule-vault-layout`, and its meaning says that the vault is `vault/wiki/`, one folder per page category.
> **＋** The row Hook names `rule-hook-registry`, and its meaning says only what that page says.
> **＋** The rows Entity (status) and Rule (status) replace the row Entity / Rule (status), and they name `rule-entities-schema` and `rule-rules-schema`.
> **＋** The row `deferred_by` names `rule-rules-schema`, and its meaning says only what that page says.
> **＋** The row `origin` names `rule-decisions-schema`, and its meaning says only what that page says, for a page a Case created.
> **＋** `vault/wiki/glossary.md` lists each of these rows under the parent MOC of its new `where` page.
> **－** The other rows of the table of `entity-glossary` do not change.

> **tasks:**
> - [ ] update `entity-glossary`
>   - old: `| Vault | The folder of Markdown pages, one per category | [[rule-page-schemas]] |`
>   - new: `` | Vault | `vault/wiki/`: one folder per page category, each page a file named by its slug | [[rule-vault-layout]] | ``
>   - old: `` | Hook | An event-triggered script behind a Rule page, the ledger writer on `Stop`, which reads the session's transcript back, keeps its `hi` window across midnight, and can block | [[rule-hook-registry]] | ``
>   - new: `` | Hook | A script that fires on an event of the session, behind a Rule page; registered in the `hooks` key of `.claude/settings.json`, which `rule-hook-registry` renders, or in an agent's own frontmatter as part of that agent's Render; a new hook in the file is an `update` of `rule-hook-registry` in the Case that creates its Rule | [[rule-hook-registry]] | ``
>   - old: `` | `deferred_by` | On an Entity, Rule or Insight, the Decision pages whose `defer` targets it; set by `generate`, cleared by a `supersedes`, shown in the index line, followed by `ask-guppi` | [[rule-page-generation]] | ``
>   - new: `` | `deferred_by` | The Decision pages whose `defer` targets the page; written by `guppi generate` on a defer, cleared when a later Case `supersedes` that one; the index line carries it, so `ask-guppi` reaches the deferred decision (case 52.3) | [[rule-rules-schema]] | ``
>   - old: `` | `origin` | The Decision that created or deleted the page, as `raw/<date>/<HHMM>/ledger.md#case-N` — the date form on older pages; kept when archived, never rewritten; `#case-N` is a grep target lint checks in `raw/` or in the archive (case 103.6) | [[rule-page-generation]] | ``
>   - new: `` | `origin` | On a page a Case created: where that Case was ratified, `raw/<date>/<HHMM>/ledger.md#case-N` — the date form `raw/<date>/ledger.md#case-N` on pages born before 2026-09-13 (case 103.6); the folder holds the Spec with the Case and, for a Case built by `case-guppi` from session 2026-09-27/1819 on, its Case file (case 513); the pointer is not rewritten when the session is archived (cases 100.1, 103.6) | [[rule-decisions-schema]] | ``
>   - old: `` | Entity / Rule (status) | `draft` / `built` / `archived`; `built` is computed once every Estimate passes, never by hand | [[rule-page-generation]] | ``
>   - new:
>     ```
>     | Entity (status) | `draft` / `built` / `archived`; `built` is set by the cascade of `generate` once every Estimate passes, never by hand | [[rule-entities-schema]] |
>     | Rule (status) | `draft` / `built` / `archived`; `built` is set by the cascade of `generate` once every Estimate passes, never by hand | [[rule-rules-schema]] |
>     ```
>   - change: `the rows Vault, Hook, deferred_by and origin point at the page that defines each, their meanings cut to it; Entity / Rule (status) splits into Entity (status) and Rule (status) (case 520)`
> - [ ] `uv run guppi glossary`
> - [ ] read `estimate-glossary-terms-defined`

> **ratification:**
> ```
> - decision[case 520][update][entity-glossary]{ref:entity-glossary}
> ```
