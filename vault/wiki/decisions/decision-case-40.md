---
type: decision
case: "40"
status: current
update: [index, glossary, decisions-schema, entities-schema, rules-schema, estimate-plan-mode-verified, rule-retro]
supersedes: [decision-case-38.1]
origin: raw/2026-09-10/ledger.md#case-40
sprint: migration
created: 2026-09-10
tags: [session, workflow, harness, render]
---

## Context

Cases 31.1, 32, 33, 34 поменяли модель в четырёх местах. Несколько документов говорят по-старому.

## Problem

Следующая сессия увидит две модели.

## Given

§2 «Six sections», §3 «Put the result in `now`», `estimate-plan-mode-verified` «in the Case's `now`».
**＋** §5 и `decisions/schema.md` «never inferred from a slug prefix». §5, §11, glossary, `entities/schema.md`: страница на решение, meaningful slug.
**＋** §8 «archived immediately». `rules/schema.md`: «its children use `partial`».
**＋** §9 «Retro → commit → handoff».

## When

Агент читает эти файлы в следующей сессии.

## Note

The `then` of the Case, as ratified:

§2, §3: семь секций, результат pre-task в `given`. `estimate-plan-mode-verified`: «in the Case's `given`».
**＋** §5, `decisions/schema.md`: категория явная на странице, скрипт выводит её из префикса, который проверяет pre-task.
**＋** §5, §11, glossary, `entities/schema.md`: одна Decision-страница на Case, `decision-case-<N>`.
**＋** §8, glossary: Estimate error-урока `passed`, не `archived`.
**＋** `rules/schema.md`: ребёнок render-MOC без Render — шаг, который рамка вызывает по имени.
**＋** `rule-retro`: коммит по одобрению, потом `/handoff`.
**－** Смысл решений не меняется.

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-40
- 2026-09-11 migrated: targets to kind and target_slug, Now to Given, Then to When · [[decision-case-52.1]]
- 2026-09-12 fields kind and target_slug folded into create, update, delete, defer · [[decision-case-59.4]]
