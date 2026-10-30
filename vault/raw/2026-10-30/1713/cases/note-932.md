# Note — Case 932 (Frontier C7, `rule-plugin-install`, defer of case 911)

STATE: Q9 answered (a). Case file written whole (932.1 install, 932.2 rule-morph); searches re-run; summary sent. Next: fix findings by Edit only.

## Questions
- Q1 **What the install does in a project that already holds its own files** — rec (c); answered (c), then the person changed it to (b): set aside, setup Case at first /hi shows them, person keeps or drops each.
- (A round Q2-Q6 on (c) was never shown; dropped.)
- Q2 **Which clashing files the install sets aside** — rec (c); answer (c): CLAUDE.md, .claude/**, .gitattributes, .github/workflows/checks.yml; clash under vault/ or .guppi/ still stops.
- Q3 **Where the set-aside files go** — rec (b); answer (b): `guppi-set-aside/`, same paths, `.set-aside` added.
- Q4 **When the project's own `.claude/settings.json` is set aside** — rec (a); answer (a): just before GUPPI's copy, after uv sync passes.
- Q5 **Where a kept part of a set-aside file lands** — rec (a); answer (a): pages of GUPPI that already write that file; no new page.
- Q6 **What happens to the set-aside folder after the setup Case** — rec (a); answer (a): setup Case deletes it in its Work Mode.
- Q7 **What happens until the setup step is built** — rec (a); answer (a): nothing extra.
- Q8 **How the Case is checked** — rec (a); answer (a): two sub-cases, new estimate each (estimate-plugin-install-sets-aside-the-files-of-the-project; estimate-morph-takes-in-the-set-aside-files), refusal lines of writes-guppi-into-an-empty-project and runs-no-hook-before-uv-sync rewritten.
- Round 3, Q9 **Where a kept part lands when no page writes its file** — asked: frame shows no page governs .gitattributes or checks.yml (checks.yml only implementation_ref of rule-github-repository; .gitattributes none). rec (a) the setup Case writes it into the file itself by a task. Answer: pending.

## Read
- case-schema, ratification, case-example; rule-plugin-install whole; decision-case-911
- Criteria of 4 estimates of rule-plugin-install; estimate-morph-sets-up-the-project-at-the-first-hi whole; estimate-guppi-package-is-ready-after-the-install Criterion (empty project, stands)
- case-929 (does not bear); rule-morph whole; rule-clean-branch Purpose
- .claude/skills/hi/SKILL.md 21-29; orchestration.md 9
- Grep guppi:install over vault/wiki,.claude,.guppi/guppi,plugin: 18 files; non-install-estimate hits read: empty-project Criteria stand; entity-sprint-plugin line 27 (what remains of rule-morph) stands
- Tests: only test_ship.py:597 names plugin/skills/install (sample); live reads of vault in tests: schemas, case-schema, orchestration only
- ledger: no lesson[error], no addresses
- WebFetch settings docs; memory docs

## Open forks
- Q9.

## To do
- Write case file: 932 parent (context/problem/recommend), 932.1 install (rule-plugin-install update Purpose+Render pairs, create estimate, update 2 estimates Criteria with sections Criterion? — replace Criterion whole via when/then? no: each sub-case has one when/then; the 2 old Estimates need their own Criterion text under sections.Criterion), 932.2 rule-morph update + create estimate-morph-takes-in-the-set-aside-files. Supersedes case 911 on a decision line naming rule-plugin-install.
