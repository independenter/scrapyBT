#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Dob

import scrapy,re
from urllib.parse import quote
from ScrapyDouban.items import ScrapyDoubanItem
from lxml.html import etree
import requests
from scrapy.http import Request


class GetDouban(scrapy.Spider):
    name = "getDouban"
    allowed_domains = ["douban.com"]
    #左闭右开 0-200 200-400 400-500
    #500看过
    #"https://movie.douban.com/subject/26985127/comments?limit=20&sort=new_score&status=P&start={}".format(n) for n in range(0,500,20)
    # 500想看
    # "https://movie.douban.com/subject/26985127/comments?limit=20&sort=new_score&status=F&start={}".format(n) for n in range(0,500,20)
    start_urls = [
        "https://movie.douban.com/subject/26985127/comments?limit=20&sort=new_score&status=F&start={}".format(n) for n in range(0, 500, 20)
        ]

    #带cookie免登陆尝试
    # def start_requests(self):  # 重构start_requests方法
    #     # 这个cookies_str是抓包获取的
    #     cookies_str = 'bid=2g-CWSYSi-0; douban-fav-remind=1; __utmz=223695111.1540563407.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ps=y; push_noty_num=0; push_doumail_num=0; __utmc=30149280; __utmz=30149280.1540695006.5.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmc=223695111; ll="118371"; ue="dh2531@foxmail.com"; _pk_ses.100001.4cf6=*; __utma=30149280.24434663.1538293737.1540695006.1540702888.6; __utma=223695111.977060243.1540563407.1540695353.1540702888.5; ap_v=0,6.0; __utmv=30149280.18652; __yadk_uid=QcQlpvBHlmkCTpOBgnruTmC12iejRXff; __utmb=30149280.8.10.1540702888; _vwo_uuid_v2=DE4D18E5F668BE348D47B8B20A38232CE|3d6afdcc96b66b75470d540589f1b16c; dbcl2="186529030:v2nZ5h7PmWs"; ck=aOYy; _pk_id.100001.4cf6=f45ec8cc131dc4f1.1540563407.5.1540703594.1540699791.; __utmt=1; __utmb=223695111.10.10.1540702888'  # 抓包获取
    #     # 将cookies_str转换为cookies_dict
    #     cookies_dict = {i.split('=')[0]: i.split('=')[1] for i in cookies_str.split('; ')}
    #     print("cookies_dict",cookies_dict)
    #     yield scrapy.Request(
    #         self.start_urls[0],
    #         callback=self.parse_page,
    #         cookies=cookies_dict
    #     )

    # 模拟表单登录
    # def start_requests(self):
    #     yield scrapy.FormRequest(
    #         "https://accounts.douban.com/login",
    #         formdata={
    #             "alias": "dh2531@foxmail.com",
    #             #"redir": "https://movie.douban.com/subject/26985127/comments?start=40",
    #             "login_type": "sms",
    #             "source": "movie",
    #             "form_email": "15501951002",
    #             "form_password": "040068"
    #         }
    #     )

    #实际登录
    # def start_requests(self, response):
    #     yield scrapy.FormRequest(url='https://accounts.douban.com/login?redir=https://movie.douban.com/subject/26985127/comments?start=40&limit=20&sort=new_score&status=P&source=movie&login_type=sms').from_response(
    #         response,  # 传入response对象,自动解析
    #         # 可以通过xpath来定位form表单,当前页只有一个form表单时,将会自动定位
    #         formxpath='//*[@id="lzform"]',
    #         formdata={'form_email': '15501951002', 'form_password': '161555'},
    #         callback=self.parse
    #     )

    def parse(self, response):
        #print(response.text)
        if(response.status!=200):
            print(response.url+'出错了')
        selector = response.xpath('//*[@id="comments"]/div[@class="comment-item"]')
        for sel in selector:
            try:
                username = sel.xpath('div[2]/h3/span[2]/a/text()').extract()[0];
                #print("username",username)
            except:
                username = '解析有误'
            try:
                stars = sel.xpath('div[2]/h3/span[2]/span[2]/@class').extract()[0];
                stars = (int)(re.findall(r'\d+', stars)[0]) / 10
                #print("stars", stars)
            except:
                stars = '解析有误'
            try:
                date = sel.xpath('div[2]/h3/span[2]/span[@class="comment-time "]/text()').extract()[0];
                date = re.sub(r'\s', '', date)
                #print("date", date)
            except:
                date = '解析有误'
            try:
                valid_num = sel.xpath('div[2]/h3/span[1]/span/text()').extract()[0];
                #print("valid_num", valid_num)
            except:
                valid_num = '解析有误'
            try:
                movie_review = sel.xpath('div[2]/p/span/text()').extract()[0];
                #print("movie_review", movie_review)
            except:
                movie_review = '解析有误'
            # print("valid_num", valid_num)
            # print("movie_review", movie_review)

            item = ScrapyDoubanItem()
            item['username'] = username
            item['stars'] = stars
            item['date'] = date
            item['valid_num'] = valid_num
            item['movie_review'] = movie_review

            print("item",item)

            yield item
