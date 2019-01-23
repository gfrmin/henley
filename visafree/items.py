# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Countrypair(scrapy.Item):
    passport = scrapy.Field()
    to = scrapy.Field()
    visafree = scrapy.Field()
