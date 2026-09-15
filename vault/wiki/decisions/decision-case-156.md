---
type: decision
case: "156"
status: current
update: ["[[rule-lint]]"]
supersedes: ["[[decision-case-146]]"]
origin: raw/2026-09-15/1110/ledger.md#case-156
sprint: migration
created: 2026-09-15
tags: [harness, workflow]
---

## Context

After sessions O and P `guppi lint` reports 10 `orphan` findings — the ten actioned Insights. An orphan in `rule-lint` is a live entity, rule, estimate or insight that no other live page names in its frontmatter. An Insight is named only by its children, through `insight`; on `actioned` the cascade of 104.2 archives the children and the Insight is left with no live inbound link by construction, while `rule-synthesis` and `index.md` §8 keep it live so a recurrence is caught by its `pattern`. Case 146 deferred the choice: an exemption for an actioned Insight, or Obsidian's notion of an orphan (no inbound link of any kind, body and decision pages included) now that the refs are wikilinks (147).

## Problem

Two ratified norms — the children of an actioned Insight are archived; an actioned Insight stays live — guarantee a third's finding, which catches nothing. Which definition of an orphan lint keeps.

## Given

`rule-lint` (`draft`, `deferred_by: [[decision-case-146]]`, `check`, `estimates: [estimate-lint-catches]` — `passed` at 11:1x today on 149.3): "How it works" lists "orphans" without a definition; the definition lives in the docstring of `guppi/lint.py`: "`orphan` (a live entity, rule, estimate or insight no other live page's frontmatter names; a lesson is a record and an Insight names it or not)"; `check_orphans` (`lint.py:355`) counts as owners only the `LINK_FIELDS` (`parent`, `children`, `estimates`, `target`, `addressed_by`, `insight`) of live pages and excludes `decisions` and `lessons`; the `create`/`update`/`delete`/`defer` lists of a decision page are not ownership.
**＋** `ask-guppi` (11:14): exists `rule-lint` — the Case carries `{supersedes:case 146}`; near `lesson-obsidian-cli-needs-the-running-app` — the Obsidian option is already rejected by a recorded lesson, `lesson-obsidian-property-links-need-wikilink-form` — the premise of the graph; missing — no page defines "orphan" outside the Context of 146 and `lint.py`; no Insight is about lint; tags `harness`, `workflow` — `rule-lint`'s own.
**＋** `index.md` §8: an Insight is created on the second lesson; actioned stays live with its `pattern` in its index line; `severity` = the count of children not archived — unchanged.
**＋** `tests/test_lint.py`: orphan tests on a rule (357) and an estimate (393); "a lesson is never an orphan" (622); no test on an insight.
**－** Live pages: 10 Insights, all `actioned`, all orphan findings; no other orphan besides the two placeholders of F1.

## Criterion

- [[estimate-lint-catches]] § case 156

## History

- 2026-09-15 created · raw/2026-09-15/1110/ledger.md#case-156
