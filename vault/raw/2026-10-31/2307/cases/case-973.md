## Case 973 — A bare link in the Result of the link graph Estimate

> **context:**
> `guppi lint` of `.guppi/guppi/lint.py` reads every `[[…]]` in the body of a live page as a link to a page, after `links_of` deletes each code span by `CODE_SPAN`, and `check_refs` reports a link that no live or archived page carries as a `ref` finding. The `## Flags` of `vault/wiki/brief.md` report the finding `estimates/estimate-link-graph-prints-the-neighbours: ref: body names slug, which no live or archived page carries`, and say its cause is the code spans `[[slug]]` and `## <slug or path>` of the Criterion of that page. That cause is wrong: each `[[slug]]` of the Criterion stands inside a code span, which `links_of` deletes. The bare `[[slug]]` stands in the `## Result` of the page, in the words `field, [[slug]], path-field`. The main agent wrote those words at the Retro of session 1831 in the estimate line at line 30 of `vault/raw/2026-10-31/1831/ledger.md`, and `generate` copied the text of the reading into `## Result` as it stood. Lint works as `estimate-lint-finds-a-broken-link` promises: a body `[[…]]` that names no page is a finding, and one inside a code span is no link. The person chose to fix the text of the page alone: the `update` writes the `## Result` whole again, its text as it stands with the bare `[[slug]]` put in a code span. A `replace` pair cannot do it, since its `old` would hold the bare link, and the check of the case file, `check_bare_links` of `.guppi/guppi/prespec.py`, reports a bare `[[slug]]` in each string of the plan. The new text also puts the mention of the session in a bracket of its own and the command and the output that name a Decision page in code spans, since `check_pointers` of `.guppi/guppi/prespec.py`, by `outside` of `.guppi/guppi/pointers.py`, reported them in the first text as pointers outside a bracket of their own; the readings it records do not change. The `update` names a section other than the Criterion, a part alone, so the status, the `## Criterion` and the `method` of the page stand, as the description of `## Criterion` in `rule-estimates-schema` sets it. The check is a new one-time Estimate with `once: true` on the live sprint page `entity-sprint-plugin`, as `rule-estimates-schema` sets for a check of one state of the data; it is read by hand after the librarian's run that applies the `update`, since `guppi check` sees the change only then, and its `method` reads the output of `guppi check` for the finding and the last change of the file of the page by `git log -p -1` for the Result and the parts that stand, both outputs saved in the estimate line, as the field `method` of `rule-estimates-schema` sets for a reading by hand. The Purpose of `entity-sprint-plugin` says that the sprint is done when every Estimate of the page passes, and lists its goals; it stands, since the new Estimate is read before the close and is no goal of the sprint. A Glob `vault/**/estimate-sprint-plugin-check-*.md` printed nothing, so the slug is free. The blocks of both pages in `.guppi/links.md` name `entity-link-graph`, `rule-case-build`, `rule-skill-grill-me`, `entity-sprint`, the sprint Estimates and the rules of the clean branch, the close, the work mode and the setup; none speaks of the text of a Result, so none changes. A Grep of `estimate-link-graph-prints-the-neighbours|entity-sprint-plugin` over `.guppi/tests/` printed three files: `test_links.py`, where the slug stands in the docstring; `test_prespec.py`, which builds the sprint page in a temporary folder; and `test_lint.py`, where the slug stands in the text of a `method`. No test reads the changed text live. Case 972 changes `.guppi/guppi/lint.py` for a wait in a `method`; this Case changes no code, and the `ref` class stays as it is. The brief is written again at each librarian's run, so its wrong cause is left to that run.

> **problem:**
> A bare `[[slug]]` in the `## Result` of `estimate-link-graph-prints-the-neighbours` names no page, so `guppi check` reports a `ref` finding at each run.

