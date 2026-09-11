---
type: decision
case: "57"
status: current
kind: [update, update, update, update, update, update, update]
target_slug: [index, claude-md, rule-cleanup, estimate-cleanup-moves, rule-spec-capture, estimate-spec-capture-appends, estimate-lint-catches]
origin: raw/2026-09-11/ledger.md#case-57
sprint: migration
created: 2026-09-11
tags: [harness, workflow, session, hooks]
---

## Context

Cases 52–56 меняют форму Decision, число индексов, чтения библиотекаря, форму Retro и `spec.md`. Pre-task (`ask-guppi`, 2026-09-11) нашёл страницы, которые описывают то же и не названы ни в одной строке.

## Problem

§5 и §10 `index.md` описывают старую форму; `CLAUDE.md` требует семь секций для любого ответа; `rule-cleanup` перестраивает пять индексов; `rule-spec-capture` считает хук единственным писателем `spec.md`; критерии `estimate-lint-catches` и `estimate-cleanup-moves` не знают новых классов и четырёх файлов.

## Given

`index.md` §5 строки 211, 225 (`targets`, `category` explicitly); §10 строка 333 («That is all … not the pages themselves»). `CLAUDE.md` строка 46: «One reply is one Case, in the seven sections». `rule-cleanup`: пять индексов, `estimates` всех живых страниц. `rule-spec-capture`: один писатель. `estimate-lint-catches`, `estimate-cleanup-moves`, `estimate-spec-capture-appends` — `passed`, по 53.2 `pending`.
**－** Ворота «Research `passed` до Insight» уходят без замены (53.1).

## When

Кто-то читает `index.md`, `CLAUDE.md`, `rule-cleanup`, `rule-spec-capture`; `guppi cleanup` и `guppi lint` идут; снимаются их чтения.

## History

- 2026-09-11 created · raw/2026-09-11/ledger.md#case-57
