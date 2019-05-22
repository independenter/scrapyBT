#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:donghui

# 导入随机模块
import random,json
# 导入settings文件中的IPPOOL
from .settings import IPPOOL
# 导入官方文档对应的HttpProxyMiddleware
from scrapy.contrib.downloadermiddleware.httpproxy import HttpProxyMiddleware
from scrapy.conf import settings

class IPPOOlS(HttpProxyMiddleware):
    with open("../EffectiveIp.json", 'r') as handler:
        ips = json.load(handler)
    handler.close()
    def __init__(self, ip=''):
        self.ip = ip

    def process_request(self, request, spider):
        proxyMode = settings['IPPoolMode']
        if proxyMode==0:
            thisip = random.choice(settings['IPPOOL'])
            print("代理ip：%s" % thisip["http"])
            request.meta["proxy"] = "http://" + thisip["http"]
        elif proxyMode==1:
            thisip = random.choice(IPPOOlS.ips)
            print("代理ip：%s" % thisip["http"])
            request.meta["proxy"] = "http://" + thisip["http"]
