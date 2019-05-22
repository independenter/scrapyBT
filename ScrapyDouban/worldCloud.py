#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Dob

import warnings  # 防止出现future warning
warnings.filterwarnings("ignore")
import pymysql,re,jieba,matplotlib,os
import pandas as pd
import numpy as np
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator # 用于生成词云
import matplotlib.pyplot as plt

#pip --default-timeout=100 install wordcloud matplotlib pandas jieba

db = pymysql.connect("localhost", "root", "123456", "test")
cursor = db.cursor()
# 使用 execute()  方法执行 SQL 查询
cursor.execute("select movie_review from review")
comments = cursor.fetchall()
# 关闭数据库连接
db.close()
'''clean comments'''
allComment = ''
for item in comments:
     allComment = allComment + item[0].strip()

# 至少匹配一个汉字,两个unicode值正好是Unicode表中的汉字的头和尾。
pattern = re.compile(r'[\u4e00-\u9fa5]+')
finalComment = ''.join(re.findall(pattern, allComment))

#切词
segment = jieba.lcut(finalComment)
words_df = pd.DataFrame({'segment': segment})

'''删除无关词语'''
# stopwords = pd.read_csv("chineseStopwords",sep=",",names=['stopword'], encoding='utf8')
# print(stopwords.stopword)
words_df = words_df[~words_df.segment.isin(["你","我","他","的","一"])]

'''获得词频'''
words_fre = words_df.groupby(by='segment')['segment'].agg({'count': np.size})
words_fre = words_fre.reset_index().sort_values(by='count', ascending=False)

#print(words_fre)

'''生成词云'''
matplotlib.rcParams['figure.figsize'] = [10.0, 5.0]
wordcloud = WordCloud(
    font_path='earther.ttf',#C:\Windows\Fonts\STZHONGS.TTF 这个不会带拼音
    background_color='black',
    stopwords=STOPWORDS,
    max_font_size=80,# 设置字体最大值
    random_state=30# 设置有多少种随机生成状态，即有多少种配色方案

)
word_fre_dic = {x[0]: x[1] for x in words_fre.values}
wordcloud = wordcloud.fit_words(word_fre_dic)
# 是否显示x轴、y轴下标
plt.axis('off')
plt.imshow(wordcloud)

# 获得模块所在的路径的
d = os.path.dirname(__file__)
# os.path.join()：  将多个路径组合后返回
wordcloud.to_file(os.path.join(d, "一出好戏-词云.jpg"))

plt.show()

