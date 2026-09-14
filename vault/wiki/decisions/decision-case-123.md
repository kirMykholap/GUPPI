---
type: decision
case: "123"
status: current
update: [rule-claude-md, case-schema]
origin: raw/2026-09-14/1029/ledger.md#case-123
sprint: migration
created: 2026-09-14
tags: [harness, render]
---

## Context

`## Language` of `CLAUDE.md` (the Render of `rule-claude-md`, lines 71–75) says: English for everything written into the repository; Russian for chat with the owner "and for the plan he reads in order to approve it". `case-schema.md` `## Language` says: Russian in the chat with the owner, English in everything that lands in the vault. In session M Case 115 was discussed in the chat in English and the Spec was written in English. Today Case 122 went the same way.

## Problem

The rule does not say in which language a Case is discussed in the chat. The agent reads "the plan in Russian" as leave to write the Case in English, because the Case is the plan to come. The Spec is English in practice, and that is right: it lands in `raw/` and in the vault.

## Given

`rule-claude-md` (`MOC`, `built`, `render_mode: full`, `governs: CLAUDE.md`, `estimate-claude-md-rendered` `passed`): the `## Language` section is three sentences inside the Render markers, so the change is a `replace` of the three (a `sections` entry would add a second `## Language` outside the Render — pre-task finding 1 of case 132), and `guppi render` carries it into `CLAUDE.md`.
**＋** `case-schema.md` is a Rule-class file: an `update` with `file` and `change`, applied by hand in Work Mode; its `## Language` (line 29) is one sentence.
**＋** `rule-case-protocol` is not touched: the form of a Case does not change, only its language.
**＋** The Spec of session M (`raw/2026-09-14/0747/spec.md`) is already English; the practice of the Spec does not change.
**－** Ledger lines, slugs, field and section names (`context`, `given`, `then`), paths and quotations from pages stay English in either language.
**－** The Frontier line F13 closes on this Case.

## History

- 2026-09-14 created · raw/2026-09-14/1029/ledger.md#case-123
