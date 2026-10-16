## Case 852 — /guppi:install offers to install uv when it is missing

> **context:**
> `/guppi:install` is the one skill of the plugin `guppi`. Its first step runs `uv --version`. When that fails, it says that GUPPI needs the tool `uv`, tells the person to install it and type `/guppi:install` again, stops and writes nothing. In `C:\PROJECTS\test-no-uv` it did just that, and the person said they would prefer the agent itself to offer to install `uv`; this session recorded `estimate-guppi-package-is-ready-after-the-install` as failed on that answer and on the offline install. The person chose that the agent asks whether it installs `uv` by the standalone installer of `uv` and runs it on a yes. After the installer, the agent runs `uv --version` again. When that passes, the install goes on in the same session, and its last message tells the person to start Claude Code from a new terminal, so that the hooks of the project find `uv`. When it fails, because this session of Claude Code does not see the new `uv`, the agent sends the person to a new terminal and a new `/guppi:install`. On a no, the agent shows the command and stops, writing nothing. The two installer commands in the new step come from the agent's knowledge: `case-guppi` could not read the installation page of `uv` from here. The person agreed that Work Mode reads that page before the render, so Case 852.1 holds a task that compares the commands with the page and stops on a difference, as condition 1 of `rule-where-to-stop` sets it. The rule is `rule-plugin-install`. Its Purpose holds one sentence on a missing `uv`, which Case 852.1 replaces, and its Render holds step 1, which Case 852.1 replaces, and step 7, to which Case 852.1 adds the new terminal. Its one Estimate, `estimate-plugin-install-writes-guppi-into-an-empty-project`, stands: its Criterion leaves out what the install does about `uv`, and its sentence that the last message tells the person to reopen Claude Code and type `/hi` stays true. The offer is a promise that can fail apart from the build of the environment, so Case 852.1 creates `estimate-plugin-install-offers-to-install-uv`, a slug that a Glob `vault/**/*install-uv*` did not print. Case 852.2 replaces the Criterion, `purpose` and `method` of `estimate-guppi-package-is-ready-after-the-install` without the missing-`uv` line and the project with no `uv`, so they no longer state the old stop. The new Criterion keeps the `When` line, the line that `uv --version` runs before any write, the line on `uv sync` after the copy and the line on the hooks word for word. It adds a `－` line that the install asks nothing about `uv` where `uv --version` passes, since the reading of this Estimate runs on the machine with `uv`, and the reading of `estimate-plugin-install-offers-to-install-uv` runs only where `uv` is missing. The line on a failed `uv --version` is dropped, since Case 852.1 sets that path anew and its Estimate checks it. At the person's word, Case 852.2 also drops the line on a failed `uv sync` and the offline project from that Estimate, so it keeps only the build of `.guppi/.venv/`. Case 853 of this session, the related item C4, sets what the install does when `uv sync` fails and creates its own Estimate on `rule-plugin-install` for it. That Case changes step 6 of the Render of `rule-plugin-install`, and Case 852.1 changes the description, step 1, step 7 and the Purpose sentence on a missing `uv`. Its case file, `vault/raw/2026-10-16/0342/cases/case-853.md`, was read whole and stands in the `given` of Case 852.1. The check of this file notes that the step 7 pair of Case 852.1 touches a sentence that Case 853 changes too. The check reads the end of the new step 6 of Case 853, which ends with a sentence that tells the agent not to send the person to `uv sync`, a reopen of Claude Code or `/hi`, and the start of step 7 as one sentence. The `old` of Case 852.1 starts at step 7, and the `old` of Case 853 ends at the end of step 6, so neither pair matches text the other changes. The two new texts were read side by side, and they fit. The new step 6 of Case 853 stops on a failed `uv sync` before step 7, and its ban on `/hi` binds only that failure. The new step 7 of Case 852.1 runs only after a successful step 6, and it adds the new terminal only when step 1 installed `uv`. The new Purpose sentence of Case 853 follows the sentence on `uv sync`, and Case 852.1 changes only the sentence on a missing `uv`. `guppi ship --check`, run by `uv run --project .guppi guppi check`, refuses a reference to a case in `plugin/skills/install/SKILL.md`, as `test_check_judges_the_plugin_skill_in_place` of `.guppi/tests/test_ship.py` shows, so the new Render text holds no pointer to a case; the pointer in the new Purpose sentence stands, since the page has no `core: true` and `guppi ship` does not write it. A Grep `rule-plugin-install|guppi:install` over the repository, outside `vault/raw/`, `vault/archive/`, `log.md` and `brief.md`, printed `vault/wiki/sprint.md`, `entity-sprint-plugin.md`, `plugin/skills/install/SKILL.md`, `estimate-clean-branch-writes-the-session-files.md`, `estimate-guppi-package-is-ready-after-the-install.md`, `estimate-morph-sets-up-the-project-at-the-first-hi.md`, `estimate-plugin-install-writes-guppi-into-an-empty-project.md`, `lesson-hi-fails-outside-a-git-repository.md`, `rule-clean-branch.md`, `estimate-sprint-plugin-installs-as-a-plugin.md`, `rule-harness.md`, `rule-plugin-install.md` and `rule-morph.md`, and no file under `.claude/`. The sentence of `rule-morph` that `/guppi:install` decides nothing and is no Case stands, since the person's yes to install a tool ratifies nothing in the vault. Its sentence, and the line of `estimate-morph-sets-up-the-project-at-the-first-hi`, that no settings file changes before the setup Case but by the copy and the render also stand, since the installer of `uv` writes no file of the project. The `method` of `estimate-clean-branch-writes-the-session-files` names the project with `uv` of the reading of `estimate-guppi-package-is-ready-after-the-install`, which Case 852.2 keeps. The other hits name the install without the step this Case changes. Case 851 sets the first `/hi` after the install and keeps the promise that the install runs no git command; this Case runs no git command and does not touch `/hi`. The Case adds no code that judges a text.

