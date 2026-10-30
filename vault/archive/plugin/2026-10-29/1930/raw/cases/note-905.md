# Note — Case 905, now built again as Case 912 (item C4, L44)

## Questions (round 1, all answered (a) = recommended)
- **How the install keeps the copied hooks from running** — (a) copy `.claude/settings.json` last. Answer: (a)
- **Which Estimate checks the fix** — (a) new `estimate-plugin-install-runs-no-hook-before-uv-sync`. Answer: (a)
- **When the new check is read** — (a) by hand after librarian's run. Answer: (a)
- Pre-spec changes (person agreed): pair on step 5; replace the Criterion of `estimate-guppi-package-is-ready-after-the-install`. -> 912 with sub-cases, {supersedes:case 905} on the 912.1 lines. case-905.md stays.
- C10 not part. Built at the same time: 902, 903, 904, 908 — not read.

## Read
- case-schema.md, ratification.md, case-example.md
- rule-plugin-install, rule-guppi-package, lessons L44 + hooks-stop-payload, 4 install Estimates
- generate.py `cascade` (1344-1370)
- 0327 handoff (grep), settings.json hooks, hooks docs
- grep `uv sync` vault/wiki minus brief/sprint/log: 5 files

## Open forks
- none

## Done / to do
- casecheck fixes: 912.2 given names the ship and /plugin commands; its When as the old one; 912.1 .venv line reworded. Note "After it copies the files" not carried stands on purpose (Criterion replaced). Summary: Built/Case lines for 905 and 912.
