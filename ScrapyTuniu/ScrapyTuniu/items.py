# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyTuniuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    名称 = scrapy.Field()
    价格 = scrapy.Field()
    满意度 = scrapy.Field()
    出游人数 = scrapy.Field()
