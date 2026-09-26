---
type: decision
case: "436.4"
status: current
update: ["[[rule-case-check]]", "[[estimate-case-check-sends-back-a-faulty-case]]"]
origin: raw/2026-09-26/1337/ledger.md#case-436.4
sprint: migration
created: 2026-09-26
tags: [hooks, harness, workflow, session]
---

## Context

The Spec hook `rule-spec-write` reads the sub-points of a `tasks` line and puts them into an item of the `then` block. The function `put` in `guppi/ratified.py` knows `old`, `new`, `reword old`, `reword new`, `set` and `sections.<Name>`. It puts any other key into the item as it is, whatever the kind of the item. In Case 434 the sub-points `replace old:` and `replace new:` stood under `update rule-case-check`. The hook wrote into the plan an item with the keys `replace old` and `replace new`, not a list of `replace` pairs. `generate` will not apply such an item. Nothing refused it. `guppi casecheck --subagent` did not: it builds the Spec section with the same `ratified.case_section`. The write of `guppi ratified` and the check after it did not: `judge` in `guppi/prespec.py` does not compare the keys of an item for any kind. The hook writes a deferred Case in the short form from its fence `then`. There it checks only that `slug`, `type` and `purpose` are present, and it lets other keys pass.

The judgment exists, but only in `materialize`, and in parts. `_lift_item` in `guppi/materialize.py` lifts the keys `set`, `sections`, `replace`, `change`, `rename` and, apart, `reword` of an `update`, and `impact` and `change` of a `delete`. It drops the other keys of these kinds without a word. For a `create` and a `defer` it reads the fields of the category from its `schema.yaml` with the function `schema_fields`. It marks `unknown` what is neither a field of the schema nor an own key of the item. The own keys are `slug`, `ref`, `sections`, `file`, `estimate`, `parent_create`, `parent_tags`, and for a `defer` also `type` and `purpose`. The old keys of a `create` of a rule or an entity, `method`, `contract`, `estimate_slug` and `estimate_kind`, it lets pass without a word. A category whose schema a decision of the same unit changes is not judged at all (`schema_changed`, case 308.2). The method `update` in `guppi/generate.py` holds its own copy of the keys of an `update`. One function can answer whether an item of a kind has a key, for all four kinds. For an `update` and a `delete` it takes a closed list. For a `create` and a `defer` it takes the fields of the category's schema and the own keys. Where there is no judgment, it answers "not judged": for a category with no schema file and for a category whose schema a decision of the session changes. This answer is the same as how `materialize` lifts the items today. So `estimate-materialize-lifts-a-create-by-the-schema` stays true and is not touched. The Estimates of `generate` are not touched either.

Today `materialize` lifts the schema fields of a `defer` into the placeholder page, and `generate` writes them. To narrow the keys of a `defer` to `slug`, `type` and `purpose` would change that behaviour, so this Case does not narrow them.

The Case touches three promises, so it splits into sub-cases: the reading of the chat form by the Spec hook (`estimate-spec-write-copies-the-ratified-case`), the finding of pre-spec (`estimate-prespec-checks-the-form-of-an-item`) and the write of a deferred Case (`estimate-spec-write-writes-a-defer`). `casecheck --subagent` gets the refusal through `case_section` and the finding through `judge`. It needs one change: it gives `judge` the schemas the session changes, taken from the lines of the session's window. The lines of its fence `ratification` still stand for the ledger. The Criteria of `estimate-case-check-sends-back-a-faulty-case` and `estimate-spec-write-checks-the-written-case` speak of running `judge`, not of the keys, and do not change. The page `rule-case-protocol` (`case-schema.md`) already says that a Case off the form is not written. The change makes that true, and the page does not change. An `update` item with `file` gets two findings: the new one and the one of case 320.

On `Stop`, `guppi ledger`, `guppi casecheck` and `guppi context` run beside `guppi ratified`. The ledger hook writes the decision lines also when `ratified` refuses (case 414.2). So the line stays without an item, and pre-spec names it — the same as at any refusal of the reading today. No vault query is needed: the Case creates nothing.

What followed: after this Case was ratified, the ratified Case 434 changed. Its sub-points became `old:` and `new:` in place of `replace old:` and `replace new:`; its own case-guppi showed it again, and it was ratified again. That change is not part of this Case.

## Problem

Only `materialize` knows which keys an item of each kind accepts, and it knows them in parts. `generate` holds its own copy. The Spec hook and the checks of pre-spec do not know these keys at all. So an item with a foreign key of any kind passes all the checks, and later it is dropped or not applied without a word. The decision is where the one judgment lives and who refuses by it.

## Given

`rule-case-check` — the rule of the check and the comparison; its How it works names what stands for the ledger
**＋** `estimate-case-check-sends-back-a-faulty-case` — the promise of the check on `SubagentStop`
**＋** `guppi/casecheck.py` — the hook module; `subagent` runs `judge`
**＋** `guppi/materialize.py` — `schema_changed`, the categories whose schema rule the session changes
**＋** `guppi/ratified.py` — the reading of the chat form, used as it stands
**＋** `guppi/prespec.py` — `judge`, which takes the categories not judged by their keys
**＋** `tests/test_casecheck.py` — the tests of the hook
**＋** `rule-one-judgment-one-implementation` — one judgment of the categories not judged, imported

## History

- 2026-09-26 created · raw/2026-09-26/1337/ledger.md#case-436.4
