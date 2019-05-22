# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyYingcaiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    岗位名称 = scrapy.Field()
    薪水范围 = scrapy.Field()
    公司名称 = scrapy.Field()
    福利待遇 = scrapy.Field()
