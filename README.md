# SoFIFA Scraper

This is the custom SoFIFA scraper built for our project of Big Data Computing 2021-22 at Sapienza University of Rome.

By [Daniele Solombrino](https://github.com/dansolombrino) and [Davide Quaranta](https://github.com/davquar).

## Requirements

Only Scrapy 2.6.1

## Usage

```shell
cd src
scrapy crawl sofifa
```

To save the output as CSV:

```shell
scrapy crawl sofifa -o out.csv -t csv -a
```

To set a specific year to scrape:

```shell
scrapy crawl sofifa -o out.csv -t csv -a year=13
```

### Extending the scraper with custom years

To scape other years than the currently supported ones, it is needed to:

1. Find the "year key" that SoFIFA uses to identity a date.
2. Add the key to [the `YEAR_KEYS` dictionary in the utils file](src/sofifa/spiders/utils.py).

Finding the year key is simple: just go to the players page on SoFIFA and select an year/date, then note in the `?r=x` value in the URL. For example, `?r=220019` refers to Dec 9 2021 (FIFA 22).

**Note** that across different FIFA versions, players' fields may be different, hence it may be needed to manually change the fields to scrape.
