---
title: "The rule-usage axis for `/vault-lint` is recorded and explicitly not built"
type: decision
status: archived
authority: rule-usage-axis-deferral
binding: deferral
basis: human
sprint: S2
decided: 2026-08-20
created: 2026-08-24
sources: ["archive/2026-08-20/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact/handoffs/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact.md", "archive/2026-08-24/2026-08-24-the-suite-learns-to-list-itself-and-every-proposal-names-its-cause/handoffs/2026-08-24-the-suite-learns-to-list-itself-and-every-proposal-names-its-cause.md"]
tags: [vault, process, harness]
---

# The ruling, 2026-08-20

> **owner:** у нас есть процесс lint... будет хорошим решением после ingest запускать еще и lint,
> который будет "смотреть lessons", "мерять как часто вызываются или пропускаются правила(для этого
> нужен счетчик) и формировать предложение добавить/убрать". Это предложение сейчас не делаем, но я
> хочу его рассмотреть на следующей сессии.

**The last sentence is the decision**: not now, and on the next session's list. Everything before it
is the design, and it lives on [[a-rule-usage-axis-for-vault-lint]].

**Rejected: building the counter that day.** The session had a working counter for one rule — the
`/pre-task` ledger — and generalising it is a different task from the one in front of it.

# What the deferral costs

**No instrument in this project answers which rules are earning their place.** `/vault-lint` is
entirely about the corpus's internal consistency and says nothing about rules.

# One half of the proposal was answered separately, and the other was not

**The cadence half — run `--lint` after every ingest — was decided on 2026-08-21**
([[the-tag-density-advisories-run-at-every-ingest]]). **The rule-usage half is still deferred**, and
it is the half this page is about.
