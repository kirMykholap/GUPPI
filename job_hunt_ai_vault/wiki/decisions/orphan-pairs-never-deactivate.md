---
title: "An orphan pair is never deactivated, and it is hidden rather than lingering in the list"
type: decision
status: current
authority: orphan-deactivation
binding: prohibition
basis: code
sprint: S0
decided: 2026-08-06
created: 2026-08-13
sources: ["archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md"]
tags: [deactivation, tag-model, filters]
---

# An orphan pair is never deactivated — and is hidden, not lingering

A pair with no link to a tag that ran is not judged at all and stays active for ever. Pairs created
before tags existed behave the same way.

## It is hidden, not visible — the wording here was inverted for a whole slice

**The pair does not "hang in the general list": it is hidden.** The mechanism belongs to
[[tags-set-marker]]; the consequence for orphans is that only the «показать вакансии, у которых нет
тега фильтра» checkbox reaches them.

The formulation "they simply hang in the general list" stood here since an earlier slice and was
**exactly backwards**. The same line also called a pseudo-filter «Найденные ранее» unimplemented
when it in fact existed as the `include_untagged` checkbox — which slice 3 removed, handing its job
to `include_unchipped`. Corrected 2026-08-06 by the final review.

**Noticeable after the very first tag deletion** — which is itself blocked, see
[[no-soft-delete-for-tags]].

See [[deactivation-cycle]] for condition 2, which is what an orphan fails, and [[tags-set-marker]]
for why the default hides it.
