## Case 680 — Old notes leave the Backlog of the migration sprint

> **context:**
> The `## Backlog` of `entity-sprint-migration` holds five plain notes from September that no Case took up: the product model (session 1119), the three notes on reuse — the edge, the question and the hook (cases 305, 319) — and a template engine for the rendered files (case 301). `guppi backlog` copies each line of that section into `## Deferred` of `vault/wiki/backlog.md`, which every session loads, and it keeps the Backlog of a closed sprint there too (case 628.12), so the notes would stay on that list after the sprint closes. While the backlog was reviewed, the main agent proposed to remove them, and the person agreed. If the product direction is ever taken up, it starts again from `entity-guppi`, which case 616 deferred. The line of `[[rule-subagent-guppi]]` in the same section also leaves. Case 676 of this session deletes that page and does not change this page. The person agreed that this Case removes the line, so that no live page links to the deleted page. The other lines of the section stay: `rule-work-mode`, `rule-spec-box`, `rule-morph` and the merge of `migration` into `main`.
> The vault's answer: the Case creates no page, so no vault query on a `create` ran. The Frontier line C9 has the source `backlog` and names the page, and the page carries `deferred_by` the Decision of case 642, which deferred the close of migration as a session of its own. The check of this file sends back a Case that changes such a page without `{supersedes:case 642}`. The person chose to retire that defer in this Case. The close does not drop out of sight: it stays the milestone line under Slice 5 of the page, which `sprint.md` shows.
> The frame. A Grep `template engine|reuse, the|product model` over `vault/wiki/` printed 3 files: `vault/wiki/backlog.md`, `vault/wiki/log.md` and `vault/wiki/entities/entity-sprint-migration.md`. The librarian writes `backlog.md` from the pages, and `log.md` is history; they stand. The same Grep over `{guppi/**,tests/**,.claude/**}` printed nothing. The Result of `estimate-backlog-renders` counts the five plain lines as of its reading of 2026-09-30. It records a past reading, and it stands. `estimate-backlog-renders` checks this Case: its Criterion says `## Deferred` lists each line of the `## Backlog` of each sprint page and each live page with `deferred_by`. Once the lines and the defer are gone, neither is listed, so the Criterion stays true and stands. `guppi backlog --check` in `make lint` reports a `backlog.md` that differs from its sources. A Grep `Backlog` over `vault/wiki/estimates/estimate-sprint-migration-*.md` printed 2 files: `estimate-sprint-migration-merges.md` and `estimate-sprint-migration-lint-clean.md`. The hits in `estimate-sprint-migration-lint-clean` are History lines, so they stand. The Criterion of `estimate-sprint-migration-merges` says that the merge of `migration` into `main` is a line of the `## Backlog` of `entity-sprint-migration`. This Case keeps that line, so the Criterion stays true and stands.

> **problem:**
> Notes that no Case took up hold places in the backlog that every session loads, and they would stay there after the sprint closes. The line of a page that Case 676 deletes would leave a link to a deleted page.

> **recommend:**
> - **What happens to the postponed close of the sprint**
>   - Recommended: (a) retire the postponement in this Case; the close stays in view as the Slice 5 milestone in `sprint.md`.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: the person agreed with the main agent's recommendation on Case 676 that this Case also removes the line of `[[rule-subagent-guppi]]` from `## Backlog`.
>   - Taken: a second `replace` pair removes that line.
> - **Change**
>   - Asked: the person agreed to the fix of a pre-spec finding: `context` must name `estimate-sprint-migration-merges`, whose Criterion speaks of a line of the `## Backlog`, and say why it stands.
>   - Taken: `context` names that Estimate and the search behind it; the Criterion stands because the merge line stays.

> **given:**
> `entity-sprint-migration`: the sprint page whose `## Backlog` loses the lines and whose defer is retired.
> **＋** `rule-page-generation`: the rule of `guppi generate`, which applies the update and retires the defer.
> **＋** `vault/wiki/backlog.md`: the backlog that lists each line of the sprint page's `## Backlog` and each page with `deferred_by`.
> **＋** `vault/raw/2026-10-05/2249/cases/case-676.md`: the Case that deletes `rule-subagent-guppi` and leaves its line to this Case.

> **when:**
> `guppi generate` of `rule-page-generation` applies the decisions of this Case, and `guppi backlog` writes `vault/wiki/backlog.md`.

> **then:**
> The `## Backlog` of `entity-sprint-migration` no longer holds the product model, the three notes on reuse, the template engine or the line of `rule-subagent-guppi`.
> **＋** `vault/wiki/backlog.md` no longer lists those notes under `## Deferred`.
> **＋** `entity-sprint-migration` no longer carries the defer of the close of migration, and `vault/wiki/backlog.md` no longer lists the page under `## Deferred`.
> **－** The other lines of the `## Backlog` of `entity-sprint-migration` stay, and its milestone of the close of migration does not change.

> **tasks:**
> - [ ] update `entity-sprint-migration`
>   - old:
>     ```
>     - the product model: `kind: test | measurement | reading`, `ask-guppi` through Entities, the vault-query questions before a product's records (session 1119); `applies_to` and `rules` taken into Slice 3f (case 301)
>     - reuse, the edge: `uses` / `used_by` between Entities — `uses` written in the Case on the side that uses, `used_by` computed by the cascade of `generate`, the pair checked by lint, the pattern of `applies_to` / `rules`; no edge Rule → Rule (cases 305, 319)
>     - reuse, the question: the vault query before a `create` asks a second question — what of the existing this thing could use, by the index lines of the Entities — and the answer stands in `context`; the Case names what it found in `uses` or says why it is not used (case 319)
>     - reuse, the hook: a lint finding on two live Entities naming one path in `code_ref` with no edge between them; a new module written beside an existing one in another file is caught by the question alone, not by a script (case 319)
>     - a template engine for the rendered files — one script with the shape of each file declared, once a third render beside `sprint.md` and `glossary.md` appears (case 301)
>     - [[rule-work-mode]]
>     ```
>   - new: `- [[rule-work-mode]]`
>   - old:
>     ```
>     - [[rule-subagent-guppi]] — what a subagent may do in Work Mode, and the fork that comes back to the main agent as a Case; cases 183, 206
>     - [[rule-spec-box]]
>     ```
>   - new: `- [[rule-spec-box]]`
>   - change: `the five plain notes of the Backlog — the product model, reuse three times, the template engine — and the line of rule-subagent-guppi leave; the defer of the close of migration is retired, and the close stays the milestone of Slice 5`

> **ratification:**
> ```
> - decision[case 680][update][entity-sprint-migration]{ref:entity-sprint-migration}{supersedes:case 642}
> ```
