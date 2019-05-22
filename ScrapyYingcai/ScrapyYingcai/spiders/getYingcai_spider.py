#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Dob

import scrapy,re
from urllib.parse import quote
from ScrapyYingcai.items import ScrapyYingcaiItem
from lxml.html import etree
import requests
from scrapy.http import Request


class GetYingcai(scrapy.Spider):
    name = "getYingcai"
    allowed_domains = ["chinahr.com"]
    #左闭右开 900/30
    start_urls = [
        "http://search.chinahr.com/sh/job/pn{}/?key=python".format(n) for n in range(0,31)
        ]

    def parse(self, response):
        selector = response.xpath('//*[@id="container"]/div[2]/div/div[1]/div')
        for sel in selector:
            try:
                var1 = sel.xpath('ul[1]/li[@class="job-name"]/text()').extract()[0];
            except:
                var1 = '解析有误'
            try:
                var2 = sel.xpath('ul[2]/li[@class="job-salary"]/text()').extract()[0];
            except:
                var2 = '解析有误'
            try:
                var3 = sel.xpath('ul[2]/li[@class="job-company"]/text()').extract()[0];
            except:
                var3 = '解析有误'
            try:
                var4 = sel.xpath('ul[3]/li[1]/div/span/text()').extract();
            except:
                var4 = '解析有误'

            item = ScrapyYingcaiItem()
            item['岗位名称'] = var1
            item['薪水范围'] = var2
            item['公司名称'] = var3
            item['福利待遇'] = var4

            print("item", item)

            yield item
