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
