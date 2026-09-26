---
type: decision
case: "440.3"
status: current
update: ["[[rule-case-protocol]]"]
origin: raw/2026-09-26/1745/ledger.md#case-440.3
sprint: migration
created: 2026-09-26
tags: [session, workflow, ledger]
---

## Context

Case 72 brought in the key `contract: same|changed`. On the flag `changed`, the script `materialize` found the Estimate of the rule by itself. It appended a `### case N` block to its Criterion and set it `pending`. `estimate_slug` corrected the slug of the Estimate the script derived, when it matched a live page. `estimate_kind` gave the derived Estimate its `kind`. `method` on a `create` of a Leaf rule was the signal to derive an Estimate. Case 189 removed all derivation: an Estimate has its own line and its own item, and its Criterion is the `when` and `then` of the Case. Case 194.1 left the old keys with no effect, so that old Specs lift with no `unknown`.

Today nothing reads these keys. On a `create` of a rule or an entity, `materialize` drops them silently through `IGNORED_KEYS`, and `item_keys` lets them pass. On a `create` of an Estimate, `estimate_kind` and `estimate_slug` are removed. On an `update` they are not in the closed list `ITEM_KEYS`, and pre-spec gives a finding (case 436.2). They carry no function that does not exist elsewhere. A search of `vault/raw/` found no item line with these keys, and `materialize` reads only `raw/`. The pass of case 194.1 protects nothing any more.

The Case takes all four keys. `method` goes only as a key of a rule or an entity: `case-schema.md` already says that a `create` of a rule or an entity carries none. On an Estimate, `method` is a field of the schema, and it stays. The keys `criterion` and `context` on a `create` of an Estimate and the nested `estimate` are not in the Case. They are other shapes (cases 193, 194.1), and a separate question. The line `contract: changed` in the unmigrated Criterion of `estimate-render-harness-reproduces` is the text of a past Case. It stays until that page is recut (case 202). The words "no `contract` line" in `estimate-case-protocol-case-form` speak of a `tasks` line, not of an item key, and they stay too.

What changes after the removal. On a `create` of a rule or an entity these keys become `unknown` in `materialize`. The Spec hook refuses them. Pre-spec gives a finding. All three go by one `item_keys`. The Criteria of `estimate-prespec-checks-the-form-of-an-item` and `estimate-spec-write-copies-the-ratified-case` speak of this in general terms, and they stay. So `rule-prespec`, deferred by Case 438, is not touched. For a category whose schema the same session changes (case 308.2), such a key now reaches `fields`, like any foreign key. Today `IGNORED_KEYS` removes it there too. The Criterion of `estimate-materialize-lifts-unfiltered-on-a-schema-change` ("every key into `fields`") agrees with this and stays.

Two Estimates of `rule-materialize` become false. `estimate-materialize-lifts-a-create-by-the-schema` lists these keys among the own keys of a `create`. The `－` line of `estimate-materialize-assembles` says they do not reach `unknown`. These are two promises, so two sub-cases. The Render of `rule-case-protocol` names the keys in two sentences, and that is the third sub-case. It changes no promise: the Estimates of `rule-case-protocol` speak of the loading of the file and of the form of a Case, not of item keys. No vault query is needed: the Case creates nothing.

## Problem

The keys `contract`, `estimate_slug`, `estimate_kind` and `method` on a rule or an entity are left from the shape before case 189. Today nothing reads them, but the code, the docstrings, the tests and the pages name them and let them pass silently. Decide how to remove them whole: from the judgment `item_keys`, from the lift of `materialize`, from the Estimates that promise their pass, and from the Render of `case-schema.md`.

## Given

`rule-case-protocol` — its Render says what an item of a `then` block carries
**＋** `vault/wiki/case-schema.md` — the Render of `rule-case-protocol`

## History

- 2026-09-26 created · raw/2026-09-26/1745/ledger.md#case-440.3
