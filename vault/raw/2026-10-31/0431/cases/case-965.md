## Case 965 — The hook copies the librarian's report into the session folder, and its Rule is born core

> **context:**
> This Case replaces sub-case 956.1 whole, found wrong in Work Mode by the first condition of `rule-where-to-stop`: a ratified Case turns out wrong. Case 956 and the findings of `/pre-spec` on it set that `rule-librarian-report-copy` has `core: true` as a boolean, since `rule-rules-schema` allows only `core: [true]`. The file of Case 956 wrote `core` as a fenced value under the `create`, and the hook of `rule-spec-write` lifted it into the `then` block of `vault/raw/2026-10-31/0431/spec.md` as the string `'true'`. The fault lies in that lift. `put` of `.guppi/guppi/ratified.py` (read whole, with `read_tasks`, `code_value` and `fenced_value`, which hand it each sub-point) parses a value as YAML only under `set`, or when the value opens with `[` or `{`; every other value, a code span or a fenced block alike, stays a string. So no sub-point of a `create` in the chat form lifts a bare boolean, and `case-schema.md` names no such form. `create_fields` and `_lift_item` of `.guppi/guppi/materialize.py` carry the string as it stands, the `create` of `.guppi/guppi/generate.py` puts it into the props, and `frontmatter` and `scalar` write a string `true` quoted, as `"true"`; so the page would be born without `core: true`. `core_as_left` of `.guppi/guppi/prespec.py` answers False for a `create` whose `core` is not `True`, which is why `guppi prespec --check` printed no finding on it. Whether the hook of `rule-spec-write` lifts `true` and `false` as booleans is not this Case; the main agent records it as a lesson. This Case writes the same Rule, Estimate and registration as 956.1, with one change: the `create` of `rule-librarian-report-copy` carries no `core`, and an `update` of that Rule right after it carries `set: {core: true}`, which `put` parses as YAML, so the `then` block holds `core: true` as a boolean. `apply` of `generate.py` applies the entries in the order of the ledger lines, so the `create` writes the page and the `update` finds it and sets the field by `update`, which puts each key of `set` into the props as it stands; `core_as_left` answers True on that `set`. The `update` names a field alone, so it carries no `status` and touches no Estimate. The `then`, the Estimate and its Criterion are those of 956.1, unchanged; `estimate-librarian-report-copy-writes-the-file` checks the hook, and no Estimate checks the field `core`, as in 956.1. The code of `.guppi/guppi/libreport.py`, `.guppi/guppi/cli.py` and `.guppi/tests/test_libreport.py` was written in this Work Mode under 956.1; the main agent ticks those tasks with no new run. The `## Render` of `rule-hook-registry`, read whole around the pair, is the `"hooks"` key of `.claude/settings.json`, from `"SessionStart"` to the closing marker, with the `"PostToolUse"`, `"Stop"` and `"SubagentStop"` entries last; the `old` of the pair hits that page once, on the one line of the `"SubagentStop"` entry, whose `hooks` list holds only `guppi casecheck --subagent`, and ends at the `] }` that closes that list and that entry. The `new` keeps that command and its timeout, adds `guppi libreport` with a timeout of 30 as the second hook of the same list, and closes the list and the entry as before, so the `"SubagentStop"` key holds one entry with two hooks and the `]` after it still closes the key. No other entry of the Render changes. Of the Cases of this session, only Case 956, in its sub-case 956.1, wrote into this page, by the same pair; Case 965 replaces 956.1, so no other pair of the session meets this one. The rest of the frame, the vault query and the searches are those of the `context` of Case 956, which stands in its file.

> **problem:**
> The `then` block of 956.1 creates `rule-librarian-report-copy` with `core` as the string `true`, so the page would be born without `core: true`.

> **recommend:**
> - Recommended: the Rule, the Estimate and the registration of 956.1 as they stood, with `core: true` set by an `update` of the new Rule right after its `create`, so that the `then` block holds a boolean.
> - Answer: ratified as built

> **given:**
> `rule-librarian-report-copy`: the new Rule of the hook.
> **＋** `estimate-librarian-report-copy-writes-the-file`: the new check of the hook.
> **＋** `rule-hook-registry`: the registry of hooks in `.claude/settings.json`, which gains the hook.
> **＋** `.guppi/guppi/libreport.py`: the new module of the hook.
> **＋** `.guppi/guppi/cli.py`: the command table, which gains `libreport`.
> **＋** `.guppi/tests/test_libreport.py`: the new test of the hook.
> **＋** `.guppi/guppi/casecheck.py` and `.guppi/guppi/ledger.py`: the reading of the outputs and of the session folder that the module imports.
> **＋** `vault/raw/<hi date>/<hi HHMM>/`: the session folder where the hook writes `report.md`.