> **recommend:**
> - **What the Case fixes**
>   - Recommended: (a) fix the page text only — the bare `[[slug]]` in the `## Result` of `estimate-link-graph-prints-the-neighbours` put in a code span.
>   - Answer: agreed, (a).
> - **How the fix is checked**
>   - Recommended: (a) a one-time Estimate with `once: true` on `entity-sprint-plugin`, read by hand after the librarian's run by `guppi check`.
>   - Answer: (a).

> **given:**
> `estimate-link-graph-prints-the-neighbours`: the page whose `## Result` holds the bare link.
> **＋** `estimate-sprint-plugin-check-finds-no-bare-slug-link`: the new one-time check.
> **＋** `entity-sprint-plugin`: the live sprint page, the target of the new check.
> **＋** `.guppi/guppi/lint.py`: the `ref` class that reads the link, unchanged.
> **＋** `vault/wiki/`: the live pages that the lint reads.
> **＋** `rule-estimates-schema`: a one-time Estimate targets the live sprint page.

> **when:**
> `uv run --project .guppi guppi check` runs the lint of `.guppi/guppi/lint.py` over the live pages of `vault/wiki/`, after the librarian's run that applies the `update` of `estimate-link-graph-prints-the-neighbours`.
> **＋** The last change of the file of `estimate-link-graph-prints-the-neighbours` is read by `git log -p -1` on its path.

> **then:**
> It prints no `ref` line for `estimate-link-graph-prints-the-neighbours`.
> **＋** The `## Result` of `estimate-link-graph-prints-the-neighbours` holds `[[slug]]` inside a code span, and the date, the commands, the counts and the outputs of the readings it records as they stood.
> **－** The status, the `## Criterion` and the `method` of `estimate-link-graph-prints-the-neighbours` do not change.

> **tasks:**
> - [ ] update `estimate-link-graph-prints-the-neighbours`
>   - sections.Result:
>     ```
>     2026-10-31, Retro (session 1831): uv run --project .guppi pytest .guppi/tests/test_links.py, 13 passed, each line of the Criterion over a vault in a temporary folder (block form, field, `[[slug]]`, path-field and body-name links outside History, agent, skill and command names of a rendered file to the page that renders or runs them, links in, a file in a named folder, purpose lines of a lesson and an insight, no Decision page, an unknown name exits 1); by hand in Work Mode: uv run --project .guppi guppi links .claude/skills/sprint-open/SKILL.md printed "- out agent case-guppi: rule-case-build — Prevents a Case from being shown before one agent has built it …", and uv run --project .guppi guppi links .claude/agents/case-guppi.md printed "- out skill grill-me: rule-skill-grill-me — Prevents an interview from acting on a plan …"; `guppi links decision-case-966` printed `links: decision-case-966 is neither a live page nor a file`, exit 1
>     ```
>   - change: `the bare link of the Result put in a code span, so lint reads no link to a page`
> - [ ] create `estimate-sprint-plugin-check-finds-no-bare-slug-link`
>   - ref: `entity-sprint-plugin`
>   - kind: `QA`
>   - purpose: `Whether guppi check prints no ref line for estimate-link-graph-prints-the-neighbours once the bare link of its Result stands in a code span, the rest of that page as it stood`
>   - method: `by hand, after the librarian's run that applies the update of estimate-link-graph-prints-the-neighbours: the output of uv run --project .guppi guppi check and the output of git log -p -1 -- vault/wiki/estimates/estimate-link-graph-prints-the-neighbours.md, the diff of the Result and of no field or Criterion, read against the Criterion, both outputs in the estimate line`
>   - once: `true`
>   - tags: `[sprint, harness]`
> - [ ] read `estimate-sprint-plugin-check-finds-no-bare-slug-link`

> **ratification:**
> ```
> - decision[case 973][update][estimate-link-graph-prints-the-neighbours]{ref:entity-link-graph}
> - decision[case 973][create][estimate-sprint-plugin-check-finds-no-bare-slug-link]{ref:entity-sprint-plugin}{tags:sprint,harness}
> ```
