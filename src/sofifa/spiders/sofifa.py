import scrapy
from .utils import *


class SofifaSpider(scrapy.Spider):
    name = "sofifa"
    allowed_domains = ["sofifa.com"]

    def __init__(self, year="14", remap_columns="True"):
        self.year = year
        self.remap_columns = remap_columns.lower() in ("true", "yes", "y", "1")
        self.start_urls = [self.__build_request_url()]
        self.logger.info(f"Scraping year {YEAR_KEYS[year]}")

    def __build_request_url(self) -> str:
        return f"{PLAYERS_BASE_URL}&r={YEAR_KEYS[self.year]}"

    def start_requests(self):
        request = scrapy.Request(self.start_urls[0])
        request.cookies["r"] = YEAR_KEYS[self.year]
        request.headers[
            "User-Agent"
        ] = "Mozilla/5.0 (X11; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0"
        yield request

    def parse(self, response):
        props_headers = response.css("table thead tr th ::text").extract()[7:]
        props_headers = list(map(clean_string, [_ for _ in props_headers]))

        if self.remap_columns:
            props_headers = rename_columns(props_headers)

        for player in response.css("table.table > tbody > tr"):
            item = {
                "sofifa_id": player.css("td.col-pi::text").get(),
                "player_url": player.css("td:nth-child(2) a::attr(href)").get(),
                "short_name": player.css("td:nth-child(2) a div.ellipsis::text").get(),
                "age": player.css("td.col-ae::text").get(),
                "nationality": player.css(
                    "td:nth-child(2) img.flag::attr(title)"
                ).get(),
                "club_name": player.css("td:nth-child(6) div.ellipsis a::text").get(),
                "player_positions": [player.css("td.col-bp a span::text").get()],
            }

            props_values = []

            for p in player.css("td")[8:]:
                value = p.css(" ::text").get()
                if value is None:
                    value = ""
                props_values.append(value.strip())
                item.update(dict(zip(props_headers, props_values)))

            yield item

        for next_page in response.css(".pagination a::attr(href)"):
            offset = next_page.get().split("offset=")[1]
            self.logger.info(f"Following next page. Offset: {offset}")
            yield response.follow(next_page, self.parse)
