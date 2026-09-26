# Handoff — 2026-09-25, the core of the scheme of Case 416: case-guppi, the checks before the showing; History cut from a read; defers by the hook

## Notes from memory

- The person took only the core of the scheme of 416 (Case 419) and put every other item that needs a decision after the new scheme of Cases works: 422, 423, 424 are short defers, C1 and C2 (Slice 3g) left for the sprint.
- The person asked twice why the Case of 419 cost so much: frame-guppi 155 380 tokens and 424 s, the main agent about 112 000 tokens for the turn. Causes found: the frame read twice (main agent and frame-guppi); the main agent's prompt widened the frame-guppi dispatch; the rule of frame-guppi reads every hook of the same event and its rule for a Case that touches a hook (421: 126 827 tokens). A narrow prompt on 420 gave 25 605 tokens and 81 s. ask-guppi at pre-spec: 173 122 tokens, 437 s, 14 findings of which 6 were real faults. case-guppi carries the same sentence on hooks in its Render: its cost is the method of `estimate-case-build-writes-the-case`.
- The person wanted the History of a page kept on the page (Obsidian) and proposed a `.claude/rules/` file; the hook on `Read` was chosen because it covers subagents and the first read. The live probe of Claude Code 2.1.282 confirmed `updatedInput` on `Read` in the main agent and in a subagent, the changed input in `PostToolUse`, and an `Edit` after a cut read (lesson line 37).
- The check after ratification refused three times (read lines of renamed Estimates, created Estimates missing from `given`, a wikilink to the not yet written `decision-case-419.3`); each time the Cases were shown and ratified again. 419.3 moves the check before the showing, from the next session.
- `claude-code-guide`, answering from the docs, said `SubagentStop` cannot block and carries no `stop_hook_active`; the live payloads of the probe of 0051 show both. The code follows the probe.
- The context passed 400 000 tokens at the prompt of `/retro`; the reading of `estimate-context-size-warns-past-the-limit` is `failed` on "the agent opens its reply with the recommendation".

## Direct instructions to the librarian

- One unit: `raw/2026-09-25/1228/`.
- Ledger line 40, the reading of `estimate-frame-check-finds-a-contradiction`, is not to be applied: Case 419.2 of the same Spec replaces its Criterion and renames the page to `estimate-case-build-writes-the-case` (case 283; lesson line 44). Its tokens and seconds stay in the ledger as data.
- Case 419.2 holds two `update` items of `rule-frame-check`: first the sections, with the markers `<!-- rule-frame-check -->`, then the `rename` to `rule-case-build`, which rewords the markers. The ledger holds one line for both.
- Cases 419.1, 421.2 and 421.4 change `rule-case-protocol` by different `replace` pairs; 419.1 and 421.4 change `rule-skill-hi`; 419.1 and 421.3 change `rule-prespec`; 419.3, 419.4 and 420.1 change `rule-hook-registry`, the anchors distinct.
- `{supersedes:case 416}` (419.2) and `{supersedes:case 403}` (419.2) clear the `deferred_by` of `rule-frame-check`, `rule-case-protocol`, `rule-spec-write`, `rule-spec-reconcile` and `rule-ask`; 422 defers `rule-context-size` again, 423 `rule-spec-reconcile`, 424 the placeholder `rule-orchestration`.
- `addressed_by` of the Insight is written as a bare slug, `decision-case-419.3`: a wikilink to a Decision page not yet written is refused by the check of case 264.2 (lesson line 36).
- Renders due: `vault/wiki/case-schema.md`, `.claude/agents/ask-guppi.md`, `.claude/agents/case-guppi.md`, `.claude/skills/hi/SKILL.md`, `.claude/skills/pre-spec/SKILL.md`, `.claude/settings.json`. After `case-guppi.md` is written, `.claude/agents/frame-guppi.md` is governed by no page and waits for `git rm` in the next session.
- The frontier source of the brief's Deferred items is `deferred`; the new closer `kept` is accepted by pre-spec from now on.

## What actually got done

- Ratified: 419 (419.1–419.4), 420 (420.1, 420.2), 421 (421.1–421.4); defers 422, 423, 424. Frontier: C3, C4 closed by 419; C5, C6, C11 by sub-cases of 419; C8 by 421; C12 by 420; C1, C2 left for the sprint; C7, C9, C10 deferred.
- Code, commit 9aae9f8: `guppi/casecheck.py` (SubagentStop check, Stop comparison), `guppi/pageread.py` (the two Read hooks), `guppi/pages.py` (`section_starts`, `history_line`, `HISTORY` shared with `generate` and `lint`), `guppi/ratified.py` (`case_section` shared with casecheck, the write of a defer-only Case), `guppi/prespec.py` (`kept`), `guppi/cli.py`; tests `test_casecheck.py`, `test_pageread.py`, and new tests in `test_ratified.py` and `test_prespec.py`. `make test` 663 passed, 2 skipped; `make style` clean.
- Readings: passed — `estimate-case-protocol-acknowledging-reply`, `estimate-case-protocol-ledger-line-form`, `estimate-hook-registry-rendered`, `estimate-prespec-reconciles`, `estimate-one-judgment-one-implementation-followed`; failed — `estimate-context-size-warns-past-the-limit`; the line of `estimate-frame-check-finds-a-contradiction` not to be applied.
- Not done:
  - The pages and renders of the Spec — the librarian's.
  - `git rm .claude/agents/frame-guppi.md` — after the render of `case-guppi.md`.
  - Every `read` line of the Spec: the pages and Criteria exist only after `generate`, and `case-guppi` and the new hooks load only in the next session. The first Case of the next session is the first live dispatch of `case-guppi`; the `Stop` hook refuses a Case the main agent writes itself.
  - Work lines W1, W3, W4, W8, W11–W14, W16–W23 of the Frontier.