> **problem:**
> When `uv` is missing, `/guppi:install` only says so and stops. The person must find out how to install `uv` alone, though the agent could offer to install it.

> **recommend:**
> - **What should `/guppi:install` do when `uv` is missing?**
>   - Recommended: (a) offer to install it: ask, run the install command on a yes, and on a no show the command, say to type `/guppi:install` again after installing `uv`, and stop with nothing written.
>   - Answer: agreed, (a).
> - **Which command should install `uv`?**
>   - Recommended: (a) the official standalone installer for the system, a PowerShell command on Windows and a shell command on macOS and Linux; Work Mode reads the installation page of `uv` and checks the exact commands.
>   - Answer: agreed, (a).
> - **What should happen right after `uv` is installed?**
>   - Recommended: (a) run `uv --version` again; when it passes, go on with the install in the same session, its last message saying to start Claude Code from a new terminal; when it fails, say to open a new terminal, start Claude Code there and type `/guppi:install` again, and stop with nothing written.
>   - Answer: agreed, (a).
> - **How should we check that this works?**
>   - Recommended: (a) a new Estimate on `rule-plugin-install`, read by hand in an empty project with Claude Code started from a terminal that does not find `uv`, once answering no and once yes; and the Criterion of `estimate-guppi-package-is-ready-after-the-install` replaced without the missing-`uv` line.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: through Case 853, drop from the new Criterion of `estimate-guppi-package-is-ready-after-the-install` the line on a failed `uv sync` and the offline project, since Case 853 checks that failure with its own Estimate.
>   - Taken: Case 852.2 drops that line, and its `purpose` and `method` drop the failure and the offline project.

### Case 852.1 — /guppi:install asks to install uv when it is missing

> **given:**
> `rule-plugin-install`: the skill `/guppi:install` and its Render.
> **＋** `plugin/skills/install/SKILL.md`: the skill file rendered from `rule-plugin-install`.
> **＋** `estimate-plugin-install-offers-to-install-uv`: the new check of this behaviour.
> **＋** `https://docs.astral.sh/uv/getting-started/installation/`: the installation page of `uv`, with its standalone installer.
> **＋** `rule-where-to-stop`: its condition 1 stops Work Mode when a command differs from that page.
> **＋** `/hi`: the skill the person types after the install.
> **＋** `vault/raw/2026-10-16/0342/cases/case-853.md`: the Case of this session that changes step 6 and the Purpose of the same page.

