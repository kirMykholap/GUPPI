---
type: decision
case: "429"
status: current
update: ["[[rule-case-protocol]]", "[[entity-glossary]]", "[[estimate-materialize-marks-superseded]]", "[[estimate-case-protocol-ledger-line-form]]"]
origin: raw/2026-09-25/1654/ledger.md#case-429
sprint: migration
created: 2026-09-25
tags: [session, workflow, ledger, harness, librarian]
---

## Context

A decision deferred several times stands in the `deferred_by` of its page under each Case that deferred it. When the decision is taken up, the decision line carries `{supersedes:case N}`. `parse_line` in `guppi/materialize.py` parses a ledger line for all readers. It puts the marks in braces into a dictionary, and of two blocks with one key the last stays. So a line holds one `supersedes`, and `lift_line` marks `superseded_by` on the entries of one Case only. `decision_record` builds the list `supersedes` from the entries of a Case, and `generate` already walks that list. For each decision named it sets `superseded` and removes its slug from the `deferred_by` of the targets (`clear_deferred_by`). So the limit sits only in the parse of the line. The case of `rule-context-size` showed it: its Case has fewer decision lines than defers. A second `update` line of the same slug is no way out: it would apply the same `then` item twice.
The form of the mark. The grammar already knows a repeated block: `{addresses:<lesson slug>}` stands once per lesson, and `parse_line` collects it into a list (case 284.2). Several `{supersedes:case N}` blocks side by side fit the same grammar and the same `BRACES`. A list inside one block, `{supersedes:case 1,case 2}`, is read by today's parse without a word as one Case with the number `1,case 2`. The ledger hook writes the line verbatim and does not judge marks. By Case 428.1 it will read lines by `parse_line`, but only the kind and the slug. `casecheck` passes the parsed records whole to `judge` of `guppi/prespec.py`, and `judge` reads `supersedes` through `superseded_in_window`. Lint reads the field `supersedes` of a decision page, and that is already a list. All readers get the parse by import from one module, as `CLAUDE.md` asks. Before this session no decision line in a ledger under `vault/` carried two real marks. The only line with two blocks lies in the archive and holds `{supersedes:case N}` as text. In the ledger of this session the line of Case 430 already carries several blocks. Only `materialize` as this Case changes it reads that line right.
Where the form changes. The field `supersedes` of a yaml entry becomes a list, like `addresses`. In the yamls already written it is one value. `decision_record` rebuilds the decision record from all entries of the unit, so it reads the old form too. `superseded_in_window` today turns the value into a string. With a list it would give a junk key, so it walks each Case of the list. Through it `check_lines`, the demand for a `tasks` block, the comparison with the ratified copy and the check of an answer of `case-guppi` in `casecheck` get the same. The code of `generate` does not change: `decision-case-419.2` already shows it, with two `supersedes` from two lines.
What taking up a deferred decision retires. One short-form Case can defer several pages at once, as the archived `decision-case-416` did. `generate` removes the defer the line supersedes from the `deferred_by` of each target of its `defer` list, not only from the page taken up. The new rule asks to name each Case of the page's `deferred_by`. So taking up one page also retires the same defers from the other pages they hold. That will be so for `rule-work-mode` and `rule-subagent-guppi`, which share their defer Cases. That is existing behaviour of `generate`, and the Case does not change it. A page that stays open gets a new defer at the close of Plan Mode.
What the frame check showed. The Case creates no page, so no vault query is due. The Render of `rule-case-protocol` speaks of the mark in two places. On taking up a deferred decision it says "writing `{supersedes:case N}` on the line", and on the ledger line it says the mark stands "when they apply". Both places get a `replace` pair, and `vault/wiki/case-schema.md` is rendered again. The glossary line in `entity-glossary` speaks of one Case per mark. It gets a pair, and `vault/wiki/glossary.md` is rebuilt.
Two promises in one Case. The Criterion of `estimate-materialize-marks-superseded` speaks of a line with one mark. That is the promise of `materialize` the Case changes, so its Criterion is replaced by the `when` and `then` of the Case. The Criterion of `estimate-case-protocol-ledger-line-form` speaks of the form of a line as the agent writes it. Its "`{supersedes:case N}` when it applies" admits both a line with a list inside one block and a taken-up decision that names only part of its defers. The new rules of the Render are not checked by that Criterion. So its Criterion is also replaced whole, by the text the item writes under `sections`. So one Case touches two promises (case 204), and `judge` accepts that form. A split into sub-cases would need new numbers and `{supersedes:case 429}` on a ratified Case, and its heading would stay in the plan. The method of this Estimate also gets the first take-up of a decision with several Cases in its `deferred_by`. The readings of both Estimates wait for the next session (case 428.1).
Which Estimates do not change and why. The Criterion of `estimate-materialize-refolds-a-reading-on-a-supersede` speaks of a line with `{supersedes:case N}` and a `create` of Case N that holds `folded`. The edit runs `refold` for each block of the line on its own, so each of its statements stays true for each Case named, and its Criterion is not replaced. `estimate-prespec-catches-a-superseded-case`, `estimate-prespec-requires-a-task-line` and `estimate-prespec-checks-the-ratified-copy` speak of any mark of the window. `estimate-retro-runs-on-to-the-handoff` and the Renders of `rule-retro` and `rule-prespec` also speak of the Case the mark names. After the edit of `superseded_in_window` all of that stays true for each mark. `estimate-generate-writes-the-decision-page` speaks of each `supersedes` of a decision record, and `generate` does not change. `estimate-materialize-assembles` names the field `supersedes`, but not its form. The Case adds or changes no hook.

## Problem

One decision line can retire only one defer. So a decision deferred several times, once taken up, leaves the other Cases in `deferred_by` and their entries without `superseded_by`. The form of several marks on one line must be chosen, and `materialize` must mark each Case named.

## Given

`guppi/materialize.py` and `tests/test_materialize.py` — `parse_line`, the one parse of a ledger line; `lift_line`, `refold` and `decision_record`, the supersede mark; and their tests
**＋** `guppi/prespec.py` and `tests/test_prespec.py` — `superseded_in_window`, which `judge` and `guppi/casecheck.py` reach, and its tests
**＋** `estimate-materialize-marks-superseded` — the promise of the mark
**＋** `estimate-case-protocol-ledger-line-form` — the promise of the written form of a ledger line and its marks
**＋** `rule-case-protocol` and its render `vault/wiki/case-schema.md` — the form of a ledger line and the take-up of a deferred decision
**＋** `entity-glossary` and its render `vault/wiki/glossary.md` — the term `supersedes`
**＋** `CLAUDE.md` "One judgment, one implementation" — the parse of a ledger line lives in one module

## History

- 2026-09-25 created · raw/2026-09-25/1654/ledger.md#case-429
