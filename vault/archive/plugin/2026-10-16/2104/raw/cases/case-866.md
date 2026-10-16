## Case 866 — The close command names the Bash tool

> **context:**
> At the end of its run the librarian commits by the command that the Render of `rule-close` writes into `.claude/agents/librarian-guppi.md`: `git add vault $(uv run --project .guppi guppi render --paths) && git commit -m "docs(vault): librarian, <date>"` (case 857). The handoff of session 1712 reports, and the brief carries as a defect, that Windows PowerShell 5.1 does not parse the `&&` of that command. The Render of `rule-documentation` gives the librarian the tools `Read, Grep, Glob, Bash, Edit, Write`, so the librarian has no PowerShell tool and runs the command with the Bash tool, where `&&` and `$(...)` parse; the brief of session 1712 says its close commit was run with the Bash tool. The Render of `rule-spec-box` tells the main agent not to commit after the librarian's run, so no other agent runs this command. The defect does not reach the librarian as it stands; the Render does not say which shell the command is written for. The person chose to name the Bash tool in the Render and to leave the command as it is. Splitting the command in two was turned down: the claim that its `$(...)` runs alike in Windows PowerShell 5.1 was never checked.
>
> The new words hold in any project that installs GUPPI, since every Claude Code project has the Bash tool; `rule-close` has `core: true`, and the new text holds no pointer to a case, so it needs no bracket for `guppi ship`. The Purpose of `rule-close` speaks of a separate commit and names no shell, so it stands. `estimate-close-commits` checks the change, and its Criterion stands, as the person chose: its `When` reads that the librarian commits as `.claude/agents/librarian-guppi.md` says, and its `Then` lines read the commit in `git log`, so a command that does not parse shows as no commit; its `purpose` and `method` name no shell. Its reading is already due after this session's librarian run; that run loads its agent file before it renders, so it commits by the Render of Case 857, and the new words change nothing the librarian does. A Grep for `rule-close` over the repository outside `vault/raw/` and `vault/archive/` printed nine files: `vault/wiki/brief.md`, `vault/wiki/log.md`, `vault/wiki/rules/rule-close.md`, `vault/wiki/rules/rule-documentation.md`, `vault/wiki/rules/rule-session.md`, `vault/wiki/estimates/estimate-close-commits.md`, `vault/wiki/estimates/estimate-brief-carries-the-run-facts.md`, `.claude/agents/librarian-guppi.md` and `.guppi/guppi/render.py`. The hits in `rule-session`, `rule-documentation` (the place of the splice), `estimate-brief-carries-the-run-facts` and `render.py` name the close commit and no shell, so they stand; the agent file follows the render. A Grep for `librarian-guppi|rule-close|git add vault` over `.guppi/tests/` printed `test_grepguard.py`, which uses the name as an agent type and does not read the file.

> **problem:**
> The close command of the librarian is written for a POSIX shell, and its Render does not say so, so a reader may take it for a command that runs in Windows PowerShell 5.1, which does not parse its `&&`.

> **recommend:**
> - **What should this Case do with the close command?**
>   - Recommended: (a) name the Bash tool in the Render and keep the command as it is.
>   - Answer: agreed, (a).
> - **How is this change checked?**
>   - Recommended: (a) use `estimate-close-commits` as it stands; no Estimate is created or changed.
>   - Answer: agreed, (a).

> **given:**
> `rule-close`: its Render sets the close command of the librarian.
> **＋** `.claude/agents/librarian-guppi.md`: the agent file that the render writes from that Render.
> **＋** `rule-documentation`: its Render gives the librarian its tools.
> **＋** `estimate-close-commits`: checks the close commit; its Criterion stands.

> **when:**
> The librarian reaches the close step of `.claude/agents/librarian-guppi.md`.

> **then:**
> The librarian runs the close command with the Bash tool.
> **＋** The close command stays one line, `git add` and `git commit` joined by `&&`.
> **－** The librarian does not run the close command in PowerShell.

> **tasks:**
> - [ ] update `rule-close`
>   - old: `Commit the vault with the files the render wrote:`
>   - new: `Commit the vault with the files the render wrote, by the Bash tool, since the command is written for a POSIX shell:`
>   - change: `the close command is run by the Bash tool`
> - [ ] `uv run --project .guppi guppi render`: `.claude/agents/librarian-guppi.md`

> **ratification:**
> ```
> - decision[case 866][update][rule-close]{ref:rule-close}
> ```
