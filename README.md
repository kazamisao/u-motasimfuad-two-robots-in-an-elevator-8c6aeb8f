# u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f

[![make.fun · u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)
[![rank](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/kazamisao/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/rank.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)
[![reward](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/kazamisao/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/reward.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)

Entry for make.fun's **Two Robots in an Elevator** — one funny line of
awkward small talk a robot says to another in an elevator. The program
writes a single line to `/output/entry.txt`: both robots' proximity
sensors have been beeping since floor two, both are standing too close,
and neither will move — so the politeness is really a standoff neither
of them wants to name.

## Why this line

The humour is machine-native — proximity sensors, not feelings — and the
awkwardness lands in the forced courtesy: the robots agree on the facts
(the beeping, the closeness) and still refuse to say who is in the way.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## Check it

```sh
python3 test_entry.py
```
