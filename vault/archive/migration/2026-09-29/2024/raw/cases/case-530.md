## Case 530 — The librarian's reads match what its brief needs, and a refused write is not worked around

> **context:**
> The librarian is the agent that runs after a session and turns its ratified decisions into vault pages. Its frame, the Render of `rule-documentation` in `.claude/agents/librarian-guppi.md`, lists the only things it may read. The brief section that `rule-brief` splices into the same frame asks for facts that no allowed read gives: the Spec lines `generate` ticked, what `cleanup` moved, and, for an Estimate read on the librarian's run, the facts "as the steps of this run before the brief printed or left them" (case 508.4). So every run reads beyond the list, and `estimate-documentation-completes` stays failed. The run of ff62585 read the tail of `log.md`, the head of the old `brief.md`, git diffs and a grep of `sprint.md`. The run of 1c196e8 (lines 2076–2119 of `raw/2026-09-29/event_log.md`) ran `git diff` on Spec, yaml and rule files, grepped the status of three Decision pages, and ran `git status` over `vault/archive`. A `bashguard` refusal (line 2115) stopped it from writing `brief.md` with a heredoc. It then wrote the brief into the scratchpad and copied it into place with `cp`, although it could have written the file with `Write`. The refusal text itself led it there: "Write the script with the Write tool into the scratchpad and run it by path; change a file with Edit" names no tool for writing a whole file. The same run also skipped `uv run guppi archive`. That is left to its own item in a later session, since the frame already demands the step. The main agent records the failed reading of 1c196e8 before the decision lines of this Case, because the ledger hook refuses a reading of an Estimate that a decision line of this session updates (case 428.1). `rule-documentation` stands `draft` with `deferred_by` `[[decision-case-525]]`, which put the item off after case 517. This Case takes it up and retires that defer. Both targets are `update`s with a `ref`, so no vault query was run. In the frame: `log.md` has 4829 lines. `generate` and `cleanup` add a dated line to it for each page they change or move, so its `git diff` before the commit holds only this run's lines. `rule-brief` says "nothing from the previous brief (case 168)", and that stands, because the old brief is read and no fact of it is carried. The opening sentence of the frame, "you write only through the scripts named below", is already qualified by the brief section, which gives the brief to the librarian; it stands. `bashguard` is the only hook on `PreToolUse` of `Bash`. Only an agent reads its refusal text, so the new text needs no old form beside it. The Estimates touched are the two whose Criterion speaks of the change: `estimate-documentation-completes`, which lists the librarian's reads, and `estimate-bash-guard`, which quotes the refusal text. Both Criteria are replaced whole. The bulleted read list of the first becomes one line of allowed reads, and the refusal sentence of the second takes the new text.

> **problem:**
> The librarian's list of allowed reads contradicts the brief section of its own frame, so every run breaks the list and `estimate-documentation-completes` cannot pass. When a hook refuses a write, the refusal text points to the scratchpad and not to `Write`, so the librarian worked around the refusal with `cp` instead of writing the file with the tool the hooks check.

> **recommend:**
> Widen the list to what this run changed. That means `git status` and `git diff` on the files the scripts of this run wrote, never over `vault/wiki/decisions/` or `vault/archive/`, `log.md` read only through its `git diff`, and the old brief read with no fact carried over. The frame also names `Write` for the brief and forbids working around a refusal. Correct the `bashguard` refusal text so that a whole file goes through `Write`, and put that in its own sub-case, since it is the guard's promise. Rejected: having the scripts print every fact the brief needs, or enforcing the list with a new hook, because both touch many scripts and Estimates for a check that fails today.

### Case 530.1 — The librarian reads what this run changed, and writes the brief with Write

> **given:**
> `rule-documentation` — the librarian's frame, the Render of `.claude/agents/librarian-guppi.md`
> **＋** `estimate-documentation-completes` — the promise of the librarian's run
> **＋** `rule-brief` — the brief section spliced into the frame; it takes nothing from the previous brief
> **＋** `rule-index-check` — the index check, whose Greps give index lines
> **＋** `rule-synthesis` — the synthesis, whose Greps give index lines
> **＋** `vault/wiki/brief.md` — the brief the librarian rewrites
> **＋** `vault/wiki/log.md` — the log that `generate` and `cleanup` append a dated line to
> **＋** `vault/archive/` — the archive the librarian never searches
> **＋** `vault/archive/**/<slug>.md` — the one Glob allowed over the archive
> **＋** `vault/wiki/decisions/` — the Decision pages the librarian never reads
> **＋** `vault/raw/<date>/<hi HHMM>/spec.md` — the Specs whose unticked lines the librarian reads
> **＋** `guppi/` — the scripts' code, which the librarian may read
> **＋** `tests/` — the scripts' tests, which the librarian may read

