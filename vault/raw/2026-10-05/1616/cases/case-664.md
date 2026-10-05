## Case 664 — A hook leaves the Decision pages out of every search

> **context:**
> `rule-search-leaves-out-decisions` keeps the text of Decision pages out of the context of the agents. Today it is only text: `.claude/rules/search-leaves-out-decisions.md` tells the main agent, `ask-guppi` and `case-guppi` to add `!**/decisions/**` at the end of the glob of every Grep over the wiki. Its Estimate `estimate-search-leaves-out-decisions-in-every-agent` failed at the `/hi` of session 1343 (L10 of that session's ledger): the file stood in all seven contexts of session 0311, but 9 Greps over `vault/`, `vault/wiki/` or the root carried no exclusion, and `case-guppi` a1cf96ac9df5edd1c read `decision-case-432` because the `addressed_by` of an Insight named it, which is no reason of `.claude/agents/ask-guppi.md`. The handoff of 1343 adds that `ask-guppi` broke the rule again, once by putting the exclusion first. The order matters: a Grep of `^type: decision` over `vault/wiki/` with the glob `!**/decisions/** *.md` counted 1127 files, pages under `vault/wiki/decisions/` among them, and the same Grep with the glob `*.md !**/decisions/**` printed only `vault/wiki/rules/rule-decisions-schema.md`. Both probes printed counts and paths, no text of a Decision page.
>
> The person chose that a `PreToolUse` hook on Grep adds the exclusion at the end of the glob, like the hook of `rule-page-read` that cuts the History from a read by `updatedInput`, for every agent, the librarian too, since `.claude/agents/librarian-guppi.md` says its job does not need the text of a Decision page. The person kept the two reasons to open a Decision page, so the read through `addressed_by` stays a breach that the check counts. The person chose two checks. Case 664.1 builds the hook and creates `estimate-search-leaves-out-decisions-by-the-grep-hook`. Case 664.2 replaces the Criterion of `estimate-search-leaves-out-decisions-in-every-agent`, so that it reads only the load of the file and the reads of Decision pages, and sets its `purpose` and `method` anew, which named the Greps. The hook stays on `rule-search-leaves-out-decisions`, which keeps `enforcement: render` for its file and takes an `implementation_ref`, as `rule-ledger-tail` does; the rule keeps its Leaf, with two Estimates. The Render loses its two lines on the glob and gains one line on the hook. `.claude/settings.json` registers no hook on `PreToolUse` of Grep today, so the new one runs alone on its event. `estimate-hook-registry-rendered` stands: its Criterion speaks of the file equal to the Render, which a render update keeps (case 378.5). At pre-spec the main agent asked whether an agent may Grep inside `vault/wiki/decisions/`, since the Render of `rule-ask` lets `ask-guppi` open or grep that folder for its two reasons. The person chose that it may: the hook leaves unchanged a Grep whose `path` is that folder or lies in it, and the text of a Decision page reaches an agent by a Read of its path or by such a Grep, for a reason of its frame alone. So the Render of `rule-ask` stands, and 664.2 promises this. A Grep whose `path` is one file is left as it is too: the glob does not filter a file that is named directly. A Grep of `^type:` with the path `vault/wiki/decisions/decision-case-640.md` and the glob `!**/decisions/**` still counted 1 match in that file. Because the hook covers the librarian, 664.1 sets the `purpose` of `rule-search-leaves-out-decisions` anew and says so in its Purpose and Render. The file itself still binds only the three agents. The line of `.claude/agents/librarian-guppi.md` that says no read is forbidden to the librarian stays true: a Read of a Decision page, or a Grep inside its folder, still works, and still takes a line under Flags of the brief. `estimate-documentation-completes` stands for the same reason. Its Criterion line asks for a Flags line for each read of the text of a Decision page, and a Grep the hook filtered reads no such text.
>
> A Grep of `search-leaves-out-decisions` over the repository root, with the glob `!**/decisions/** !vault/raw/** !vault/archive/**`, printed 9 files. `vault/wiki/brief.md` and `vault/wiki/log.md` are not read. `rule-search-leaves-out-decisions` and `estimate-search-leaves-out-decisions-in-every-agent` enter the Case. `vault/wiki/rules/rule-harness.md` lists the rule as a child, which stays true. `vault/wiki/rules/rule-ask.md` and its render `.claude/agents/ask-guppi.md`, and `vault/wiki/estimates/estimate-ask-finds.md`, name a search that breaks a rule of the file; this stays true, since the file keeps its rule on the reads. The last `－` line of the Criterion of `vault/wiki/estimates/estimate-ask-searches-at-prespec.md` says that `estimate-search-leaves-out-decisions-in-every-agent` reads whether a Grep or a Read of the agent reaches `vault/wiki/decisions/`. After the split, that is false for the Grep. So Case 664.3 replaces that Criterion whole, with every other line as it stands. The Estimate is already `pending` from case 655. Its `purpose` names only a count over Decision pages that is not run again, and its `method` names no Decision page. Neither states what the replaced line said, so both stand. Cases 662 and 663 of this session change other pages and other moments, so this Case does not clash with them.
>
> The check of the file noted lines of the two replaced Criteria that the new ones do not carry word for word. In `estimate-search-leaves-out-decisions-in-every-agent`, the line on the Greps leaves for the new Estimate of 664.1, the `When:` line names a Read, or a Grep inside `vault/wiki/decisions/`, in place of Grep, Glob or Read, and the line on the reads names that Grep and the two reasons of the frame. In `estimate-ask-searches-at-prespec`, the last `－` line splits in two: one line for the Greps over a folder that holds the Decision pages, and one for the Reads and the Greps inside it. Each change is made by intent, and the rest of each Criterion is carried whole. The check noted too that the `－` lines of 664.2 and 664.3 that leave the Greps or the Reads to another Estimate share most of their words. That is by intent: each line bounds its own Estimate, and each names the other check. The `－` line of 664.1 on a Grep inside `vault/wiki/decisions/` and the line of 664.2 on how a Decision page may reach an agent also share words. That is by intent too: 664.1 says the hook lets such a Grep pass, and 664.2 says the agent runs it only for a reason of its frame.

> **problem:**
> The rule that keeps the text of Decision pages out of a search is text that loads but is not followed. Agents leave the exclusion out, or put it first, where it does not work. The questions were how the exclusion is enforced, whether a Decision page named by `addressed_by` may be opened, whether an agent may Grep inside the folder of the Decision pages, which agents the hook covers, and how the change is checked.

> **recommend:**
> - **How every search leaves out the Decision pages**
>   - Recommended: (a) a hook adds the exclusion at the end of the glob of each Grep over the wiki, by changing the call, as the hook of `rule-page-read` does for a read; the rule file keeps only the part on reading a Decision page.
>   - Answer: agreed, (a).
> - **When an agent may open a Decision page**
>   - Recommended: (b) keep the two reasons; a read through `addressed_by` stays a breach that the check counts.
>   - Answer: agreed, (b).
> - **Which agents the new hook covers**
>   - Recommended: (a) every agent, the librarian too.
>   - Answer: agreed, (a).
> - **How the change is checked**
>   - Recommended: (a) two checks: a new Estimate of the hook, read by a test and one live search in the main agent and in a subagent; the existing Estimate rewritten to cover only the load of the file and the reads of Decision pages.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: at pre-spec, may an agent Grep inside `vault/wiki/decisions/`: (a) only a Read, `rule-ask` changes and the hook covers a Grep inside the folder too; or (b) a Grep is allowed for the two reasons, the hook leaves a Grep whose path is inside `decisions/` unchanged, 664.2 says the text arrives by a Read or such a Grep for one of the two reasons, and the frame of `ask-guppi` stays. The person chose (b).
>   - Taken: 664.1 leaves unchanged a Grep whose `path` is `vault/wiki/decisions/` or lies in it; 664.1 sets the rule's `purpose` and Purpose anew and makes its Render say the hook covers every agent and a Grep inside the folder is allowed for a reason; 664.2 promises that the text arrives by a Read or such a Grep, for a reason of the frame only.

### Case 664.1 — A hook adds the exclusion to every Grep over the wiki

> **given:**
> `estimate-search-leaves-out-decisions-by-the-grep-hook`: the new check of the hook.
> **＋** `rule-search-leaves-out-decisions`: the rule of the hook and of the file it renders.
> **＋** `.claude/rules/search-leaves-out-decisions.md`: the file rendered from `rule-search-leaves-out-decisions`.
> **＋** `guppi/grepguard.py`: the new hook `uv run guppi grepguard`.
> **＋** `guppi/cli.py`: the entry point that maps the command to its module.
> **＋** `tests/test_grepguard.py`: the tests of the hook.
> **＋** `rule-hook-registry`: its Render registers the hook in `.claude/settings.json`.
> **＋** `.claude/settings.json`: the file rendered from `rule-settings` and its children.
> **＋** `vault/wiki/decisions/`: the folder of the Decision pages.
> **＋** `!**/decisions/**`: the glob filter that leaves that folder out.
> **＋** `.claude/agents/librarian-guppi.md`: the frame of the librarian, whose Greps the hook changes too.

> **when:**
> The main agent or any subagent calls Grep, and `uv run guppi grepguard` of `guppi/grepguard.py`, registered on `PreToolUse` of `Grep` in `.claude/settings.json`, reads the call.

> **then:**
> When the searched folder — the `path` of the call, or the working directory when the call has none — is a folder that holds `vault/wiki/decisions/`, the hook returns the call by `updatedInput` with `!**/decisions/**` at the end of its `glob`, after a space when the `glob` holds another filter, and with no permission decision.
> **＋** A `glob` that already ends with `!**/decisions/**` is not changed; one that holds it elsewhere gets it again at the end.
> **＋** The Grep then prints no line and no path of a file under `vault/wiki/decisions/`.
> **＋** A call of the librarian is changed in the same way as a call of any other agent.
> **－** A Grep whose `path` is `vault/wiki/decisions/` or lies in it passes unchanged: an agent greps there only for a reason of its frame.
> **－** A Grep whose `path` is one file, or a folder that does not hold `vault/wiki/decisions/`, passes unchanged.
> **－** The hook never refuses a call; a payload it cannot read or an error lets the call pass unchanged.

> **tasks:**
> - [ ] create `estimate-search-leaves-out-decisions-by-the-grep-hook`
>   - ref: `rule-search-leaves-out-decisions`
>   - kind: `QA`
>   - purpose: `Whether every Grep over vault/wiki/ or a folder that holds it runs with !**/decisions/** at the end of its glob, added by the PreToolUse hook, and prints nothing under vault/wiki/decisions/`
>   - method: `uv run pytest tests/test_grepguard.py, then by hand at the /hi of a later session after the render a Grep over vault/wiki/ with no glob in the main agent and in a subagent, whether it prints a file under vault/wiki/decisions/`
>   - tags: `[hooks, harness, session]`
> - [ ] update `rule-search-leaves-out-decisions`
>   - old: `` - Every Grep whose `path` is `vault/wiki/` or a folder that holds it, the repository root included, carries `!**/decisions/**` in its `glob`: alone, or after another filter with a space between them, as in `*.md !**/decisions/**`. - A glob written from the searched folder, such as `!decisions/**`, does not leave the folder out: the Grep tool reads a glob that holds a slash from the working directory, the repository root, and not from its `path`. ``
>   - new: `` - A hook adds `!**/decisions/**` at the end of the `glob` of every Grep whose `path` is `vault/wiki/` or a folder that holds it, the repository root included, in every agent, the librarian too, whom the rest of this file does not bind; a Grep over such a folder prints nothing under `vault/wiki/decisions/`, and an exclusion written first, where it does not work, is put last by the hook (case 664.1). ``
>   - old: `` - The text of a Decision page under `vault/wiki/decisions/` is read only by a Read of its path, and only for a reason the frame of the agent names. ``
>   - new: `` - The text of a Decision page under `vault/wiki/decisions/` is read only by a Read of its path, or by a Grep whose `path` is that folder or lies in it, which the hook leaves unchanged, and only for a reason the frame of the agent names (case 664.1). ``
>   - old: `The librarian follows its own frame, which flags such a read rather than forbids it.`
>   - new: `The librarian follows its own frame, which flags such a read rather than forbids it; the hook filters its Greps over the wiki too, and a read of a Decision page it needs stays open to it (case 664.1).`
>   - old: `` and if it does not, a later Case moves the text to `CLAUDE.md`. ``
>   - new: `` and if it does not, a later Case moves the text to `CLAUDE.md`. The file loaded in every agent, but the agents did not follow it for Grep: in the reading of session 1343 nine Greps over the wiki carried no exclusion, and one put it first, where it leaves nothing out. So a `PreToolUse` hook on Grep adds the exclusion at the end of the glob, in every agent, the librarian too; a Grep inside `vault/wiki/decisions/` it leaves unchanged, and the file keeps the rule on reading a Decision page (case 664.1). ``
>   - set:
>     ```
>     implementation_ref: [guppi/grepguard.py, tests/test_grepguard.py, .claude/settings.json]
>     purpose: "Prevents the text of a Decision page from entering the context of an agent through a search of the vault: a hook leaves the Decision pages out of every Grep over the wiki, and the main agent, ask-guppi and case-guppi read a Decision page only for a reason of their frame"
>     ```
>   - change: `a PreToolUse hook on Grep adds !**/decisions/** at the end of the glob in every agent, a Grep inside decisions/ left unchanged; the Render keeps the rule on reads; purpose set anew (case 664.1)`
> - [ ] update `rule-hook-registry`
>   - old:
>     ```
>     { "matcher": "Read",
>       "hooks": [ { "type": "command", "command": "uv run guppi pageread", "timeout": 30 } ] }
>     ```
>   - new:
>     ```
>     { "matcher": "Read",
>       "hooks": [ { "type": "command", "command": "uv run guppi pageread", "timeout": 30 } ] },
>     { "matcher": "Grep",
>       "hooks": [ { "type": "command", "command": "uv run guppi grepguard", "timeout": 30 } ] }
>     ```
>   - change: `the hook grepguard registered on PreToolUse of Grep (case 664.1)`
> - [ ] `guppi/grepguard.py`: the hook reads the payload as UTF-8, judges whether the searched folder holds `vault/wiki/decisions/` and does not lie in it by `inside` of `guppi/pageread.py`, and prints `hookSpecificOutput.updatedInput` with the glob ended by `!**/decisions/**`; it never raises; the module docstring describes the hook and names the rule page.
> - [ ] `guppi/cli.py`: the command `grepguard` maps to `grepguard.run`, and the docstring lists it among the hook commands.
> - [ ] `tests/test_grepguard.py`: one test per line of the `then`, among them a Grep with no path, a Grep with the exclusion first, a Grep whose path is `vault/wiki/decisions/`, and a Grep whose path is one file.
> - [ ] `uv run guppi render`: `.claude/settings.json`
> - [ ] `uv run guppi render`: `.claude/rules/search-leaves-out-decisions.md`
> - [ ] read `estimate-search-leaves-out-decisions-by-the-grep-hook`

> **ratification:**
> ```
> - decision[case 664.1][create][estimate-search-leaves-out-decisions-by-the-grep-hook]{ref:rule-search-leaves-out-decisions}{tags:hooks,harness,session}
> - decision[case 664.1][update][rule-search-leaves-out-decisions]{ref:rule-search-leaves-out-decisions}
> - decision[case 664.1][update][rule-hook-registry]{ref:rule-hook-registry}
> ```

### Case 664.2 — The rule file loads and a Decision page is read only for a reason of the frame

> **given:**
> `estimate-search-leaves-out-decisions-in-every-agent`: its Criterion, `purpose` and `method` are replaced.
> **＋** `rule-search-leaves-out-decisions`: the rule whose file the agents load.
> **＋** `.claude/rules/search-leaves-out-decisions.md`: the file rendered from `rule-search-leaves-out-decisions`.
> **＋** `.claude/agents/ask-guppi.md`: the two reasons to open a Decision page.
> **＋** `.claude/agents/librarian-guppi.md`: the frame of the librarian.
> **＋** `estimate-search-leaves-out-decisions-by-the-grep-hook`: the check of the Greps.
> **＋** `vault/wiki/decisions/`: the folder of the Decision pages.

> **when:**
> A session starts after `uv run guppi render` has written `.claude/rules/search-leaves-out-decisions.md` from `rule-search-leaves-out-decisions`, and the main agent, `ask-guppi` or `case-guppi` calls Read, or Grep with a `path` that is `vault/wiki/decisions/` or lies in it.

> **then:**
> `.claude/rules/search-leaves-out-decisions.md` stands in the context of the main agent, of `ask-guppi` and of `case-guppi`.
> **＋** The text of a Decision page reaches one of these agents only by a Read of its path or by a Grep whose `path` is `vault/wiki/decisions/` or lies in it, for a reason of `.claude/agents/ask-guppi.md` in `ask-guppi` and `case-guppi` — a page of its answer carries `deferred_by`, or the question asks why something was decided — and for no reason in the main agent.
> **－** An `addressed_by` that names a Decision page is no reason to read it.
> **－** Whether a Grep over a folder that holds `vault/wiki/decisions/` leaves that folder out is outside this promise: `estimate-search-leaves-out-decisions-by-the-grep-hook` reads it.
> **－** A Glob that prints the path of a Decision page breaks nothing: it shows no text of the page.
> **－** The calls of the librarian are outside this promise: it follows `.claude/agents/librarian-guppi.md`.

> **tasks:**
> - [ ] update `estimate-search-leaves-out-decisions-in-every-agent`
>   - set:
>     ```
>     status: pending
>     purpose: "Whether the main agent, ask-guppi and case-guppi load .claude/rules/search-leaves-out-decisions.md, and the text of a Decision page reaches them only by a Read of its path, or a Grep inside vault/wiki/decisions/, for a reason their frame names"
>     method: "by hand at the /hi of a later session: the transcripts of the main agent and of each ask-guppi and case-guppi of a session after the render of .claude/rules/search-leaves-out-decisions.md by case 664.1, whether the file stands in each context and each Read of a page under vault/wiki/decisions/ and each Grep inside that folder, read against the Criterion, recorded in the estimate line"
>     ```
>   - change: `the Criterion replaced whole — the load of the file and the reads of Decision pages only; the Greps move to estimate-search-leaves-out-decisions-by-the-grep-hook; purpose and method set anew (case 664.2)`
> - [ ] read `estimate-search-leaves-out-decisions-in-every-agent`

> **ratification:**
> ```
> - decision[case 664.2][update][estimate-search-leaves-out-decisions-in-every-agent]{ref:rule-search-leaves-out-decisions}
> ```

### Case 664.3 — The check of the searches of ask-guppi points to both checks of Decision pages

> **given:**
> `estimate-ask-searches-at-prespec`: its Criterion is replaced whole.
> **＋** `rule-ask`: the rule rendered into `.claude/agents/ask-guppi.md`.
> **＋** `.claude/agents/ask-guppi.md`: the frame of `ask-guppi`.
> **＋** `.claude/skills/pre-spec/SKILL.md`: the questions the main agent sends at pre-spec.
> **＋** `estimate-search-leaves-out-decisions-by-the-grep-hook`: the check of the Greps over Decision pages.
> **＋** `estimate-search-leaves-out-decisions-in-every-agent`: the check of the reads of Decision pages.
> **＋** `vault/wiki/rules/`: the folder the first Grep of the agent runs over.
> **＋** `vault/wiki/decisions/`: the folder of the Decision pages.

> **when:**
> At the first run of `/pre-spec` in a session, the main agent dispatches `ask-guppi` through the `Agent` tool with the plan file and the questions of `.claude/skills/pre-spec/SKILL.md`, and the agent follows `.claude/agents/ask-guppi.md` as rendered from `rule-ask`.

> **then:**
> The agent starts with the Grep `^(purpose|deferred_by):` over `vault/wiki/rules/`, then runs one Grep per other category the question touches.
> **＋** After those Greps it runs further Greps and Reads as a finding needs, including the search behind a count that a `context` states.
> **＋** A count of a `context` whose search covers `vault/wiki/decisions/` is not run again and is no finding.
> **－** Whether a Grep of the agent over a folder that holds `vault/wiki/decisions/` leaves that folder out is outside this promise: `estimate-search-leaves-out-decisions-by-the-grep-hook` reads it.
> **－** Whether a Read of the agent, or a Grep inside `vault/wiki/decisions/`, reaches a Decision page only for a reason of its frame is outside this promise: `estimate-search-leaves-out-decisions-in-every-agent` reads it.

> **tasks:**
> - [ ] update `estimate-ask-searches-at-prespec`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the Greps over a folder that holds the Decision pages are left to estimate-search-leaves-out-decisions-by-the-grep-hook, the Reads and the Greps inside it to estimate-search-leaves-out-decisions-in-every-agent (case 664.3)`
> - [ ] read `estimate-ask-searches-at-prespec`

> **ratification:**
> ```
> - decision[case 664.3][update][estimate-ask-searches-at-prespec]{ref:rule-ask}
> ```
