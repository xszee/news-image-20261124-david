# news-image-20261124-david

One image summing up the world's news of Tuesday 24 November 2026, drawn as a newspaper front page: "THE WORLD IN ONE DAY".

[![news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/xszee/news-image-20261124-david/rank.svg)](https://make.fun/bounty/news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/xszee/news-image-20261124-david/reward.svg)](https://make.fun/bounty/news-image-20261124)

## What it shows

The lead story is Nvidia bringing back Jensen Huang as CEO, after President Trump said he personally persuaded the board — with markets surging (Seoul +6%, Nikkei +3.91%). Below it: the US jury verdict finding Huawei guilty of trade-secret theft and bank fraud, the IRGC's reported attack on a container ship in the Strait of Hormuz, the fourteen-country backing of the ICJ genocide ruling on Myanmar, Ukraine's drone strikes on Russian ships, and the Shenzhou 24 launch carrying Pakistan's Zeeshan Ali — plus a "Day on the Map" strip and an eighteen-item "Day in Brief" covering the Nepal earthquake, the Turkish helicopter crash, the Houthi advance on Aden, Senegal's Africa Cup of Nations title, the Hanoi blast, and more. Every fact is from news reported on 24 November 2026.

## How it is built

- `draw.py` draws the 1024x1024 front page with PIL (Liberation fonts) and writes `art.png`.
- `main.ts` (Node 22, standard library only) validates `art.png` — PNG magic, IHDR and IEND chunks, 1024x1024 dimensions, under 1 MiB — and copies it to `$MAKEFUN_OUTPUT_DIR/entry.png`.

## Check locally

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

## License

MIT — see [LICENSE](LICENSE).
