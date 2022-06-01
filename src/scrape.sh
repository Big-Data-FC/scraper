#!/bin/bash

echo "SCRAPING YEAR 14"
scrapy crawl sofifa -L INFO -a year=14 -o ../../datasets/14.csv -t csv -s JOBDIR=../../datasets/crawls/sofifa-14
echo "\n\nSCRAPING YEAR 13"
scrapy crawl sofifa -L INFO -a year=13 -o ../../datasets/13.csv -t csv -s JOBDIR=../../datasets/crawls/sofifa-13
echo "\n\nSCRAPING YEAR 12"
scrapy crawl sofifa -L INFO -a year=12 -o ../../datasets/12.csv -t csv -s JOBDIR=../../datasets/crawls/sofifa-12
echo "\n\nSCRAPING YEAR 11"
scrapy crawl sofifa -L INFO -a year=11 -o ../../datasets/11.csv -t csv -s JOBDIR=../../datasets/crawls/sofifa-11
echo "\n\nSCRAPING YEAR 10"
scrapy crawl sofifa -L INFO -a year=10 -o ../../datasets/10.csv -t csv -s JOBDIR=../../datasets/crawls/sofifa-10
echo "\n\nSCRAPING YEAR 09"
scrapy crawl sofifa -L INFO -a year=09 -o ../../datasets/09.csv -t csv -s JOBDIR=../../datasets/crawls/sofifa-09
echo "\n\nSCRAPING YEAR 08"
scrapy crawl sofifa -L INFO -a year=08 -o ../../datasets/08.csv -t csv -s JOBDIR=../../datasets/crawls/sofifa-08
echo "\n\nSCRAPING YEAR 07"
scrapy crawl sofifa -L INFO -a year=07 -o ../../datasets/07.csv -t csv -s JOBDIR=../../datasets/crawls/sofifa-07