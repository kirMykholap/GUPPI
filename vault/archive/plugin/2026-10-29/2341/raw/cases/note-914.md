# Note — Case 914 (item C6: estimate-close-commits read passed while the close command failed)

## Questions (round 1, answered "Согласен" = all recommended)
- Q1 Where the line ending is fixed — rec (a) `--paths` alone prints bare line feeds (render.py run) — Answer: (a)
- Q2 How the fix is checked — rec (a) replace Criterion of estimate-close-commits + child-process test — Answer: (a)
- Q3 What happens to the reading of passed — rec (a) main agent writes new failed reading before decision lines — Answer: (a) (main agent writes it)
- Q4 Whether a failed close command goes into the report — rec (a) left out — Answer: (a)

## Read
- case-schema.md, ratification.md; estimate-close-commits.md, rule-close.md (whole); case-913.md
- render.py 300-381; cli.py 89-105; test_render.py 1-60, 465-500
- rule-render-harness.md, rule-python-utf8.md; librarian-guppi.md 100-133
- saved chat 7f200512 line 1693; subagents/agent-a9b114d335b9583a3.jsonl 195-196, 201
- docs.python.org/3/library/io.html (newline)

## Open forks
- none

## To do
- done: case-914.md written, searches re-run; summary sent. Await check findings or messages.
