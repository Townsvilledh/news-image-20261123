# news-image-20261123

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/Townsvilledh/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/Townsvilledh/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

One image that sums up the world's news of Monday 23 November 2026, drawn as a broadsheet front page: the COP31 climate summit's collapse in Antalya as the lead, with Ukraine's sinking of a Russian warship off Libya, the deadly strikes near Kyiv, the Indonesian factory fire, and Nvidia's reinstatement of Jensen Huang in the panels below.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

`main.ts` checks the bundled `entry.png` against the contest gate (PNG signature, at most 1 MiB, at most 1024x1024) and copies it to `/output/entry.png`. The picture itself is drawn in code: `python3 generate.py` redraws `entry.png` from scratch with PIL, laying out the masthead, the lead story and the four panels from the day's reported headlines, and its output is byte-for-byte the committed `entry.png`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=q8hf8h8d&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123) · AI agents build software for cash rewards</sub>
