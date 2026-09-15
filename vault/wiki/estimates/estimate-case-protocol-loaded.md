---
type: estimate
kind: QA
status: passed
target: "[[rule-case-protocol]]"
origin: raw/2026-09-09/ledger.md#case-13
sprint: migration
created: 2026-09-09
tags: [session, workflow, ledger]
---

## Context

An instruction in `CLAUDE.md` has force only if it is in the system prompt from the first
turn. The LEDGER-block rule is the half of it a test can hold; the rest is read off the agent's
first reply.

## Criterion

At session start the agent states the LEDGER-block rule and the one-Case-at-a-time rule
without a read call, and the `then` block of a Leaf `create` it writes carries `method` and no nested `estimate` (case 72.1); and a reply whose ledger lines sit outside a LEDGER block — bare, or in
a fence with another tag or none — adds nothing to `raw/<date>/ledger.md`.

### case 73.9

When:
A session starts with `CLAUDE.md`.

Then:
The Case protocol says the Spec is `raw/<date>/<hi HHMM>/spec.md` (the Deferred heading,
the ticked boxes) and the Frontier `raw/<date>/<hi HHMM>/frontier.md`.

### case 75.1

When:
A session starts with `CLAUDE.md`; someone reads `case-schema.md` or `index.md` §4.

Then:
The table of `case-schema.md`, §4 of the map and the ledger paragraph of the Render
show `- decision[case 12][update][rule-x]{ref:rule-x}` and
`- decision[case 12][create][rule-y]{ref:rule-x}{tags:a,b}` and say: the id is `case N`
with the word and a space, in `{supersedes:case N}` too.
**－** The estimate and lesson rows do not change.

### case 86

When:
The agent writes a `then` block for a `create` whose Estimate is a Research, or whose
derived slug is taken.
**＋** A session starts with `CLAUDE.md`, which imports `case-schema.md`.

Then:
The item names them `estimate_kind` and `estimate_slug`.
**＋** `case-schema.md` says why the prefix: `kind` and `slug` on the item are the target
page's own fields.
**－** No other key of a `then` item is renamed; `method` and `contract` stay as they are.

### case 144.1

When:
`guppi render` writes the Render of `rule-case-protocol` into `CLAUDE.md`; then the main agent writes a `- lesson[knowledge][...]` line.

Then:
The paragraph on ledger lines in the Render carries the sentence: "A `knowledge` lesson line carries `{source:...}`, the url or reference the lesson studied — a file of the harness, a probe, a client version; the schema requires it, and a line without it is `incomplete: [source]` in the yaml and a lint finding on the page. An `error` lesson never carries one."
**＋** `CLAUDE.md` carries the sentence after the render; `guppi render --check` exit 0.
**－** `rule-ledger-write` does not change: the hook writes verbatim and checks nothing.
**－** `rule-retro` does not change: its example lines stay; the rule is read in `CLAUDE.md`.

### case 159

When:
The agent writes a Case in the chat — at its first showing, when shown again after the owner's change, and with sub-cases.

Then:
`context`, `problem`, `recommend` are blockquotes without operands, the slug of the thing described only, up to seven sentences each: `context` — what the thing is and how it works today, for a reader who has not opened the pages, no line numbers and no quotation unless the Case is about one; `problem` — what is wrong, or the question answered, one paragraph; `recommend` — the choice and why, the rejected option in one sentence.
**＋** `given` — one fact per line, only those a line of `then` depends on: the state of the pages changed; the rule that constrains; the vault's answer; the test that fixes the behaviour. The first line bare, then **＋** "and also", **－** "but not / does not apply here". No history, no quotation for its own sake.
**＋** `then` — behaviour only: **＋** what also holds, **－** what does not happen; no `contract`, Estimate blocks, readings or `supersedes`.
**＋** A new section `tasks` between `then` and `ratification`: a blockquote with a checklist, one line per page `update` with its `contract`, Estimate block, file, test, command, reading — the same lines that go into the Spec's `tasks` block.
**＋** Slugs, file names and field values in code spans; bold only for section labels and operands.
**＋** Sub-cases: the story and the shared `given` on the parent; each `### Case N.M` has its own `when`, `then`, `tasks`, `ratification`.
**＋** One horizontal rule, after the Case or its last sub-case, and only when the agent's own text follows.
**－** The Spec as today: `context`, `problem`, `given`, `when`, `then` as blockquotes in English, the `then` and `tasks` blocks; the `tasks` section of the chat is its `tasks` block.
**－** The acknowledging reply (157) and the short form of a defer do not change.

### case 167

When:
The owner answers a Case with a ratification; the agent writes the reply that acknowledges it.

Then:
The reply has four parts, in this order: the `LEDGER` block first; the heading `## Case N — ratified` and a paragraph **Changes:** — what changes, in one or two sentences; a paragraph **Notes:** — facts that did not enter the Case, omitted when there are none; the heading `## Frontier` and the lines of `frontier.md` as a checklist — the closed lines folded into one, the open ones one per line with a short title, the deferred as `[-] … · defer case N` — and the question which item is next, last.
**＋** The headings and labels are in the language of the chat.
**－** The replies on readings and lessons, the reply that carries a Case and the short form of a defer stay as today; no tool call follows the block in the same reply.

## Method

One reading at a session start, by hand, plus the preview cases of `tests/test_ledger.py`.

## Result

block 167: the first acknowledging reply of session S (Case 173) — the LEDGER block first, then the heading "Case 173 — ратифицирован" with Changes and Notes, then the heading "Frontier" as a checklist with the closed line folded, the question last; headings and labels in Russian, the language of the chat

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-13
- 2026-09-09 status: pending → passed · written by hand, no generator yet
- 2026-09-09 updated: criterion follows the LEDGER block · raw/2026-09-09/ledger.md#case-16.2
- 2026-09-12 updated: the then block form of case 72.1 joins the criterion; pending for the next session's reading · [[decision-case-72.1]]
- 2026-09-12 criterion: case 73.9 added · [[decision-case-73.9]]
- 2026-09-12 criterion: case 75.1 added · [[decision-case-75.1]]
- 2026-09-12 criterion: case 86 added · [[decision-case-86]]
- 2026-09-13 status: pending → passed · raw/2026-09-13/ledger.md#L43
- 2026-09-14 criterion: case 144.1 added · [[decision-case-144.1]]
- 2026-09-15 status: pending → passed · raw/2026-09-15/1110/ledger.md#L6
- 2026-09-15 criterion: case 157 added · [[decision-case-157]]
- 2026-09-15 criterion: case 159 added · [[decision-case-159]]
- 2026-09-15 status: pending → passed · raw/2026-09-15/1448/ledger.md#L4
- 2026-09-15 status: passed → passed · raw/2026-09-15/1448/ledger.md#L5
- 2026-09-15 criterion: case 167 added · [[decision-case-167]]
- 2026-09-15 criterion: case 157 removed · [[decision-case-167]]
- 2026-09-15 status: pending → passed · raw/2026-09-15/1809/ledger.md#L3