> **when:**
> `librarian-guppi` starts after the handoff and runs to the end, in a clean context. Its frame is the Render of `rule-documentation`. Its inputs are the `handoff.md` of the session's folder, every `materialize.yaml` the walk named, and `tags.md`. The index lines are the Greps that `rule-index-check` and `rule-synthesis` name.

> **then:**
> `make test-documentation` is green: materialize, generate and cleanup as one pipeline.
> **＋** Live, after the run: every decision line of the session's ledger has a Decision page and its target page, and no page exists that no ledger line produced.
> **＋** The librarian read only its inputs — `handoff.md`, the yamls that `guppi materialize` named, the index lines and `tags.md` — and these reads that its frame allows: a file where the harness saved the output of one of its own commands because the output was too long to show; the wiki pages it names in the report, each with the outcome and one of the reasons of its frame; a page under `vault/archive/` found by the Glob `vault/archive/**/<slug>.md` for a slug that a script named in an error, named in the report with the error; the unticked `- [ ]` lines of the `spec.md` files, and the lines this run ticked as its `git diff` shows them; of the ledger, only the count of its lines and the lines the yaml does not account for, named in the report; the output of `git status` and `git diff` on the files the scripts of this run wrote, never over `vault/wiki/decisions/` or `vault/archive/`; `vault/wiki/log.md` only through its `git diff` before the commit; and the old `vault/wiki/brief.md`.
> **＋** It edited no yaml entry beyond the marks and the entries of the index check and the synthesis. Its commands are in `event_log.md`, its commit is separate from the session's, and it did not stop to ask.
> **＋** It wrote `vault/wiki/brief.md` with the `Write` tool. The new brief holds no fact taken from the old brief, and the librarian put no file under `vault/` by `cp`, `mv`, a redirect or a heredoc.
> **＋** After `cleanup` and before the brief, it runs `uv run guppi render`, then `uv run guppi sprint`, then `uv run guppi backlog`, then `uv run guppi glossary`. Every line on their stderr is a flag. A file the render could not write is left to the next session start. `make lint` then passes its `render --check` step.
> **＋** After the brief and before the close, it runs `uv run guppi archive`. Every line on its stderr is a flag. The units it moved and the units it kept, with the reason, go into the report. It skips the session of the run, which is the latest session folder of the run day or else the nearest date back, across midnight too. The commit picks the move up.
> **－** It read no other part of a Spec, no plan, no Decision page, no `materialize.yaml` that `guppi materialize` did not name, and no line of `vault/wiki/log.md` outside its `git diff`. The `Makefile`, `guppi/` and `tests/` are the scripts' own files and may be read.
> **－** A hook's refusal of one of its calls is not worked around by another route: the librarian names the refusal in the report and goes on as the refusal says.
> **－** The librarian refuses an instruction of the handoff to repair a yaml entry, to read the ledger beyond the one read above, a Spec beyond its `- [ ]` lines or a Decision page, to search the archive, or to open an archived page that no script named in an error. It names what was asked and why in the report, and the refusal does not stop the run.
> **－** The librarian never searches `vault/archive/`: no Grep, `grep`, `find`, `ls` or `git status` runs over it, and no Glob other than `vault/archive/**/<slug>.md` for a slug a script named in an error.

