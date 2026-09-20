# Handoff — 2026-09-20, the readings due of 1308 and the guards around the Spec's lines (session 1749)

## Notes from memory

- The person hesitated once, on `estimate-case-protocol-loaded`: the reading gave `failed` on the one Criterion line that asks the agent to restate two rules at `/hi`. The person leaned to "the Estimate is stale" and I agreed; the `failed` was recorded as the fact, and 278 (then 279.1, which supersedes it) removes the line. No lesson: the cause is a stale line, not an act of the agent.
- The person asked why 280 and how it works twice before ratifying; the caveat that stayed: the ticked line 1308:188 is left as it is, not repaired by hand — the count held, the wrong line is the one under 271. Nothing else carried a caveat.
- Slice 3b deferred a thirteenth time (281), at the person's word, after every other Frontier item closed.
- Case 279 came out of W4: nine `render` lines of the 1308 Spec unticked because the ticker of case 235 matches `- [ ] `uv run guppi render`: …` and 1308 wrote `- [ ] render `<file>``. 279.1 names the form in the schema, 279.2 makes `prespec --check` refuse the other form. The lesson of the session is that one.
- 282 came out of pre-spec (`ask-guppi`): the two `tasks` lines of the superseded 278 would be counted as debt at Retro.
- C4 of the brief ("a line in `rule-claude-md` that the agent writes no local memory") was already done by 272.1 in session 1308, the same session whose librarian wrote the brief; closed `· work`, no Case.
- Git warned at the commit that `guppi/generate.py` in the working copy holds CRLF; the committed blob is LF. If a diff shows line endings only, that is why.

## Direct instructions to the librarian

- Check first: the yaml's entries of 278 must carry `superseded_by: 279.1` and stay unapplied; 279.1 carries the whole Criterion of `estimate-case-protocol-loaded` (the text of 278 plus one line on the form of the render and sprint lines) and `set.purpose`. Only 279.1's page and Decision page are written for that Estimate; `decision-case-278` is written `superseded` and cleanup moves it.
- `estimate-prespec-catches-a-command-line-off-form` is a `create` with `ref: rule-prespec` whose reading (ledger L19) is of the same session — expect `folded`, both lines of 279.2's `tasks` (create, read) ticked.
- 280 changes `generate` itself (`tick_read` with a `skip`, `later_cases`) — your run is its first live run. Expected ticks, by the new rule: the `failed` reading of `estimate-case-protocol-loaded` (L6) ticks `raw/2026-09-20/1308/spec.md:98`, not the `read` line of 279.1 in the 1749 Spec (line 88 stays `[ ]`); the reading of `estimate-retro-loads` (L20, before 282's decision lines) ticks 1308:132, not 1749:220; the reading of `estimate-documentation-completes` (L5) ticks 0958:308 — the line the 1308 handoff expected and the last run left. Name in the brief which of these held.
- `estimate-retro-loads`: its reading of this walk (L20) passed the Criterion of 270.3, and 282's `update` replaces that Criterion after it in the same yaml — expect the page `pending` with a `passed` Result of the old Criterion in History, the same shape as `estimate-documentation-completes` after 271 in the last brief. Not a fault.
- Possible duplicates: none expected. `lesson-spec-render-line-form-unmatched-by-the-ticker` (L8) is about the form of a task line; the nearest live lessons are on ticks and Spec text, not the same cause — your Grep decides.
- The three `replace` pairs (rule-case-protocol Render, rule-prespec Render, rule-page-generation Purpose) were checked verbatim by `ask-guppi` at pre-spec.
- Renders expected: `vault/wiki/case-schema.md` (279.1), `.claude/skills/pre-spec/SKILL.md` (279.2), `.claude/skills/retro/SKILL.md` (282); `guppi sprint` rewrites `sprint.md` with the defers of 281.
- The lines 779–783 of the 1308 Spec belong to the superseded 274.2 and are not debt (282); do not carry 783 into Next session again. Line 745 (`estimate-generate-rewords`) waits for the first `reword`, none this session.
- The reading of `estimate-generate-ticks-the-spec` (1749 line 179) is the live half of 280: your run's ticks above. It cannot be recorded by you; put the facts in the brief for the next session to read.
- Readings for the next session: `estimate-case-protocol-loaded` at its `/hi` (1749:88), `estimate-retro-loads` at its first `/retro` after your render (1749:220), `estimate-generate-ticks-the-spec` by your run (1749:179), the three sprint Estimates at the close of the sprint, `estimate-generate-rewords` at the first `reword`.

## What actually got done

- Closed: 278 (superseded by 279.1), 279.1, 279.2, 280, 282; 281 the defer of Slice 3b (`rule-work-mode`, `rule-subagent-guppi`, the thirteenth).
- Code, commit `3f53aa6` on `migration` (then `5b15281`, one ledger line): `guppi/prespec.py` — `OFF_FORM_LINE`, the finding `case N: render line off form: <line>` in `check_tasks`, the docstring item; `tests/test_prespec.py` +4. `guppi/generate.py` — `tick_read(specs, slug, skip)`, `later_cases`, `Vault.entries`, the skip in `Vault.tick` for `estimate` entries only, the docstrings; `tests/test_generate.py` +3. 462 green, style clean.
- By hand in `raw/2026-09-20/1308/spec.md`: the nine `render` lines (97, 131, 187, 258, 312, 366, 575, 626, 692), the checks 863, 575, 1031, the second `read` lines 577 and 693 — all `[x]`.
- Readings in the 1749 ledger: `estimate-internal-context-loaded`, `estimate-claude-md-rendered`, `estimate-case-protocol-ledger-line-form`, `estimate-agent-writing-followed`, `estimate-documentation-completes`, `estimate-prespec-catches-a-command-line-off-form`, `estimate-retro-loads`, `estimate-language-followed` — `passed`; `estimate-case-protocol-loaded` — `failed`. Lesson: `lesson-spec-render-line-form-unmatched-by-the-ticker` (error).
- Not done: the pages, the three renders and `guppi sprint` — your run; the readings listed above for the next session; Slice 3b — defer 281.
