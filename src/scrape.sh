#!/bin/bash

echo "SCRAPING YEAR 14"
scrapy crawl sofifa -L INFO -a year=14 -o ../../datasets/14.csv -t csv -s JOBDIR=../../datasets/crawls/sofifa-14
echo "\n\nSCRAPING YEAR 13"
scrapy crawl sofifa -L INFO -a year=13 -o ../../datasets/13.csv -t csv -s JOBDIR=../../datasets/crawls/sofifa-13
echo "\n\nSCRAPING YEAR 12"
scrapy crawl sofifa -L INFO -a year=12 -o ../../datasets/12.csv -t csv -s JOBDIR=../../datasets/crawls/sofifa-12