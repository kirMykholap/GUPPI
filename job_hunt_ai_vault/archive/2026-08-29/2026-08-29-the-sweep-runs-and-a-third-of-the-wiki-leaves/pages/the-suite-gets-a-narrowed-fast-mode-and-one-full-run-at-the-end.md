---
title: "The suite gets a narrowed fast mode for the loop and one full run at the end, and the narrowing itself waits for a measurement"
type: decision
status: archived
authority: suite-narrowing-order
binding: deferral
basis: human
sprint: S3
decided: 2026-08-24
created: 2026-08-24
sources: ["archive/2026-08-24/2026-08-24-the-suite-learns-to-list-itself-and-every-proposal-names-its-cause/handoffs/2026-08-24-the-suite-learns-to-list-itself-and-every-proposal-names-its-cause.md", "scripts/vault-check-selftest.sh"]
tags: [testing, harness, vault]
---

# The ruling, 2026-08-24

> **owner:** «Берем пункт 1 и оставляем пункт 2 до получения измерений. Подписываюсь.»

> **owner:** «Мне нравится идея делать небольшой прогон для быстрой проверки, а уже в конце -
> запускать полный прогон. То есть если прогон ломает какое-то правило - проверяем его, копим такие
> прогоны и уже потом заупскаем один полный сквозной. Это хорошее решение, принимается.»

**Step one is taken and step two waits for a number.** The proposal it rules on is
[[the-suite-gets-a-scanner-exclusion-before-a-narrowed-gate]], whose order is: exclude the sandbox
from the scanner first, because that measurement says whether the redesign is worth doing; then
narrow the gate to one rule.

**Rejected: paying the incidental-coverage price permanently.** That price is what the proposal
itself names as the cost of its second step — running all twenty rules gives coverage nobody
designed and nobody watches, and narrowing removes it silently.

# The owner's own contribution is the shape that removes the objection

**A fast narrowed run inside the loop, and one full end-to-end run at the end.** The full run
restores what the narrowing loses, so the price becomes *you find out later* rather than *you never
find out*.

**The proposal page does not contemplate that answer.** It records the loss as a flat cost of
step two, with no recovery. That gap is written on the proposal itself and is the reason this
decision is not merely an approval of what was already designed.

# What the measurement since says about the ceiling

**Narrowing buys far less than the arithmetic suggests.** Measured 2026-08-24 on a quiet machine:
of a 15.3 s gate, rules 12 and 13 are the separable part and the gate's own passes over the corpus
are the rest, and rules 1 through 10 ride one shared pass that cannot be skipped one rule at a time
([[the-gate-is-a-shared-pass-over-the-corpus-plus-the-scripts-it-delegates-to]]).

**So the deferral is not merely caution.** The number that step two was to be justified by now
exists and points the other way.
