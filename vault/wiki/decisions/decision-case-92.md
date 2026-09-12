---
type: decision
case: "92"
status: current
update: [index, case-schema]
origin: raw/2026-09-12/ledger.md#case-92
sprint: migration
created: 2026-09-12
tags: []
---

## Context

The librarian raised two facts for this Plan Mode that ask for no new work, only for a
signature under what already stands. First: §4 of `index.md` says `ref` is omitted on
`update` and `delete`, while its own example two lines above carries `{ref:rule-x}` on an
`update`, and every line of the last four sessions carries it. Second: the Work Mode of
session J changed two mentions of the Spec in `case-schema.md` to the session folder,
beyond what the `change` lines of case 73 named literally.

## Problem

In both the text and the practice have parted, and neither side is signed. Either the
text follows the practice, or the practice goes back to the text.

## Given

`index.md` line 181 is the example
`- decision[case 12][update][rule-x]{ref:rule-x}{source:external_id}{tags:a,b}`; line 185
says "`ref` — the parent, for a `create` that adds a child. Omitted for update/delete:
`slug` already identifies the target". Two lines of one section contradict each other.
**＋** The Render of `rule-case-protocol`, and so `CLAUDE.md`, already says "A record is a
`- decision[case 12][update][rule-x]{ref:rule-x}`": the ratified text is on the side of
the practice, and only §4 disagrees.
**＋** `materialize.parse_line` reads `options.get("ref")` for a decision line of any
kind; a `ref` on an `update` overrides nothing and breaks nothing.
**＋** `case-schema.md` names the session folder in two places, line 60 (Work Mode ticks
the boxes of the Spec) and line 68 (the short form is appended to the Spec). Both say what
case 73 decided.
**－** Both files are Rule-class: applied by hand in Work Mode, no Estimate, no reading
born here.

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#case-92
