#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:donghui
from urllib.parse import quote
title_name = quote("人兽-49部-小合集-19G")
# url_module = "http://www.btkuai.org/word/"+title_name+"_{}.html"
# print(url_module)
# start_urls = [
#     url_module.format(n) for n in range(2)
# ]
start_urls = [
        "http://www.btkuai.org/word/" + title_name + "_{}.html".format(n) for n in range(1,3)
    ]
print(start_urls)

import csv
with open("res/test.csv","w") as csvfile:
    writer = csv.writer(csvfile)

    #先写入columns_name
    writer.writerow(["title","link"])
    var1=["171129大学教师酒店和女学生开房美女柔弱无骨啊-19" + "," + "http://www.btkuai.org/read/3f91861ca6c2e50f825819cb694490dfabb220b0.html"]
    var2=["良家教师少妇白天在于情人疯狂做爱动作很猛 国语对白 妈妈帮我手淫然后插入清晰国语淫荡对白，让人欲血沸腾" + "," + "http://www.btkuai.org/read/352a42012d6c1267686a6db0314beb8df30a8581.html"]
    var3=["我老公的家庭教师 2017.mp4" + "," + "http://www.btkuai.org/read/e3d21a4d18b013997d6f585c4f28c8435823d28c.html"]
    #写入多行用writerows
    writer.writerows([var1,var2,var3])
csvfile.close()

import pymongo
mongo = pymongo.MongoClient(host="127.0.0.1", port=27017)
db = mongo["runoob"]
collection = db['btKuai']
collection.insert({'title':"171129大学教师酒店和女学生开房美女柔弱无骨啊-19", "link":"http://www.btkuai.org/read/3f91861ca6c2e50f825819cb694490dfabb220b0.html"})
mongo.close()