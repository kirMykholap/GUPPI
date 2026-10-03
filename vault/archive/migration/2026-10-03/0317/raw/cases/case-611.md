## Case 611 — The Stop check refuses a showing of a Case with the agent's own text outside its list and ratification

> **context:**
> When `case-guppi` has built a Case, the main agent shows it in one reply. It sends the Case file. It writes the Case heading with the name in Russian, one list under the heading with a short text on each Case and sub-case, and one `ratification` with the ledger lines. The agent's own text comes only after one horizontal rule. `orchestration.md`, the Render of `rule-orchestration`, sets this layout, and the promise of `estimate-orchestration-shows-the-built-case` states it. The `Stop` run of `guppi/casecheck.py` compares the `ratification` with the stored answer. Since case 562 it also refuses a round of questions that has the agent's own text before it. Nothing reads the other text of a showing: its docstring says that text under the heading outside its sections is not compared. In session 0115 the batch showing after `/pre-spec` put a sentence on the renumbering of Case 608 between the heading of Case 610 and its list. Nothing refused it. The reading of `estimate-orchestration-shows-the-built-case` failed on it (ledger line 18 of `raw/2026-10-03/0115/ledger.md`). `lesson-orchestration-own-sentence-between-heading-and-list` records it. That lesson and `lesson-orchestration-own-text-before-a-prespec-round` reopened `insight-case-form-chat-form-read-by-no-script` at the synthesis of 0115.
>
> The person chose that the check refuse such a note rather than allow it. The check reads the whole showing up to the horizontal rule, heading by heading. The person read text before the heading as part of the showing. The agent's own text written in the turn before its last tool call also stands above the heading in the chat, so this Case judges it too. It uses the same judgment of that text, `texts_before_last_call`, that the check of a round has used since case 562, with no second copy (`rule-one-judgment-one-implementation`). A Case heading here is `## Case N —` or `### Case N.M —`. A sub-case shown alone under its own heading is judged the same way. Any section other than `ratification` under a heading is refused, since `orchestration.md` already forbids showing `given`, `when`, `then` or `tasks`.
>
> The new promise is `estimate-case-check-refuses-text-outside-the-list`, on `rule-case-check`. Three Estimates stand as they are:
> `estimate-case-check-refuses-text-before-a-round` keeps its Criterion, because it speaks only of a turn that holds a round.
> `estimate-case-check-shows-only-the-checked-case` keeps its Criterion. It speaks of the comparison with the stored answer, which does not change. Its line that text under the heading outside its sections is not compared stays true of that comparison. Its line that a showing of the heading, a short text and `ratification` alone passes when its `ratification` equals the answer also stands, because the short text of a showing is the list item that `orchestration.md` sets. That showing passes both the comparison and the new check. A short text that is not a list item is refused by the new check, and that promise does not speak of it.
> `estimate-orchestration-shows-the-built-case` keeps its Criterion word for word, because it already forbids the note. It is read again in a later session.
> The reader in code changes, and the text it enforces already stands in `orchestration.md`, so nothing waits for a render. The refusal loses nothing: a showing carries its ledger lines only as a preview, never in a `LEDGER` block, and the refused reply is shown again. So the check keeps no old form.
>
> The frame contains these facts. `.claude/settings.json` registers six commands on `Stop`: `guppi ledger`, `guppi ratified`, `guppi casecheck`, `guppi context`, `guppi onward` and `guppi onward --plan`. None of the others sets the layout of a showing. The Spec hook `guppi ratified` reads a showing by `showings` and is not changed. A Grep of `casecheck` over `tests/test_ratified.py` printed only calls of `store_of`, `shows_sections`, `shown_text` and `case_file`, not the `Stop` run, so its tests are not touched. In `.claude/skills/pre-spec/SKILL.md`, step 6 shows each Case built again in the showing that `orchestration.md` sets, so the batch is judged like any showing. In the turn of that showing, the last answer of a `case-guppi` opens the turn, and no `**Waiting:**` line stands there.
>
> In `tests/test_casecheck.py`, a multiline Grep of `show\(\s*working,\s*ANSWER` printed six calls, at lines 819, 823, 829, 970, 1320 and 1329:
> Line 819 expects exit 0 with the full answer under its heading, and it changes.
> Lines 823, 829 and 1320 expect exit 2 with reasons that still come.
> Lines 970 and 1329 are the re-fire.
>
> A Grep of `== \(0, ""\)` over the same file printed further `show(` calls that expect exit 0 with sections under a heading, or with a short text that is not a list item. They are at lines 842, 870, 872, 891, 910, 922, 951, 963, 964, 1020 and 1290, the last one on `RECUT`. These now get the layout reason too. Where such a test checks the comparison, it asserts the comparison's reason alone. Where it checks a pass, it shows the list layout, as `SHORT_SHOWING` will with its short text as a list item. The other calls that this Grep printed are not judged by the new check, or already pass it:
> The acknowledging reply, a `DIFF` fence and the short form are at lines 928, 941, 942 and 943.
> A list showing is at line 1001.
> Replies with no Case heading are at lines 1098, 1109, 1111 and 1124.
> A re-fire is at line 1151.
>
> A Grep of `showing of a Case|shows a Case|show(s|n)? the Case` over `vault/wiki/rules/` and `.claude/` printed one file: `vault/wiki/rules/rule-orchestration.md`, the source of `orchestration.md`, which sets the layout this Case enforces.
>
> A Grep of `outside its sections|under the heading` over `vault/wiki/` outside `decisions/`, `.claude/`, `guppi/` and `tests/` printed 13 files. They are `brief.md`, `orchestration.md`, `case-schema.md`, `log.md`, `rules/rule-case-protocol.md`, `lessons/lesson-orchestration-own-sentence-between-heading-and-list.md`, `rules/rule-case-check.md`, `guppi/casecheck.py`, `tests/test_casecheck.py`, `rules/rule-orchestration.md`, `estimates/estimate-case-check-shows-only-the-checked-case.md`, `tests/test_ratified.py` and `guppi/generate.py`. Each one stays true, for these reasons:
> `orchestration.md` and its source set the layout.
> `case-schema.md` and its source `rule-case-protocol` speak of the heading of the Case file.
> The docstring of `guppi/casecheck.py` and the Estimate speak of the comparison.
> The test at line 617 of `tests/test_ratified.py` shows a list under its heading, which the new check passes.
> Line 474 of `guppi/generate.py` speaks of the Spec.
> The hit in `tests/test_casecheck.py` heads the tests of the list showing.
> `brief.md` and `log.md` were not read.
>
> A Grep of `insight-case-form-chat-form-read-by-no-script` over the repository outside `vault/wiki/decisions/` printed 54 files. Six are in `vault/wiki/`: `brief.md`, `backlog.md`, `log.md`, the two lessons, and `rules/rule-case-check.md`, whose Purpose says that until case 419 no script read a Case before its ratification, which stays true. Three are in `vault/raw/2026-10-03/`: `0317/ledger.md`, `0317/frontier.md` and `0115/materialize.yaml`, which are records of the sessions. The other 45 are under `vault/archive/`.
>
> The Insight is set `actioned`, as case 605 did after the check of a round. Its `addressed_by` names `decision-case-611`. Its two live children stand `clustered`, so the cascade of `guppi/generate.py` archives them, and `guppi backlog` drops the Insight's line. Both lessons stand in the ledger of session 0115, so no decision line carries `{addresses}`. The Insight has no `deferred_by`, so no `{supersedes:case N}` block is needed. `insight-workflow-case-schema-silent-on-what-the-scripts-accept` is not touched: it is about the forms the scripts accept in a Case, not about the layout of a showing. The Case makes no `create` without a `ref`, so the vault query was not run.
>
> Not done: `orchestration.md` and the Criteria of the three Estimates above do not change. The comparison of `given`, `when`, `then` and `tasks` in a showing stays in the code, although the new check now refuses a showing of those sections.

