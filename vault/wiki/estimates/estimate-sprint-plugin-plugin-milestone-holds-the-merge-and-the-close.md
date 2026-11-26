---
type: estimate
kind: QA
status: passed
target: "[[entity-sprint-plugin]]"
purpose: Whether the milestone The plugin of the sprint page holds the merge line and then the close line alone, and Closed holds the plugin that installs, the setup and the README; read once
method: "by hand, at the Retro of the session that sets this Criterion: the update of entity-sprint-plugin in the Spec read against the Criterion, recorded in the estimate line"
origin: raw/2026-11-26/2333/ledger.md#case-1075
sprint: plugin
created: 2026-11-26
tags: [sprint, workflow]
once: true
---

## Criterion

When:
Someone reads the `## Milestones` and the `## Closed` of `entity-sprint-plugin` in the Spec, at the Retro of the session that ratified this Criterion.

Then:
The milestone The plugin holds the line ``- the merge of `main` into `plugin` — `/merge-main`, a session of its own``, and after it the close line ``- the close of `plugin` — `/sprint-close`, a session of its own``, as its last item.
**＋** The milestone holds no other item: the clean version made into a plugin, the line of `rule-morph` and the README have left it.
**＋** `## Closed` holds, after the lines it held, a line for the clean version made into a plugin, one for the setup of a new project and one for the README.
**－** The milestone The clean branch, the `## Backlog` and the Purpose of `entity-sprint-plugin` stay as they were.
**－** The close line keeps the words that `estimate-sprint-plugin-close-steps-run-from-the-line` quotes.

## Result

2026-11-26, Retro of session 2333, the update of entity-sprint-plugin under Case 1075 in vault/raw/2026-11-26/2333/spec.md read against the Criterion and the live page: its replace takes the three lines 27 to 29 of the milestone The plugin word for word and puts in their place the line "- the merge of `main` into `plugin` — `/merge-main`, a session of its own", so the milestone holds that line and then the close line "- the close of `plugin` — `/sprint-close`, a session of its own" as its last item and nothing else; its second replace keeps the two lines of `## Closed` and adds after them the lines of the clean version made into a plugin, the setup of a new project and the README; no replace touches the milestone The clean branch, the `## Backlog` or the Purpose, and the close line keeps its words

## History

- 2026-11-27 created · [[decision-case-1075]]
- 2026-11-27 status: pending → passed · raw/2026-11-26/2333/ledger.md#L11
