---
type: decision
case: "211.2"
status: archived
update: ["[[estimate-generate-fails-alone]]"]
origin: raw/2026-09-16/2238/ledger.md#case-211.2
sprint: migration
created: 2026-09-16
tags: [harness, workflow, ledger, tests]
---

## Context

A recut is the first touch of an old Estimate page: an `update` that replaces the Criterion whole and sets `pending` (cases 193, 201–204). `generate` then writes `sections` and `set`, and keeps `## Context` and `## Method` "where a page carries them" (`estimate-generate-writes`, `estimates/schema.md`); the field `method` appears only on pages born after 193. So the six recuts of session 1955 stayed in the old shape: five — `estimate-generate-writes`, `-generate-walks-dates`, `-lint-catches`, `-pretask-reconciles`, `-materialize-assembles` — without a `method` field and with the two old sections; the sixth, `estimate-case-protocol-case-form`, is in the shape of the model. Lint counts the remainder as `unmigrated` (42) and drops the checks of the old shape once the counter reads zero (case 202). `index.md` §7, `case-schema.md`, `estimates/schema.md` and `schema.yaml` say "until the recut" and do not say what a recut must do. This Case touches two promises of `rule-page-generation` — `estimate-generate-writes` (the shape of the page) and `estimate-generate-fails-alone` (the refusal) — one per sub-case; `-cascades`, `-walks-dates` and `-writes-the-decision-page` it does not touch.

## Problem

A recut that leaves the page in the old shape is no recut: the `unmigrated` counter does not fall, and the page gets a third state — a new Criterion beside the old sections — while lint reads its `method` from the section. Nobody has to write `set: {method: …}` and `generate` does not have to drop the sections, so both forget.

## History

- 2026-09-17 created · raw/2026-09-16/2238/ledger.md#case-211.2
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
