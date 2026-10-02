## Case 589 — The language finding accepts Latin letters in a code span

> **context:**
> The language finding of `/pre-spec` reads the name, `context` and `problem` of every Case of the plan. It reports a letter outside the script of `documentation_lang`, which `guppi.toml` sets. The hook of `rule-case-check` runs the same finding on each answer of `case-guppi`. `check_untranslated` of `guppi/prespec.py` calls `ratified.untranslated`, which calls `config.outside`, the one judgment of a letter's script (case 476.3). That judgment reads the whole text, code spans included. A slug, a path or a field name in a code span is always Latin. For `en` this changes nothing. For a documentation language in another script, such as `ru`, every Case that names a page in a code span gets a finding. Work Mode of session 1318 found this, and case 481 put it off on the placeholder `rule-prespec-script-skips-code-spans`. The page holds only its purpose and its defer.
> The person chose to put no rule of its own in the vault. The code-span sentence goes into the description of the finding in the docstring of `guppi/prespec.py`, which `rule-prespec` points to (case 561.1). The Criteria of the two Estimates of the finding are replaced whole. The placeholder is deleted, and its delete line carries the supersede of case 481, which retires the defer. The person also chose what the check does inside a code span: a Latin letter there is accepted, and a letter of any other script is judged as in prose. So for `en` the finding behaves exactly as it does today, and a Russian word between backticks is still a finding. 589.1 changes the judgment and the Estimate of `/pre-spec`. 589.2 replaces the Estimate of the hook and changes `rule-case-check`. These are two promises of two Estimates, because the run at `/pre-spec` and the run on an answer can fail apart.
> The `## How it works` of `rule-case-check`. It states that any such letter is a finding, which would no longer be true. A pre-spec finding showed that `vault/wiki/rules/schema.yaml` asks a Leaf to lose that section at its next touch, with the mechanism in the docstring of its code (cases 193, 200.2). The person chose that the section leaves now. They also chose that 589.2 removes it by hand, as a one-off task of Work Mode, after the docstring of `guppi/casecheck.py` carries each fact of it that still holds. No script can remove a section: an `update` replaces the text of a section or words inside it, and `body` of `guppi/generate.py` writes a section given empty text as a bare heading. The section left `rule-materialize`, `rule-spec-capture` and `rule-lint` the same way (cases 189, 200.4, 202). The removal is an exception to the sentence of `rule-page-generation` that the script is the only writer to `wiki/`, and that sentence stands. So the update of `rule-case-check` carries only its History line, and no `replace` pair, which would miss the removed section at the librarian's run. Its Purpose says the hook judges the script of the name, `context` and `problem`, and that stays true. Case 590.1 changes the turn sentence of the same section and the paragraphs on how a round opens in the docstring of `guppi/casecheck.py`. With the person's answer, 590.1 makes no change of its own in the section and names this Case. The docstring task of 589.2 carries the turn sentence as 590.1 sets it, so the `given` of 589.2 names its case file.
> What `case-guppi` found in the frame. `config.outside` stays the one judgment of a letter's script. The code span is read by `CODE_SPAN` of `guppi/lint.py`, the pattern that `guppi/prespec.py` and `guppi/generate.py` already import, so no second pattern of a code span is written. A Grep of `CODE_SPAN|code_spans|def spans|SPAN =|outside\(` over `guppi/` printed `guppi/config.py`, `guppi/generate.py`, `guppi/prespec.py`, `guppi/ratified.py` and `guppi/lint.py`. `guppi/config.py` imports no module of `guppi`, and `guppi/lint.py` imports neither `guppi/config.py` nor `guppi/ratified.py`, so the import makes no cycle. A Grep of ``outside the script|config\.outside|letter outside|ratified\.untranslated`` over the repository outside `vault/raw/` and `vault/archive/` printed 25 files: `backlog.md`, `log.md`, `rule-case-check.md`, `rule-prespec.md`, `rule-prespec-script-skips-code-spans.md`, `estimate-case-check-refuses-a-letter-outside-the-script.md`, `estimate-language-spec-prose-in-english.md`, `guppi/casecheck.py`, `guppi/prespec.py`, `guppi/ratified.py`, `guppi/config.py`, `tests/test_casecheck.py`, `tests/test_prespec.py`, `tests/test_config.py`, and the Decision pages of cases 445.1, 445.2, 445.3, 445.4, 445.6, 445.7, 476.1, 476.2, 476.3, 476.4 and 481. The log, the backlog and the Decision pages are not read. The hit in `rule-prespec.md` is a History line. The two Criteria, the docstrings of the three modules and the tests enter the sub-cases. The `purpose` of each Estimate states the old promise without the exception, so it is set anew. The `method` of each names its test run, so it stands. `estimate-language-followed`, the other Estimate of `rule-language`, says that slugs and paths stay as they are in either language. The change makes that easier to keep, so it stands. A Grep of ``How it works of `?rule-case-check|rule-case-check`?'s How it works|rule-case-check#How`` over the same paths printed no file, so no page points to the section that leaves. A Grep of `rule-prespec-script-skips-code-spans` over the same paths printed 4 files: `brief.md`, `backlog.md`, `log.md` and `decision-case-481.md`. None of them is a live page that the delete makes false. A Grep of `outside the script|letter outside|language finding` over `.claude/` printed no file. The only hook on `SubagentStop` in `.claude/settings.json` is `uv run guppi casecheck --subagent`, and this Case changes what it judges, not its registration. The judgment only accepts more text than before, so no reader refuses an old form, and no old form is kept. Case 588 changes the notes of `/pre-spec` on an Estimate `update` and other tests of `tests/test_prespec.py`. It does not touch the language finding, so the two Cases do not meet. The Grep of `^(purpose|deferred_by):` over `vault/wiki/rules/` printed the placeholder and no other rule on code spans in the language finding. No `create` is made, so no slug is checked. Not done: a code span of two or more backticks, which `CODE_SPAN` does not match, is still read as prose, and a `[[slug]]` outside a code span is still judged letter by letter.
> The notes of the check, and why each change is kept. In each sub-case the first line of the old Criterion, that any such letter is a finding, is not carried word for word. It is replaced by a line that adds the exception for a Latin letter in a code span, and that exception is the behaviour this Case changes. The other old lines are carried word for word. 589.2 names `/pre-spec` in its `given`, so its line on the function the hook runs stands as it was. The line of 589.1 on where the judgment lives stands as it was, and the code span has a line of its own. Some `then` lines of 589.2 share most of their words with lines of 589.1, among them the line on an answer with no such letter and the two lines on a Latin slug in a code span. They are the same behaviour checked from two angles, the run of `/pre-spec` on the plan and the run of the hook on an answer. Each Estimate must read without the other, so both stand. The `given` of 589.2 holds more than seven `**＋**` lines. The frame of the hook, the removal of the section and the Case it shares the docstring with all need a line, and the promise is still one, the finding on an answer.

