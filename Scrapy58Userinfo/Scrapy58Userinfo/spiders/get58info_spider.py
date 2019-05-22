#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Dob

import scrapy,re
from urllib.parse import quote
from Scrapy58Userinfo.items import Scrapy58UserinfoItem
import requests,time
from lxml.html import etree

#[{商铺出售：shangpucs},{商铺出租：shangpucz},{商铺：shangpu},{生意转让：shangpu},{写字楼出租:zhaozu},{厂房:changfang},{写字楼出租:zhaozu},{写字楼出租:zhaozu},{写字楼出租:zhaozu}]

class Get58Spider(scrapy.Spider):
    name = "get58"
    allowed_domains = ["58.com"]
    start_urls = [
        "https://haikou.58.com/changfang/pn{}".format(n) for n in range(1,7)
    ]

    def savefile(self,var):
        f = open("Scrapy58Userinfo/res/181010.log","w+",encoding='utf-8')  #路径一定要写对
        f.write(var)
        f.close()
        #print("保存完毕")

    def parse(self, response):
        url_head = 'https://haikou.58.com'
        #filename = response.url.split("/")[-3]+"_"+response.url.split("/")[-2]
        #停顿20秒，防止机器人检测
        #time.sleep(20)
        category = response.url.split("/")[-3]

#/html/body/div[5]/div[4]/div[1]/ul/li[1]/div[4]/p/span
        selector = response.xpath('/html/body/div[5]/div[5]/div[1]/ul/li')

        for sel in selector:
            title = sel.xpath('div[2]/h2/a/span/text()').extract()[0]
            money = sel.xpath('div[4]/p/b/text()').extract()[0] + sel.xpath('div[4]/p/span/text()').extract()[0]
            tel_link = sel.xpath('div[2]/h2/a/@href').extract()[0]

            item = Scrapy58UserinfoItem()
            item['category'] = category
            item['title'] = title
            item['money'] = money

            r = requests.get(tel_link)
            try:
                if r.status_code == 200:
                    selector1 = etree.HTML(r.text)
                    tel = selector1.xpath('//*[@class="phone-num"]/text()')[0]
                    tel = re.sub(r'\s', '', tel)

                    name = selector1.xpath('//*[@class="c_000 agent-name-txt"]/text()')
                    name = len(name)==0 and '获取不到' or name

                    try:
                        city = selector1.xpath('//*[@id="commonTopbar"]/div/div[1]/h2/text()')[0] + \
                               selector1.xpath('/html/body/div[4]/div[2]/div[2]/ul/li[5]/a[1]/text()')[0] + \
                               selector1.xpath('/html/body/div[4]/div[2]/div[2]/ul/li[5]/a[2]/text()')[0] + \
                               selector1.xpath('/html/body/div[4]/div[2]/div[2]/ul/li[5]/span[2]/text()')[0]
                        city = re.sub(r'\s', '', city)
                    except Exception as e:
                        city = '未知'

                    item['name'] = name
                    item['city'] = city
                    item['tel'] = tel

                    print('item',item)

            except Exception as e:
                print(e)
                continue
            finally:
                #print()
                yield item
