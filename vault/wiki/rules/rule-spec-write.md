---
type: rule
kind: Leaf
purpose: Prevents a ratified Case from entering the Spec in other words than the Case case-guppi wrote into its file, whose given, when, then, tasks and ratification the person signed and the check of rule-case-check stored
status: built
enforcement: hook
implementation_ref: [.guppi/guppi/ratified.py, .guppi/tests/test_ratified.py, .claude/settings.json]
parent: "[[rule-plan-mode]]"
estimates: ["[[estimate-spec-write-copies-the-ratified-case]]", "[[estimate-spec-write-checks-the-written-case]]", "[[estimate-spec-write-writes-a-defer]]", "[[estimate-spec-write-reaches-the-approved-spec]]", "[[estimate-spec-write-removes-a-superseded-case]]", "[[estimate-spec-write-exits-2-on-an-error]]", "[[estimate-spec-write-answers-a-refusal]]", "[[estimate-spec-write-refuses-a-changed-case-file]]", "[[estimate-spec-write-tells-each-reason-once]]", "[[estimate-spec-write-reads-a-new-tag]]", "[[estimate-spec-write-copies-a-built-defer-only-case]]"]
origin: raw/2026-09-23/1859/ledger.md#case-387.2
sprint: migration
created: 2026-09-23
tags: [hooks, harness, workflow, session]
core: true
---

## Purpose

Prevents a ratified Case from entering the Spec in other words than the Case `case-guppi` wrote into its file, whose `given`, `when`, `then`, `tasks` and `ratification` the person signed and the check of `rule-case-check` stored (case 645.5). `case-guppi` writes the whole Case in the documentation language, and a hook copies its stored answer (cases 437, 441; until case 387 the agent wrote each Case into the plan file itself, translated from the chat, and nobody compared the two).

## History

