#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Dob

import scrapy,re
from urllib.parse import quote
from ScrapyTuniu.items import ScrapyTuniuItem
from lxml.html import etree
import requests
from scrapy.http import Request


class GetTuniu(scrapy.Spider):
    name = "getTuniu"
    allowed_domains = ["tuniu.com"]
    #左闭右开 600/30
    start_urls = [
        "http://s.tuniu.com/search_complex/whole-nj-0-泰国/{}".format(n) for n in range(1,2)
        ]

    def start_requests(self):
        for url in self.start_urls:
            yield self.make_requests_from_url(url)

    def make_requests_from_url(self, url):
        # 这个cookies_str是抓包获取的
        cookies_str = 'Hm_lvt_19f9e31a97c820b0081af5bccd6bb217=1540695217,1540695273,1540695273,1540695273'  # 抓包获取
        # 将cookies_str转换为cookies_dict
        cookies_dict = {i.split('=')[0]: i.split('=')[1] for i in cookies_str.split('; ')}
        return Request(url, dont_filter=True,cookies=cookies_dict)

    def parse(self, response):
        with open('tuniu_2.txt', 'w+') as f:
            f.write(response.text)
        selector = response.xpath('//*[@id="niuren_list"]/div[2]/div[2]/div[1]/div[1]/ul/li')
        for sel in selector:
            try:
                # var1 = sel.xpath('div/a/dl/dt/p[1]/span/@name').extract()[0] + \
                #        sel.xpath('div/a/dl/dt/p[1]/span/span/text()').extract()[0];
                print(sel.xpath('div/a/dl/dt/p[1]/span/@name'))
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

            item = ScrapyTuniuItem()
            item['名称'] = var1
            item['价格'] = var2
            item['满意度'] = var3
            item['出游人数'] = var4

            print("item", item)

            #yield item