> **problem:**
> The language finding cannot tell a word written in the wrong language from a slug or a path in a code span. So for a documentation language not written in Latin script, it reports almost every Case. The question was where the fix is recorded, and what the check does with the letters inside a code span.

> **recommend:**
> - **Where is the change recorded in the vault?**
>   - Recommended: (b) no new rule. One sentence goes into the description of `/pre-spec` next to the language check, the promises of the two existing Estimates are rewritten whole, and the empty page `rule-prespec-script-skips-code-spans` is deleted, which closes the put-off item. The behaviour is one sentence about a check that already has its description and two Estimates.
>   - Answer: Agreed: (b).
> - **What does the check do with the letters inside a code span?**
>   - Recommended: (b) inside a code span, accept Latin letters and judge all other letters as in prose. It solves the problem, a Russian word between backticks is still caught, and for English nothing changes.
>   - Answer: Agreed: (b).

### Case 589.1 — The pre-spec language finding accepts a Latin letter in a code span

> **given:**
> `estimate-language-spec-prose-in-english` — the promise of the finding at `/pre-spec`, its Criterion replaced whole
> **＋** `rule-prespec-script-skips-code-spans` — the placeholder of the defer of case 481, deleted
> **＋** `guppi/config.py` — `outside`, the one judgment of a letter's script
> **＋** `guppi/lint.py` — `CODE_SPAN`, the one pattern of a code span, unchanged
> **＋** `guppi/ratified.py` — `untranslated`, which reads the name, `context` and `problem` of each Case
> **＋** `guppi/prespec.py` — `check_untranslated` and the description of the finding in the module docstring
> **＋** `tests/test_prespec.py` — the tests of the finding
> **＋** `tests/test_config.py` — the test of `outside`

> **when:**
> `guppi prespec --check <plan>` runs at `/pre-spec`, and reads the plan file and `guppi.toml`.

