---
session: 2026-08-13
sprint: S0
commits: 46a168d..7e77ec7
---

# Handoff — 2026-08-13 (phase 2)

The second brain, phase 2. Tasks 5 to 10 of 10, the whole-branch review, and four fix waves.

## 1. State

**Done.** All ten tasks of `docs/superpowers/plans/2026-08-13-second-brain.md` are on
`feature/second-brain`, 13 commits from `46a168d`, 91 files, +4246/−1630.

- **Task 5** — `/handoff` (`0ccb28b`).
- **Task 6** — `/ingest` and the first generated brief (`19d84f6`).
- **Task 7 and 8** — the `SessionStart` hook and the rule-override guard (`f0ac900`).
- **Task 9** — `/vault-lint`, `/sprint`, `sprint.md`, the tag rules and `vault-check-selftest.sh`
  (`e48eef2`).
- **The task 10 gate** — every one of the old handoff's 332 claims carries a verdict (`94cec21`).
- **Task 10** — `docs/HANDOFF.md` 1307 lines → 27, `CLAUDE.md` 231 → 190 (`d30b317`).
- **Four fix waves** — `abe0377`, `cf349d4`, `ccfaa74`, then the whole-branch pair `ea11cdc`
  (tooling) and `7e77ec7` (corpus).

**Not done.** Nothing in the plan. Its own "After the plan" list stands: the owner's Q5, and the
task tracker that would fill the brief's empty section.

**In flight.** Nothing. Working tree clean.

**Next step.** The owner runs `/clear` or starts a session. **That is the last unverified thing on
this branch** — the `SessionStart` hook has never been observed firing, because a hook is read
when a session starts and this one wrote it. If the brief does not appear, the diagnosis is
`.claude/settings.json`: both hooks are registered by `$CLAUDE_PROJECT_DIR`, and whether that
expands depends on the shell the harness spawns hooks with on Windows. The fallback is a relative
path, which works from the project root and fails from anywhere else. Then: the merge decision.

**Checks.** Full suite **605 passed**, `ruff check` and `ruff format --check` clean.
`bash scripts/vault-check.sh` — ok, 15 failing rules and 2 advisories, 3 s.
`bash scripts/vault-check-selftest.sh` — **54 of 54**, ~2 min.
`powershell -File scripts/hook-selftest.ps1` — **25 of 25**.
`bash scripts/vault-coverage.sh` — 332 of 332 and 33 of 33, INGEST COMPLETE, 0.7 s.
No browser walk: nothing on this branch renders a page.

## 2. Entities

**Appeared.** `/handoff`, `/ingest`, `/pre-task`, `/sprint`, `/vault-lint` — five skills;
`.claude/hooks/session-brief.ps1`, `ask-the-vault.ps1` and the shared `vault-path.ps1`;
`.claude/settings.json` with a `SessionStart` and a `PreToolUse` hook;
`scripts/vault-check-selftest.sh` and `scripts/hook-selftest.ps1`; `job_hunt_ai_vault/sprint.md`
and `brief.md`; two coverage sidecars; `job_hunt_ai_vault/raw/notes/`, which now holds the owner's
two design notes.

**Changed.** `docs/HANDOFF.md` is a pointer. `CLAUDE.md` is rules with `[[wikilinks]]`, and a new
check rule requires every one of them to resolve. `vault-units.sh` counts every claim rather than
only bold ones. `vault-check.sh` was rewritten: 71 s → 3 s, and it reads frontmatter rather than
whole files. `vault-coverage.sh` validates verdicts and runs in 0.7 s instead of 22.
`docker-entrypoint.sh` said `STALE_AFTER` was 15 minutes; it is 30. `.env.example` names
`MIGRATION_CHECK_DATABASE_URL`, which nothing named before.

**Out of service.** `docs/second-brain-info.md` and `docs/second-brain-instructions.md` as
documentation — they are the owner's notes, they describe a design that was partly overridden,
and they sat beside `HANDOFF.md` reading like a spec. Moved into `raw/notes/`, cited, not yet
ingested.

## 3. Decisions

- **Two conditions in `vault-check.sh` are advisories that print without failing** — a tag on more
  than ~20 pages, and a tag registered but unused. Rejected: making them fail. Neither has a fix
  that is correct to apply on the spot; splitting a tag means re-tagging pages the session never
  touched. An alarm that fires every run and cannot be acted on is one you learn not to read.
- **The hooks are PowerShell, not bash.** `bash` on this machine's system PATH is the WSL shim in
  `WindowsApps` and answers `execvpe(/bin/bash) failed`. A hook is spawned by the OS, not by the
  agent's shell, so it gets that one.
- **`/sprint` does not archive the sprint's handoffs on close.** Rejected before it was ever run,
  by measurement: 31 pages cite `raw/handoffs/...` in `sources:`, so the first close would have
  turned the check red on all 31 — the exact failure that rule exists to catch — and would have
  made an immutable file's wikilinks load-bearing.
- **The brief carries `generated-at:` and the hook compares it to HEAD.** Rejected: trusting the
  ingest to be the last thing a session does. It was not, for six commits of this branch.
- **The librarian's ten-page ceiling is scoped to topic queries.** `/pre-task` asks a different
  question — completeness, not relevance — and gets a cheap frontmatter enumeration instead.
- **Merging near-duplicate pages was deferred to `/lint`**, not done here. Merging is supersession
  and a judgement about the corpus rather than a defect.

## 4. How it is built