- 2026-09-24 created · [[decision-case-387.2]]
- 2026-09-24 estimate estimate-spec-write-copies-the-ratified-case added · [[decision-case-387.2]]
- 2026-09-24 deferred · [[decision-case-394]]
- 2026-09-24 status: draft → built · cascade
- 2026-09-25 defer by decision-case-394 superseded · [[decision-case-402]]
- 2026-09-25 updated: a value holding a backtick is refused unless its outer span is padded by one space on each side (case 402, supersedes 394) · [[decision-case-402]]
- 2026-09-25 status: built → draft · cascade
- 2026-09-25 deferred · [[decision-case-412]]
- 2026-09-25 status: draft → built · cascade
- 2026-09-25 defer by decision-case-412 superseded · [[decision-case-414.1]]
- 2026-09-25 updated: the Stop hook checks each Case it wrote (case 414.1) · [[decision-case-414.1]]
- 2026-09-25 estimate estimate-spec-write-checks-the-written-case added · [[decision-case-414.1]]
- 2026-09-25 deferred · [[decision-case-416]]
- 2026-09-25 status: built → draft · cascade
- 2026-09-25 defer by decision-case-416 superseded · [[decision-case-419.2]]
- 2026-09-25 updated: the hook writes a defer-only Case too (case 421.1) · [[decision-case-421.1]]
- 2026-09-25 estimate estimate-spec-write-writes-a-defer added · [[decision-case-421.1]]
- 2026-09-26 updated: a sub-point outside the keys item_keys gives its item is refused (case 436.1) · [[decision-case-436.1]]
- 2026-09-26 updated: a key of a defer item outside the keys item_keys gives it is refused (case 436.3) · [[decision-case-436.3]]
- 2026-09-26 updated: the Spec hook writes the stored answer of case-guppi and refuses a showing that differs from it (case 437) · [[decision-case-437]]
- 2026-09-26 updated: once spec.md stands, a Case ratified after the approval is written into it too, its ticks kept (case 441.6) · [[decision-case-441.6]]
- 2026-09-26 estimate estimate-spec-write-reaches-the-approved-spec added · [[decision-case-441.6]]
- 2026-09-26 updated: the Stop hook removes a Case superseded by a line of the reply from the plan, its copy and spec.md (case 441.7) · [[decision-case-441.7]]
- 2026-09-26 estimate estimate-spec-write-removes-a-superseded-case added · [[decision-case-441.7]]
- 2026-09-26 updated: the hook copies the stored English answer; a DIFF no longer skips a Case (case 441.8) · [[decision-case-441.8]]
- 2026-09-27 updated: the fence of the then and tasks blocks is chosen by their content (case 444.2) · [[decision-case-444.2]]
- 2026-09-27 updated: the hook writes no ratified copy (case 445.2) · [[decision-case-445.2]]
- 2026-09-27 updated: the Spec hook writes a Case whose file was sent after its newest store and no longer needs a showing whole; the function that names the plan file named right (case 452.3) · [[decision-case-452.3]]
- 2026-09-28 deferred · [[decision-case-475]]
- 2026-09-29 updated: a short Case whose then block holds a YAML comment is refused, judged by the function of guppi/materialize.py (case 521.1) · [[decision-case-521.1]]
- 2026-09-30 updated: the refusal of a comment says YAML cuts a value at a # after a space and PyYAML refuses the block at a # after a tab (case 526) · [[decision-case-526]]
- 2026-09-30 updated: a short defer goes under ## Deferred of spec.md once it stands, with no Retro moment (case 542) · [[decision-case-542]]
- 2026-09-30 updated: the Spec holds recommend (case 544.5) · [[decision-case-544.5]]
- 2026-09-30 updated: the Stop hook exits 2 on its own error after the payload is read, and 0 on an error while it reads the payload (case 554) · [[decision-case-554]]
- 2026-09-30 estimate estimate-spec-write-exits-2-on-an-error added · [[decision-case-554]]
- 2026-10-03 defer by decision-case-475 superseded · [[decision-case-608]]
- 2026-10-03 updated: the put-off change to drop the parent's old body on re-ratification is not taken: a Case ratified in the session that is built again in another shape takes a new number that supersedes it, and the check of rule-case-check sends back one that keeps its number (case 610.1) · [[decision-case-610.1]]
- 2026-10-05 estimate estimate-spec-write-answers-a-refusal added · [[decision-case-644.1]]
- 2026-10-05 updated: the hook writes, removes and checks whether stop_hook_active is set or not, and gives each reason once a stretch, judged by its own refusals in the transcript (cases 644.1, 644.8) · [[decision-case-644.1]]
- 2026-10-05 estimate estimate-spec-write-refuses-a-changed-case-file added · [[decision-case-645.5]]
- 2026-10-05 updated: the hook copies the text of the file case-guppi wrote, as the check stored it, and writes nothing of a Case whose file differs from it; the purpose follows (case 645.5) · [[decision-case-645.5]]
- 2026-10-05 estimate estimate-spec-write-tells-each-reason-once added · [[decision-case-644.8]]
- 2026-10-05 status: draft → built · cascade
- 2026-10-07 estimate estimate-spec-write-reads-a-new-tag added · [[decision-case-702]]
- 2026-10-07 updated: a task line tag with the sub-points meaning and aliases declares a new tag into new_tags of the then block and stands in no tasks block (case 702) · [[decision-case-702]]
- 2026-10-07 updated: the Spec hook removes a parent whose every sub-case with a decision line is retired (case 722.2) · [[decision-case-722.2]]
- 2026-10-13 updated: ships in the clean version (case 804) · [[decision-case-804.5]]
- 2026-10-14 updated: the history of the hook stands in the bracket of its pointers · [[decision-case-809]]
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-10-15 updated: the Purpose names the language of a Case by its role · [[decision-case-824]]
- 2026-10-17 updated: the hook refuses a short defer of a Lesson or a Decision page (case 865) · [[decision-case-865.3]]
- 2026-10-17 estimate estimate-spec-write-copies-a-built-defer-only-case added · [[decision-case-879.1]]
- 2026-10-17 updated: a Case built by case-guppi with only defer lines is copied from its stored file; only a Case the reply shows in the short form goes under ## Deferred · [[decision-case-879.1]]
- 2026-10-17 status: built → draft · cascade
- 2026-10-26 status: draft → built · cascade
- 2026-10-30 updated: ## How it works left the Leaf, its mechanism in the docstring of .guppi/guppi/ratified.py · [[decision-case-942.1]]