> **then:**
> A name, `context` or `problem` of a Case of the plan that holds, outside a code span, a letter outside the script of the language `guppi.toml` sets as `documentation_lang`, or, inside a code span, a letter that is neither Latin nor of that script, gives one finding naming the Case, the part and the language.
> **＋** A Latin slug, path or field name in a code span gives no finding, whatever the documentation language.
> **＋** A short-form Case under `## Deferred` is read the same way.
> **＋** A plan whose names, contexts and problems hold no letter outside that script gives no finding of this check.
> **＋** A `guppi.toml` that is missing, or that names a code the table of `guppi/config.py` does not hold, gives one finding that names `guppi.toml`, and no Case is read by this check.
> **＋** The judgment of a letter's script lives in `guppi/config.py`, and `guppi/ratified.py` imports it.
> **＋** `guppi/config.py` reads a code span by `CODE_SPAN` of `guppi/lint.py`, and holds no pattern of its own.
> **－** The `given`, `when`, `then` and the blocks of a Case are not read by this check: a quotation there keeps its language.
> **－** The plan is compared with no other file: no ratified copy is read.

> **tasks:**
> - [ ] `guppi/config.py`: `outside` reads the code spans of the text by `CODE_SPAN` of `guppi/lint.py`, and a letter inside a span counts as outside only when it is neither Latin nor of the script of the language; the module docstring and the docstring of `outside` say so
> - [ ] `guppi/ratified.py`: the module docstring and the docstring of `untranslated` say that a Latin letter in a code span gives no finding
> - [ ] `guppi/prespec.py`: the language item of the module docstring and the docstring of `check_untranslated` say that a Latin letter in a code span gives no finding (case 589.1)
> - [ ] `tests/test_config.py`: `test_outside_finds_a_letter_of_another_script` asserts that a Latin slug in a code span is not outside for `ru`, that a Cyrillic word in a code span is outside for `en`, and that a Greek letter in a code span is outside for `ru`
> - [ ] `tests/test_prespec.py`: a test `test_script_a_latin_code_span_passes_under_russian`, a plan in Russian whose `context` names a slug in a code span gives no finding under `documentation_lang = "ru"`; a test `test_script_a_cyrillic_code_span_is_found_under_english`, a Russian word in a code span of a `context` gives the finding under `en`
> - [ ] `uv run pytest tests/test_config.py tests/test_prespec.py`: green
> - [ ] update `estimate-language-spec-prose-in-english`
>   - set: `{status: pending, purpose: "Pre-spec finds a name, context or problem of a Case of the plan that holds a letter outside the script of the documentation language of guppi.toml, a Latin letter in a code span excepted, a short form under Deferred included"}`
>   - change: `the Criterion replaced whole — a Latin letter in a code span gives no finding, any other letter there is judged as in prose (case 589.1)`
> - [ ] delete `rule-prespec-script-skips-code-spans`
>   - impact: `its one sentence stands in the Criterion of estimate-language-spec-prose-in-english and the description of the finding in guppi/prespec.py; in vault/wiki/ only brief.md, backlog.md, log.md and decision-case-481 name it, and the supersede of case 481 retires that defer`
> - [ ] read `estimate-language-spec-prose-in-english` — in a later session: `uv run pytest tests/test_prespec.py -k script`

> **ratification:**
> ```
> - decision[case 589.1][update][estimate-language-spec-prose-in-english]{ref:rule-language}
> - decision[case 589.1][delete][rule-prespec-script-skips-code-spans]{ref:rule-prespec-script-skips-code-spans}{supersedes:case 481}
> ```

### Case 589.2 — The check of each answer of `case-guppi` accepts a Latin letter in a code span

> **recommend:**
> - **Change**
>   - Asked: a pre-spec finding showed that `vault/wiki/rules/schema.yaml` asks a Leaf to lose its `## How it works` at its next touch, and this sub-case added a sentence to that section of `rule-case-check`. The person agreed that the section leaves at this touch, and that what still holds of it moves into the docstring of `guppi/casecheck.py`.
>   - Taken: the `replace` pair on the section is dropped, the docstring of `guppi/casecheck.py` takes the facts of the section, and the update of `rule-case-check` carries only its History line.
> - **How does the `## How it works` section leave `rule-case-check`, when no script can remove a section?**
>   - Recommended: (a) remove it by hand, as a one-off task of Work Mode. This Case takes the removal, and Case 590 makes no change of its own in that section and names this Case. It is how the section left three rule pages before, it keeps both Cases small, and the content only moves.
>   - Answer: (a).

