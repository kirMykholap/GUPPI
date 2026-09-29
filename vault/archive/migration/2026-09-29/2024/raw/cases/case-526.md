## Case 526 — The pages say what PyYAML does with a `#` after a tab

> **context:**
> When the person puts a decision off, the main agent writes a short Case itself. Its fence tagged `then` holds plain YAML. The `Stop` hook of `rule-spec-write` (`guppi/ratified.py`) refuses the fence when it holds a YAML comment, and `materialize` marks the entries of that Case `incomplete: [comment]`. Both call `then_comments` of `guppi/materialize.py`, which judges each fence by `yaml_comments` (cases 521.1, 521.2). `yaml_comments` counts a `#` at the start of a line or after a space or a tab. Case 521 gave one reason for both characters: YAML drops the rest of the line, so an unquoted value is cut. That reason holds for a space. It does not hold for a tab. PyYAML, the library the scripts use, does not cut the value at a tab before `#`. It refuses the whole block. The handoff of session 1753 says so: "PyYAML does not cut a value at a tab before `#`: it refuses the block." The comment in `tests/test_materialize.py` says the same: "PyYAML cuts the value there; a tab before `#` it refuses to parse". The YAML standard counts a tab as a separator, so the old sentences are true of the language but not of the library we run. The check behaves correctly for both characters, and the tests of both files cover the tab. Only the explanation is wrong.
> The wrong reason stands in the three rule pages, in four places of the code and in one test. In `rule-case-protocol` it is the short-form paragraph, rendered into `case-schema.md`: "YAML reads the rest of the line as a comment". In `rule-spec-write` and `rule-materialize` it reads "YAML drops the rest of the line". In the code, the docstring of `yaml_comments` and the module docstring of `guppi/ratified.py` repeat it. The refusal message of `deferred_section` in `guppi/ratified.py` says "put the value in quotes, since YAML drops the rest of the line". The comment at the call of `then_comments` for a decision entry in `guppi/materialize.py` says "YAML may have cut a value there". In the tests, the comment over the tab parameter `"a\t# b"` in `tests/test_ratified.py` says "YAML reads the rest of the line as a comment, so the value would be cut". This Case corrects every one of them. The person chose in the round that the code and the pages must say the same thing.
> In one round the person accepted every recommendation. Name both outcomes, fix the code text in the same Case, and change no promise. The Case creates no page, so no vault query was run. The text of Case 521 in the Spec of session 1753 and on its Decision pages stays as history. This context records the correction.
> What `case-guppi` found in the frame. `estimate-spec-write-writes-a-defer` and `estimate-materialize-marks-a-comment` define what the function counts, a tab included. Neither says that YAML cuts the value. The line "The entry keeps the values that YAML read, and nothing is invented for the text after the `#`" still holds for a tab: YAML read nothing, and nothing is invented. So both Criteria stand. The other Estimates of `rule-case-protocol`, `rule-spec-write` and `rule-materialize` speak of other behaviour, and they stand too. An `update` of the Render of `rule-case-protocol` touches no Estimate of the live reading (case 378.5). The other hooks on `Stop` in `.claude/settings.json` are `guppi ledger`, `guppi casecheck` and `guppi context`. None of them reads the message. The hook refuses exactly what it refused before, and only the wording of its reason changes. So nothing is refused in between, and no old form is kept. `tests/test_ratified.py` checks only the prefix "put the value in quotes", and the new message keeps it. A changed comment in a test file changes nothing that the test checks. One Case does the whole job: it is one correction of one claim, and its pages have no promise that could fail on its own. Pre-spec found the code comment in `guppi/materialize.py` and the test comment, and it found that the earlier text of this context called `yaml_comments` the function both sides call. This text corrects all three.
> Not done: the function, the refusal and the mark do not change. The Spec of session 1753 and the Decision pages of case 521 keep the old sentence.

> **problem:**
> Three rule pages, `case-schema.md`, the code and one test say that YAML cuts an unquoted value at a `#` after a tab. PyYAML refuses the block there instead. A reader of the pages, the code or the test learns a false fact about the parser the harness runs.

> **recommend:**
> Name both outcomes wherever the reason stands. After a space, YAML drops the rest of the line. After a tab, PyYAML refuses the whole block. Then say that the check refuses both. A short reason that fits both ("drops the rest of the line or refuses the block") was rejected, because it does not say which outcome goes with which character.

