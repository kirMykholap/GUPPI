---
type: decision
case: "487.3"
status: current
update: ["[[rule-synthesis]]"]
origin: raw/2026-09-28/2229/ledger.md#case-487.3
sprint: migration
created: 2026-09-28
tags: [harness, workflow, librarian]
---

## Context

A code block in a page opens on a line of three or more backticks and closes on a line of the same backticks with nothing after them. If text follows the backticks on that line, Markdown does not read it as a close. The block stays open and swallows the text after it. Today nothing checks this. `/pre-spec` applies each `replace` and `reword` pair of the plan to copies of the pages in memory, but it only counts how often each anchor is found. It never looks at what the pair leaves behind. `guppi lint` has no check of code blocks. `make style` runs ruff on Python only. So a pair whose `new` ends on a closing fence, anchored in the middle of a line, joins the rest of that line to the fence. Case 483 did this to `rule-retro`, and only the librarian found it, by eye. Case 486 of this session fixes that page.
The person agreed on one judgment in one module, called from both sides. `fence_breaks` in `guppi/materialize.py` sits beside `fence_opening` and `closes_fence`, the one judgment of a fence since case 444.1. `/pre-spec` calls it on each section that a pair changes and reports only a break the pair adds. It also calls it on each section text that a `sections` value writes whole. `lint` calls it on every section of every live page. The person chose two promises, each with a new Estimate, and chose to check the pages only. A harness file is a copy of its Render, and `render --check` already reports any difference. The person also chose to drop the full trial run of `materialize`, `generate` and `render` in Work Mode: it would not have caught this break, and nothing about it is recorded.
A grep of the live pages for a fence line with more than one word after its run found two lines. One is in `rule-retro` (line 73), which case 486 fixes. The other is in `rule-synthesis` (line 70), "``` One lesson without a pair": the sample entries of the librarian's synthesis run on into its instructions. The person chose to fix it here, as 487.3. At pre-spec, a third page came to light: `decision-case-13`. Its line 35 opens a `markdown` fence that no line closes, so the block swallows its `## History`. The person chose not to fix it here. It stays with the other old Decision pages of cases 1–28 and their 62 `schema` findings, which are debt of Slice 4 and 5.
The vault's answer: both `create` items are Estimates with a `ref`, so no vault query ran. No live page speaks of a broken code fence. The frame:
- `estimate-prespec-simulates-the-pairs` promises the anchor counts. It stands, and its `－` line on meaning stays true, because a fence is structure, not meaning.
- `estimate-lint-catches` lists the classes of lint and the form of a finding line. The new class keeps that form, so it stands.
- `estimate-case-check-sends-back-a-faulty-case` promises that the answer check runs `judge` of `guppi/prespec.py`, which calls `check_pairs`. So the new finding also sends a broken pair back to `case-guppi` before the person sees it, with no change to that Criterion.
- The estimates of `rule-synthesis` speak of clustering, not of the layout of the file, so no Estimate is touched there.
- At pre-spec, the vault query found that `estimate-materialize-judges-a-fence` speaks of the change. Its `When:` lists every reader of a fence but not the two new callers. Its line that "a word after its run stays inside the fence as content" is still true of the parsing, but that line is now what `fence_breaks` reports as a break. The person agreed to 487.4, which replaces that Criterion whole.
- `lint` only goes red, so it keeps no old form. From Work Mode until the librarian's run writes the fixes of 486 and 487.3, `make lint` reports `rule-retro`, `rule-synthesis` and `decision-case-13` under the class `fence`. After that run it still reports `decision-case-13`, so `lint` stays red on `fence`. That red is a note for the handoff, by `rule-retro`.
- The two new Estimates and the one set `pending` are read in a later session (case 428.1).

The answer check noted that some `then` lines of 487.2 and 487.4 share words with 487.1. This is expected: 487.1 defines the judgment, 487.2 applies it, and 487.4 keeps the parsing lines of the old Criterion word for word. The check also noted that the old `When:` of `estimate-materialize-judges-a-fence` is not carried. That is on purpose: the new `When:` adds the two new readers.

## Problem

A `replace` pair, or a section written whole, can leave a code fence broken in a page. Neither `/pre-spec` nor `lint` looks for this. So the break reaches the vault and the rendered harness files, and only someone reading by eye catches it.

## Given

`rule-synthesis` — its Render: the closing fence of the sample entries and the sentence after it
**＋** `.claude/agents/librarian-guppi.md` — the agent file rendered from `rule-synthesis`

## History

- 2026-09-29 created · raw/2026-09-28/2229/ledger.md#case-487.3
