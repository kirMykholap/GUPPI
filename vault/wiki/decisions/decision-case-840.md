---
type: decision
case: "840"
status: current
children: ["[[decision-case-840.1]]", "[[decision-case-840.2]]"]
origin: raw/2026-10-16/0104/ledger.md#case-840
sprint: plugin
created: 2026-10-16
tags: [harness, workflow, ledger, plugin]
---

## Problem

Two live pages use the path `tests/` as the example of a path pair of `reword`, and the Criterion of `estimate-guppi-package-runs-from-its-own-folder` forbids such a path on a live page. Its test stays red, and the Estimate stays `failed` and put off.

## Recommend

- **How do we settle the clash between the example and the test?**
  - Recommended: (a) change the example to a neutral folder, such as `docs/` → `site/docs/`, in both pages; the Criterion of `estimate-generate-rewords` replaced whole and set `pending`.
  - Answer: agreed, (a).
- **Does this Case also re-read the failed Estimate (item C3)?**
  - Recommended: (a) yes, as a second part of this Case: the Estimate set `pending` with its Criterion unchanged, the defer taken up, and a `method` that waits for the librarian's run of the session that changes the example.
  - Answer: agreed, (a).
- **What does the reading of `estimate-generate-rewords` run once its Criterion is replaced?**
  - Recommended: (a) keep only the test, `pytest .guppi/tests/test_generate.py`, read at this session's Retro.
  - Answer: agreed, (a).

## History

- 2026-10-16 created · raw/2026-10-16/0104/ledger.md#case-840
