#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Dob

import requests,re
from lxml.html import etree

r=requests.get("https://jxjump.58.com/service?target=FCADV8oV3os7xtAhI2suhvPnTEBzv3yWxPUi9689VPTYLrfDZpk1zEffDjhGKDukKaSGKEtf3gzeNV-hi1br_YYHKV4VXQUowmqf0x_7k2_EqtKr-8LJfFr3I9CHuQmrfqvi_rE2gJv3TDO4nP8HmJCXfD8ohc64lcmQwr-QuiAazy30tuCRZ9nGadawT5rZ_Zr_79oKcmX61M0gM2JLS9IQWX5FQCNhY8leAoCkNHmFZGkfxhkTb2iVPBKOzcS_xaxNx&local=2053&pubid=45264482&apptype=0&psid=163735267201740195586571804&entinfo=35729620095427_0&cookie=|||c5/njVu9plgga4PnAwR2Ag&fzbref=0&key=&params=jxshangpurctrpcA^desc")
item={}
if r.status_code == 200:
    selector = etree.HTML(r.text)
    tel = selector.xpath('//*[@id="houseChatEntry"]/div/p[1]/text()')[0]
    tel = re.sub(r'\s', '', tel)
    name = selector.xpath('/html/body/div[4]/div[2]/div[2]/div[1]/div/a/text()')[0]
    city = selector.xpath('//*[@id="houseChatEntry"]/div/p[2]/span[2]/text()')[0] + \
           selector.xpath('/html/body/div[4]/div[2]/div[2]/ul/li[6]/a[1]/text()')[0] + \
           selector.xpath('/html/body/div[4]/div[2]/div[2]/ul/li[6]/a[2]/text()')[0] + \
           selector.xpath('/html/body/div[4]/div[2]/div[2]/ul/li[6]/span[2]/text()')[0]
    city = re.sub(r'\s', '', city)
    item['name'] = name
    item['city'] = city
    item['tel'] = tel
    print("item", item)
