<!-- approved 20:43:32 · session f5656086 -->

# Spec — 2026-09-18, session 1957

## Case 245 — `entity-sprint-migration`: the Insight in the milestone of Slice 3b

> **context:**
> `entity-sprint-migration` holds the milestones of the sprint under `## Milestones`; Slice 3b has two items, `rule-work-mode` and `rule-subagent-guppi`. Case 238 deferred `insight-workflow-code-live-before-the-page-it-reads` to Slice 3b, but the milestone does not name it, so the brief (229.4 leaves out only what the sprint page names) and `/hi` carry it as an item of its own. `guppi sprint` ticks an item by the status of its page: `DONE = {built, passed, archived}`; an Insight `actioned` is not in it, and as a line `- [[insight-…]]` of its own it would never close. The Case touches no Estimate: the render of `sprint.md` does not change, the text of one item does.

> **problem:**
> Where on the sprint page to name the Insight so that it goes with `rule-work-mode` and does not stand as a separate item.

> **given:**
> The brief and `/carry` leave out of Deferred a target the sprint page names under a milestone or in its Backlog (case 229.4).
> **＋** `/hi` takes the Frontier from the current milestone (case 229.3).
> **－** An item line `- [[slug]]` is ticked only by a status in `DONE`; an Insight `actioned` is not in it.

> **when:**
> The librarian applied the `update` and `guppi sprint` wrote `sprint.md`; the next brief and the next `/hi` read it.

> **then:**
> The item line of `rule-work-mode` in Slice 3b names `[[insight-workflow-code-live-before-the-page-it-reads]]` — the sentence of its Proposal enters the rule; case 238 is in the list of cases.
> **＋** The brief leaves the Insight out of Deferred; `/hi` carries it inside the item of Slice 3b.
> **－** The Insight stays `open`, `deferred_by: decision-case-238`; it has no line of its own in the milestone.

```then
update:
  - slug: entity-sprint-migration
    replace:
      - old: "- [[rule-work-mode]] — Work Mode: the Spec as tasks with code, the ticked boxes in `spec.md`, the test of each Estimate written first and turned green; cases 183, 206"
        new: "- [[rule-work-mode]] — Work Mode: the Spec as tasks with code, the ticked boxes in `spec.md`, the test of each Estimate written first and turned green; the sentence of [[insight-workflow-code-live-before-the-page-it-reads]] on a check that reads a page the same Spec changes; cases 183, 206, 238"
    change: the item rule-work-mode of Slice 3b names the Insight deferred to it by case 238 (case 245)
```

```tasks
- [ ] update `entity-sprint-migration`: `replace` on the `rule-work-mode` line of Slice 3b
- [ ] `uv run guppi sprint` at the librarian's run
```

## Case 246 — `insight-hi-skill-substitution-checked-by-a-model-call`: rejected