The loop is journal → ingest → brief → hook → next session, and this session found that **its
seams were where it broke, not its pieces**. Three things now close it: `CLAUDE.md` says a session
ends with `/handoff` then `/ingest`; the brief is stamped with the commit it was built at; and the
hook reports both a stamp older than HEAD and a journal newer than the brief, which are different
failures.

The ingest is units and verdicts, and the denominator is produced by a script so that the party
accounting for the claims did not also decide what the claims are. Fidelity is the other half and
no script can check it: it is sampling plus the acceptance questions.

`vault-check.sh` is one pass over frontmatter and one set of links built once. Everything it knows
about a page comes from between the two `---` markers, because reading whole files let a fenced
YAML example satisfy the required-field rule and forge a duplicate `authority`.

The guard cannot enforce the one-writer rule — a `PreToolUse` payload does not say who is writing —
so the enforcement is `git diff` plus `log.md`, and `/ingest` now asks the caller for it.

## 5. Lessons

**A fix can be worse than the defect, and this session shipped one.** The `page:` verdict rule was
tightened to catch a name after a comma-space, and it rejected the free prose the file's own header
promises — turning one real annotation into eleven `BAD VERDICT` lines and making the ingest gate
red on data committed six commits earlier. The fix that stuck reads names up to an em dash, which
is how every verdict here already writes its prose.

**A test suite has a vacuum failure mode, and it is on its negative half.** Reshape the corpus and
three cases went quiet while staying green — all three of them cases that assert nothing happens,
because a `sed` that matches nothing leaves a tree that is clean by construction. Subjects are now
picked by what the cases need, and every case asserts that its mutation changed the tree at all.

**"The superseded passage comes earlier" was false both times it could be tested**, and it was the
vault's own account of its own worst failure. The document grew by prepending, not appending. The
rule that survives is: prefer the passage carrying a date or a commit; where neither does, read the
code. The mechanism of the original defect turned out to be **vocabulary, not position** — the
first pass took its topic sentence from the passage whose wording matched the page's topic.

**A verdict can point at a page that does not contain the claim, and coverage cannot see it.**
Found once by sampling (a number in a title that no tool ever produced) and once by a reviewer
(`alembic check` filed to a page with no mention of migrations). The librarian then found the same
class at 24× the scale: 24 pages cited `docs/HANDOFF.md`, which is now a 27-line pointer. The
`sources:` rule checks that a path exists, never that it still holds the claim.

**A `.ps1` without a BOM is read in the ANSI codepage.** The hook self-test broke on its own
fixture before it reached a hook. Every `.ps1` here is ASCII now, and non-ASCII test data is built
from char codes.

**The three-lens review earned its cost again.** Each lens found what the others could not: the
corpus lens found the inverted lesson, the loop lens found both seam Criticals, and the
arrival lens found that a shrunk `CLAUDE.md` had dropped the only statement of where our own
JavaScript lives — so the owed AST test would have been written to scan `static/`, found nothing
of ours, and passed having read nothing.

## 6. Deferred

- **The owner's `/clear`** — the `SessionStart` hook is unobserved. Everything else on this branch
  has been run.
- **The merge of the branch.** 13 commits, unreviewed by anyone but this session's reviewers.
- **Four merge candidates and four missing subjects** are on the `/lint` agenda in `log.md`: the
  hooks, the module map (§3 of the old handoff, which is fenced and therefore produced no units),
  the CLI, and the data model.
- **The two owner notes in `raw/notes/` are not ingested.** They have no verdicts, so `/vault-lint`
  will report them as an unfinished ingest, correctly.
- **The AST test pinning the JavaScript boundary** — owed since 2026-08-12, still unwritten. It
  now has the three script locations it needs.
- **The brief's growth threshold** — to be measured at sprint 1's retrospective, not invented.
- **Beads**, and with it the brief's "active tasks" section.

## 7. Feedback to the librarian

- **No Russian word reaches a database or schema question.** `rg -il "колонк|таблиц|миграц|схем"`
  over the wiki returned zero. Closed the same day by minting `schema` with the Russian words a
  real question uses — the second word-shaped miss, after `frontend`.
- **There is no page about React**, so a question about rewriting the view had to be assembled by
  walking links out of `the-stack-stays-htmx`. `rg -il react` finds only the two JavaScript pages.
- **`/vault-ask` has still never been used as an entry point.** Every librarian call this session
  was a direct dispatch. Registration itself is now proved: the acceptance run was dispatched by
  name and the definition arrived as the agent's system prompt.
- **The harness injects `CLAUDE.md` into a subagent as it stood at session start.** That is why the
  acceptance re-run cannot prove the shortened file is sufficient — the agent had the long version
  for free and said so itself. Any future test of an entry point has the same confound.
- **The sidecar's grammar is undocumented and was discovered by breaking it**: prose after a
  verdict must follow ` — ` in the same tab field, and a third tab field turns twenty words into
  page names.

## 8. Anything else worth keeping

The measured argument for the review process held up in both directions. Three passes over the
tooling found four defects **inside** the previous pass's fixes, which is the case for keeping the
re-review whole. And the whole-branch review at three lenses found two Criticals that no
per-task review could have seen, because both were about how the parts join rather than about any
part — the rule that a session ends by writing its journal existed nowhere, and a brief that had
been overtaken by six commits looked exactly like one that had not.

The owner asked one question this session — when to run the final review — and answering it now
rather than deferring it is what made the two seam findings arrive while the branch could still
absorb them.
