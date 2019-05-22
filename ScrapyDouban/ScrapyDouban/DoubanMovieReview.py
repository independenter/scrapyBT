#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Dob

import requests,re,time,json
from bs4 import BeautifulSoup

class DoubanMovieReview(object):
    def __init__(self,movie_name):
        print('一出好戏影评下载中··· ···')
        self.movie_name = movie_name
        self.i = 0
        self.headers = {
               'Accept-Encoding': 'gzip, deflate, br',
               'Accept-Language': 'zh-CN,zh;q=0.9',
               'Connection': 'keep-alive',
               'Cookie': 'bid=2g-CWSYSi-0; douban-fav-remind=1; __utmz=223695111.1540563407.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ps=y; push_noty_num=0; push_doumail_num=0; __utmz=30149280.1540695006.5.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ll="118371"; ue="dh2531@foxmail.com"; __yadk_uid=QcQlpvBHlmkCTpOBgnruTmC12iejRXff; _vwo_uuid_v2=DE4D18E5F668BE348D47B8B20A38232CE|3d6afdcc96b66b75470d540589f1b16c; __utmv=30149280.18646; ct=y; __utmc=30149280; __utmc=223695111; as="https://www.douban.com/accounts/safety/locked"; dbcl2="186463708:IeumDYsLfdE"; ck=UWUV; douban-profile-remind=1; _pk_id.100001.4cf6=f45ec8cc131dc4f1.1540563407.12.1540822571.1540817989.; __utma=30149280.24434663.1538293737.1540816764.1540822571.13; __utma=223695111.977060243.1540563407.1540816764.1540822571.12',
               'Host': 'movie.douban.com',
               'Referer': "https://movie.douban.com/subject/26985127/comments?start=240&limit=20&sort=new_score&status=P",
               'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
               'X-Requested-With': 'XMLHttpRequest'
               }
        cookies_str = 'bid=2g-CWSYSi-0; douban-fav-remind=1; __utmz=223695111.1540563407.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ps=y; push_noty_num=0; push_doumail_num=0; __utmz=30149280.1540695006.5.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ll="118371"; ue="dh2531@foxmail.com"; __yadk_uid=QcQlpvBHlmkCTpOBgnruTmC12iejRXff; _vwo_uuid_v2=DE4D18E5F668BE348D47B8B20A38232CE|3d6afdcc96b66b75470d540589f1b16c; __utmv=30149280.18646; ct=y; __utmc=30149280; __utmc=223695111; as="https://www.douban.com/accounts/safety/locked"; dbcl2="186463708:IeumDYsLfdE"; ck=UWUV; douban-profile-remind=1; _pk_id.100001.4cf6=f45ec8cc131dc4f1.1540563407.12.1540822571.1540817989.; __utma=30149280.24434663.1538293737.1540816764.1540822571.13; __utma=223695111.977060243.1540563407.1540816764.1540822571.12'  # 抓包获取
        self.cookies =  {i.split('=')[0]: i.split('=')[1] for i in cookies_str.split('; ')}


    def request(self,url):
        r = requests.get(url, headers=self.headers, cookies=self.cookies)
        if (r.status_code == 200):
            time.sleep(1);
            soup = BeautifulSoup(r.text, 'lxml')
            items = soup.find_all(attrs={'class':'comment-item'})
            for item in items:
                username = item.a['title']
                #print(username)
                try:
                    stars = item.find_all('span', attrs={'title': '推荐'}).__str__()
                    stars = int(int(re.findall(r'\d+', stars)[0]) / 10)
                except:
                    stars = 0
                date = item.find('span', attrs={'class': 'comment-time '}).string
                date = re.sub(r'\s', '', date)
                valid_num = item.find('span', attrs={'class': 'votes'}).string
                movie_review = item.find('span', attrs={'class': 'short'}).string

                # 测试保存
                review = Review(username=username, stars=stars, date=date, valid_num=valid_num,
                                movie_review=movie_review)
                review.save();
                self.i += 1
                print('处理了%s个' % self.i)
                review = None
        r.close();

class Review(object):
    def __init__(self, username, stars, date, valid_num, movie_review):
        self.username = username;
        self.stars = stars;
        self.date = date;
        self.valid_num = valid_num;
        self.movie_review = movie_review;

    def save(self):
        self.f = open("yichuhaoxi-yingping.json", "a+", encoding='utf-8')  # 路径一定要写对
        #self.f.write(self)
        #print('line',self.toString())
        json.dump(self.toString(),self.f,ensure_ascii=False)
        self.f.write(',')
        self.f.close();

    def toString(self):
        return {
            "username" : self.username,
            "stars": self.stars,
            "date": self.date,
            "valid_num": self.valid_num,
            "movie_review": self.movie_review,
        }


if __name__=="__main__":
    # 左闭右开 0-200 200-400 400-5{}
    # 500看过
    # "https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start={}&type=T".format(n) for n in range(0,500,20)
    # 500想看
    # "https://movie.douban.com/subject/26985127/comments?limit=20&sort=new_score&status=F&start={}".format(n) for n in range(0,500,20)
    start_urls = [
        "https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start={}&type=T".format(n) for n in range(0,500,20)
    ]

    doubanreview = DoubanMovieReview('一出好戏')
    for start_url in start_urls:
        doubanreview.request(start_url);






