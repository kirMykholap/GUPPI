# guppi agents — the numbers the trial of Case 1029 starts from

Output of `uv run --project .guppi guppi agents <transcript>`, taken at the Retro of session 0807 (2026-11-20). Every dispatch below ran at the frontmatter of its agent (`case-guppi` at `effort: medium`); no Agent call passed an effort, so each line shows `effort -`. `seconds` of an agent is the sum of the `duration_ms` of its finished runs; a run cut off by the end of the Claude Code process has no notice and is not counted, and a librarian that ran in the foreground has none, so it shows `runs -`. `seconds` of the main agent spans the first record to the last, pauses included.

## Session 0807 (this session, f7321efe)

```
main	calls 254	tokens 70658381	tools 239	seconds 1402372
agent a577edf9a38f2717e	claude-code-guide	Effort and prompt cache facts	effort -	model claude-haiku-5-5	calls 4	tokens 178699	last 67585	tools 9	runs 1	seconds 116
agent a5bede5207edcd936	case-guppi	Build Case 1029	effort -	model claude-opus-5-5	calls 52	tokens 11343170	last 308659	tools 185	runs 7	seconds 994
agent a60a9419c158d3be3	case-guppi	Build Case 1036	effort -	model claude-opus-5-5	calls 43	tokens 5306251	last 163930	tools 66	runs 3	seconds 374
agent a7057f81c76086861	case-guppi	Build Case 1032	effort -	model claude-opus-5-5	calls 136	tokens 24631364	last 284792	tools 166	runs 5	seconds 1182
agent a8a2fe3fd16f32407	case-guppi	Build Case 1030	effort -	model claude-opus-5-5	calls 51	tokens 10074555	last 265463	tools 144	runs 5	seconds 877
agent ab4e9a4d1ad17fce3	case-guppi	Build Case 1035	effort -	model claude-opus-5-5	calls 84	tokens 16792005	last 300502	tools 119	runs 4	seconds 848
agent ac4d23900d1280ba7	ask-guppi	Pre-spec audit of plan 0807	effort -	model claude-opus-5-5	calls 80	tokens 16371932	last 335311	tools 112	runs 2	seconds 156
agent ac799710809af11a8	case-guppi	Build Case 1034	effort -	model claude-opus-5-5	calls 41	tokens 4529104	last 162999	tools 69	runs 3	seconds 447
agent af7c1ce17f93c76f9	case-guppi	Build Case 1033	effort -	model claude-opus-5-5	calls 26	tokens 2465949	last 124304	tools 60	runs 1	seconds 269
agent afa272be684678537	case-guppi	Build Case 1031	effort -	model claude-opus-5-5	calls 68	tokens 14865830	last 286887	tools 144	runs 4	seconds 551
```

## Trial installs of session 0358 (`~/.claude/projects/C--PROJECTS-guppi-trial-0358-*/`)

### empty-git

```
== 93058e9a-a55c-4dc8-95fc-ac1c650219ea.jsonl
main	calls 94	tokens 13610319	tools 67	seconds 3337
agent a2d982452650d5d0f	case-guppi	Build the setup Case guppi-1	effort -	model claude-opus-5-5	calls 53	tokens 4459672	last 137964	tools 92	runs 5	seconds 460
agent a4e45442ba2c829ba	case-guppi	Build opening Case of the sprint	effort -	model claude-opus-5-5	calls 31	tokens 2296352	last 100803	tools 51	runs 4	seconds 317
agent a51d1e57fea618647	ask-guppi	Pre-spec vault check of the plan	effort -	model claude-opus-5-5	calls 41	tokens 3668560	last 143202	tools 69	runs 2	seconds 421
agent adda7375e88d49456	librarian-guppi	Materialize the session into the vault	effort -	model claude-opus-5-5	calls 26	tokens 1404130	last 70858	tools 30	runs -	seconds -
== bedb515e-dfe4-4389-885c-d2dfcf3584c0.jsonl
main	calls 7	tokens 476454	tools 9	seconds 264
```

### no-git

```
== 07cfacdd-aa2f-4da2-a0ad-3831ae6115b8.jsonl
main	calls 2	tokens 165785	tools 0	seconds 20
== 2b6bed0c-675a-46ff-8b0d-82e6d19838a8.jsonl
main	calls 109	tokens 18578457	tools 66	seconds 2883
agent a29614727c2d6519d	case-guppi	Build the setup Case	effort -	model claude-opus-5-5	calls 48	tokens 4478418	last 131162	tools 82	runs 5	seconds 454
agent a98d2e3fd79893e0c	librarian-guppi	Librarian materializes session	effort -	model claude-opus-5-5	calls 26	tokens 1222967	last 64580	tools 31	runs -	seconds -
agent a9c9f793d60df2b19	ask-guppi	Pre-spec vault check	effort -	model claude-opus-5-5	calls 18	tokens 1314626	last 114549	tools 56	runs 2	seconds 270
agent aab5a1391e42a3657	case-guppi	Build the opening Case	effort -	model claude-opus-5-5	calls 44	tokens 3680135	last 115507	tools 77	runs 4	seconds 331
== 2cb6dba1-836b-489a-8b55-4e1086bd3135.jsonl
main	calls 9	tokens 612113	tools 10	seconds 65
```

### own-files

```
== 36b6e39b-7323-4638-8d29-7608d3856ae2.jsonl
main	calls 86	tokens 12043591	tools 63	seconds 3056
agent a1d6c653bfa4bcaa6	case-guppi	Build setup Case guppi-1	effort -	model claude-opus-5-5	calls 64	tokens 6791619	last 156631	tools 100	runs 3	seconds 418
agent a4ba64d6768400d83	ask-guppi	Pre-spec vault check of plan	effort -	model claude-opus-5-5	calls 34	tokens 3490576	last 154061	tools 76	runs 2	seconds 369
agent a94a50316535b34fd	librarian-guppi	Materialize session 2026-11-04 0644	effort -	model claude-opus-5-5	calls 32	tokens 1592710	last 69879	tools 40	runs -	seconds -
agent aeefae8f1ead50395	case-guppi	Build opening Case of sprint	effort -	model claude-opus-5-5	calls 48	tokens 4088339	last 112466	tools 68	runs 4	seconds 304
== c06fffe8-cf7d-4739-acd5-8e73b172f9b9.jsonl
main	calls 9	tokens 542067	tools 10	seconds 115
```
