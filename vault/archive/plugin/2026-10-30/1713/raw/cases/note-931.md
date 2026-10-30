# Note — Case 931 (Frontier C6, backlog `rule-page-generation`)

## Questions
- R1 Q1 "What does this Case do with the put-off?" — rec (a); answer (a)
- R2 Q2 "Which sections may the new key remove?" — rec (a); answer (a)
- R2 Q3 "What happens when a named section is not on the page?" — rec (a); answer (a)
- R2 Q4 "How is the new key checked?" — rec (b) Criterion of estimate-generate-writes replaced whole; answer (b)
- R2 Q5 "What is the key called?" — rec (a) `drop`; answer (a)
- R3 (after pre-spec findings) Q1 "Where does the promise that the lift carries `drop` stand?" — rec (b) new top-level Case beside 931 for estimate-materialize-assembles + rule-materialize pair; 931 drops its ITEM_KEYS line from then/Criterion; answer pending

## Pre-spec findings (no word of the person)
- 1 done: Criterion line "set carries method drops no section" reworded
- 2 done for case-schema line 30 (pair on rule-case-protocol added); rule-materialize pair waits on R3
- 3 estimate-materialize-assembles: R3
- Recommend needs **Change** items for these; context needs words on the 2nd pair and on names_a_part (drop alone on an Estimate is a part: names_a_part read, returns True)
- 929 and 932 built at same time: read no file of theirs

## Read
- case-schema, ratification, rule-page-generation whole; decision 897.3/897/793
- generate.py docstring, body, update; materialize.py ITEM_KEYS, _lift_item, item_keys, names_a_part; ratified.py put; lint.py check_schema, unmet_conditions, holds, load_schema
- estimate-generate-writes whole; rule-materialize 1-23; estimate-materialize-* lines naming keys
- ledger: case 931 has 3 decision lines (18:07:40)

## To do
- after R3: apply choice, fix context/recommend, rerun searches, summary
