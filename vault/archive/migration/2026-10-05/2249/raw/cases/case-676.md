## Case 676 — The draft of the subagent rule leaves the backlog

> **context:**
> The draft `rule-subagent-guppi` was to say what a subagent may do in Work Mode, and how a fork that a subagent meets comes back to the main agent as a Case. It holds only its Purpose, and it waits in the backlog in two places: as a page with `deferred_by`, and as a line of `## Backlog` in `entity-sprint-migration`. The backlog counts 29 sessions that put it off, and no Case took it up since case 183. While the backlog was reviewed, the main agent proposed to delete it: what still matters of it is closer to `rule-work-mode`, which stays in the backlog. The person agreed. So this Case deletes the page, and `rule-work-mode` does not change.
> The vault's answer: the Case creates no page, so no vault query on a `create` ran. The Frontier line has the source `backlog`, and the page carries `deferred_by` the Decisions of cases 183, 206, 218, 231, 242, 248, 252, 254, 260, 263, 269, 276, 281, 285, 289, 293, 303, 307 and 322, so the delete line carries one `{supersedes:case N}` for each of them, as case 675 did for the one defer of the draft it deleted. All nineteen Decision pages stand archived: a Glob of their paths under `vault/archive/migration/2026-09-28/1318/decisions/` printed all nineteen, and the same Glob under `vault/wiki/decisions/` printed none. Today `generate.decision` sets such a page `superseded` again, and `guppi cleanup` would then bring it back to the live vault. Case 683 of this session fixes that: an archived Decision that a later Case supersedes stays `archived` where it lies and only takes the later Decision into `superseded_by`, with one History line, while the defers it names are cleared as for any supersede. The nineteen marks of this Case rely on the code of Case 683 standing in the working tree before the librarian's run of this session. Case 683 replaces the Criterion of `estimate-generate-writes-the-decision-page`, whose line on a `supersedes` describes what the nineteen marks do; that Estimate, read in the Retro of this session, checks this part of this Case, and this Case does not change its Criterion again. The one sentence on a subagent's fork that stays in force is in `ratification.md`, the Render of `rule-ratification`: a subagent that hits a fork stops and returns, and never decides; it does not depend on the draft, and it stands.
> The frame. A Grep `rule-subagent-guppi` over `{vault/wiki/**,guppi/**,.claude/**,tests/**}` printed 5 files: `vault/wiki/brief.md`, `vault/wiki/backlog.md`, `vault/wiki/log.md`, `vault/wiki/entities/entity-sprint-migration.md` and `tests/test_sprint.py`. The librarian writes `backlog.md` and `brief.md` from the pages, and `log.md` is history; they were not read, and they stand. In `entity-sprint-migration` the hit is the line of `## Backlog` that links the page. This Case does not change that page: the page carries `deferred_by` the Decision of case 642, and its open Frontier line C9 is Case 680 of this session, which removes the plain lines of the same section and retires that defer. The check of this file sends back a Case that names the page without `{supersedes:case 642}`, and that mark belongs to Case 680, not to this Case. So Case 680 needs one more `replace` pair that removes the line of `[[rule-subagent-guppi]]` from `## Backlog`, so that no live page links to the deleted page; until it does, the `make lint` of the librarian's run reports that link. In `tests/test_sprint.py` the slug names a page of a fixture vault that the test writes itself, so the test does not read the live page and it stands. The deleted page carries no promise. `estimate-backlog-renders` checks that `## Deferred` of `backlog.md` lists each live page with `deferred_by` and each line of the `## Backlog` of the sprint page; once the page and its line are gone, through this Case and Case 680, neither is listed, so its Criterion stays true and stands, and it checks this Case. `estimate-prespec-requires-a-backlog-item-decided-on-its-page` checks that the Case names the page and carries each mark, which the delete line does. The `make lint` of the librarian's run checks that no live page links to the deleted page.

> **problem:**
> A draft page that no Case took up in 29 sessions holds a place in the backlog twice, as a page and as a line of the sprint page, while what still matters of it belongs with `rule-work-mode`.

> **recommend:**
> - Recommended: delete `rule-subagent-guppi`, and retire each of its defers; Case 680 removes its line from the `## Backlog` of `entity-sprint-migration`; `rule-work-mode` stays in the backlog as it is.
>   Answer: ratified as built
> - **Change**
>   - Asked: the person agreed to the fixes of the pre-spec report: say that the nineteen Decisions the delete line supersedes stand archived, that the marks rely on the code of Case 683 in the working tree before the librarian's run, and name `estimate-generate-writes-the-decision-page` as Case 683 replaces it.
>   - Taken: `context` and the `impact` of the delete say so, and `given` names the case file of Case 683.

> **given:**
> `rule-subagent-guppi`: the draft page of the backlog item, which this Case deletes.
> **＋** `rule-page-generation`: the rule of `guppi generate`, which deletes the page and retires the defers.
> **＋** `vault/raw/2026-10-05/2249/cases/case-683.md`: Case 683, which keeps an archived Decision archived when a later Case supersedes it.
> **＋** `vault/wiki/backlog.md`: the backlog that lists a deferred page and each line of the sprint page's `## Backlog`.
> **＋** `rule-work-mode`: the draft of the rest of Work Mode, which stays in the backlog as it is.

> **when:**
> `guppi generate` of `rule-page-generation` applies the decisions of this Case, and `guppi backlog` writes `vault/wiki/backlog.md`.

> **then:**
> `rule-subagent-guppi` no longer stands under `vault/wiki/`.
> **＋** `vault/wiki/backlog.md` no longer lists `rule-subagent-guppi` under `## Deferred`.
> **－** `rule-work-mode` does not change, and it stays in the backlog.

> **tasks:**
> - [ ] delete `rule-subagent-guppi`
>   - impact: `the draft of the backlog leaves; what still matters of it is closer to rule-work-mode, which stays in the backlog; a subagent that hits a fork still stops and returns, as ratification.md sets; each defer of its deferred_by is retired by the supersedes marks of this line; the nineteen Decision pages they name stand archived and stay archived by the code of case 683, which stands in the working tree before the librarian's run`

> **ratification:**
> ```
> - decision[case 676][delete][rule-subagent-guppi]{ref:rule-subagent-guppi}{supersedes:case 183}{supersedes:case 206}{supersedes:case 218}{supersedes:case 231}{supersedes:case 242}{supersedes:case 248}{supersedes:case 252}{supersedes:case 254}{supersedes:case 260}{supersedes:case 263}{supersedes:case 269}{supersedes:case 276}{supersedes:case 281}{supersedes:case 285}{supersedes:case 289}{supersedes:case 293}{supersedes:case 303}{supersedes:case 307}{supersedes:case 322}
> ```
