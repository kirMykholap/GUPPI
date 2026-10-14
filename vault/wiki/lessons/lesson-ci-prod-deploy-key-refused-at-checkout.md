---
type: lesson
kind: error
root_cause: the private half in PROD_DEPLOY_KEY does not open the deploy key prod_deploy_pub, and no run tested the pair when the two were set
status: new
origin: raw/2026-10-14/0232/ledger.md#L14
sprint: plugin
created: 2026-10-14
tags: [ci, github]
---

## Trigger

the CI run 38489789184 of the tag prod-1 on 3a50557a failed at actions/checkout with "git@github.com: Permission denied (publickey)" in three tries, and wrote no branch prod; the deploy key prod_deploy_pub stands with write access and last_used null, the secret PROD_DEPLOY_KEY was set 48 seconds after it on 2026-10-13

## Root cause

the private half in PROD_DEPLOY_KEY does not open the deploy key prod_deploy_pub, and no run tested the pair when the two were set

## History

- 2026-10-14 created · raw/2026-10-14/0232/ledger.md#L14
