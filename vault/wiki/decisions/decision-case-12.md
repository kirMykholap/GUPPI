---
type: decision
case: "12"
status: current
create: ["[[rule-session-start]]", "[[estimate-session-start-context]]"]
origin: raw/2026-09-09/ledger.md#case-12
sprint: migration
created: 2026-09-09
tags: [session, workflow, hooks]
---

## When

**context.** Родитель трёх механизмов, ратифицированных в Case 9–11. Rule MOC: порядок
детей — содержание. Не рендерится (это не файл harness'а, а описание фазы), поэтому
`enforcement` нет; сила — в детях.

**now.** Черновик `docs/migration/rule-session-start.md` целиком, с `TBD` в `origin`,
`sprint`, `created`. Его секция `## The Frontier` не входит в список секций
`rules/schema.yaml` — переносится в `## How it works`. Родителя у MOC фазы нет (верхний
уровень). `estimates: [estimate-session-start-context]` — уже назван черновиком.

**problem.** Только сквозная проверка: что именно измеряет Estimate MOC, чего не
измеряют Estimates детей. Дети проверяют, что каждый механизм работает; MOC — что
различение «обычная / рабочая сессия» держится насквозь.

**recommend.** Страница — черновик с реальными значениями, Frontier внутри
`## How it works`. Estimate — два показания, два запуска: обычная сессия (без `/hi`), в
которой агент пишет голую `- decision[...]`-строку → строка не попадает в `ledger.md`, и
человек видит в ответе причину; рабочая сессия (после `/hi`) с той же строкой → строка в
`ledger.md`. Метод ручной, оба показания в строку `estimate[...]`.

**then.**

```
slug: rule-session-start
type: rule
kind: MOC
purpose: Prevents a working session from starting against unknown state
children: [rule-skill-hi, rule-event-log, rule-ledger-write]   # порядок — содержание
sprint: migration
tags: [session, workflow, hooks]       # workflow — новый тег
body: черновик docs/migration/rule-session-start.md, секции Purpose / How it works
      (включая The Frontier) / Children / Estimates / History
estimate:
  slug: estimate-session-start-context
  kind: QA
  criterion: >
    In a session opened without /hi, a bare `- decision[...]` line in a reply does not
    reach raw/<date>/ledger.md and the reply the person sees names the cause. In a session
    opened with /hi, the same line does reach it. Both readings taken end-to-end.
  method: two session starts, by hand, one reading each, recorded in the estimate line
```

Файлы: `vault/wiki/rules/rule-session-start.md`,
`vault/wiki/estimates/estimate-session-start-context.md`. Черновик в `docs/migration/`
остаётся до Slice 5 (spec C6).

Ledger:
```
- decision[case 12][create][rule-session-start]
- decision[case 12][create][estimate-session-start-context]{ref:rule-session-start}
```

**ratification.** Ратифицирован владельцем 2026-09-09, как предложено.

---

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-12
- 2026-09-11 migrated: targets to kind and target_slug, Now to Given, Then to When · [[decision-case-52.1]]
- 2026-09-12 fields kind and target_slug folded into create, update, delete, defer · [[decision-case-59.4]]