> **problem:**
> The rule of how a built Case is shown puts every text of the agent's own after the horizontal rule, but no script reads that part of a showing. In session 0115 a note under the heading of a Case went through, and the reading of `estimate-orchestration-shows-the-built-case` failed. The question was whether such a note is allowed, or whether the `Stop` check of `rule-case-check` refuses it, and how much of the showing the check reads.

> **recommend:**
> - **A note between the Case heading and its list**
>   - Recommended: (a) the check refuses it; a note goes after the horizontal rule.
>   - Answer: agreed, (a).
> - **How much of the showing the check reads**
>   - Recommended: (b) the whole showing up to the horizontal rule: nothing before the first Case heading, and under each heading only the list, the `ratification` blockquote and blank lines.
>   - Answer: accepted the recommendation, (b).
> - **What checks the new refusal**
>   - Recommended: (a) a new promise of its own on `rule-case-check`; the promise on rounds and the comparison promise stand.
>   - Answer: accepted the recommendation, (a).
> - **The failed reading and the open insight**
>   - Recommended: (a) the promise of `estimate-orchestration-shows-the-built-case` stays word for word and is read again in a later session; the insight is marked as acted on; `insight-workflow-case-schema-silent-on-what-the-scripts-accept` is not touched.
>   - Answer: accepted the recommendation, (a).

> **given:**
> `guppi/casecheck.py` — the `Stop` run that gains the refusal; its docstring says how it works
> **＋** `tests/test_casecheck.py` — the tests of the `Stop` run
> **＋** `.claude/settings.json` — registers `uv run guppi casecheck` on `Stop`
> **＋** `rule-case-check` — the rule of the check; its Purpose gains the refusal
> **＋** `estimate-case-check-refuses-text-outside-the-list` — the new promise
> **＋** `vault/wiki/orchestration.md` — rendered from `rule-orchestration`; sets the layout of a showing that the check enforces
> **＋** `estimate-orchestration-shows-the-built-case` — the promise of the showing, read again
> **＋** `insight-case-form-chat-form-read-by-no-script` — the Insight on rules of the chat form that no script reads, set `actioned`

