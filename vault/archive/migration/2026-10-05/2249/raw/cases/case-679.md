## Case 679 — The Insight on the refused `!` commands names its real cause and closes

> **context:**
> Before a call that is not read-only runs, Claude Code checks it with a model call. That covers a `!` command of a skill, and an Agent or SendMessage call in plan mode. When the check gives no verdict, the call is refused. `insight-hi-skill-substitution-checked-by-a-model-call` groups the lessons of this failure. Its `pattern`, `## Pattern` and `## Proposal` name a lapsed login as the cause and `/login` as the cure. Case 246 rejected that Proposal and set the Insight `actioned`. Then `lesson-hi-substitution-gets-no-verdict-from-the-server-side-classifier` found the real cause, and `/login` did not help. The real cause: since client 2.1.282 the check is made by a server-side classifier, and for a `!` substitution that the person types, it gives no verdict. Case 439 listed the `!` commands of `/hi` under `allowed-tools`, so they need no verdict. Case 448 put off the rewrite of the Pattern and Proposal. `lesson-plan-mode-agent-and-sendmessage-pass-the-auto-mode-classifier` then reopened the Insight: in plan mode, Agent and SendMessage calls were refused the same way, and the same calls went through once the server answered again. In the backlog review the person chose to close the Insight as a fault of Claude Code's environment, not of the harness. In the round the person also chose to rewrite the cause first (Q1) and to replace the text of `## Proposal` with the outcome (Q2), since `guppi generate` replaces the text of a section and cannot remove its heading.
> The vault's answer: this Case creates no page, so no vault query on a `create` ran. Per `rule-insights-schema`, an `update` that sets `status: actioned` and `addressed_by` rejects an Insight. Case 246 did the same. The page carries `deferred_by` the Decision of case 448, so the decision line carries `{supersedes:case 448}`. Once the Insight is `actioned`, the cascade of `generate` archives its one live `clustered` lesson. `rule-skill-hi` already states the server-side cause and the `allowed-tools` cure, and it stays as it is.
> The frame. A Grep `insight-hi-skill-substitution-checked-by-a-model-call` over `{vault/wiki/**,guppi/**,.claude/**,tests/**}` printed 4 files: `vault/wiki/backlog.md`, `vault/wiki/log.md`, `vault/wiki/estimates/estimate-backlog-renders.md` and `vault/wiki/lessons/lesson-plan-mode-agent-and-sendmessage-pass-the-auto-mode-classifier.md`. The librarian writes `backlog.md` from the pages, and `log.md` is history, so they stand. The hit in `estimate-backlog-renders` is in its `## Result`, a past reading, so it stands. The lesson names the Insight in its `insight` field, which stays true. A Grep `lapsed login` over `{vault/wiki/**,.claude/**}` printed 3 files: `vault/wiki/backlog.md`, `vault/wiki/log.md` and the Insight page itself. So no rule and no harness file states the old cause. The Insight page carries no Estimate. `estimate-backlog-renders` checks this Case: its Criterion lists an Insight under `## Deferred` only while its `status` is `open`, so once the page is `actioned` it leaves `backlog.md`. That Criterion stays true and stands. `estimate-insights-schema-checked` checks that an `actioned` Insight carries `addressed_by`, and this Case writes it, so that Criterion stands too.

> **problem:**
> An open Insight names a lapsed login as the cause and `/login` as the cure. Later lessons refuted both. The failure comes from Claude Code's server, and the harness has nothing to fix.

> **recommend:**
> - **What the closed Insight says is the cause**
>   - Recommended: (a) rewrite the cause, then close: the `pattern` and `## Pattern` name the server-side check that gives no verdict, the `/login` cure goes, and the Insight is set `actioned` as rejected.
>   - Answer: agreed, (a).
> - **What happens to the Proposal section**
>   - Recommended: (a) replace its text with the outcome: the harness has nothing to fix, and `/hi` gets past the check because its `!` commands are allowed in `rule-skill-hi`.
>   - Answer: agreed, (a).

> **given:**
> `insight-hi-skill-substitution-checked-by-a-model-call`: the Insight that this Case rewrites and closes.
> **＋** `rule-insights-schema`: the form of an Insight and of the `update` that rejects it.
> **＋** `rule-page-generation`: the rule of `guppi generate`, which applies the update, retires the defer and archives the lessons of an `actioned` Insight.
> **＋** `vault/wiki/backlog.md`: the backlog, which lists each `open` Insight.
> **＋** `rule-skill-hi`: the rule that names the `!` commands of `/hi` in `allowed-tools`.

> **when:**
> `guppi generate` of `rule-page-generation` applies the decision of this Case, and `guppi backlog` writes `vault/wiki/backlog.md`.

> **then:**
> `insight-hi-skill-substitution-checked-by-a-model-call` is `actioned`, and its `addressed_by` names the Decision of this Case.
> **＋** Its `pattern` and `## Pattern` name as the cause the server-side check of Claude Code, which gives no verdict on a call that is not read-only.
> **＋** Its `## Proposal` says that the harness has nothing to fix, and that `/hi` gets past the check through the `allowed-tools` of `rule-skill-hi`.
> **＋** No text of the page gives a fresh login as the cure.
> **＋** Its `clustered` lessons are `archived`.
> **＋** `vault/wiki/backlog.md` no longer lists it.
> **－** `rule-skill-hi` does not change.

> **tasks:**
> - [ ] update `insight-hi-skill-substitution-checked-by-a-model-call`
>   - set: `{status: actioned, addressed_by: decision-case-679, pattern: "A call that is not read-only — a ! command of a skill, an Agent or SendMessage call in plan mode — is checked by Claude Code's server-side classifier before it runs; when that server gives no verdict the call is refused, and the same call passes once the server answers again; a call that a permission rule allows needs no verdict."}`
>   - sections.Pattern:
>     ```
>     Four lessons, one cause. At /hi of sessions 1119 and 1252 the `!` substitution of `uv run guppi render --sync` was refused with the model reported unavailable; the second lesson took a lapsed login for the cause, since a /hi after /login ran whole. On 2026-09-26, in session 1b191eaf, /hi failed at every run: since client 2.1.282 the server-side classifier gives no verdict for a `!` substitution the person types, and a fresh /login did not help. On 2026-09-28, in session 1318, Agent and SendMessage calls in plan mode were refused the same way, and the same calls passed unchanged once the server answered again. The check is Claude Code's, made on its server before the call runs; the harness neither makes it nor sees why it fails. A call that a permission rule allows needs no verdict.
>     ```
>   - sections.Proposal:
>     ```
>     Rejected (case 679): the refusal comes from Claude Code's server, and the harness has nothing to fix. /hi gets past the check, since the `allowed-tools` of `rule-skill-hi` names its `!` commands and an allowed command needs no verdict.
>     ```
>   - change: `rejected — the cause rewritten: the server-side classifier of Claude Code gives no verdict, not a lapsed login; the /login cure removed; the harness has nothing to fix (case 679)`

> **ratification:**
> ```
> - decision[case 679][update][insight-hi-skill-substitution-checked-by-a-model-call]{ref:insight-hi-skill-substitution-checked-by-a-model-call}{supersedes:case 448}
> ```