> **when:**
> The person types `/guppi:install` of `plugin/skills/install/SKILL.md` in an empty project open in Claude Code, where `uv --version` fails.

> **then:**
> Before it writes anything, the agent says that GUPPI needs the tool `uv` and asks the person whether it installs `uv` now by the standalone installer of `uv` for the system: a PowerShell command on Windows, a shell command on macOS and Linux.
> **＋** On the person's no, it shows that command, says that the person installs `uv` with it and types `/guppi:install` again, and stops.
> **＋** On the person's yes, it runs that command, and then `uv --version` again.
> **＋** When `uv --version` then passes, it goes on with the install in the same session, and its last message tells the person to start Claude Code in the project from a new terminal and type `/hi`.
> **＋** When `uv --version` still fails, it says that this session of Claude Code does not find the new `uv`, and that the person opens a new terminal, starts Claude Code there and types `/guppi:install` again, and stops.
> **－** When the installer fails or Claude Code does not run it, the agent shows its output and the command, says that the person installs `uv` with it and types `/guppi:install` again, and stops.
> **－** It writes nothing into the project before `uv --version` passes.

> **tasks:**
> - [ ] update `rule-plugin-install`
>   - old: `` The skill first runs `uv --version`; when the tool `uv` is missing, it says that GUPPI needs it and writes nothing. ``
>   - new: `` The skill first runs `uv --version`; when the tool `uv` is missing, it says that GUPPI needs it and asks the person whether it installs `uv` by the standalone installer of `uv`, runs that installer on a yes and `uv --version` again, and writes nothing into the project until `uv --version` passes; on a no, a failed installer or a `uv` that this session of Claude Code does not find yet, it stops and tells the person what to do (case 852.1). ``
>   - old: `check uv, copy its files from this plugin`
>   - new: `check uv and offer to install it when it is missing, copy its files from this plugin`
>   - old:
>     ```
>     1. Run `uv --version`. When it fails, say that GUPPI needs the tool `uv`, which installs Python and runs the code of GUPPI, and that the person installs `uv` and types `/guppi:install` again, and stop. Write nothing.
>     ```
>   - new:
>     ```
>     1. Run `uv --version`. When it passes, go on with step 2. When it fails, say that GUPPI needs the tool `uv`, which installs Python and runs the code of GUPPI, and ask the person whether you install `uv` now by its standalone installer. On Windows its command is `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`; on macOS and Linux it is `curl -LsSf https://astral.sh/uv/install.sh | sh`. Write nothing into the project until `uv --version` passes.
>        - On a no, show the command for this system, say that the person installs `uv` with it and types `/guppi:install` again, and stop.
>        - On a yes, run the command for this system. When it fails, or Claude Code does not run it, show its output and the command, say that the person installs `uv` with it and types `/guppi:install` again, and stop.
>        - Then run `uv --version` again. When it passes, go on with step 2. When it fails, say that this session of Claude Code does not find the new `uv` yet, and that the person opens a new terminal, starts Claude Code there in this project and types `/guppi:install` again, and stop.
>     ```
>   - old: `` 7. Say that GUPPI is installed, and that the person reopens Claude Code in this project and types `/hi`. ``
>   - new: `` 7. Say that GUPPI is installed, and that the person reopens Claude Code in this project and types `/hi`. When step 1 installed `uv`, say that the person starts Claude Code from a new terminal, so that the hooks of the project find `uv`. ``
>   - change: `when uv is missing, /guppi:install asks to install it by the standalone installer of uv and goes on once uv --version passes`
> - [ ] Read the standalone installer commands of `https://docs.astral.sh/uv/getting-started/installation/` against the two commands of the new step 1 of `rule-plugin-install` in the Spec; a command that differs is a fork by condition 1 of `rule-where-to-stop`.
> - [ ] create `estimate-plugin-install-offers-to-install-uv`
>   - ref: `rule-plugin-install`
>   - kind: `QA`
>   - purpose: `Whether /guppi:install, where uv is missing, asks to install uv by its standalone installer, stops with nothing written on a no, and on a yes goes on once uv --version passes or sends the person to a new terminal`
>   - method: `by hand, after the librarian's run of the session that sets this Criterion, with a tag prod-x.y.z in the history of HEAD: the clean version written into a local folder by uv run --project .guppi guppi ship --allow-draft, that folder added as a catalogue by /plugin marketplace add and guppi installed from it by /plugin install guppi@guppi-marketplace; in an empty project with Claude Code started from a terminal whose PATH holds no folder of uv, /guppi:install typed and the offer answered no, then /guppi:install typed again and the offer answered yes; the replies, the files of the project and uv --version in a new terminal read against the Criterion`
>   - tags: `[plugin, harness]`
> - [ ] `uv run --project .guppi guppi render`: `plugin/skills/install/SKILL.md`
> - [ ] read `estimate-plugin-install-offers-to-install-uv`

