---
type: decision
case: "383"
status: current
update: ["[[rule-case-protocol]]", "[[insight-workflow-case-schema-silent-on-what-the-scripts-accept]]"]
origin: raw/2026-09-23/1859/ledger.md#case-383
sprint: migration
created: 2026-09-23
tags: [session, workflow, ledger, harness]
---

## Context

The agent writes a Case by `case-schema.md`, and the scripts apply it. In two places the scripts read the text more narrowly than the schema says, and the schema is silent on it. The first place is a `replace` pair: `generate` looks for `old` inside one `##` section, History excluded, and needs exactly one hit on the page; in session 1355 the anchor of Case 381 opened with the heading `## Milestones` and did not match. The second place is a sub-case's `given`: `materialize` takes it as it stands, and the parent's when it is absent; in session 1853 the sub-cases of 299 wrote "The parent's." and their own lines, a pointer the script does not resolve. Pre-spec caught both, not the schema. The two lessons are the children of `insight-workflow-case-schema-silent-on-what-the-scripts-accept`, `open`, severity 2. Every item is an `update` with a `ref`, so no vault query. No Estimate is touched: the scripts do not change, an `update` of a Render touches no Estimate of the live reading (case 378.5), and the four Estimates of `rule-case-protocol` speak of other things.

## Problem

The agent learns the limits the scripts put on a `replace` pair and on a sub-case's `given` from the check, not from the schema. Should the schema state them beside the form, and the Insight close?

## Given

`rule-case-protocol` — its Render is `case-schema.md`; the Case changes two sentences of it.
**＋** `vault/wiki/case-schema.md` — the rendered file, loaded by `/hi`.
**＋** `insight-workflow-case-schema-silent-on-what-the-scripts-accept` — the Insight the Case sets `actioned`.
**＋** `lesson-generate-replace-anchor-stays-in-one-section` — its child on the `replace` pair.
**＋** `lesson-sub-case-given-the-parents-plus-lines-has-no-form` — its child on a sub-case's `given`.
**＋** `guppi/generate.py` `replace_hits` — the one matching rule of a pair, which pre-spec uses too.
**＋** `guppi/materialize.py` — takes a sub-case's `given` as it stands, the parent's when it is absent.

## History

- 2026-09-24 created · raw/2026-09-23/1859/ledger.md#case-383
