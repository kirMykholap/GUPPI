---
type: decision
case: "464"
status: current
update: ["[[estimate-sprint-migration-file-route-gone]]"]
origin: raw/2026-09-27/2050/ledger.md#case-464
sprint: migration
created: 2026-09-27
tags: [sprint, workflow, harness]
---

## Context

`materialize` gives `category: unknown` to the entry of a ledger line whose slug has no category prefix (case 320). `generate` then treats that entry in one of four ways, by its kind. A `create` fails with `category 'unknown' is not a vault folder`. A `defer` with no page fails the same way. An `update` applies to the page of that slug, in whatever folder it is in. A `delete` prints `outside the vault, nothing to archive`, applies and ticks its line (case 48). Case 460.1 relied on the `update` road: it renamed `harness-senduserfile-renders-a-markdown-file-on-the-phone`, and that entry was `category: unknown`.
The Criterion of `estimate-sprint-migration-file-route-gone` (status `passed`, from case 320) says the entry "lands `category: unknown`, and `generate` reports an error instead of 'applied by hand'". That is true for a `create` and a page-less `defer`. It is false for an `update` and a `delete`. The docstring of `guppi/generate.py` already describes both roads that apply (cases 460.1, 463). In session 1819 the person left the Estimate as it stood (Q7), and the brief flagged the contradiction again.
The Criterion also keeps the old shape: a `Given:` block, and a `－` line that only bounds the edit ("`rule-morph` is untouched"). Its `method` still reads "at the close of theme 5", and theme 5 is closed. `tests/test_generate.py` covers the unknown-category `delete` (`test_a_delete_outside_the_vault_applies_and_a_delete_of_a_missing_page_fails`, `test_a_delete_of_an_unknown_category_is_outside_the_vault`). No test covers the `update`, the `create` or the page-less `defer` of that category.
The item is an `update` of an existing page, so no vault query ran. In the frame: the `purpose` of the Estimate and the Purpose of `entity-sprint-migration` stay true. No sentence of `rule-page-generation` speaks of an unknown category outside its History. Of the Estimates of `rule-page-generation`, `estimate-generate-fails-alone` names only failures in general, and the unknown `create` failing agrees with it. `estimate-generate-renames` speaks of the page's own category prefix, which a page found in its folder has. Neither speaks of the unknown category, so both stand. The code does not change.
In the rounds, the person chose these answers: replace the Criterion so that it describes the code; write it in the current model, with no `Given:`, the input in `When:` and the `rule-morph` line dropped; state all four roads; add tests for the untested roads and set a `method` without theme 5.

## Problem

A `passed` Estimate promises that `generate` reports an error for every entry of unknown category. The code applies the `update` and the `delete` of such an entry, and a ratified Case depends on the `update` applying. The promise and the behaviour disagree, and no test holds three of the four roads.

## Given

`estimate-sprint-migration-file-route-gone` — the promise that the file route is gone
**＋** `guppi/` — the scripts the file route left
**＋** `guppi/generate.py` — applies or fails the entry of each kind, and ticks the line of an applied entry
**＋** `guppi/materialize.py` — `category_of` gives the entry of a slug with no prefix `category: unknown`
**＋** `guppi/prespec.py` — `check_governed` refuses an `update` item that carries `file`
**＋** `tests/test_generate.py` — the tests of the unknown-category roads
**＋** `vault/wiki/sprint.md` — shows the status of the Estimate

## History

- 2026-09-27 created · raw/2026-09-27/2050/ledger.md#case-464
