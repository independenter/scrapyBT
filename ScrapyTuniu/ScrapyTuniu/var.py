#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Dob

import requests

headers = {
                'Accept':'*/*',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.9',
               'Connection': 'keep-alive',
               'Cookie': 'Hm_lvt_19f9e31a97c820b0081af5bccd6bb217=1540695217,1540695273,1540695273,1540695273',
               'Host': '45.126.123.80:118',
               'Referer': "http://s.tuniu.com/search_complex/whole-nj-0-%E6%B3%B0%E5%9B%BD/20",
               'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
                'X-Requested-With':'XMLHttpRequest'
}
cookies_str = 'Hm_lvt_19f9e31a97c820b0081af5bccd6bb217=1540695217,1540695273,1540695273,1540695273'; # 抓包获取
# 将cookies_str转换为cookies_dict
cookies = {i.split('=')[0]: i.split('=')[1] for i in cookies_str.split('; ')}
url = 'https://bbs.pcauto.com.cn/forum-17442-7.html'
r = requests.get(url)
print(r.status_code)
with open('taipingyang_2.txt', 'wb') as f:
    print(r.text)
    f.write(r.content)