## Case 858 — The record of the put-off session-files reading notes that the git-init /hi ends

> **context:**
> At the `/hi` of session 0342 the person put off `estimate-clean-branch-writes-the-session-files`, by the short-form defer of Case 855. Its Decision page, `decision-case-855`, keeps the context of that defer, since a short-form Case has no Case file. That context says that Case 851 makes `/hi` offer `git init -b main` and go on to `/sprint-open`, and that the context of Case 851 says the Criterion of the Estimate holds with it. Both claims were true when Case 855 was ratified. Later, at the pre-spec of the same session, Case 851 changed: on the yes the agent runs `git init -b main` and ends `/hi`, and the person types `/hi` again (the `**Change**` items of `vault/raw/2026-10-16/0342/cases/case-851.md`). The rendered `.claude/skills/hi/SKILL.md` now says: "After either answer, start no `/sprint-open`, write no Frontier, and end the reply." The ratified context of Case 851 now says that in a folder with no git the session opens at the `/hi` after the person's `git init -b main`, and it no longer says that the Criterion holds. The handoff of session 0342 (Notes) and the brief (Flags, Next session) report the contradiction. The handoff says the defer itself stands. The `## Problem` and the `## Deferred` of the page describe what was true when the defer was signed, and this Case leaves them as they are.
>
> `rule-decisions-schema` says that a decision is not edited: only `status` and `superseded_by` change, and one more History line is allowed, `updated:` of a Case that signs the page's text after the fact (case 358). So this Case leaves the `## Context` as it was ratified. It adds one History line, by an `update` with `change` alone, that says how the text reads today. That is the form Case 358 used on `decision-case-347`, and `update` of `.guppi/guppi/generate.py` writes History `updated: <change>` for an entry that carries only `change`. Replacing the sentence was turned down because it edits the body of a Decision page, against that rule. A reader shown the page through the page-read hook does not see History, and that cost was accepted.
>
> Case 859 of this session replaces the Criterion of `estimate-clean-branch-writes-the-session-files`, and its decision line carries `{supersedes:case 855}`. That mark retires the one defer of `decision-case-855`, so the cascade of `generate` sets the page `superseded` and then `archived`. This Case does not cover that change. The History line still stands on the retired page, for two reasons. First, a Decision page stays a record after it is archived, and its `## Context` keeps the false sentence. Second, `update` of `.guppi/guppi/generate.py` reaches a page under `vault/archive/` when it is not under `wiki/` (case 105.3), so the update applies whether it runs before or after the cascade. The line says nothing of the defer. Case 859 retires the defer, and the cascade writes its own History line for that, so nothing is said twice.
>
> How it is checked: `estimate-decisions-schema-checked` (passed) checks that a Decision page in the shape of the schema has no schema finding. It also checks that the schema allows one `updated:` History line of a Case that signs the text after the fact. This Case adds only such a line and keeps the page in that shape, so the Criterion stands and the Estimate is not set `pending`. No Estimate reads the words of the line. They rest on the librarian's run applying the update as signed.
>
> Searches. A Grep for `decision-case-855` over `vault/wiki/`, which the search hook runs without `decisions/`, printed `vault/wiki/brief.md`, `vault/wiki/log.md` and `vault/wiki/estimates/estimate-clean-branch-writes-the-session-files.md`. The brief and the log are records. The Estimate names the page in `deferred_by`, which Case 859 changes when it retires the defer. A Grep for `decision-case-855|ROOT.*decisions|VAULT.*decisions|REPO.*decisions` over `.guppi/tests/` printed only lines of `.guppi/tests/test_generate.py` that seed a vault under `tmp_path`. No test reads `decision-case-855` live. Cases 856 and 857 of this session change neither this page nor `/hi`.
>
> The person agreed to rebuild this Case after it was first ratified, so that it fits Case 859.

> **problem:**
> The Context of `decision-case-855` says that the `/hi` that offers `git init -b main` goes on to `/sprint-open`, and that the context of Case 851 says the Estimate holds with it. Since the pre-spec change of Case 851, that `/hi` ends after the person's answer, and the next `/hi` starts `/sprint-open`.

> **recommend:**
> - **How should the false sentence on `decision-case-855` be fixed?**
>   - Recommended: (b) add a correction line to History only, by an `update` with `change` alone; the `## Context` stays as it was ratified.
>   - Answer: agreed, (b).
> - **What checks that the correction landed?**
>   - Recommended: (a) the existing `estimate-decisions-schema-checked` checks it, its Criterion unchanged.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: rebuild the Case so that it fits Case 859, which retires the defer of `decision-case-855`: the `context` says why the update stands on a page that Case 859 retires, and the `change` no longer says that the defer stands.
>   - Taken: the `change` drops "the defer stands"; the `context` explains the retirement by Case 859 and why the History line still applies; `given` names the file of Case 859; the `－` line of `then` no longer says that the fields of the page do not change.

> **given:**
> `decision-case-855`: the Decision page of the defer, whose History takes the correction.
> **＋** `rule-decisions-schema`: a Decision page is not edited, but for one `updated:` History line of a Case that signs its text after the fact.
> **＋** `estimate-decisions-schema-checked`: checks that a Decision page keeps the shape of the schema.
> **＋** `.claude/skills/hi/SKILL.md`: the `/hi` that offers `git init -b main` ends after either answer.
> **＋** `vault/raw/2026-10-16/1712/cases/case-859.md`: retires the defer of `decision-case-855`, which the cascade then archives.
> **＋** `/sprint-open`: the skill that the next `/hi` starts, as `rule-skill-sprint-open` sets it.
> **＋** `.guppi/guppi/generate.py`: `update` writes History `updated: <change>` for an entry with `change` alone.

> **when:**
> Someone reads `decision-case-855` after the librarian's run of this session.

> **then:**
> The History of the page holds an `updated:` line that says that the `/hi` that runs `git init -b main` ends after the person's answer, that the next `/hi` starts `/sprint-open`, and that the Context sentence saying otherwise is out of date.
> **－** The `## Context`, the `## Problem` and the `## Deferred` of `decision-case-855` do not change.
> **－** `estimate-decisions-schema-checked` finds no schema defect on the page.

> **tasks:**
> - [ ] update `decision-case-855`
>   - change: `the Context is out of date since the pre-spec change of Case 851 in session 0342: the /hi that runs git init -b main ends after the person's answer and starts no /sprint-open, the next /hi starts it, and the context of Case 851 no longer says that the Criterion of estimate-clean-branch-writes-the-session-files holds`

> **ratification:**
> ```
> - decision[case 858][update][decision-case-855]{ref:decision-case-855}
> ```
