## Case 474 — The librarian opens an archived page by its slug, reads the saved output of its own command, and finds the form of a synthesis entry in its frame

> **context:**
> This Case replaces Case 471 with the same content. After 471 was ratified again, the plan file still held the first body of 471 under its parent heading, with the same `replace` pairs on `rule-documentation` and `rule-synthesis`. Those first pairs used up the anchors, so the pairs of 471.1 missed and `guppi ratified` refused them. The agent may not edit the plan. A superseding Case removes 471 from the Spec. `remove_case` removes a Case together with its sub-cases, but `mark_superseded` in `guppi/materialize.py` marks only the entries whose case id is exactly the one named. So the lines of 474 carry one `{supersedes:case N}` block each for 471, 471.1 and 471.2 (case 429), and every entry of the three ids is superseded.
> The librarian runs after the handoff with the frame of `rule-documentation`, rendered into `.claude/agents/librarian-guppi.md`. The frame bans every read of `vault/archive/`, and only the prose holds the ban. `estimate-documentation-completes` failed on the librarian run over session 1819. The transcript of that run shows two reads outside the frame. First, the index Grep over `vault/wiki/lessons/` printed 21 KB. The harness saved that output to a file under `~/.claude/projects/…/tool-results/`, and the librarian read the file back. That file is the index lines, and the frame allows the index lines, but the Criterion counts the read as a breach. Second, at 20:40:20 and 20:40:26 the librarian grepped every `vault/raw/*/*/materialize.yaml` for `librarian:` entries, and at 20:40:39 it ran `grep -rln "status: clustered" raw archive`. It was looking for an earlier synthesis entry to copy its form. The event log of 2026-09-27 shows the same search in the librarian run of 04:20:33, over the yaml of session 2026-09-26/1745. It also shows that the librarian run of 18:08–18:13 listed `vault/archive/` and read a file under `~/.claude/projects/`. The line at 23:38:43 comes before the handoff of session 2050, so it is not from a librarian run. The frame names the fields of a synthesis entry but shows none. `tests/test_generate.py` holds a synthesis `create` of an Insight, but the frame does not point to it.
> The full ban also blocks one read that the librarian needs. `guppi/generate.py` fails on a slug taken by an archived page and on a `rename` of an archived page. Its error names only the slug, and archived pages lie at any depth under `vault/archive/`. The frame tells the librarian to say why a script failed, but it may open only pages under `vault/wiki/`. `rule-ask` finds an archived page by slug alone, with the Glob `vault/archive/**/<slug>.md`, and this Case gives the librarian the same lookup.
> `rule-documentation` is `draft`, and `estimate-documentation-completes` is `failed`. The Case creates no page, so no vault query ran. In the frame: the Render of `rule-synthesis` keeps "Do not read the archive", and its Purpose keeps "The archive is not read". Both are about the synthesis, which still does not read the archive. `estimate-synthesis-clusters` says, of the whole run, "no archive file was read". An archived page opened for a script's error would fail that line, so sub-case 474.2 replaces that Criterion whole and limits the line to the synthesis. `estimate-synthesis-keeps-actioned-by-the-mark` speaks only of `addressed_by`, and it stands.
> In the rounds and at pre-spec, the person chose these answers: allow the saved output of the librarian's own command; do not ban the archive completely, but allow the Glob by slug for a script's error and forbid any search of the archive; add no hook; write every form of a synthesis entry in the frame itself, with a ban on reading a `materialize.yaml` that `materialize` did not name; and add the sub-case for `estimate-synthesis-clusters`.

> **problem:**
> The frame bans a read that the librarian needs, the read of an archived page named in a script's error, and it does not say how to find that page. It counts the saved output of the librarian's own command as a breach. It gives no example of a synthesis entry, so the librarian searches the yamls of other sessions and the archive for one. Two Estimates fail on reads that the frame should allow or should make needless. Case 471, which decided this, cannot be written into the Spec as it stands.

> **recommend:**
> Change the frame. The librarian finds an archived page only by the Glob `vault/archive/**/<slug>.md`, for a slug that a script named in an error. It may read the file that holds the saved output of its own command, and it never searches the archive. The synthesis section gets the form of each of its entries and a ban on reading yamls that `materialize` did not name. Both Criteria are replaced whole to match. Carry it as Case 474, which supersedes 471, 471.1 and 471.2. A hook that refuses every read of the archive was rejected, because it would also block the read by slug that a script's error needs.

### Case 474.1 — The frame and the promise of the librarian's run

