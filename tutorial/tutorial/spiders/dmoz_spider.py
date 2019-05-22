#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:donghui

import scrapy
import re
from urllib.parse import quote
from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.btkuai.org/word/" + quote("风光") + "_{}.html".format(n) for n in range(1,10)
    ]

    def savefile(self,filename,var):
        f = open("tutorial/res/"+filename+".csv","w+")  #路径一定要写对
        f.write(var)
        f.close()
        #print("保存完毕")

    def parse(self, response):
        url_head = 'http://www.btkuai.org'
        #filename = response.url.split("/")[-2]

        selector = response.xpath('//div[@id="container"]/div/ul/li/div[@class="T1"]')
        for sel in selector:
            title = sel.xpath('a/text()').extract()[0]
            link = url_head +(sel.xpath('a/@href').extract()[0])
            if re.findall('([a-zA-z]+://[^\s]*html$)',link,re.S):
                #print(title, link)
                #self.savefile(filename, title + "," + link)
                item = DmozItem()
                item['title'] = title
                item['link'] = link
                yield item


