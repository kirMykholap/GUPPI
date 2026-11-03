---
type: estimate
kind: QA
status: passed
target: "[[rule-case-check]]"
purpose: Whether the Stop check refuses a showing of a Case that differs from the answer of case-guppi or that the checks did not pass, after a refusal of any Stop hook too, while fewer than three refusals of that Case stand since the person's last message
method: uv run --project .guppi pytest .guppi/tests/test_casecheck.py -k stop, then by hand the first reply the hook refuses
checked: 2026-10-06
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [hooks, harness, workflow]
core: true
---

## Criterion

When:
`Stop` fires after a reply of the main agent that shows a Case under `## Case N —` or `### Case N.M —` with at least one of its sections.

Then:
`uv run --project .guppi guppi casecheck` compares each such Case with the Case of the same id in `<plan>.checked.json` in each of its `given`, `when`, `then`, `tasks` and `ratification` that the reply shows, line by line once line ends and trailing spaces are the same.
**＋** Under the heading of a top-level Case, one `ratification` whose fence holds the ledger lines of its sub-cases, as the list of a showing holds them, is read as the showing of each sub-case whose id a line names: the lines that name that id are compared with the `ratification` of that sub-case in the store, and a stored line that is missing or a line the store lacks is a difference.
**＋** A section the reply does not show is not compared: a showing of the heading, a short text and `ratification` alone passes when its `ratification` equals the stored text and `raw/<date>/<hi HHMM>/cases/case-<N>.md` equals the store, as `estimate-case-check-refuses-a-changed-case-file` sets it.
**＋** The name of its heading, its `context`, `problem` and `recommend`, and text under the heading outside its sections are not compared.
**＋** A Case the store does not hold, a Case that differs in a compared section, a Case stored with findings, a Case whose file differs from the store, or a Case with no `SendUserFile` call on `raw/<date>/<hi HHMM>/cases/case-<N>.md` in the turn of the reply, N the id of its top-level Case, exits 2, the reason and the findings on stderr.
**＋** A parent shown with its sub-cases is compared part by part, as the store holds each.
**＋** The Spec hook `.guppi/guppi/ratified.py` judges a showing by the same comparison, and a sending by the same reading of the transcript, both imported from `.guppi/guppi/casecheck.py`.
**－** A heading with no section, as in the acknowledging reply, a fence tagged `DIFF`, and a deferred decision in the short form — `context`, `problem` and a fence tagged `then` with `defer` items, no `given` and no `when` — are not compared and need no sending.
**－** With `stop_hook_active` set the comparison runs the same, so a Case shown again after a refusal is compared again; its reasons are given as `estimate-case-check-judges-a-showing-after-a-refusal` sets it.

## Result

2026-10-06, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