> **tasks:**
> - [ ] update `rule-documentation` — the frame allows the reads of what this run changed, names `Write` for the brief, and forbids working around a refusal
>   - old: `` When the harness saves the output of one of your commands to a file because the output is too long to show, read that file: it is the output of your command (case 474.1). ``
>   - new: `` When the harness saves the output of one of your commands to a file because the output is too long to show, read that file: it is the output of your command (case 474.1). For the facts the brief takes from what this run left on disk, run `git status` and `git diff` on the files the scripts of this run wrote, never over `vault/wiki/decisions/` or `vault/archive/`. Read `vault/wiki/log.md` only through `git diff -- vault/wiki/log.md`, which before the commit shows only the lines this run added; never `Read`, `tail`, `head` or `grep` it. You may read the old `vault/wiki/brief.md` before you rewrite it; the new brief takes no fact from it. Write `vault/wiki/brief.md` with the `Write` tool, and put no file under `vault/` by `cp`, `mv`, a redirect or a heredoc. A hook that refuses one of your calls is not worked around by another route: name the refusal in the report and go on as the refusal says (case 530.1). ``
>   - old: `` nor read `spec.md` beyond its unticked `- [ ]` lines — the ones Readings due and Next session take (cases 200.3, 268.1, 271) ``
>   - new: `` nor read `spec.md` beyond its unticked `- [ ]` lines — the ones Readings due and Next session take — and the lines this run ticked, as its `git diff` shows them (cases 200.3, 268.1, 271, 530.1) ``
>   - change: `the librarian reads git status and git diff of what this run wrote, log.md only through its diff, and the old brief; it writes the brief with Write and never works around a refusal (case 530.1)`
> - [ ] update `estimate-documentation-completes` — the Criterion replaced whole
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the reads of what this run changed, log.md through its diff, the old brief read, the brief written with Write, no refusal worked around (case 530.1)`
> - [ ] `uv run guppi render`: `.claude/agents/librarian-guppi.md`
> - [ ] read `estimate-documentation-completes` — `make test-documentation`, then by hand on the librarian's run of a later session, from its transcript and `event_log.md`

> **ratification:**
> ```
> - decision[case 530.1][update][rule-documentation]{ref:rule-documentation}{supersedes:case 525}
> - decision[case 530.1][update][estimate-documentation-completes]{ref:rule-documentation}
> ```

### Case 530.2 — The bash guard's refusal sends a whole file to Write

> **given:**
> `rule-bash-guard` — the hook on `PreToolUse` of `Bash` that refuses a heredoc
> **＋** `guppi/bashguard.py` — the hook's code, which prints the refusal
> **＋** `tests/test_bashguard.py` — the tests of the refusal and its text
> **＋** `estimate-bash-guard` — the promise of the hook
> **＋** `.claude/settings.json` — the registration; no other hook on `PreToolUse` of `Bash`
> **＋** `raw/<date>/event_log.md` — the log that takes the line of each refusal
> **＋** `/dev/null` — the one redirect target a heredoc may write to

> **when:**
> The agent calls `Bash`, and `uv run guppi bashguard` on `PreToolUse` reads `tool_input.command` of the payload and finds every heredoc (`<<` or `<<-`, the marker quoted or not) and its body up to the closing line.

> **then:**
> A body with a backslash, or a marker line that writes a file (`>` or `>>` not to `/dev/null`, `tee`), exits 2 with the reason on stderr: `bashguard: heredoc refused — <a backslash in its body | it writes <path>>. Write a whole file with the Write tool and change a file with Edit, never through Bash; only a script goes into the scratchpad, written with the Write tool and run by path. The refusal is this guard working as designed, not an event of the session: do not report it at Retro.`
> **＋** Before the refusal one line `- HH:MM:SS <stamp> bashguard refused: <reason>` goes to `raw/<date>/event_log.md`.
> **＋** A `<<<` here-string, a heredoc with no backslash and no file write, a command without a heredoc, another tool — exit 0.
> **＋** A payload the hook cannot read — exit 0 with one line on stderr.
> **－** The hook never raises.

> **tasks:**
> - [ ] update `rule-bash-guard` — the refusal text sends a whole file to Write
>   - old: `Write the script with the Write tool into the scratchpad and run it by path; change a file with Edit.`
>   - new: `Write a whole file with the Write tool and change a file with Edit, never through Bash; only a script goes into the scratchpad, written with the Write tool and run by path.`
>   - change: `the refusal text sends a whole file to Write and only a script to the scratchpad (case 530.2)`
> - [ ] update `estimate-bash-guard` — the Criterion replaced whole
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the refusal text sends a whole file to Write and only a script to the scratchpad (case 530.2)`
> - [ ] `guppi/bashguard.py` — the refusal text and the module docstring carry the new sentence
> - [ ] `tests/test_bashguard.py` — the refusal tests assert the new sentence whole
> - [ ] read `estimate-bash-guard` — `uv run pytest tests/test_bashguard.py`, then the first refusal of a later session, its message read on stderr

> **ratification:**
> ```
> - decision[case 530.2][update][rule-bash-guard]{ref:rule-bash-guard}
> - decision[case 530.2][update][estimate-bash-guard]{ref:rule-bash-guard}
> ```
