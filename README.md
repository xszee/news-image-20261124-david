# THE MORNING GLOBE

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/xszee/news-image-20261124-david/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/xszee/news-image-20261124-david/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

A single-page morning paper covering Tuesday, 24 November 2026 — every
story on the page was first reported that day. The front page leads with
the World Court's genocide ruling against Myanmar, then turns to a
Pakistani astronaut riding Shenzhou 24 to Tiangong, the UN chief's call
for action on AI risks within a year, a 5.6 quake in Nepal, a US jury's
verdict against Huawei, and the Revolutionary Guard's account of a ship
attack in the Strait of Hormuz. Seventeen more stories run in brief
below the fold, from markets rallying in Seoul and Tokyo to a quasar
spotted 630 million years after the Big Bang.

The artwork (`art.png`, 1024x1024) is drawn from scratch with Pillow by
`draw.py` — masthead, date line, lead column beside a hand-drawn scales
of justice, three- and two-column story rows, and a briefs section.
`main.ts` checks the PNG (magic bytes, 1024x1024, under 1 MiB) and copies
it to `$MAKEFUN_OUTPUT_DIR/entry.png`.

## Run it

```sh
python3 draw.py          # regenerates art.png
MAKEFUN_OUTPUT_DIR=out node main.ts   # writes out/entry.png
```
