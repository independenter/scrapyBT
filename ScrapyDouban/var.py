#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Dob

import json,re,time,datetime


#f = open("EffectiveIp.json", 'r')
# f = open("ScrapyDoubsn/res/yichuhaoxi-yingping.json", 'r')
# ips = json.load(f)
# print(type(ips))
# print(len(ips))

import requests,re

# f = open("yichuhaoxi-yingping.json", 'r')
# ips = json.load(f)
# print(type(ips))
# print(len(ips))

a=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','AA','AB'
    ,'AC','AD','AE','AF','AG','AH','AI','AJ','AK','AL','AM','AN','AO','AP','AQ','AR']
a=['17 一', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

print(a.index("AF"))

d = 0.3666658401489258;
from xlrd import xldate_as_tuple
from xlrd import xldate_as_datetime
import xlrd
print(*xldate_as_tuple(d,0))
print(xldate_as_datetime(d,0))

print(xlrd.xldate_as_tuple(d, 0) )

b= '旷工\n(天)';
print(re.sub(r'\s', '', b))

c="考勤日期：2018-12-17～2018-12-21";
mat = re.findall(r"(\d{4}-\d{1,2}-\d{1,2})",c)
d1 = datetime.datetime.strptime(mat[0], '%Y-%m-%d')
d2 = datetime.datetime.strptime(mat[1], '%Y-%m-%d')
delta = d1 - d2
print(delta.days)





# headers = {'Accept':'*/*',
# 'Accept-Encoding':'gzip, deflate, br',
# 'Accept-Language':'zh-CN,zh;q=0.9',
# 'Connection':'keep-alive',
# 'Cookie':'bid=2g-CWSYSi-0; doub-------an-fav-remind=1; __utmz=223695111.1540563407.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ps=y; push_noty_num=0; push_doumail_num=0; __utmc=30149280; __utmz=30149280.1540695006.5.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmc=223695111; ll="118371"; ue="dh2531@foxmail.com"; _pk_ses.100001.4cf6=*; __utma=30149280.24434663.1538293737.1540695006.1540702888.6; __utma=223695111.977060243.1540563407.1540695353.1540702888.5; ap_v=0,6.0; __utmv=30149280.18652; __yadk_uid=QcQlpvBHlmkCTpOBgnruTmC12iejRXff; __utmb=30149280.8.10.1540702888; _vwo_uuid_v2=DE4D18E5F668BE348D47B8B20A38232CE|3d6afdcc96b66b75470d540589f1b16c; __utmt=1; dbcl2="186529030:7r5PcPbBjfI"; ck=bQEY; _pk_id.100001.4cf6=f45ec8cc131dc4f1.1540563407.5.1540704910.1540699791.; __utmb=223695111.15.10.1540702888',
# 'Host':'movie.douban.com',
# 'Referer':"https://movie.douban.com/subject/26985127/comments?start=240&limit=20&sort=new_score&status=P",
# 'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
# 'X-Requested-With':'XMLHttpRequest'
# }
# cookies_str = 'bid=2g-CWSYSi-0; douban-fav-remind=1; __utmz=223695111.1540563407.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ps=y; push_noty_num=0; push_doumail_num=0; __utmc=30149280; __utmz=30149280.1540695006.5.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmc=223695111; ll="118371"; ue="dh2531@foxmail.com"; _pk_ses.100001.4cf6=*; __utma=30149280.24434663.1538293737.1540695006.1540702888.6; __utma=223695111.977060243.1540563407.1540695353.1540702888.5; ap_v=0,6.0; __utmv=30149280.18652; __yadk_uid=QcQlpvBHlmkCTpOBgnruTmC12iejRXff; __utmb=30149280.8.10.1540702888; _vwo_uuid_v2=DE4D18E5F668BE348D47B8B20A38232CE|3d6afdcc96b66b75470d540589f1b16c; __utmt=1; dbcl2="186529030:7r5PcPbBjfI"; ck=bQEY; _pk_id.100001.4cf6=f45ec8cc131dc4f1.1540563407.5.1540704910.1540699791.; __utmb=223695111.15.10.1540702888'; # 抓包获取
# # 将cookies_str转换为cookies_dict
# cookies = {i.split('=')[0]: i.split('=')[1] for i in cookies_str.split('; ')}
# url = 'https://movie.douban.com/subject/26985127/comments?start=300&limit=20&sort=new_score&status=P'
# r = requests.get(url, cookies=cookies)
# with open('douban_2.txt', 'wb') as f:
#     f.write(r.content)