> **given:**
> `rule-case-protocol` — the rule; its Render is the case schema, with the short-form paragraph
> **＋** `vault/wiki/case-schema.md` — the file rendered from it
> **＋** `rule-spec-write` — the rule of the `Stop` hook that refuses a short Case whose `then` block holds a comment
> **＋** `rule-materialize` — the rule of `materialize`, which marks such a Case's entries
> **＋** `guppi/materialize.py` — `then_comments`, which both sides call, and `yaml_comments`, which it uses; the docstring of `yaml_comments`; and the comment at the call of `then_comments` for a decision entry
> **＋** `guppi/ratified.py` — the module docstring on the defer, and the refusal message of `deferred_section`
> **＋** `tests/test_ratified.py` and `tests/test_materialize.py` — the tests of the refusal and the mark; the first holds a comment over the tab case

> **when:**
> An agent or the person reads the short-form paragraph of `vault/wiki/case-schema.md`, the sentence on a comment in `rule-spec-write` or `rule-materialize`, the docstrings and the comment in `guppi/materialize.py` and `guppi/ratified.py`, or the comment over the tab case in `tests/test_ratified.py`.
> **＋** The `Stop` hook `uv run guppi ratified` refuses a short Case whose `then` block holds a comment and writes its reason on stderr.

> **then:**
> Each of these texts says that after a space YAML drops the rest of the line, so an unquoted value is cut there, and that after a tab PyYAML, the library the scripts use, refuses the whole block.
> **＋** Each rule page and each docstring of these texts says that the hook refuses the block in both cases.
> **＋** The refusal on stderr gives the line of the comment and the advice to put the value in quotes, and it names both outcomes.
> **＋** The comment over the tab case in `tests/test_ratified.py` names the refusal by PyYAML. What `tests/test_ratified.py` and `tests/test_materialize.py` check does not change, and they pass.
> **－** What `yaml_comments` of `guppi/materialize.py` counts as a comment does not change. A `#` after a tab is still refused by the hook and still marked `incomplete: [comment]` by `materialize`.

> **tasks:**
> - [ ] update `rule-case-protocol`
>   - old: `` since YAML reads the rest of the line as a comment and the `Stop` hook of `rule-spec-write` refuses a block that holds one (case 521.4) ``
>   - new: `` since YAML drops the rest of the line at a `#` after a space, PyYAML, the library the scripts use, refuses the whole block at a `#` after a tab, and the `Stop` hook of `rule-spec-write` refuses a block that holds either (cases 521.4, 526) ``
>   - change: `the short form says YAML cuts a value at a # after a space and PyYAML refuses the block at a # after a tab (case 526)`
> - [ ] update `rule-spec-write`
>   - old: `since YAML drops the rest of the line and no page receives it (case 521.1)`
>   - new: `since after a space YAML drops the rest of the line and no page receives it, and after a tab PyYAML, the library the scripts use, refuses the whole block (cases 521.1, 526)`
>   - change: `the refusal of a comment says YAML cuts a value at a # after a space and PyYAML refuses the block at a # after a tab (case 526)`
> - [ ] update `rule-materialize`
>   - old: `YAML drops the rest of the line, so the value may be cut;`
>   - new: `after a space YAML drops the rest of the line, so the value may be cut, and after a tab PyYAML, the library the scripts use, refuses the whole block;`
>   - change: `the mark of a comment says YAML cuts a value at a # after a space and PyYAML refuses the block at a # after a tab (case 526)`
> - [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
> - [ ] `guppi/materialize.py`: the docstring of `yaml_comments` says that after a space YAML drops the rest of the line, so an unquoted value may be cut, and that after a tab PyYAML refuses the whole block; the comment at the call of `then_comments` for a decision entry names both outcomes
> - [ ] `guppi/ratified.py`: the module docstring on the defer says the same; the refusal message of `deferred_section` keeps "put the value in quotes" and names both outcomes
> - [ ] `tests/test_ratified.py`: the comment over the parameters of the refused defer says that YAML cuts `a ## b` and that PyYAML refuses the block of `a\t# b`; no assertion changes
> - [ ] `uv run pytest tests/test_ratified.py tests/test_materialize.py -k comment`: passes

> **ratification:**
> ```
> - decision[case 526][update][rule-case-protocol]{ref:rule-case-protocol}
> - decision[case 526][update][rule-spec-write]{ref:rule-spec-write}
> - decision[case 526][update][rule-materialize]{ref:rule-materialize}
> ```
