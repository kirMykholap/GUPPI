---
type: decision
case: "393"
status: archived
update: ["[[rule-case-protocol]]"]
origin: raw/2026-09-24/1303/ledger.md#case-393
sprint: migration
created: 2026-09-24
tags: [session, workflow, ledger]
---

## Context

The value of a sub-point in the chat is one code span or a fenced block under the sub-point. The schema says: as many backticks as the value needs. But when the value itself opens or closes with a backtick, the outer span needs one space on each side, or its backticks run into those of the value. CommonMark reads it so, `code_value` in `guppi/ratified.py` reads it so, and its docstring says so. The schema is silent, and after the ratification of Case 392.1 the agent wrote such a value without the spaces. The hook of `rule-spec-write` refused it, and the Case was shown and ratified again: the lesson `lesson-spec-write-sub-point-opening-with-a-code-span-unpadded`. The code does not change. A test of the form is added, since `tests/test_ratified.py` has none: a grep for double backticks finds only a value with no backtick at its edge. `rule-case-protocol` stands `draft`. No Estimate is touched: the Criterion of `estimate-spec-write-copies-the-ratified-case` ("each value one code span") stays true, since a padded value is one span, and the new test pins the reading that Estimate already promises, so the Case signs no line of it again; `estimate-case-protocol-loaded`, still in the old model, is left to the one pass of Slice 3g (378.1). The Case changes no behaviour of a rule or a hook, so it calls no `frame-guppi` (391.2). No vault query: the item is an `update` with a `ref`. The lesson gets `{addresses:…}` on the ratification line, since it already stands in this session's ledger. Read against the Case: the Language paragraph of `rule-case-protocol`, where the anchor stands once, `code_value` and `tests/test_ratified.py`.

## Problem

The schema does not say how to write a value that opens or closes with a backtick, and the agent learns it from the refusal of the hook; the ratified Case then does not reach the Spec.

## Given

`rule-case-protocol` — the Language section of its Render, on the form of a sub-point value.
**＋** `vault/wiki/case-schema.md` — the Render, written by `uv run guppi render`.
**＋** `guppi/ratified.py` — `code_value`, which reads the value of a sub-point.
**＋** `tests/test_ratified.py` — its tests.
**＋** `rule-spec-write` — its `Stop` hook refuses a value that is not one code span.

## History

- 2026-09-24 created · raw/2026-09-24/1303/ledger.md#case-393
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