> **ratification:**
> ```
> - decision[case 852.1][update][rule-plugin-install]{ref:rule-plugin-install}
> - decision[case 852.1][create][estimate-plugin-install-offers-to-install-uv]{ref:rule-plugin-install}{tags:plugin,harness}
> ```

### Case 852.2 — The check of the Python environment leaves the missing uv out

> **given:**
> `estimate-guppi-package-is-ready-after-the-install`: its Criterion, `purpose` and `method` are replaced.
> **＋** `rule-guppi-package`: the target of that Estimate.
> **＋** `rule-plugin-install`: the skill `/guppi:install`.
> **＋** `/plugin marketplace add <folder>`: the command of Claude Code that adds the copy as a catalogue.
> **＋** `/plugin install guppi@guppi-marketplace`: the command of Claude Code that installs the plugin.
> **＋** `.guppi/.venv/`: the Python environment of GUPPI in the project.
> **＋** `/hi`: the skill the person types after the install.

> **when:**
> The person writes the clean version into a local folder by `uv run --project .guppi guppi ship --allow-draft <folder>`, adds that folder as a catalogue by `/plugin marketplace add <folder>`, installs the plugin by `/plugin install guppi@guppi-marketplace` and types `/guppi:install` in an empty project open in Claude Code, as `rule-plugin-install` sets it.

> **then:**
> Before it writes anything, `/guppi:install` runs `uv --version`.
> **＋** After it copies the files, it runs `uv sync --project .guppi` in the project, which builds the Python environment `.guppi/.venv/` before it tells the person to reopen Claude Code and type `/hi`.
> **＋** The hooks of the project find that environment built at the first `/hi`.
> **－** Where `uv --version` passes, it asks nothing about `uv`.

> **tasks:**
> - [ ] update `estimate-guppi-package-is-ready-after-the-install`
>   - set:
>     ```
>     status: pending
>     purpose: Whether /guppi:install runs uv --version before it writes anything and, where it passes, asks nothing about uv and builds the Python environment .guppi/.venv/ by uv sync after the copy before it sends the person to /hi
>     method: "by hand, after a tag prod-x.y.z stands in the history of HEAD: the agent writes the clean version into a local folder by uv run --project .guppi guppi ship --allow-draft; then, at a stop of Work Mode, the person adds that folder as a catalogue, installs the plugin guppi from it and, in an empty project on the machine with uv, types /guppi:install, reopens Claude Code there and types /hi; the person's answer on the output of the install, the files of the project and its .guppi/.venv/, read against the Criterion; the copy and the project may be those of the reading of estimate-plugin-install-writes-guppi-into-an-empty-project at the same commit"
>     ```
>   - change: `the Criterion replaced whole — the missing uv is left to estimate-plugin-install-offers-to-install-uv and the failed uv sync to the Estimate of case 853, and the method drops the project with no uv and the offline project`
> - [ ] read `estimate-guppi-package-is-ready-after-the-install`

> **ratification:**
> ```
> - decision[case 852.2][update][estimate-guppi-package-is-ready-after-the-install]{ref:rule-guppi-package}
> ```