> **given:**
> `estimate-case-check-refuses-a-letter-outside-the-script` — the promise of the finding on an answer, its Criterion replaced whole
> **＋** `rule-case-check` — the rule; its `## How it works` leaves the page by hand
> **＋** `vault/wiki/rules/schema.yaml` — a Leaf loses its `## How it works` at its next touch, its mechanism in the docstring of its code
> **＋** `guppi/casecheck.py` — runs `check_untranslated` on `SubagentStop`; its module docstring takes the facts of the section
> **＋** `guppi/prespec.py` — `check_untranslated`, imported, unchanged by this sub-case
> **＋** `/pre-spec` — the skill whose check runs the same function
> **＋** `guppi/config.py` — the judgment of a letter's script, as 589.1 sets it
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md` — the file of the Case the hook writes
> **＋** `tests/test_casecheck.py` — the tests of the finding on an answer
> **＋** `raw/2026-10-02/1202/cases/case-590.md` — 590.1 sets the turn sentence of the docstring of `guppi/casecheck.py` and leaves the removal of the section to this Case

> **when:**
> `SubagentStop` fires when `case-guppi` answers with a Case, and `uv run guppi casecheck --subagent` reads the answer and `guppi.toml`.

> **then:**
> A name, `context` or `problem` of a Case of the answer that holds, outside a code span, a letter outside the script of the language `guppi.toml` sets as `documentation_lang`, or, inside a code span, a letter that is neither Latin nor of that script, is a finding of that Case, stored with the Case in `<plan>.checked.json`: the hook exits 2 with it on stderr, and `case-guppi` answers again.
> **＋** While such a finding stands, no `raw/<date>/<hi HHMM>/cases/case-<N>.md` is written for the answer.
> **＋** An answer whose names, contexts and problems hold no such letter gets no finding from this check.
> **＋** A Latin slug or path in a code span of an answer is no finding, whatever the documentation language.
> **＋** A `guppi.toml` that is missing, or that names a code the table of `guppi/config.py` does not hold, gives one finding that names `guppi.toml`.
> **＋** The hook runs `check_untranslated` of `guppi/prespec.py`, the function `/pre-spec` runs, and holds no second copy of its judgment.
> **－** An answer whose text `<plan>.checked.json` already holds with findings is stored again with this finding and exits 0, so an unchanged answer is not sent back twice, and no file is written for it.
> **－** The `given`, `when`, `then` and the blocks of a Case are not read by this check: a quotation there keeps its language.

> **tasks:**
> - [ ] `guppi/casecheck.py`: the module docstring carries each fact of the `## How it works` of `rule-case-check` that it does not yet hold, the sentence on the turn of the reply as case 590.1 sets it, and says that a Latin letter in a code span of a name, `context` or `problem` is no finding (case 589.2)
> - [ ] one-off: remove the `## How it works` section from `vault/wiki/rules/rule-case-check.md` by hand, once the docstring of `guppi/casecheck.py` carries each fact of it that still holds, as `vault/wiki/rules/schema.yaml` asks of a Leaf at its next touch; nothing else of the page changes by hand
> - [ ] `tests/test_casecheck.py`: a test `test_subagent_script_a_latin_code_span_passes_under_russian`, an answer whose name, `context` and `problem` are in Russian and name a slug in a code span gets no finding under `documentation_lang = "ru"`, and its file is written; a test `test_subagent_script_a_cyrillic_code_span_is_a_finding`, a Russian word in a code span of the `context` is a finding under `en`, and no file is written
> - [ ] `uv run pytest tests/test_casecheck.py -k script`: green
> - [ ] update `rule-case-check`
>   - change: `How it works removed by hand, a one-off, its facts in the docstring of guppi/casecheck.py; the language finding on an answer accepts a Latin letter in a code span (case 589.2)`
> - [ ] update `estimate-case-check-refuses-a-letter-outside-the-script`
>   - set: `{status: pending, purpose: "An answer of case-guppi whose name, context or problem holds a letter outside the script of the documentation language, a Latin letter in a code span excepted, is a finding of the check, and no file of the Case is written while it stands"}`
>   - change: `the Criterion replaced whole — a Latin letter in a code span is no finding, any other letter there is judged as in prose (case 589.2)`
> - [ ] read `estimate-case-check-refuses-a-letter-outside-the-script` — in a later session: `uv run pytest tests/test_casecheck.py -k script`

> **ratification:**
> ```
> - decision[case 589.2][update][rule-case-check]{ref:rule-case-check}
> - decision[case 589.2][update][estimate-case-check-refuses-a-letter-outside-the-script]{ref:rule-case-check}
> ```
