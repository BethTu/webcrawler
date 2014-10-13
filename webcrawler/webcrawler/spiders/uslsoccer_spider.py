__author__ = 'beth'
import scrapy
import json

class UslsoccerSpider(scrapy.Spider):
    name = "uslsoccer"
    allowed_domain = ["uslpro.uslsoccer.com"]
    start_urls = ["http://uslpro.uslsoccer.com/teams/65672455/67653369-65672522-ros.js"]

    def parse(self, response):
        players = json.loads(response.body)
        i = 1
        for id, player in players["players"].items():
            print "Player", i
            for key, value in player.items():
                print key, ":", value
            i = i + 1