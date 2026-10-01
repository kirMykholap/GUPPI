## Case 537 — The check of each answer of case-guppi runs the language finding, and the insight closes

> **context:**
> Every answer of `case-guppi` goes through the `SubagentStop` check of `rule-case-check` before the main agent sees it. The check builds each Case of the answer as the Spec would hold it, runs the `/pre-spec` checks over that text through `prespec.judge`, and sends back an answer that has a finding. The language finding of `/pre-spec` is not one of those checks. It is `check_untranslated` of `guppi/prespec.py`, and only `guppi prespec --check` runs it. So a name, `context` or `problem` that holds Russian letters passes the check, and the person sees the Case with them. `/pre-spec` finds the letters near the end of Plan Mode, and then the Case is built and ratified again. This happened twice: Case 512 quoted the person in Russian (`lesson-case-build-quotes-the-person-in-the-chat-language`), and the rebuild of Case 524 held the person's Russian reply (`lesson-case-build-rebuild-quotes-the-relayed-words`). Both lessons are the live children of `insight-case-form-chat-form-read-by-no-script`. That insight is `open` with severity 2, and its `addressed_by` names `decision-case-449`. Case 536, ratified in this session, tells `case-guppi` never to quote the person's words. That closes the cause of the second lesson. The first lesson names the check itself as its cause.
> The person chose three things. First, to close the insight and add the language finding to the check. Second, to make it a finding, not a note. A finding works as every finding of the check works today. It sends a changed answer back to `case-guppi`. When the store already holds the same text with findings, the check stores it again and exits 0, so an unchanged answer is not sent back twice. In `guppi/casecheck.py` no file of the Case is written while a finding stands, in either path, and the `Stop` check refuses to show a Case stored with findings. A note would go back only once, and the file would then be written. Third, to give the check a new promise and not replace the Criterion of an existing one. The check imports `check_untranslated` and calls it on the Spec text it already builds. It holds no copy of the judgment (`rule-one-judgment-one-implementation`). `prespec.judge` does not change, and its docstring keeps the language finding out of `judge`. The one new Estimate has a `ref`, so no vault query ran. The slug `estimate-case-check-refuses-a-letter-outside-the-script` is free.
> In the frame, one sentence of the Purpose of `rule-case-check` says that the text of the story sections is not among the checks, only their presence and their order. The change makes that sentence false, so the Case rewords it. The sentence of `rule-case-protocol` that says no script judges the story sections stands: it speaks of their length and clarity, and `/pre-spec` has judged their script since case 387.4. The Criterion of `estimate-case-check-sends-back-a-faulty-case` says the check runs `judge`, and it does not say that the check runs nothing else. Its line on an unchanged answer holds for the new finding as it holds for any other, so the person left it as it stands. The other four Estimates of `rule-case-check` speak of the `Stop` comparison, the backlog lines and the two notes, and are not touched. `estimate-language-spec-prose-in-english` speaks of `/pre-spec` only, and it stands. `.claude/settings.json` registers no other hook on `SubagentStop`. The new reader needs no old form. It sends the answer back to `case-guppi`, which writes it again, so nothing is lost while the frame of Case 536 waits for the render.
> The insight is set `actioned`, and `addressed_by` names this Case. The cascade of `generate` then archives the two clustered lessons. The rest of its Proposal, a script that judges the text of the story sections, was rejected by case 449. One thing stays not done: the backlog item `rule-prespec-script-skips-code-spans` is left as it stands. When it is taken up, it changes the imported function, and so both checks at once.

> **problem:**
> A Case with Russian letters in its name, `context` or `problem` reaches the person, because the check of each answer of `case-guppi` does not run the language finding. `/pre-spec` finds the letters only later, and the Case is built and ratified again. The insight that records this pattern is still open.

> **recommend:**
> Have the `SubagentStop` check import and run `check_untranslated` over the Spec text it builds. Make each hit a finding, give the new check its own Estimate, and set the insight `actioned` by this Case. With this, both lessons have their cause closed: Case 536 tells `case-guppi` not to quote the person, and this check catches a quotation that gets through anyway. The rejected option was to close the insight on Case 536 alone. That would leave the first lesson's cause, the check, as it is.

