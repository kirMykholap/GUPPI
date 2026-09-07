---
title: "Sorting reads the vacancy's objective dates, so «long open to me» and «long open on the exchange» have diverged"
type: decision
status: current
authority: list-ordering-source
binding: prohibition
basis: code
sprint: S0
decided: 2026-08-06
created: 2026-08-13
sources: ["archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md", "src/jobhunt/web/data/vacancies.py"]
tags: [filters, data]
---

# Sorting reads objective dates, not the pair's

The vacancy list orders by the **vacancy's** objective fields. `first_seen_at` and `last_seen_at`
on the profile↔vacancy pair are written and never read by the ordering.

So two different questions have quietly become one:

| Question | Answered by |
|---|---|
| how long has this been open on the exchange | the vacancy's dates — **this is what sorting uses** |
| how long have *I* been sitting on it | the pair's dates — **nothing reads them** |

**They have diverged, and sorting knows only the first one — the exchange's.** The order is
`Vacancy.posted_at DESC NULLS LAST, Vacancy.first_seen_at DESC, Vacancy.id`
(`src/jobhunt/web/data/vacancies.py`), and every key in it belongs to the vacancy. *Corrected
2026-08-13: this sentence said «only the second one», which contradicted the table directly above
it.* For a single profile the difference
is small; it is the same asymmetry that [[why-deactivation-is-profile-scoped]] resolves for
judgement, left unresolved for ordering.

Accepted rather than fixed: the fix is a sort key, and no ordering has yet been asked for that
needs it. Recorded so that "sort by how long I have had it" is understood as new work rather than
a bug in the existing sort. See [[vacancy-list-invariants]] for the rules the ordering does keep.
