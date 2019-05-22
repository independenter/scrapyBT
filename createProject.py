#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:donghui


#创建scrapy项目
#scrapy startproject JdFresh

#url加密
from urllib.parse import quote
title_name = quote("")

#url解密


#base64加密
import base64
open_icon = open("./11.ico","r")
b64str = base64.b64encode(("img = %s " % open_icon.read()).encode('utf-8'))
open_icon.close()

#base64解密
from icon import img

tmp = open("tmp.ico", "wb+")
tmp.write(base64.b64decode(img))
tmp.close()
