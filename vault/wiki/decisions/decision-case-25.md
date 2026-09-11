---
type: decision
case: "25"
status: current
kind: [update]
target_slug: [glossary]
origin: raw/2026-09-09/ledger.md#case-25
sprint: migration
created: 2026-09-09
tags: []
---

## When

```
update:
  slug: glossary
  file: vault/wiki/glossary.md
  shape: per section one table — term | meaning (≤ 100 chars, no argument) | where
  rule: no fact is dropped — a fact with no home in `where` stays in `meaning` or becomes a lesson[knowledge] line
  size: ≤ 8 000 chars
  sections kept: all nine, Retired terms included
```

Переписанный файл — Приложение A: измерено 8 002 знака, 1 319 слов, около 1 750 токенов
против 6 300 сегодня. Два факта из старого глоссария, у которых нет дома,
уходят в ledger строками `lesson[knowledge]` в ответе, где ложится файл:

```
- lesson[knowledge][lesson-hooks-sessionstart-cannot-block] trigger: the old glossary's Hook entry, carried since the earlier harness root_cause: `SessionStart` cannot block — exit 2 is a no-op there — so gating belongs on `PreToolUse`
- lesson[knowledge][lesson-hooks-messagedisplay-cannot-block] trigger: the old glossary's Hook entry, measured 2026-08-29 root_cause: `MessageDisplay` can neither block nor add context, which is why the ledger writer lives on `Stop`
```

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-25
- 2026-09-11 migrated: targets to kind and target_slug, Now to Given, Then to When · [[decision-case-52.1]]
