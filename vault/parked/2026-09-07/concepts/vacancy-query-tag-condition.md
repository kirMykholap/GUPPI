---
title: "In build_vacancy_query the tag condition is the terminal step, and anything added after it is unreachable"
type: concept
status: current
authority: tag-condition-placement
basis: code
sprint: S0
created: 2026-08-13
sources: ["CLAUDE.md"]
tags: [filters, tag-model]
---

# The tag condition is applied once, at the end

In `build_vacancy_query` the tag condition is applied **once, at the end**, and that application is
the function's **terminal step**. The block that builds `chosen_link`, `enabled_link` and
`any_link` ends in

```python
if filters.include_unchipped:
    return query.where(or_(chips, ~any_link))
return query.where(chips)
```

**Every other condition must be added before that block.**

- Appended at the bottom of the function, a condition is unreachable.
- Written between the two `return`s, it is silently skipped the moment the user ticks
  «показать вакансии, у которых нет тега фильтра».

## This is the old defect moved, not its absence

An earlier version returned from inside the chip branch, and a *selected chip* cancelled whatever
followed. Today the same trap belongs to `include_unchipped` — twelve lines further down. The
shape survived; only the trigger moved.

See [[tags-set-marker]] for the other half of the chip model, and [[vacancy-list-invariants]] for
the rest of the list's rules.
