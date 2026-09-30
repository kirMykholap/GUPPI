---
type: rule
kind: Leaf
purpose: Prevents a ratified Case from entering the Spec in other words than the answer of case-guppi whose given, when, then, tasks and ratification the person signed
status: draft
enforcement: hook
implementation_ref: [guppi/ratified.py, tests/test_ratified.py, .claude/settings.json]
parent: "[[rule-plan-mode]]"
estimates: ["[[estimate-spec-write-copies-the-ratified-case]]", "[[estimate-spec-write-checks-the-written-case]]", "[[estimate-spec-write-writes-a-defer]]", "[[estimate-spec-write-reaches-the-approved-spec]]", "[[estimate-spec-write-removes-a-superseded-case]]", "[[estimate-spec-write-exits-2-on-an-error]]"]
deferred_by: ["[[decision-case-475]]"]
origin: raw/2026-09-23/1859/ledger.md#case-387.2
sprint: migration
created: 2026-09-23
tags: [hooks, harness, workflow, session]
---

## Purpose

Prevents a ratified Case from entering the Spec in other words than the answer of `case-guppi` whose `given`, `when`, `then`, `tasks` and `ratification` the person signed. Until case 387 the agent wrote each Case into the plan file itself, translated from the chat, and nobody compared the two. Now `case-guppi` writes the whole Case in English, and a hook copies its stored answer (cases 437, 441).

## How it works

`uv run guppi ratified` on `Stop`. After a reply whose `LEDGER` block holds `- decision[case N]` lines of a kind other than `defer`, it reads `<plan>.checked.json` for the answer of `case-guppi` stored under Case N by `rule-case-check`, and the session's transcript for a `SendUserFile` call on `raw/<date>/<hi HHMM>/cases/case-<N>.md`, N the id of the top-level Case, and for the last earlier reply that shows Case N with a section; no such call made after the time of the store (case 452.3), a showing that differs from that answer in a section it shows — by the one comparison of `guppi/casecheck.py` on `Stop`, imported with its reading of a sending — a store with no Case N, or a Case N stored with findings is a refusal, exit 2, and nothing of Case N is written (case 437); otherwise it writes the stored answer of Case N into the plan file named by `plan_path` of the ledger module, outside the repository: the heading, `context`, `problem`, `recommend`, `given`, `when` and `then` as they stand — a sub-case's own `recommend` under its heading (case 544.5) — a block tagged `then` built from the sub-points of `tasks`, and a block tagged `tasks` of the task lines without their sub-points, each opened and closed by a fence of backticks one longer than the longest run of backticks that opens a line inside it, three at the least (case 444.2); the section of Case N is replaced when it stands, appended otherwise. Once `spec.md` in the session's folder stands, the hook writes the same stored answer into it too: every section of Case N there replaced, or the Case placed after its family, before the `## Deferred` of the last approved document, or at the end; a task line whose text stood in a replaced section keeps its box; the `context`, `problem` and `recommend` of a sub-case's parent come from the parent's stored answer, never from the reply (case 441). After the write it runs the checks of `prespec --check`, imported from `guppi/prespec.py`, on each Case it wrote, with the decision lines of the reply added to those of the session's ledger — the ledger hook runs in parallel on the same `Stop` — and without the Frontier, the translation and the grammar of the ledger, which stay with `/pre-spec`; on a finding it exits 2 with the findings on stderr, each naming its Case, and the written Case stays (case 414.1). No plan file, or a sub-point it cannot read — a value holding a backtick whose outer span is not padded by one space on each side among them (case 402): exit 2 with the reason on stderr; on the re-fire (`stop_hook_active`) exit 0. A sub-point that reads into no key `item_keys` of `guppi/materialize.py` gives its item — `slug` a key of every kind; the one judgment `materialize` lifts by and `generate` applies by — is refused the same way: exit 2, and nothing of the Case is written (case 436.1). A `create` or a `defer` of a category with no schema file, or of one whose schema rule a decision line of the session or of the reply creates or updates, is not judged by its keys (case 308.2). A defer-only Case — a Case whose lines in the reply are all `defer`, beside other Cases or alone — is written by the same hook from the reply that carries its lines and shows it in the short form — `context`, `problem`, a fence tagged `then` — under `## Deferred` of the plan file, or of `spec.md` in the session's folder once that file stands; the check after the write does not run on it (cases 421.1, 542); a key of a `defer` item that `item_keys` of `guppi/materialize.py` does not give a `defer` of its category is refused, exit 2, and nothing of the Case is written (case 436.3); so is a `then` block that holds a YAML comment — a `#` at the start of a line or after a space or a tab, outside a quoted value and outside a `|` or `>` block — by the one function of `guppi/materialize.py`, since after a space YAML drops the rest of the line and no page receives it, and after a tab PyYAML, the library the scripts use, refuses the whole block (cases 521.1, 526). After the writes, a decision line of the reply that carries `{supersedes:case N}`, its own Case written in this run, removes the section of Case N — with its sub-cases, or `### Case N.M` alone when the line names a sub-case — from the plan file and, once it stands, `spec.md` in the session's folder, under `## Deferred` too; a Case N none of them holds is no refusal (case 441). An error of the hook itself after it has read the payload — an exception while it reads the transcript, the store, the plan file or `spec.md`, or writes, removes or checks a Case — exits 2 with `ratified: not done: <error>` and the advice to repeat the ledger lines once the cause is fixed on stderr, so the agent sees it at the end of that reply; a Case not yet written is written at the reply that repeats its lines, and one written before the error stays and is replaced then. An error while it reads the payload exits 0 with the error on stderr, since the hook cannot tell a re-fire then; the guard of `rule-spec-reconcile` keeps exit 0 on its own error (case 554).

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