> **given:**
> `rule-case-check` — the rule of the check on each answer of `case-guppi`
> **＋** `estimate-case-check-refuses-a-letter-outside-the-script` — the new promise of the language check
> **＋** `insight-case-form-chat-form-read-by-no-script` — the insight this Case actions
> **＋** `guppi/casecheck.py` — `uv run guppi casecheck --subagent`, the hook on `SubagentStop`, and its store `<plan>.checked.json`
> **＋** `guppi/prespec.py` — `check_untranslated`, the language finding of `/pre-spec`
> **＋** `guppi/config.py` — reads `guppi.toml`, its `documentation_lang`, and judges the script of a letter
> **＋** `tests/test_casecheck.py` — the tests of the hook
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md` — the file the hook writes for a Case that passed

> **when:**
> `SubagentStop` fires when `case-guppi` answers with a Case, and `uv run guppi casecheck --subagent` reads the answer and `guppi.toml`.

> **then:**
> A name, `context` or `problem` of a Case of the answer that holds a letter outside the script of the language `guppi.toml` sets as `documentation_lang` is a finding of that Case, stored with the Case in `<plan>.checked.json`: the hook exits 2 with it on stderr, and `case-guppi` answers again.
> **＋** While such a finding stands, no `raw/<date>/<hi HHMM>/cases/case-<N>.md` is written for the answer.
> **＋** An answer whose names, contexts and problems hold no such letter gets no finding from this check.
> **＋** A `guppi.toml` that is missing, or that names a code the table of `guppi/config.py` does not hold, gives one finding that names `guppi.toml`.
> **＋** The hook runs `check_untranslated` of `guppi/prespec.py`, the function `/pre-spec` runs, and holds no second copy of its judgment.
> **－** An answer whose text `<plan>.checked.json` already holds with findings is stored again with this finding and exits 0, so an unchanged answer is not sent back twice, and no file is written for it.
> **－** The `given`, `when`, `then` and the blocks of a Case are not read by this check: a quotation there keeps its language.

> **tasks:**
> - [ ] update `rule-case-check`
>   - old: `` the text of the story sections — `context`, `problem` and `recommend` — is not among them, only their presence and their order: the person judges the text (case 449). ``
>   - new: `` the text of the story sections — `context`, `problem` and `recommend` — is not among them, only their presence, their order and the script of the name, `context` and `problem` of a Case, by the language finding of pre-spec: the person judges the text (cases 449, 537). ``
>   - old: `` It checks besides the order of the sections and the ones the schema requires, and that `ratification` holds one untagged fence of ledger lines and nothing else. ``
>   - new: `` It checks besides the order of the sections and the ones the schema requires, and that `ratification` holds one untagged fence of ledger lines and nothing else. It runs besides the language finding of `/pre-spec`, `check_untranslated` of `guppi/prespec.py`, imported, over the same text: a name, `context` or `problem` of a Case of the answer that holds a letter outside the script of the documentation language `guppi.toml` sets is a finding of that Case, sent back and stored as any other finding, and a `guppi.toml` that is missing or names a code the table does not hold is one finding, given to the first Case of the answer (case 537). ``
>   - change: `the check of each answer of case-guppi runs the language finding of pre-spec as a finding (case 537)`
> - [ ] create `estimate-case-check-refuses-a-letter-outside-the-script`
>   - type: `estimate`
>   - ref: `rule-case-check`
>   - kind: `QA`
>   - purpose: `An answer of case-guppi whose name, context or problem holds a letter outside the script of the documentation language is a finding of the check, and no file of the Case is written while it stands`
>   - method: `uv run pytest tests/test_casecheck.py -k script`
>   - tags: `[hooks, harness, workflow]`
> - [ ] update `insight-case-form-chat-form-read-by-no-script`
>   - set: `{status: actioned, addressed_by: decision-case-537}`
>   - change: `actioned: case-guppi quotes none of the person's words (case 536), and the check of each answer runs the language finding (case 537)`
> - [ ] `guppi/casecheck.py` — `check_answer` imports `check_untranslated` from `guppi/prespec.py` and runs it on the Spec text it builds, each finding to its Case; the docstring says so
> - [ ] `tests/test_casecheck.py` — tests whose names hold `script`: a Russian letter in a name, a `context` and a `problem` is a finding with exit 2 and no file written; the same answer again is stored and exits 0 with no file written; an English answer passes; a Russian quotation in `then` passes; a missing `guppi.toml` is one finding
> - [ ] read `estimate-case-check-refuses-a-letter-outside-the-script` at a later session

> **ratification:**
> ```
> - decision[case 537][update][rule-case-check]{ref:rule-case-check}
> - decision[case 537][create][estimate-case-check-refuses-a-letter-outside-the-script]{ref:rule-case-check}{tags:hooks,harness,workflow}
> - decision[case 537][update][insight-case-form-chat-form-read-by-no-script]{ref:insight-case-form-chat-form-read-by-no-script}
> ```
