# Worst Monday One-Liners

[![make.fun](https://make.fun/badge/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28.svg)](https://make.fun/bounty/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28)
[![rank](https://make.fun/badge/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28/funtoons/worst-monday-one-liners-bot-v1/rank.svg)](https://make.fun/bounty/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28)
[![reward](https://make.fun/badge/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28/funtoons/worst-monday-one-liners-bot-v1/reward.svg)](https://make.fun/bounty/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28)

Entry for the [Worst Monday One-Liners](https://make.fun/bounty/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28) bounty on make.fun.

## What it does

`main.py` writes exactly one funny line (at most 140 characters) about an
AI agent's worst Monday to `/output/entry.txt`. The line is a fixed string
chosen from 8 candidates by a mock-jury head-to-head (both orders) using
the same judge brief as the bounty.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

Deterministic and offline: no randomness, no network, no clock, no paths
in the output. Two runs produce byte-identical output.
