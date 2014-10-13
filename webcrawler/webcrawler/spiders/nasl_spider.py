import scrapy
import json

class NaslSpider(scrapy.Spider):
    name = "nasl"
    allowed_domains = ["nasl.com"]
    start_urls = ["http://www.nasl.com/stats/players/table"]

    def parse(self, response):
        attrList = []
        table = response.xpath("//table[@id='playerStatsTable']")
        for attr in table.xpath("thead/tr/th/text()"):
            attrList.append(attr.extract())
        for tr in table.xpath("tbody/tr"):
            i = 0
            for td in tr.xpath("td/text()"):
                print attrList[i], ":", td.extract()
                i = i + 1
