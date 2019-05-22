#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:donghui

from urllib.parse import quote
import requests
from lxml import etree
title_name = '小龙虾'


#http://search.jd.com/Search?keyword=%E5%B0%8F%E9%BE%99%E8%99%BE&enc=utf-8&cid1=12218&wq=%E5%B0%8F%E9%BE%99%E8%99%BE&pvid=5b0ac1c845e746d497437f2d4a40f595
#print(quote(title_name))
# Field_name = 'http://search.jd.com/Search'
# params = {"keyword":quote(title_name),"enc":"utf-8","cid1":"12218","wq":quote(title_name),"pvid":"5b0ac1c845e746d497437f2d4a40f595",}
#
# r = requests.post(Field_name, json=params)

r = requests.get("http://search.jd.com/Search?keyword=%E5%B0%8F%E9%BE%99%E8%99%BE&enc=utf-8&cid1=12218&wq=%E5%B0%8F%E9%BE%99%E8%99%BE&pvid=5b0ac1c845e746d497437f2d4a40f595")
#print(r.url)
if r.status_code != 200:
    print("状态机%s出错" % r.status_code)
else:
    src_selector = etree.HTML(r.text)
    items = src_selector.xpath('//*[@id="J_goodsList"]/ul/li')

for item in items:
    # store_name = item.xpath('//*[@span="J_im_icon"]/a/text()').extract()
    # title_name = item.xpath('//*[@class="p-name p-name-type-2"]/a/em/i/text()').extract()
    # price = item.xpath('//*[@class="p-price"]/strong/i/text()').extract()
    # print(store_name,":",title_name,":",price)
    #print(item.xpath('//*[@class="p-shop"]/@data-score'))
    print(etree.tostring(item))
r.close()