---
type: rule
kind: Leaf
purpose: Prevents a Rule page and the harness file it governs from becoming two copies of one text
status: draft
enforcement: check
implementation_ref: [guppi/render.py, tests/test_render.py, .claude/settings.json]
parent: "[[rule-harness]]"
estimates: ["[[estimate-render-harness-reproduces]]", "[[estimate-render-sync-reports]]", "[[estimate-render-harness-ticks-the-spec]]"]
origin: raw/2026-09-09/ledger.md#case-18.1
sprint: migration
created: 2026-09-09
tags: [harness, render]
---

## Purpose

Prevents a Rule page and the harness file it governs from becoming two copies of one
text. Without a renderer `enforcement: render` is a label: the skill and `CLAUDE.md` are
edited by hand, the page follows or does not, and the vault stops being the source.

`parent: rule-harness` names the MOC of the harness tools: the renderer runs with lint and as the librarian's step after `cleanup` (case 89.1); the tick of case 226.2 belongs to that step.

## How it works

`uv run guppi render` writes every governed file from its Rule page; `--check`
renders in memory and names the files that differ, for `make lint`; `--sync`, the `SessionStart` hook and, since case 115, the `Render:` line of `/hi` after the pull, prints a unified diff for each differing file — the file as it
is, then the rendered text — and writes it, so the agent's first turn shows what
the render changed: the pages the librarian updated, or a hand edit that is now
gone and may deserve a Case. It exits 0 always; `SessionStart` cannot block, and a
render error goes to stderr. A governed file whose name ends in `.json` is parsed before anything is written: when one of them does not parse, the run writes nothing and names the file and its page on stderr (case 89.4). When Claude Code reads an agent file under `.claude/agents/` — at session start or on the call — is the reading of case 139.1 on `estimate-render-harness-reproduces`; the librarian's render is its last step before the commit, and an agent it renders is planned for from the next session (case 139.1). The rendered files are committed by the librarian, in its own commit (case 89.2). Once the plain `guppi render` wrote the files and exits 0, it ticks every unticked task line that opens with a code span holding `guppi render` — the render lines of the Spec, never a `read` line that names the command later — in the `spec.md` of every unit under `raw/` whose yaml is applied whole; `--check`, `--sync` and an exit 1 tick nothing (cases 226.2, 235).

A child of a `full` page lands between its own markers, which stay in the file and
say who owns the text. A file that cannot hold a comment takes the child's text
bare: the markers would make it unparsable. The owner is then named by the
`<!-- child -->` line of the parent's body, and `render --check` compares the whole
file, so nothing is lost but the label in the file itself (case 85.1).

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-18.1
- 2026-09-10 updated: a child without enforcement render contributes nothing to a full render; a marker line for it is an error · raw/2026-09-10/ledger.md#case-36.2
- 2026-09-10 updated: parent is rule-harness · raw/2026-09-10/ledger.md#case-37
- 2026-09-10 status: draft → built · cascade
- 2026-09-12 updated: render --sync at SessionStart — diff on stdout, then the write; enforcement hook (case 59.7) · [[decision-case-59.7]]
- 2026-09-12 status: built → draft · cascade
- 2026-09-12 deferred · [[decision-case-84]]
- 2026-09-12 updated: a child spliced into a file that cannot hold a comment lands without its markers (case 85.1) · [[decision-case-85.1]]
- 2026-09-12 defer by decision-case-84 superseded · [[decision-case-88.1]]
- 2026-09-12 updated: the live clause of the render reading is a standing rule, read against the pages that changed (case 88.1) · [[decision-case-88.1]]
- 2026-09-12 updated: a json target is parsed before the write, and one failure stops the whole write (case 89.4) · [[decision-case-89.4]]
- 2026-09-13 status: draft → built · cascade
- 2026-09-14 updated: --sync is named as the SessionStart hook and the Render line of /hi after the pull (case 115.1) · [[decision-case-115.1]]
- 2026-09-14 updated: the moment Claude Code reads an agent file is the reading of case 139.1; a rendered agent is planned for from the next session (case 139.1) · [[decision-case-139.1]]
- 2026-09-14 updated: no indexes in make lint (case 147.9) · [[decision-case-147.9]]
- 2026-09-18 estimate estimate-render-harness-ticks-the-spec added · [[decision-case-226.2]]
- 2026-09-18 updated: render ticks the guppi render lines of the applied Specs under raw/; the Purpose names the librarian's step (cases 226.2, 233) · [[decision-case-226.2]]
- 2026-09-18 status: built → draft · cascade
- 2026-09-18 updated: a render line opens with the code span holding guppi render; a read line that names the command later is not ticked (case 235) · [[decision-case-235]]
