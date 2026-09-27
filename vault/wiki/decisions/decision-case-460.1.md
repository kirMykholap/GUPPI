---
type: decision
case: "460.1"
status: current
update: ["[[lesson-harness-senduserfile-renders-a-markdown-file-on-the-phone]]"]
origin: raw/2026-09-27/1819/ledger.md#case-460.1
sprint: migration
created: 2026-09-27
tags: []
---

## Context

A lesson reaches the vault straight from its ledger line. The ledger hook writes any `lesson[...]` line from a `LEDGER` block. `lesson_entry` in `guppi/materialize.py` sends the line to the lessons folder because it is a lesson record, not because of its slug. `generate` then writes the page under the slug as written. Lint checks that `type` matches the folder and that the `slug` matches the filename, but it never checks the prefix. So ledger line 54 of session 1255 put `lesson-harness-senduserfile-renders-a-markdown-file-on-the-phone` into the vault without its `lesson-` prefix, and nothing reported it. A Glob over the six category folders finds no other live page without its category prefix.
The prefix table is kept twice. `category_of` in `guppi/materialize.py` reads six prefixes, and `generate` imports that table. `guppi/lint.py` keeps its own copy of five prefixes, without `decision-`, for `check_decision` alone. So a `decision-` slug in a Decision list is a page for `materialize`, but lint does not look it up. `CLAUDE.md` calls a second copy of one judgment a defect. The deferred `decision-case-455` covers a different pair of functions.
The lesson is `new`, and no live page links to it. `brief.md` and `log.md` name it, but they are records. The rules of the lessons schema say a lesson goes through no Case. That covers its birth, not a later change: the one rule still requires a Case to rename a page. The old slug has no prefix, so `materialize` marks the entry of 460.1 `category: unknown` and `incomplete: [category]` (case 320). `generate` still applies it: `Vault.update` finds the page in any folder, and `rename` requires the new slug to open with `lesson-`. `apply` ticks the line of every applied entry, whatever its category. The docstring of `guppi/generate.py` says the opposite, so 460.1 corrects it.
`estimate-sprint-migration-file-route-gone` promises that a line with no prefix lands `category: unknown` and that `generate` "reports an error instead of 'applied by hand'". That line records the end of the file route. The code never failed an `update` or a `delete` of an unknown category (`test_a_delete_of_an_unknown_category_is_outside_the_vault`), and 460.1 relies on the `update` applying. The person chose to leave that Estimate as it is. The session 1255 entry is marked `applied`, so no rerun creates the old page again.
The refusal of 460.5 goes beside the refusal of case 428.1 in the same hook. The other `Stop` hooks, `guppi ratified`, `guppi casecheck` and `guppi context`, do not read the slug of a lesson line, and `.claude/settings.json` does not change. The Criterion of `estimate-ledger-write-lifts` promises that every `- lesson[` line lands. That becomes false, so 460.4 replaces it whole with an exception, as case 428.2 did for 428.1. `case-schema.md` makes no claim that every lesson line lands, so it stays as it is. `rule-ledger-write` carries `deferred_by` `decision-case-442`, which is about another gap of the same hook, and 460 leaves it open. 460.3 replaces the Criterion of `estimate-lint-finds-a-broken-link` whole: every old line is kept word for word, and only the `decision` line changes. Live Decision lists name four `decision-` slugs: `decision-case-130.1`, `decision-case-140` and `decision-case-347` are live, and `decision-case-130.2` is archived. So I expect no new finding, but I have not run `make lint`. `rule-vault-layout` and `estimate-vault-layout-holds` are not touched, because the lint layout option was not chosen. The one `create` carries `ref: rule-ledger-write`, so no vault query ran. A Glob found the new Estimate slug and the new lesson slug free.
460.5 supersedes 460.2 of the first ratification. The ledger is append-only and still holds the three lines of 460.2, among them an update of `estimate-ledger-write-lifts`, which is now the work of 460.4. The text of the refusal is unchanged. 460.2 leaves the Spec (case 299.1), and its entries are marked superseded.
In the rounds, the person chose these answers: the rename, a check in the ledger hook, and one table of prefixes; the prefix is added and nothing else changes; a new Estimate for the refusal, with the Criterion of `estimate-ledger-write-lifts` replaced in a sub-case of its own; lesson lines only, with the exceptions of case 428.1; the migration Estimate left as it is; the docstring of `generate` corrected.

## Problem

One lesson page has no `lesson-` prefix, and nothing on the path from the ledger line to the page checks the prefix of a lesson slug. The table that judges a prefix also lives in two modules that already disagree on `decision-`.

## Given

`lesson-harness-senduserfile-renders-a-markdown-file-on-the-phone` — the lesson page that is renamed
**＋** `lesson-harness-senduserfile-renders-a-markdown-file-on-the-phone` — the slug the page takes
**＋** `guppi/generate.py` — applies the `update` and its `rename`, and ticks the line of an applied entry
**＋** `guppi/materialize.py` — lifts the decision line into an entry
**＋** `rule-lessons-schema` — the slug of a lesson: `lesson-`, then the area, then the cause
**＋** `rule-vault-layout` — the filename is the slug
**＋** `vault/wiki/brief.md` — a record that names the old slug
**＋** `vault/wiki/log.md` — a record that names the old slug

## History

- 2026-09-27 created · raw/2026-09-27/1819/ledger.md#case-460.1
