---
type: decision
case: "55.2"
status: current
update: ["[[rule-ledger-write]]", "[[estimate-ledger-write-lifts]]"]
origin: raw/2026-09-11/ledger.md#case-55.2
sprint: migration
created: 2026-09-11
tags: [session, hooks, harness, ledger]
---

## Context

Хук ledger дважды терял ратифицированные строки. Вчера: реплики Cases 48 и 49 кончались `/pre-task` и `ExitPlanMode`, `Stop` не сработал (Case 51, отложен). Сегодня: сессия перешла полночь, хук искал `session-start` и `hi` в сегодняшнем логе; 44 строки Case 53 ушли только после resume.

## Problem

Окно `hi` привязано к файлу одного дня; хук привязан к одному событию, которого у части реплик нет.

## Given

`ledger.py`: `log_path(project_dir, now)` — только `raw/<today>/event_log.md`; `hi_recorded` требует `session-start` своей сессии до `hi` в одном тексте. `reply_text` берёт `last_assistant_message` из payload `Stop`; payload несёт и `transcript_path` (`lesson-hooks-stop-payload`).
**＋** `existing_bodies` не пишет строку, чей текст уже в ledger.
**＋** `rule-ledger-write` `built`, `estimate-ledger-write-lifts` `passed`; по 53.2 критерий правится, `pending`. `deferred_by` Case 51 снимается `{supersedes:case 51}`.
**＋** Уроки: `lesson-ledger-hook-misses-a-reply-ending-in-a-tool-call`, `lesson-ledger-hook-hi-lost-at-midnight`.
**－** Формат строки, тег `LEDGER`, отказ без `hi`, `settings.json` — без изменений.

## When

Хук `Stop` срабатывает.

## History

- 2026-09-11 created · raw/2026-09-11/ledger.md#case-55.2
- 2026-09-12 Given inherited from the parent Case · [[decision-case-60]]
- 2026-09-12 fields kind and target_slug folded into create, update, delete, defer · [[decision-case-59.4]]