> **context:**
> `insight-hi-skill-substitution-checked-by-a-model-call` — an Insight `open`, severity 2, made by the librarian of the 1252 run over `lesson-hi-substitution-refused-when-the-permission-classifier-is-unavailable` (session 1119: the cause named as the classifier's model, `render --check` by hand as the fallback) and `lesson-hi-substitution-fails-when-the-login-has-lapsed` (session 1252: the cause is a lapsed login, the cure is `/login` and `/hi` again; the first lesson was wrong). No Case touched it; session 1252 closed the question with the lesson. Its Proposal is one sentence in `rule-skill-hi`. `rule-skill-hi` is `built`, its Render is `.claude/skills/hi/SKILL.md`; its Estimate `estimate-hi-no-read-calls` is in the shape before case 193, so a change of the Render would bring a recut and a reading that only a live lapsed login can take. The Case touches no Estimate.

> **problem:**
> The Insight asks to write the cure into the rule. The check of a `!` command is the client's, not the harness's: the harness has nothing to refuse and nothing to guard, and the lesson of 1252 already holds the cause and the cure. The question: accept the Proposal, reject it or defer.

> **given:**
> The check of a skill's `!` command is a model call the client makes before the command runs; the SessionStart hook does not pass through it.
> **＋** A Rule guards a condition one case can break, with something to refuse it (case 240.2).
> **－** No code of the harness sees the client's login.

> **when:**
> At `/hi` a `!` substitution is refused with "unavailable" and the `Render:` line is empty.

> **then:**
> `rule-skill-hi` does not change; the cure — `/login` and `/hi` again — stands in the Insight's `pattern` and on the Decision page, not in the rule.
> **＋** The Insight is `actioned`; its lessons go to the archive by the cascade; a third lesson with the same cause reopens it.
> **－** Neither `render --check` by hand nor an allow entry for the command is a cure — the `pattern` says so.

```then
update:
  - slug: insight-hi-skill-substitution-checked-by-a-model-call
    set: {status: actioned, addressed_by: "[[decision-case-246]]"}
    change: "rejected — the check of a `!` command is the client's, the harness has no guard for a lapsed login, and the cure stands in the pattern and in lesson 1252; rule-skill-hi unchanged (case 246)"
```

```tasks
- [ ] update `insight-hi-skill-substitution-checked-by-a-model-call`: `status: actioned`, `addressed_by: [[decision-case-246]]`, rejected
```

## Case 247 — `entity-sprint-migration`: `rule-git-context` and `rule-github-issues` in Slice 5

> **context:**
> Slice 5 "closing" on `entity-sprint-migration` holds four items: `estimate-sprint-migration-lint-clean`, `estimate-sprint-migration-merges`, `rule-spec-box`, `rule-morph`. `rule-git-context` (the pull without an upstream, decision 11.1) and `rule-github-issues` (`gh` not logged in, no GitHub remote, decision 11.2) are both `built`, deferred by 220 and 243 "to the close of the sprint", but the milestone does not name them, so they surface in the brief (Deferred 3–4) and in the Frontier of every session. `guppi sprint` ticks an item by the status of its page and `built` is in `DONE`; an item without a wikilink is never ticked. The Case touches no Estimate: the text of one item changes.

> **problem:**
> Where on the sprint page to name the two rules so that they go with the close of the sprint, are not ticked before their time and do not stand in Deferred.

> **given:**
> The brief and `/carry` leave out of Deferred a target the sprint page names under a milestone (case 229.4).
> **＋** An item `- [[slug]]` is ticked by a status in `DONE`; `built` is in it, an item without a wikilink is never ticked.

> **when:**
> The librarian applied the `update` and `guppi sprint` wrote `sprint.md`; the next brief and `/hi` read it.

> **then:**
> The item `estimate-sprint-migration-merges` in Slice 5 names `[[rule-git-context]]` and `[[rule-github-issues]]` — the upstream of the branch and the GitHub remote are decided at the merge; cases 11.1, 11.2, 243 in the text.
> **＋** The brief leaves both rules out of Deferred; `/hi` does not carry them before Slice 5.
> **－** Both rules stay `built`, `deferred_by` as it is; they have no line of their own in the milestone.

```then
update:
  - slug: entity-sprint-migration
    replace:
      - old: "- [[estimate-sprint-migration-merges]] — `make test` green, `migration` merged into `main`"
        new: "- [[estimate-sprint-migration-merges]] — `make test` green, `migration` merged into `main`; the upstream of the branch and the GitHub remote decided at the merge — [[rule-git-context]], [[rule-github-issues]], cases 11.1, 11.2, 243"
    change: the item estimate-sprint-migration-merges of Slice 5 names rule-git-context and rule-github-issues, deferred to the close by cases 220 and 243 (case 247)
```

```tasks
- [ ] update `entity-sprint-migration`: `replace` on the `estimate-sprint-migration-merges` line of Slice 5
- [ ] `uv run guppi sprint` at the librarian's run
```

## Case 249 — `entity-sprint-migration`: the item text of Slice 5 names the reading

> **context:**
> Case 247 wrote `rule-git-context` and `rule-github-issues` into the item `estimate-sprint-migration-merges` of Slice 5 as "decided at the merge". Pre-task: the Criterion of `estimate-sprint-migration-merges` is `make test` and the merge, nothing on an upstream or a remote; the promise on decisions 11.1 and 11.2 is held by `estimate-sprint-migration-leftovers-gone` (Slice 4), and `## Closed` of the page points to it too. The item text attributed to one Estimate the promise of another and cited cases 11.1, 11.2, 243 in place of the defers 220, 243. The Case touches no Estimate: the same item text changes.

> **problem:**
> The item has to name both rules under Slice 5 without attributing to `estimate-sprint-migration-merges` a promise its Criterion does not hold.

> **given:**
> As in 247: the brief and `/carry` leave out of Deferred a target the milestone names (case 229.4); an item is ticked by the status of the page behind its first wikilink.
> **＋** The promise on decisions 11.1 and 11.2 is held by the Criterion of `estimate-sprint-migration-leftovers-gone`.

> **when:**
> The librarian applied the `update` and `guppi sprint` wrote `sprint.md`.

> **then:**
> The item `estimate-sprint-migration-merges` in Slice 5 names `[[rule-git-context]]` and `[[rule-github-issues]]` — the upstream and the GitHub remote, decisions 11.1, 11.2, defers 220, 243, read by `[[estimate-sprint-migration-leftovers-gone]]` at the close.
> **＋** The brief leaves both rules out of Deferred; `/hi` does not carry them before Slice 5.
> **－** No Criterion changes; both rules stay `built`, `deferred_by` as it is.

```then
update:
  - slug: entity-sprint-migration
    replace:
      - old: "- [[estimate-sprint-migration-merges]] — `make test` green, `migration` merged into `main`"
        new: "- [[estimate-sprint-migration-merges]] — `make test` green, `migration` merged into `main`; at the close [[rule-git-context]] and [[rule-github-issues]] — the upstream of the branch and the GitHub remote, decisions 11.1, 11.2, defers 220, 243 — read by [[estimate-sprint-migration-leftovers-gone]]"
    change: the item estimate-sprint-migration-merges of Slice 5 names rule-git-context and rule-github-issues, read by estimate-sprint-migration-leftovers-gone at the close (case 249, supersedes 247)
```

```tasks
- [ ] update `entity-sprint-migration`: `replace` on the `estimate-sprint-migration-merges` line of Slice 5, in place of case 247
- [ ] `uv run guppi sprint` at the librarian's run
```

## Deferred

## Case 248 — `rule-work-mode`, `rule-subagent-guppi`: Slice 3b to the next session

> **context:**
> `rule-work-mode` and `rule-subagent-guppi` are the two items of Slice 3b, the current milestone, both placeholders in `draft`, deferred by 183, 206, 218, 231 and 242; the draft of Work Mode stands in `docs/migration/rule-work-mode.md`. Since case 245 the item of `rule-work-mode` also names `insight-workflow-code-live-before-the-page-it-reads`, whose sentence enters the rule. This session took the five other Frontier items — two readings, three sprint-page and Insight decisions — and closed Plan Mode with Slice 3b untouched.

> **problem:**
> Slice 3b is a whole session's work: the body of two rules, their Estimates, the code of Work Mode. The person chose to close this session on the small items and open the next one on Slice 3b as its first item.

```then
defer:
  - slug: rule-work-mode
    type: rule
    purpose: Slice 3b, the first item of the next session — the body of Work Mode with the sentence of the Insight on a check that reads a page the same Spec changes
  - slug: rule-subagent-guppi
    type: rule
    purpose: Slice 3b, with rule-work-mode — what a subagent may do in Work Mode, and the fork that comes back as a Case
```
