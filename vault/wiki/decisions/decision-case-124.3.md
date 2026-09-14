---
type: decision
case: "124.3"
status: current
update: [glossary, index, insights-schema]
origin: raw/2026-09-14/1029/ledger.md#case-124.3
sprint: migration
created: 2026-09-14
tags: []
---

## Context

Today an Insight is "never a Decision target" (glossary, `insights/schema.md`, `index.md` §8); it reaches the Frontier only as the "Related Insight" of a deferred Case. `insight-session-vault-knowledge-not-loaded` (severity 4, the heredoc trap among its children) and `insight-ledger-hook-reads-only-the-final-text` (severity 3) have Proposals nobody was ever asked to ratify or reject; the same trap returns every session. (Case 119 as it stands.)

## Problem

Lessons pile up, the librarian writes the Insight, and nothing puts it in front of the person as a Case. The owner's design: the librarian surfaces an open Insight in the brief as a Case for the next Plan Mode, where it is ratified into a decision on its Proposal, or rejected, or deferred with a count — the same lifecycle a deferred Case has. (Case 119 as it stands.)

## Given

`rule-brief` (`Leaf`, `built`, `render` into `.claude/agents/librarian-guppi.md`, `estimate-brief-written` `passed`, `deferred_by: [decision-case-119]`): the Deferred item of the Render reads "at most seven items, one per target of a `defer` entry … plus every item of the previous brief's list whose decision no `supersedes` retired. Rank by the `severity` of a related Insight, then by the number of times the item was postponed".
**＋** `rule-page-generation` (`Leaf`, `built`, `estimate-generate-writes` `passed`): `defer` sets `deferred_by` for `rules` and `entities` only (`generate.py:565-568, 579-580`); `KEY_ORDER["insights"]` has no `deferred_by`; `update` is not bound to a category; the cascade archives the `clustered` children of an `actioned` Insight and recounts `severity` (104.2, 104.3, 110); `derive_insight` builds a lesson's `## Insight` from its field — the model for `## Addressed by`. `clear_deferred_by` on a `supersedes` works through `find`, whatever the category. `index.py` shows `deferred_by` on a line of any category; `lint` treats it as a ref.
**＋** Rule-class files: `glossary.md` — the `Insight` row ("never a Decision target") and the `deferred_by` row ("On an Entity or Rule"); `index.md` §8 — "An Insight is never the target of a Decision. It reaches you as a `brief.md` candidate in a later session and becomes an ordinary ratified Case there"; `insights/schema.md` — "Created by the librarian, never by a decision", the `addressed_by` row, the `## Addressed by` section ("Script places the decision link here once fixed"), no `deferred_by` row.
**＋** Ten Insights today, all `open`, severity 2–4; under the cap of 7 with six deferred Cases the first lines go to the Insights of severity 4 and 3.
**＋** `/hi` assembles the Frontier from the whole brief; a Deferred item is already an item, `rule-skill-hi` is not changed (F4 is its own Case).
**－** The creation of an Insight stays with the librarian; a Decision neither creates nor deletes one. `severity` is still never written by hand (110.1).
**－** `rule-synthesis` is not changed: clustering as it was.
**－** The Frontier line F2 closes on this Case.

## History

- 2026-09-14 created · raw/2026-09-14/1029/ledger.md#case-124.3