> **given:**
> `rule-documentation` — the frame of the librarian: its inputs, its bans and its refusals
> **＋** `rule-synthesis` — the synthesis section of the frame
> **＋** `rule-index-check` — the index lines of the frame
> **＋** `.claude/agents/librarian-guppi.md` — the agent file rendered from both rules
> **＋** `estimate-documentation-completes` — the promise of the phase, its Criterion replaced whole
> **＋** `guppi/generate.py` — the script whose error can name an archived page
> **＋** `guppi/`, `tests/`, `Makefile` — the scripts' own files the librarian may read
> **＋** `vault/archive/`, `vault/archive/**/<slug>.md` — the archive, and the one Glob that finds a page in it by slug; the archive is never searched

> **when:**
> `librarian-guppi` starts after the handoff and runs to the end, in a clean context. Its frame is the Render of `rule-documentation`. Its inputs are the `handoff.md` of the session's folder, every `materialize.yaml` the walk named, and `tags.md`. The index lines are the Greps that `rule-index-check` and `rule-synthesis` name.

> **then:**
> `make test-documentation` is green: materialize, generate and cleanup as one pipeline.
> **＋** Live, after the run: every decision line of the session's ledger has a Decision page and its target page, and no page exists that no ledger line produced.
> **＋** The librarian read only the following, and nothing else:
> - `handoff.md`, the yamls that `guppi materialize` named, the index lines and `tags.md`;
> - a file where the harness saved the output of one of the librarian's own commands because the output was too long to show;
> - the wiki pages it names in the report, each with the outcome and one of the reasons of its frame (same or near; a candidate cluster; a script's error; a fact for the brief);
> - a page under `vault/archive/` found by the Glob `vault/archive/**/<slug>.md` for a slug that a script named in an error, named in the report with the error;
> - the unticked `- [ ]` lines of the `spec.md` files, for Readings due and Next session;
> - of the ledger, only the count of its lines and the lines the yaml does not account for, named in the report.
>
> It read no other part of a Spec, no plan, no Decision page, and no `materialize.yaml` that `guppi materialize` did not name. The `Makefile`, `guppi/` and `tests/` are the scripts' own files and may be read.
> **＋** It edited no yaml entry beyond the marks and the entries of the index check and the synthesis. Its commands are in `event_log.md`, its commit is separate from the session's, and it did not stop to ask.
> **＋** After `cleanup` and before the brief, it runs `uv run guppi render`, then `uv run guppi sprint`, then `uv run guppi backlog`, then `uv run guppi glossary`. Every line on their stderr is a flag. A file the render could not write is left to the next session start. `make lint` then passes its `render --check` step.
> **＋** After the brief and before the close, it runs `uv run guppi archive`. Every line on its stderr is a flag. The units it moved and the units it kept, with the reason, go into the report. It skips the session of the run, which is the latest session folder of the run day or else the nearest date back, across midnight too. The commit picks the move up.
> **－** The librarian refuses an instruction of the handoff to repair a yaml entry, to read the ledger beyond the one read above, a Spec beyond its `- [ ]` lines or a Decision page, to search the archive, or to open an archived page that no script named in an error. It names what was asked and why in the report, and the refusal does not stop the run.
> **－** The librarian never searches `vault/archive/`: no Grep, `grep`, `find` or `ls` runs over it, and no Glob other than `vault/archive/**/<slug>.md` for a slug a script named in an error.

> **tasks:**
> - [ ] update `rule-documentation`
>   - old: `` Never read `ledger.md`, `plan.md`, `wiki/decisions/` or `vault/archive/`, nor ``
>   - new: `` Never read `ledger.md`, `plan.md` or `wiki/decisions/`, never search `vault/archive/`, nor read ``
>   - old: `name that read in the report (case 349).`
>   - new: `` name that read in the report (case 349). When a script names a slug in an error and you say why it failed, find its page under `vault/archive/` only by the Glob `vault/archive/**/<slug>.md`, open it, and name the page in the report; no other Glob, Grep, `grep`, `find` or `ls` runs over the archive (case 474.1). When the harness saves the output of one of your commands to a file because the output is too long to show, read that file: it is the output of your command (case 474.1). ``
>   - old: `a Spec beyond its unticked lines, a decision page or the archive — you do not`
>   - new: `a Spec beyond its unticked lines, a decision page, a search of the archive or an archived page that no script named in an error — you do not`
>   - change: `the librarian finds an archived page by the Glob of the slug a script named in an error, never searches the archive, and reads the saved output of its own command (case 474.1)`
> - [ ] update `rule-synthesis`
>   - old: `` Mark each entry you add with `librarian: synthesis`. ``
>   - new:
>     ````
>     Mark each entry you add with `librarian: synthesis`. Read no `materialize.yaml` other than the ones `guppi materialize` names, and look for no earlier entry: the entries of the synthesis have these forms (case 474.1).
>
>     ```yaml
>     # a new Insight from two lessons of one cause
>     - kind: create
>       category: insights
>       slug: insight-<area>-<pattern>
>       origin: <the origin of the new lesson entry>
>       fields: {type: insight, pattern: <the shared cause>, children: [<lesson-a>, <lesson-b>]}
>       tags: [<the union of the tags of both lessons>]
>       sections: {Pattern: <text>, Proposal: <text>}
>       librarian: synthesis
>     # right after the create, only when the lesson entry carries addressed_by
>     - kind: update
>       category: insights
>       slug: insight-<area>-<pattern>
>       origin: <the origin of the new lesson entry>
>       set: {status: actioned, addressed_by: decision-case-N}
>       change: born actioned, its cause closed by case N (synthesis)
>       librarian: synthesis
>     # an existing Insight of the same pattern
>     - kind: update
>       category: insights
>       slug: <the live Insight>
>       origin: <the origin of the new lesson entry>
>       set: {children: [<its children>, <the new lesson>]}
>       change: child <the new lesson> added (synthesis)
>       librarian: synthesis
>     # set also takes status: open, or addressed_by: decision-case-N, as the rule above says
>     # each lesson that joins an Insight
>     - kind: update
>       category: lessons
>       slug: <lesson-a>
>       origin: <the origin of the new lesson entry>
>       set: {status: clustered, insight: <the Insight>}
>       change: clustered under <the Insight> (synthesis)
>       librarian: synthesis
>     ```
>     ````
>   - change: `the synthesis shows the form of each of its entries and reads no yaml that materialize did not name (case 474.1)`
> - [ ] update `estimate-documentation-completes`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — an archived page found by the Glob of the slug a script named in an error, the archive never searched, the saved output of the librarian's own command allowed, no yaml that materialize did not name (case 474.1)`
> - [ ] `uv run guppi render`: `.claude/agents/librarian-guppi.md`
> - [ ] read `estimate-documentation-completes` — `make test-documentation` and the live reading of the transcript of the librarian's run in a later session

> **ratification:**
> ```
> - decision[case 474.1][update][rule-documentation]{ref:rule-documentation}{supersedes:case 471}{supersedes:case 471.1}
> - decision[case 474.1][update][rule-synthesis]{ref:rule-synthesis}
> - decision[case 474.1][update][estimate-documentation-completes]{ref:estimate-documentation-completes}
> ```

### Case 474.2 — The synthesis promise bans the archive at synthesis only

> **given:**
> `estimate-synthesis-clusters` — the promise of the synthesis, its Criterion replaced whole
> **＋** `rule-synthesis` — the synthesis section of the frame
> **＋** `.claude/agents/librarian-guppi.md` — the agent file that holds the synthesis
> **＋** `materialize.yaml` — the yaml the synthesis appends its entries to
> **＋** `vault/wiki/lessons/`, `vault/wiki/insights/` — the folders the Greps of the synthesis run over
> **＋** `vault/archive/` — the archive, which the synthesis does not read

> **when:**
> `librarian-guppi` does the synthesis in a live run whose `materialize.yaml` holds at least two lesson entries.

> **then:**
> The report names the Greps of the synthesis, `^(root_cause|deferred_by):` over `vault/wiki/lessons/` and `^(pattern|deferred_by):` over `vault/wiki/insights/`, and the comparisons made against their lines, by meaning.
> **＋** Two lessons with one root cause and no Insight give one `create` of an Insight with `pattern`, both children, the union of their tags, `Pattern` and `Proposal`, and one `update` per lesson with `set: {status: clustered, insight: <slug>}`.
> **＋** A lesson whose root cause matches the pattern of a live Insight gives an `update` of that Insight with the lesson added to its `children`, and an `update` of the lesson.
> **＋** Every entry the synthesis adds carries `librarian: synthesis`.
> **＋** Every lesson page read at synthesis is named in the report with the outcome: the Insight it joined, or none and why.
> **＋** A lesson without a pair stays `new`.
> **－** The synthesis reads no file under `vault/archive/`: an actioned Insight stays live with its pattern in its index line.

> **tasks:**
> - [ ] update `estimate-synthesis-clusters`
>   - set: `{status: pending, method: "one reading by hand of the yaml and the report after a live librarian run whose yaml holds at least two lesson entries"}`
>   - change: `the Criterion replaced whole — the ban on the archive is the synthesis's, not the whole run's; the base text and the block of case 147.4 folded into one Criterion (case 474.2)`
> - [ ] read `estimate-synthesis-clusters` — by hand, the yaml and the report of a live librarian run with at least two lesson entries, in a later session

> **ratification:**
> ```
> - decision[case 474.2][update][estimate-synthesis-clusters]{ref:estimate-synthesis-clusters}{supersedes:case 471.2}
> ```