> **when:**
> `SubagentStop` fires at the end of an agent, and `uv run --project .guppi guppi libreport` of `.guppi/guppi/libreport.py` reads its payload.

> **then:**
> For `librarian-guppi`, the hook writes the last output of the agent in its `agent_transcript_path`, a text or the `message` of a `SubagentHandback` call, whole into `report.md` in the session folder `vault/raw/<hi date>/<hi HHMM>/`, and replaces a file that stands there.
> **＋** A second `SubagentStop` of the same run writes the file again from the last output at that moment.
> **＋** The hook reads the outputs by `subagent_outputs` of `.guppi/guppi/casecheck.py` and the folder by `session_dir` of `.guppi/guppi/ledger.py`.
> **－** For any other agent, the hook writes nothing.
> **－** The hook blocks nothing and exits 0; with no readable transcript, no output or no session folder it writes nothing and prints one line on stderr.

> **tasks:**
> - [ ] create `rule-librarian-report-copy`
>   - ref: `rule-documentation`
>   - type: `rule`
>   - kind: `Leaf`
>   - purpose: `Prevents the librarian's report from standing in no file when Claude Code refuses the Write of a report file by a subagent`
>   - enforcement: `hook`
>   - implementation_ref: `[.guppi/guppi/libreport.py, .guppi/tests/test_libreport.py, .claude/settings.json]`
>   - tags: `[hooks, harness, librarian]`
>   - sections.Purpose: `` Prevents the librarian's report from standing in no file when Claude Code refuses the `Write` of a report file by a subagent. Claude Code refused the librarian's `Write` of `report.md` with the message that subagents return findings as text and write no report files (as set in case 956). The `SubagentStop` hook `uv run --project .guppi guppi libreport` copies the last output that `librarian-guppi` returned into `report.md` in the session folder by its own code, so no `Write` call of a subagent is made, and `/handoff` or `/box` shows that file and commits it (as set in case 956). ``
> - [ ] update `rule-librarian-report-copy`
>   - set: `{core: true}`
>   - change: `core set as a boolean`
> - [ ] create `estimate-librarian-report-copy-writes-the-file`
>   - ref: `rule-librarian-report-copy`
>   - kind: `QA`
>   - purpose: `Whether the SubagentStop hook writes the last output of librarian-guppi, a text or a handback message, into report.md of the session folder, writes it again at a second fire, and writes nothing for another agent or with no transcript, output or folder`
>   - method: `uv run --project .guppi guppi test, which runs .guppi/tests/test_libreport.py`
>   - tags: `[hooks, harness, librarian]`
> - [ ] update `rule-hook-registry`
>   - old: `"command": "uv run --project .guppi guppi casecheck --subagent", "timeout": 30 } ] }`
>   - new: `"command": "uv run --project .guppi guppi casecheck --subagent", "timeout": 30 }, { "type": "command", "command": "uv run --project .guppi guppi libreport", "timeout": 30 } ] }`
>   - change: `the SubagentStop hook guppi libreport registered`
> - [ ] `.guppi/guppi/libreport.py`: the hook as `then` sets it, importing `subagent_outputs` from `casecheck.py`, `session_dir` from `ledger.py` and `session_stamp` and `read_payload` from `event.py`; written in this Work Mode under 956.1, ticked with no new run.
> - [ ] `.guppi/guppi/cli.py`: the command `libreport` runs `libreport.run`; written in this Work Mode under 956.1, ticked with no new run.
> - [ ] `.guppi/tests/test_libreport.py`: one test per line of `then`, over a transcript and an event log under a temporary folder: a last text, a last handback message, a second fire, another agent, and no transcript, no output or no session folder; written in this Work Mode under 956.1, ticked with no new run.
> - [ ] `uv run --project .guppi guppi render`: `.claude/settings.json`
> - [ ] read `estimate-librarian-report-copy-writes-the-file`

> **ratification:**
> ```
> - decision[case 965][create][rule-librarian-report-copy]{ref:rule-documentation}{tags:hooks,harness,librarian}{supersedes:case 956.1}
> - decision[case 965][update][rule-librarian-report-copy]{ref:rule-librarian-report-copy}{supersedes:case 956.1}
> - decision[case 965][create][estimate-librarian-report-copy-writes-the-file]{ref:rule-librarian-report-copy}{tags:hooks,harness,librarian}{supersedes:case 956.1}
> - decision[case 965][update][rule-hook-registry]{ref:rule-hook-registry}{supersedes:case 956.1}
> ```
