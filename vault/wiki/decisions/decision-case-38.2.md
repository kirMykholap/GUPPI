---
type: decision
case: "38.2"
status: current
create: [rule-retro-commit, estimate-retro-commit-gates]
update: [rule-hook-registry]
origin: raw/2026-09-10/ledger.md#case-38.2
sprint: migration
created: 2026-09-10
tags: [session, workflow, hooks, harness, git, render]
---

## Context

Конец работы: Retro, коммит, handoff с вызовом librarian'а. Сейчас всё по памяти.

## Problem

Retro без рамки. Коммит — инструкция, которую можно пропустить. Handoff без формы.

## Given

Инструкция «закоммить перед handoff» пропускается. Хук `PreToolUse` — нет.
**－** Если `/handoff` наберёт человек, хук молчит. Сам skill проверяет дерево.

## When

Инструмент `Skill` вызван со skill `handoff`.

## Note

The `then` of the Case, as ratified:

`uv run guppi gate` читает `git status --porcelain`. Грязное дерево — exit 2 «commit first». Чистое — exit 0.
**＋** Другой skill или инструмент — exit 0.
**＋** `rule-hook-registry`: запись `PreToolUse`, matcher `Skill`.
**－** Хук ничего не пишет и не коммитит.

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-38.2
- 2026-09-11 migrated: targets to kind and target_slug, Now to Given, Then to When · [[decision-case-52.1]]
- 2026-09-12 fields kind and target_slug folded into create, update, delete, defer · [[decision-case-59.4]]
