## Case 737 — The tags case-build and prespec are declared

> **context:**
> A tag is a short topic label on a vault page, and `vault/wiki/tags.md` lists the tags a page may carry. The ledger hook of `rule-ledger-write` refuses a fresh lesson line whose tag is not in that list, unless a ratified Case of the session declares it. At the Retro of session 0213 the agent wanted to tag the lesson `lesson-case-build-misses-the-example-a-changed-check-runs-over` with `case-build` and `prespec`. The hook refused both, and the lesson went in with `workflow, tests` (handoff of session 0213, For the next session). The list holds broad topics and has no tag for how `case-guppi` builds a Case or for the `/pre-spec` check of the ratified Cases. A Grep of `^tags:.*\bworkflow\b` over `vault/wiki/` printed 306 files, so `workflow` does not tell those topics apart.
>
> This Case declares the two tags by tag lines so that later lessons and pages can use them, and adds them to that lesson by an `update` of its `tags`. That lesson does not stay live. It is a `clustered` child of `insight-workflow-contract-change-leaves-its-derived-text-stale`, which Case 736.1 of this session sets `actioned`. The status field of `rule-lessons-schema` archives a Lesson when its Insight is `actioned`, and the cascade of `guppi/generate.py` sets each `clustered` child of an `actioned` Insight `archived` in the same librarian run. `rule-cleanup` then moves the page out of the live pages. The lesson therefore keeps the new tags under `vault/archive/`. The point of this Case is the declaration of the tags. The librarian's `guppi generate` writes a declared tag into `tags.md` by `register_tags` of `guppi/generate.py`. From the ratification on, the ledger hook and the check of a Case file take the two tags as listed in this session too (`ratified_tags` of `guppi/tags.py`). The person chose to tag only that lesson, so the other pages whose slugs name the two topics keep their tags. That includes the Estimate that Case 736.1 of this session creates on `rule-case-build` with `workflow, harness, tests`. A later Case or lesson may use the new tags.
>
> No new Estimate is made. `estimate-generate-writes` already checks the change, since its Criterion says that a tag of `new_tags` lands in `tags.md` and that an `update` applies `set` to the frontmatter. Its Criterion stands because this Case uses that behaviour and does not change it. `estimate-spec-write-reads-a-new-tag` stands for the same reason: it checks that the Spec hook turns a tag line of a Case file into an entry of `new_tags`, which is how the tags of this Case reach the Spec. `estimate-ledger-write-refuses-a-lesson-with-an-unlisted-tag` and `estimate-case-check-sends-back-an-unlisted-tag` stand too: they speak of the refusal of an unlisted tag, which stays as it is. No sentence of a live page becomes false. `tags.md` names no count of its rows, and the lesson page states its tags only in its `tags` field.

> **problem:**
> The tags the agent needs to mark lessons on how `case-guppi` builds a Case and on the `/pre-spec` check do not exist, so the ledger hook refuses them and the lesson that asked for them carries only broad tags.

> **recommend:**
> - **Should the two tags be added, and on which pages?**
>   - Recommended: (a) add both, and tag only `lesson-case-build-misses-the-example-a-changed-check-runs-over`, the lesson that asked for them.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: after the pre-spec findings, keep the target as it is, name `estimate-spec-write-reads-a-new-tag`, and say in `context` and `then` that the cascade of Case 736.1 archives the lesson in the same run and that the point of the Case is the declaration of the tags for later lessons and pages; no tags on rule pages.
>   - Taken: `context` names that Estimate and the archiving, and the `then` line on the lesson says that the cascade archives it and `rule-cleanup` moves it.

> **given:**
> `vault/wiki/tags.md`: the list of tags a page may carry.
> **＋** `lesson-case-build-misses-the-example-a-changed-check-runs-over`: the lesson that asked for the two tags.
> **＋** `insight-workflow-contract-change-leaves-its-derived-text-stale`: the Insight of that lesson, which Case 736.1 sets `actioned`.
> **＋** `guppi/generate.py`: `register_tags` writes a declared tag into `tags.md` at the librarian's run, and its cascade archives the `clustered` lessons of an `actioned` Insight.
> **＋** `rule-cleanup`: moves an archived page out of the live pages.
> **＋** `guppi/ledger.py`: the ledger hook, which refuses a lesson line with a tag that is not listed.
> **＋** `rule-ledger-write`: the rule of that refusal; it stands.

> **when:**
> `guppi generate` of `guppi/generate.py` applies the `then` block of this Case at the librarian's run.
> **＋** Or the ledger hook of `guppi/ledger.py` judges a fresh lesson line whose `{tags:...}` names `case-build` or `prespec`.

> **then:**
> `vault/wiki/tags.md` holds a row for `case-build` and a row for `prespec`, each with its meaning and its Russian aliases.
> **＋** `lesson-case-build-misses-the-example-a-changed-check-runs-over` carries the tags `workflow`, `tests`, `case-build` and `prespec`; in the same run the cascade of `guppi/generate.py` sets it `archived`, since `insight-workflow-contract-change-leaves-its-derived-text-stale` stands `actioned`, and `rule-cleanup` moves it out of the live pages.
> **＋** The ledger hook of `guppi/ledger.py` writes such a lesson line, in this session after the ratification of this Case and in each later session.
> **－** No other page changes its tags.

> **tasks:**
> - [ ] tag `case-build`
>   - meaning: `how case-guppi builds a Case: its rounds, its reading of the frame and the file it writes`
>   - aliases: `сборка кейса, построение кейса`
> - [ ] tag `prespec`
>   - meaning: `the check of the ratified Cases before the Spec: /pre-spec, its hook and its findings`
>   - aliases: `пре-спек, проверка плана`
> - [ ] update `lesson-case-build-misses-the-example-a-changed-check-runs-over`
>   - set: `{tags: [workflow, tests, case-build, prespec]}`
>   - change: `tagged case-build and prespec, the tags the ledger hook refused at the Retro of session 0213 (case 737)`

> **ratification:**
> ```
> - decision[case 737][update][lesson-case-build-misses-the-example-a-changed-check-runs-over]{ref:lesson-case-build-misses-the-example-a-changed-check-runs-over}
> ```
