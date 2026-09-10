---
type: decision
case: "38.2"
status: current
targets:
  - {kind: create, category: rules, slug: rule-retro-commit, ref: rule-end-of-work}
  - {kind: create, category: estimates, slug: estimate-retro-commit-gates, ref: rule-retro-commit}
  - {kind: update, category: rules, slug: rule-hook-registry}
origin: raw/2026-09-10/ledger.md#case-38.2
sprint: migration
created: 2026-09-10
tags: [session, workflow, hooks, harness, git, render]
---

## Context

Конец работы: Retro, коммит, handoff с вызовом librarian'а. Сейчас всё по памяти.

## Now

Инструкция «закоммить перед handoff» пропускается. Хук `PreToolUse` — нет.
**－** Если `/handoff` наберёт человек, хук молчит. Сам skill проверяет дерево.

## Problem

Retro без рамки. Коммит — инструкция, которую можно пропустить. Handoff без формы.

## Then

Инструмент `Skill` вызван со skill `handoff`.

`uv run guppi gate` читает `git status --porcelain`. Грязное дерево — exit 2 «commit first». Чистое — exit 0.
**＋** Другой skill или инструмент — exit 0.
**＋** `rule-hook-registry`: запись `PreToolUse`, matcher `Skill`.
**－** Хук ничего не пишет и не коммитит.

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-38.2
