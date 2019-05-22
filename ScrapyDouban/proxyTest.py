#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:donghui

import requests,json
from lxml.html import etree

# 本机IP
#localip = "172.18.48.29"

# 待清洗代理IP数据池
proxies = [
    #{"http": "190.2.137.9:1080" },
    # {"https": "119.28.138.104:3128" },
    # {"https": "117.64.237.244:18118"},
    # {"https": "58.19.13.93:18118" },
    # {"https": "183.159.90.60:18118" },
    # {"http": "111.155.116.220:8123"},
    # {"https": "58.19.63.57:18118" },
    # {"https": "183.159.85.234:3128" },
    # {"https": "223.240.208.151:18118"},
    # {"http": "117.68.193.19:18118" },
    ]
httpCol={}
# 有效代理IP池
proxypool = []
#http://www.66ip.cn/
proxy_urls = ['http://www.ip3366.net/?stype=1&page={}'.format(n) for n in range(1,11)]
for proxy_url in proxy_urls:
    #print(proxy_url)
    r = requests.get(url=proxy_url)
    if r.status_code==200:
        html = etree.HTML(r.text)
        selectors = html.xpath('//*[@id="list"]/table/tbody/tr')
        #print(selectors)
        for row in selectors:
            host = row.xpath('td[1]/text()')[0]
            port = row.xpath('td[2]/text()')[0]
            httpCol['http']=host+":"+port
            proxies.append(httpCol)
            httpCol={}
    r.close()
#print(proxies)


f = open("EffectiveIp.json", 'w')
f.write('[')

#清洗代理IP，去除无效的代理IP
for index in range(len(proxies)):
    print(proxies[index])
    try:
        result = requests.get('https://twitter.com/', proxies={'http': '64.15.69.126:8080'})
    except Exception as e:
        continue
    # 与本机IP对比，相等则说明没用到代理IP，为无效项
    #print(result.content)
    if result.status_code==200:
        print(result.text)
        proxypool.append(proxies[index])  #集合元素追加到列表
        # print(result.text.encode("utf-8"))
        json.dump(proxies[index], f)  # var为字典列表
        f.write(',')
    result.close()

f.write(']')
f.close()

print(proxypool)