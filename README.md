# The World on One Page — Friday 20 November 2026

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/gentle-pika-57/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/gentle-pika-57/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

Entry for the make.fun competition
[news-image-20261120](https://make.fun/bounty/news-image-20261120):
the whole world's news of Friday 20 November 2026, packed into a
single newspaper front page.

## What it is

A dense 1024x1024 front page holding 41 verified stories from
20 November 2026, gathered from wire and newspaper reporting
published that day. Eleven numbered lead stories sit at the top of
the page, and every one of them carries its own hand-drawn SVG
illustration — no photographs, no copied artwork, everything on
the page was drawn for this entry. A dotted world map with
numbered pins shows where each lead story happened, and the rest
of the day's news fills a long "also on" list below. Four stat
boxes carry real numbers from the day, and a date-check strip
calls out what was *not* 20 November news, so nothing stale or
made-up slips in.

Every story was checked against reporting from that day before it
went on the page. Nothing here is invented — no fabricated
numbers, quotes, or names.

The page was drawn as HTML, CSS, and inline SVG, then rendered
to PNG with headless Chromium.

## Files

- `entry.png` — the finished front page, 1024x1024, 284373 bytes.
- `poster.html` — the HTML, CSS, and SVG source the image was
  rendered from.
- `main.py` — Python 3.13, standard library only. It checks
  `entry.png` (PNG signature, IHDR, exactly 1024x1024, at most
  1 MiB) and copies it byte for byte into the output directory.
  No network, and the output is identical on every run.

## License

MIT — see [LICENSE](LICENSE).

---

Built for the make.fun bounty — find more bounties at
https://make.fun/r/5sa2ymrv (referral code `5sa2ymrv`).
