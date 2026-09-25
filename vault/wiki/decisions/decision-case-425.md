---
type: decision
case: "425"
status: current
update: ["[[rule-case-build]]"]
origin: raw/2026-09-25/1654/ledger.md#case-425
sprint: migration
created: 2026-09-25
tags: [session, workflow, harness]
---

## Context

Case 419.2 replaced the agent `frame-guppi` with `case-guppi`. For the page `rule-case-build` it signed two `update` items: first the new `Purpose` and `Render`, then the `rename` to `rule-case-build`. A Case has one ledger line per page. `materialize` takes the first item with that slug for it (`find_item` in `guppi/materialize.py`), and the second item, with the `rename`, drops out without a word. The sections were applied, the rename was not. So the rule stands under the old slug, and its Render stands between the markers `rule-case-build`. At the same time `rule-case-protocol`, `rule-skill-hi` and their renders `vault/wiki/case-schema.md` and `.claude/skills/hi/SKILL.md` name the page `rule-case-build` in a code span, and it does not exist. Lint does not check such code spans. The slug `rule-case-build` is free: no page has it in `wiki/` or in the archive.
`rename` in `guppi/generate.py` moves the page. It changes the old slug as a whole word in all its sections but History. The Render markers change too, so `render` finds them by the new slug. It changes the same slug in all live pages: in `children` of `rule-plan-mode`, in `target` of `estimate-case-build-writes-the-case`, in the lists and text of decision pages. After that the decision page of 419.2 names the rule by the new slug twice in `given`: that is what this mechanism writes, and the Case does not edit it. `.claude/agents/case-guppi.md` is rendered without markers, so its text does not change.
What the frame check showed. A Grep over `vault/wiki/` without `brief.md` and `log.md` found only one Estimate that names the old slug: `estimate-case-build-writes-the-case`, and only in `target`. No Estimate names the new slug. The Criterion of `estimate-case-build-writes-the-case` speaks of the behaviour of `case-guppi`, and the rename does not change behaviour. So the Estimate gets no `update`: `rename` changes only its `target`.
What this Case does not do. It does not close the cause: no check refuses two items of one slug in one `then` block, though the schema asks for one item per target. That is a separate item. The line `update rule-case-build` in `raw/2026-09-25/1228/spec.md` stays unticked: `generate` ticks it by the ledger of session 1228, not by this Case. `git rm .claude/agents/frame-guppi.md` is W25 and is not part of this Case.
C4 is a separate Case, not a sub-case of this one. The reading entry of `estimate-frame-check-finds-a-contradiction` failed on the rename of the Estimate, and that rename was applied. The rename of the rule does not touch it: after this Case it fails the same way. Its question is another: the reading was taken on a Criterion the same session replaced. It must be decided how to mark that entry so that the unit 1228 is applied whole. W26 and W27 depend on C4, not on this Case.

## Problem

The rename signed in Case 419.2 is not applied. Harness files and rule pages name the rule by a slug that does not exist. It must be decided by which path to apply the rename now.

## Given

`rule-case-build` — the rule of the agent `case-guppi`, renamed `rule-case-build`
**＋** `.claude/agents/case-guppi.md` — the file its Render writes
**＋** `rule-plan-mode` — its parent, which lists it in `children`
**＋** `estimate-case-build-writes-the-case` — its Estimate, which names it in `target`
**＋** `rule-case-protocol` and its render `vault/wiki/case-schema.md` — a text that names the rule by the new slug
**＋** `rule-skill-hi` and its render `.claude/skills/hi/SKILL.md` — a text that names the rule by the new slug
**＋** `guppi/generate.py` — the `rename` of an `update` (case 258.1)

## History

- 2026-09-25 created · raw/2026-09-25/1654/ledger.md#case-425