> **when:**
> `Stop` fires after a reply of the main agent that shows a Case under `## Case N —` or `### Case N.M —` with at least one of its sections, not a deferred decision in the short form, and `uv run guppi casecheck` runs on it, as `.claude/settings.json` registers it.

> **then:**
> `uv run guppi casecheck` exits 2 when a line that is not blank stands in the reply before its first Case heading.
> **＋** It exits 2 when a line stands between a Case heading and the next Case heading or the horizontal rule `---` that is not blank, not a list item — a line that opens with `- `, `* ` or a number and `. ` — not a line indented under a list item, and not a line of the `ratification` blockquote, its `> **ratification:**` line and the `>` lines after it.
> **＋** It exits 2 when the main agent wrote text in the turn of the reply before its last tool call, judged by `texts_before_last_call` of `guppi/casecheck.py`, the judgment the check of a round uses.
> **＋** Its reason on stderr quotes the first such text and tells the agent to show the Case again with that text moved after the horizontal rule.
> **＋** The check runs in the same `Stop` run as the comparison of shown Cases with the stored answer and the check of how a round opens, and a reply that more than one of them refuse gives each reason.
> **－** Text after the horizontal rule is not judged.
> **－** A reply with no Case heading that holds a section, the acknowledging reply among them, a fence tagged `DIFF`, and a deferred decision in the short form are not judged.
> **－** On the re-fire (`stop_hook_active`) it exits 0, so the Case shown again after a refusal is not judged again.
> **－** It stores nothing and writes no file.

> **tasks:**
> - [ ] `guppi/casecheck.py`: the `Stop` run refuses a showing with text before its first Case heading, text under a Case heading that is not a list item, its indented line or the `ratification` blockquote, and text of the main agent's own before the last tool call of the turn; the text before the last tool call is judged by the existing `texts_before_last_call`, and the `ratification` blockquote by the existing `RATIFICATION_HEAD` and `quoted_sections`, with no second copy of either; the module docstring says how
> - [ ] `tests/test_casecheck.py`: tests of each refusal, of a list showing and a batch that pass, of text after the horizontal rule left alone and of the re-fire; the `show(` calls that expect exit 0 with sections under a heading or a short text that is not a list item show the list layout where they check a pass, and assert the comparison's reason alone where they check the comparison
> - [ ] update `rule-case-check`
>   - set: `{purpose: "Prevents a Case from being shown to the person in a form the checks of pre-spec refuse, or with other given, when, then, tasks or ratification than the ones that passed them, a round of case-guppi from reaching the main agent with a question out of the form of the grill-me template, a round of case-guppi from being shown after a text of the main agent's own, and a Case from being shown with a text of the main agent's own outside the list under its heading and its ratification"}`
>   - old: `` (case 601.1), and a round of `case-guppi` from being shown after a text of the main agent's own (case 562) ``
>   - new: `` (case 601.1), a round of `case-guppi` from being shown after a text of the main agent's own (case 562), and a Case from being shown with a text of the main agent's own outside the list under its heading and its `ratification` (case 611) ``
>   - change: `the Stop check refuses a showing of a Case with a text of the main agent's own outside the list under its heading and its ratification (case 611)`
> - [ ] create `estimate-case-check-refuses-text-outside-the-list`
>   - ref: `rule-case-check`
>   - kind: `QA`
>   - purpose: `Whether the Stop run of the Case check refuses a reply that shows a Case with a text of the main agent's own before its first Case heading, under a heading outside the list and the ratification, or before the last tool call of the turn`
>   - method: `uv run pytest tests/test_casecheck.py; by hand in a later session, the showings of Cases and the hook's refusals of them read in the transcript`
>   - tags: `[hooks, harness, workflow]`
> - [ ] update `insight-case-form-chat-form-read-by-no-script`
>   - set: `{status: actioned, addressed_by: decision-case-611}`
>   - change: `actioned: the Stop check of rule-case-check refuses a showing of a Case with a text of the main agent's own outside the list under its heading and its ratification (case 611)`
> - [ ] read `estimate-case-check-refuses-text-outside-the-list`
> - [ ] read `estimate-orchestration-shows-the-built-case`

> **ratification:**
> ```
> - decision[case 611][update][rule-case-check]{ref:rule-case-check}
> - decision[case 611][create][estimate-case-check-refuses-text-outside-the-list]{ref:rule-case-check}{tags:hooks,harness,workflow}
> - decision[case 611][update][insight-case-form-chat-form-read-by-no-script]{ref:insight-case-form-chat-form-read-by-no-script}
> ```
