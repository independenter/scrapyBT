# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Scrapy58UserinfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    category = scrapy.Field()
    title = scrapy.Field()
    money = scrapy.Field()
    name = scrapy.Field()
    tel = scrapy.Field()
    city = scrapy.Field()
