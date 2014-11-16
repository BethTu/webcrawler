# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class USLPlayerRos(scrapy.Item):
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


class USLPlayerStat(scrapy.Item):
    ln = scrapy.Field()
    fn = scrapy.Field()
    seq = scrapy.Field()
    personkey = scrapy.Field()
    team = scrapy.Field()
    jersey = scrapy.Field()
    midname = scrapy.Field()
    nickname = scrapy.Field()
    birthdate = scrapy.Field()
    regnum = scrapy.Field()
    pos1 = scrapy.Field()
    pos2 = scrapy.Field()
    GP = scrapy.Field()
    Points = scrapy.Field()
    Min = scrapy.Field()
    G = scrapy.Field()
    A = scrapy.Field()
    S = scrapy.Field()
    F = scrapy.Field()
    pending = scrapy.Field()


class USLTeam(scrapy.Item):
    TeamName = scrapy.Field()
    OverallPts = scrapy.Field()
    OverallGP = scrapy.Field()
    OverallW = scrapy.Field()
    OverallL = scrapy.Field()
    OverallT = scrapy.Field()
    OverallGF = scrapy.Field()
    OverallGA = scrapy.Field()
    HomeW = scrapy.Field()
    HomeL = scrapy.Field()
    HomeT = scrapy.Field()
    HomeGF = scrapy.Field()
    HomeGA = scrapy.Field()
    AwayW = scrapy.Field()
    AwayL = scrapy.Field()
    AwayT = scrapy.Field()
    AwayGF = scrapy.Field()
    AwayGA = scrapy.Field()


class NASLPlayer(scrapy.Item):
    Player = scrapy.Field()
    Team = scrapy.Field()
    Gls = scrapy.Field()
    Ast = scrapy.Field()
    Yel = scrapy.Field()
    Red = scrapy.Field()


class NASLTeam(scrapy.Item):
    Team = scrapy.Field()
    GP = scrapy.Field()
    Gls = scrapy.Field()
    Sht = scrapy.Field()
    Fouls = scrapy.Field()
    Yel = scrapy.Field()
    Red = scrapy.Field()


class SBNationPlayer(scrapy.Item):
    Name = scrapy.Field()
    Pos = scrapy.Field()
    Team  = scrapy.Field()
    Born = scrapy.Field()
    Age = scrapy.Field()
    Height = scrapy.Field()
    Weight = scrapy.Field()
    Seasons = scrapy.Field()


class WhoscoredTeamForm3(scrapy.Item):
    ID = scrapy.Field()
    Tournament = scrapy.Field()
    Team = scrapy.Field()
    OverallP = scrapy.Field()
    OverallW = scrapy.Field()
    OverallD = scrapy.Field()
    OverallL = scrapy.Field()
    OverallGF = scrapy.Field()
    OverallGA = scrapy.Field()
    OverallGD = scrapy.Field()
    OverallPts = scrapy.Field()
    HomeP = scrapy.Field()
    HomeW = scrapy.Field()
    HomeD = scrapy.Field()
    HomeL = scrapy.Field()
    HomeGF = scrapy.Field()
    HomeGA = scrapy.Field()
    HomeGD = scrapy.Field()
    HomePts = scrapy.Field()
    AwayP = scrapy.Field()
    AwayW = scrapy.Field()
    AwayD = scrapy.Field()
    AwayL = scrapy.Field()
    AwayGF = scrapy.Field()
    AwayGA = scrapy.Field()
    AwayGD = scrapy.Field()
    AwayPts = scrapy.Field()


class WhoscoredTeamForm6(scrapy.Item):
    ID = scrapy.Field()
    Tournament = scrapy.Field()
    Team = scrapy.Field()
    OverallP = scrapy.Field()
    OverallW = scrapy.Field()
    OverallD = scrapy.Field()
    OverallL = scrapy.Field()
    OverallGF = scrapy.Field()
    OverallGA = scrapy.Field()
    OverallGD = scrapy.Field()
    OverallPts = scrapy.Field()
    HomeP = scrapy.Field()
    HomeW = scrapy.Field()
    HomeD = scrapy.Field()
    HomeL = scrapy.Field()
    HomeGF = scrapy.Field()
    HomeGA = scrapy.Field()
    HomeGD = scrapy.Field()
    HomePts = scrapy.Field()
    AwayP = scrapy.Field()
    AwayW = scrapy.Field()
    AwayD = scrapy.Field()
    AwayL = scrapy.Field()
    AwayGF = scrapy.Field()
    AwayGA = scrapy.Field()
    AwayGD = scrapy.Field()
    AwayPts = scrapy.Field()


class WhoscoredTeamStreaks(scrapy.Item):
    ID = scrapy.Field()
    Tournament = scrapy.Field()
    Team = scrapy.Field()
    OverallStreaks = scrapy.Field()
    OverallPlayed = scrapy.Field()
    HomeStreaks = scrapy.Field()
    HomePlayed = scrapy.Field()
    AwayStreaks = scrapy.Field()
    AwayPlayed = scrapy.Field()


class WhoscoredTeamPerformances(scrapy.Item):
    ID = scrapy.Field()
    Tournament = scrapy.Field()
    Team = scrapy.Field()
    OverallP = scrapy.Field()
    OverallW = scrapy.Field()
    OverallD = scrapy.Field()
    OverallL = scrapy.Field()
    OverallGF = scrapy.Field()
    OverallGA = scrapy.Field()
    OverallGD = scrapy.Field()
    OverallPts = scrapy.Field()
    HomeP = scrapy.Field()
    HomeW = scrapy.Field()
    HomeD = scrapy.Field()
    HomeL = scrapy.Field()
    HomeGF = scrapy.Field()
    HomeGA = scrapy.Field()
    HomeGD = scrapy.Field()
    HomePts = scrapy.Field()
    AwayP = scrapy.Field()
    AwayW = scrapy.Field()
    AwayD = scrapy.Field()
    AwayL = scrapy.Field()
    AwayGF = scrapy.Field()
    AwayGA = scrapy.Field()
    AwayGD = scrapy.Field()
    AwayPts = scrapy.Field()
