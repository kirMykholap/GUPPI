---
type: decision
case: "474.2"
status: current
update: ["[[estimate-synthesis-clusters]]"]
supersedes: ["[[decision-case-471.2]]"]
origin: raw/2026-09-28/0000/ledger.md#case-474.2
sprint: migration
created: 2026-09-28
tags: [harness, workflow, librarian]
---

## Context

This Case replaces Case 471 with the same content. After 471 was ratified again, the plan file still held the first body of 471 under its parent heading, with the same `replace` pairs on `rule-documentation` and `rule-synthesis`. Those first pairs used up the anchors, so the pairs of 471.1 missed and `guppi ratified` refused them. The agent may not edit the plan. A superseding Case removes 471 from the Spec. `remove_case` removes a Case together with its sub-cases, but `mark_superseded` in `guppi/materialize.py` marks only the entries whose case id is exactly the one named. So the lines of 474 carry one `{supersedes:case N}` block each for 471, 471.1 and 471.2 (case 429), and every entry of the three ids is superseded.
The librarian runs after the handoff with the frame of `rule-documentation`, rendered into `.claude/agents/librarian-guppi.md`. The frame bans every read of `vault/archive/`, and only the prose holds the ban. `estimate-documentation-completes` failed on the librarian run over session 1819. The transcript of that run shows two reads outside the frame. First, the index Grep over `vault/wiki/lessons/` printed 21 KB. The harness saved that output to a file under `~/.claude/projects/…/tool-results/`, and the librarian read the file back. That file is the index lines, and the frame allows the index lines, but the Criterion counts the read as a breach. Second, at 20:40:20 and 20:40:26 the librarian grepped every `vault/raw/*/*/materialize.yaml` for `librarian:` entries, and at 20:40:39 it ran `grep -rln "status: clustered" raw archive`. It was looking for an earlier synthesis entry to copy its form. The event log of 2026-09-27 shows the same search in the librarian run of 04:20:33, over the yaml of session 2026-09-26/1745. It also shows that the librarian run of 18:08–18:13 listed `vault/archive/` and read a file under `~/.claude/projects/`. The line at 23:38:43 comes before the handoff of session 2050, so it is not from a librarian run. The frame names the fields of a synthesis entry but shows none. `tests/test_generate.py` holds a synthesis `create` of an Insight, but the frame does not point to it.
The full ban also blocks one read that the librarian needs. `guppi/generate.py` fails on a slug taken by an archived page and on a `rename` of an archived page. Its error names only the slug, and archived pages lie at any depth under `vault/archive/`. The frame tells the librarian to say why a script failed, but it may open only pages under `vault/wiki/`. `rule-ask` finds an archived page by slug alone, with the Glob `vault/archive/**/<slug>.md`, and this Case gives the librarian the same lookup.
`rule-documentation` is `draft`, and `estimate-documentation-completes` is `failed`. The Case creates no page, so no vault query ran. In the frame: the Render of `rule-synthesis` keeps "Do not read the archive", and its Purpose keeps "The archive is not read". Both are about the synthesis, which still does not read the archive. `estimate-synthesis-clusters` says, of the whole run, "no archive file was read". An archived page opened for a script's error would fail that line, so sub-case 474.2 replaces that Criterion whole and limits the line to the synthesis. `estimate-synthesis-keeps-actioned-by-the-mark` speaks only of `addressed_by`, and it stands.
In the rounds and at pre-spec, the person chose these answers: allow the saved output of the librarian's own command; do not ban the archive completely, but allow the Glob by slug for a script's error and forbid any search of the archive; add no hook; write every form of a synthesis entry in the frame itself, with a ban on reading a `materialize.yaml` that `materialize` did not name; and add the sub-case for `estimate-synthesis-clusters`.

## Problem

The frame bans a read that the librarian needs, the read of an archived page named in a script's error, and it does not say how to find that page. It counts the saved output of the librarian's own command as a breach. It gives no example of a synthesis entry, so the librarian searches the yamls of other sessions and the archive for one. Two Estimates fail on reads that the frame should allow or should make needless. Case 471, which decided this, cannot be written into the Spec as it stands.

## Given

`estimate-synthesis-clusters` — the promise of the synthesis, its Criterion replaced whole
**＋** `rule-synthesis` — the synthesis section of the frame
**＋** `.claude/agents/librarian-guppi.md` — the agent file that holds the synthesis
**＋** `materialize.yaml` — the yaml the synthesis appends its entries to
**＋** `vault/wiki/lessons/`, `vault/wiki/insights/` — the folders the Greps of the synthesis run over
**＋** `vault/archive/` — the archive, which the synthesis does not read

## History

- 2026-09-28 created · raw/2026-09-28/0000/ledger.md#case-474.2
