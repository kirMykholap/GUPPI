---
type: decision
case: "478.1"
status: archived
update: ["[[estimate-sprint-migration-file-route-gone]]"]
origin: raw/2026-09-28/1318/ledger.md#case-478.1
sprint: migration
created: 2026-09-28
tags: [sprint, workflow, harness]
---

## Context

`make lint` prints one line per finding, in the form `<category>/<slug>: <class>: <what>`. `guppi/lint.py` also prints findings on the `schema.yaml` of a category folder. Those findings are named `<category>/schema`, with the class `schema-description` or `schema.yaml is missing`. The Criterion of `estimate-sprint-migration-file-route-gone` ends with "`make lint` has no finding on a schema". The line can be read two ways. If it means "no finding of the class `schema`", it fails today on 64 findings: 62 on the Decision pages of cases 1–28 and 2 on `rule-spec-box`. If it means "no finding on a `<category>/schema`", it passes. The brief lists 98 lint findings, and none of them is on a schema file. Case 320 wrote the line when the file route was the way to change the schema files by hand. The first reading of 2026-09-22 recorded "no finding on a <category>/schema". The Estimate is `pending`. The main agent ran the grep of its `method` on `guppi/` today and it found no match.
The person decided in one round. The line means no finding on a `<category>/schema`. The Criterion is replaced whole with that wording, and `purpose` and `method` are reworded to match. The person also asked whether an Estimate like this one goes to the archive once its condition holds. An Estimate has three statuses, `pending`, `passed` and `failed`, and no status for "done". The only way to remove it is a `delete`. The person chose to keep the Estimate live until the sprint closes, so that it still catches a regression. The general rule is that the sprint page and its Estimates go to the archive together at the close of a sprint. It belongs to Slice 5 and is not decided here. It becomes a note in the Slice 5 milestone of `entity-sprint-migration`. Under `rule-sprint`, a note is a line with no wikilink before the ` — `: a task not yet cut into pages, never ticked. At pre-spec, the check of the plan found two parts of the note that the `then` of 478.2 did not state: the condition "once each has passed" and the reason. The person accepted the fix, and the `then` of 478.2 now states both.
The vault's answer: no `create`, so no vault query ran. The frame. Each line of the old Criterion is carried unchanged, except the lint line, which is changed on purpose, so the check notes it as not carried. 478.1 adds a `－` line that leaves the findings on pages to `estimate-sprint-migration-lint-clean`. That Estimate promises that `make lint` exits 0 at the close of the sprint. It stays true and is not touched. The Purpose of `entity-sprint-migration` says "the `file` route out of the scripts", which stays true. The Criterion of `estimate-sprint-migration-lint-clean` wants each item of `## Milestones` to be "a wikilink to a page or a plain line", and the note is a plain line. Under `rule-sprint`, the note keeps Slice 5 open until a Case cuts it or removes it. Slice 5 already stands open. No reader in code changes.
Not done: this session cannot read the Estimate, because a Case of this session replaces its Criterion (case 428.1). The brief listed it under Work, and it now moves to a later session. The Estimate is not deleted. No rule on the close of a sprint is written, and no Estimate is archived.

## Problem

One line of the Criterion of `estimate-sprint-migration-file-route-gone` has two readings: one passes today and one fails. A reader cannot tell which reading the promise means. No page says what happens to the Estimates of a sprint when it closes.

## Given

`estimate-sprint-migration-file-route-gone` — the promise that the file route is gone; its Criterion replaced whole
**＋** `guppi/` — the scripts the file route left
**＋** `guppi/generate.py` — applies or fails the entry of each kind, and ticks the line of an applied entry
**＋** `guppi/materialize.py` — `category_of` gives the entry of a slug with no prefix `category: unknown`
**＋** `guppi/prespec.py` — `check_governed` refuses an `update` item that carries `file`
**＋** `guppi/lint.py` — reports a finding on the `schema.yaml` of a category folder as `<category>/schema`
**＋** `estimate-sprint-migration-lint-clean` — the promise of `make lint` at the close of the sprint, which stands
**＋** `vault/wiki/sprint.md` — shows the `purpose` of the Estimate

## History

- 2026-09-28 created · raw/2026-09-28/1318/ledger.md#case-478.1
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
