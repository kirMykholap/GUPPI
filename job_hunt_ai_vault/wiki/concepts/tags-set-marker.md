---
title: "tags_set separates «every chip cleared» from «the page was just opened»"
type: concept
status: current
authority: cleared-chips-vs-fresh-page
basis: code
sprint: S0
created: 2026-08-13
sources: ["CLAUDE.md", "archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md"]
tags: [filters, tag-model]
---

# `tags_set` separates a cleared set from an absent one

A form submits only its checked boxes, so "the user cleared every chip" and "the user has just
opened the page" both arrive as a request with **no `tag` values at all** — and they must mean
opposite things.

- **With the marker** the chosen set is authoritative, empty included: no chip means no rows.
- **Without it** the chips inherit `ProfileTag.is_enabled`.

The marker is rendered only when at least one chip exists: a row that never offered a chip cannot
have had one cleared.

## Consequences worth knowing

A pair with no tag link is an orphan and is hidden by default — because without the marker
`build_vacancy_query` applies `enabled_link`, and an orphan has no links at all. The only way to
see one is the «показать вакансии, у которых нет тега фильтра» checkbox
(`include_unchipped`). See [[orphan-pairs-never-deactivate]].

Test fixtures must attach an enabled tag, or a test will see an empty table for the wrong reason.

See [[vacancy-query-tag-condition]] for where in the query this lands, and
[[collection-end-resets-the-chips]] for what the marker cannot rescue.
