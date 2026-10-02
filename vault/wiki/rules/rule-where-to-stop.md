---
type: rule
kind: Leaf
purpose: Prevents the run from /work to the librarian from stopping where the person is not needed, or going on where only the person can decide
status: draft
enforcement: render
governs: vault/wiki/where-to-stop.md
render_mode: full
estimates: ["[[estimate-where-to-stop-stops-only-on-its-conditions]]"]
origin: raw/2026-09-29/2024/ledger.md#case-531.7
sprint: migration
created: 2026-09-29
tags: [session, workflow, harness, render]
---

## Purpose

Prevents the run from /work to the librarian from stopping where the person is not needed, or going on where only the person can decide. The person keeps three questions: what to do, the Cases of Plan Mode; what done means and how to check it, the Estimates; and where to stop, this page (case 531.7). `/work` and `/box` load its text by an import of `vault/wiki/where-to-stop.md` (case 591), and the refusal of `rule-retro-onward` names the file. A hook on a single action, such as a push, may enforce a condition later; until then the text in the context is the guard.

## Render

<!-- rule-where-to-stop -->
# Where to stop

From the approved Spec to the librarian's report the run needs no person: `/box`, `/work`, the Work readings, `/retro` and `/handoff` run in one turn. Stop and ask the person only on one of these conditions:

1. A fork that changes a contract: the work needs a choice that no ratified Case makes, so a new Case is needed.
2. A hook refuses, and its text gives no step you can follow, or says that the refusal is a stop.
3. An action that git in this repository cannot undo, such as a push to a remote or a deletion outside the repository.
4. A task of the Spec whose text opens with `stop:`: stop before it runs, and run it after the person's word.
5. The branch is `main`: Work Mode does not start there; say so, and go on after the person moves to another branch.
6. `/box` cannot go on: its check `uv run guppi box --check` prints a reason, or one of its `git merge --ff-only` refuses; show what stopped it, and go on after the person's word.

To stop, end the reply with the question to the person. From the call of `/retro` until `handoff.md` stands, open that reply with `STOP:`, so that the hook of `rule-retro-onward` lets it end. Nothing else is a stop: a red test, a reading that only the person can take, an observation or a doubt goes on as a lesson or a line of `handoff.md`, as `/retro` says. After the person's answer, the run goes on from where it stopped.
<!-- /rule-where-to-stop -->

## History

- 2026-09-30 created · [[decision-case-531.7]]
- 2026-09-30 estimate estimate-where-to-stop-stops-only-on-its-conditions added · [[decision-case-531.7]]
- 2026-10-01 status: draft → built · cascade
- 2026-10-02 updated: /box imports the file, and its stops — a reason of its check, a fast-forward merge that refuses — are condition 6 (case 591.10) · [[decision-case-591.10]]
- 2026-10-02 status: built → draft · cascade
