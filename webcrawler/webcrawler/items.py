# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class USLPlayer(scrapy.Item):
    ln = scrapy.Field()
    fn = scrapy.Field()
    seq = scrapy.Field()
    personkey = scrapy.Field()
    team = scrapy.Field()
    jersey = scrapy.Field()
    midname = scrapy.Field()
    regnum = scrapy.Field()
    last_team = scrapy.Field()
    pos1 = scrapy.Field()
    pos2 = scrapy.Field()
    hgtF = scrapy.Field()
    hgtI = scrapy.Field()
    wght = scrapy.Field()
    birthdate = scrapy.Field()
    apprvd = scrapy.Field()

class NASLPlayer(scrapy.Item):
    Player = scrapy.Field()
    Team = scrapy.Field()
    Gls = scrapy.Field()
    Ast = scrapy.Field()
    Yel = scrapy.Field()
    Red = scrapy.Field()
