#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Dob

from bs4 import BeautifulSoup
html_doc = """
<div class="comment-item" data-cid="1430401603">
<div class="avatar">
<a href="https://www.douban.com/people/kulilin/" title="kulilin">
<img class="" src="https://img3.doubanio.com/icon/u1386944-25.jpg"/>
</a>
</div>
<div class="comment">
<h3>
<span class="comment-vote">
<span class="votes">1719</span>
<input type="hidden" value="1430401603"/>
<a class="j a_show_login" href="javascript:;" onclick="">有用</a>
</span>
<span class="comment-info">
<a class="" href="https://www.douban.com/people/kulilin/">kulilin</a>
<span>看过</span>
<span class="allstar40 rating" title="推荐">2</span>
<span class="comment-time " title="2018-08-08 23:31:08">
                    2018-08-08
                </span>
</span>
</h3>
<p class="">
<span class="short">黄渤是有追求的导演，之前真没敢报期望。中国式反乌托邦，以为会是麻花式的喜剧，会在老本行上偷懒，但远远挖掘了更深层次的东西，这对于处女作来说实属不易。体制内无法呈现的阴暗面，以巧妙的抉择呈现，效果惊艳。美术、音乐以及表演掌控自如，恭喜黄渤！</span>
</p>
</div>
</div>
"""

from bs4 import BeautifulSoup#导入BeautifulSoup的方法
import re
#可以传入一段字符串，或者传入一个文件句柄。一般都会先用requests库获取网页内容，然后使用soup解析。
soup=BeautifulSoup(html_doc,'lxml')#这里一定要指定解析器，可以使用默认的html，也可以使用lxml比较快。
#print(soup.prettify())#按照标准的缩进格式输出获取的soup内容。
# stars=soup.find_all('span',attrs={'title':'推荐'}).__str__()
# print(int(int(re.findall(r'\d+', stars)[0])/10))
# for a in a_list:
#     print(a.attrs['class'])

print(soup.find('span',attrs={'class':'votes'}).string)

#print(soup.select('[title~=推荐]'))
#print(soup.select('[title~=推荐]'))
#textlist=soup.select('[title~=推荐]')
# for t in textlist:
#     print (t) #获取单条html信息
#     print (t.get_text()) #获取中间文字信息

#几种简单浏览结构化数据的方法：
# print(soup.title)#获取文档的title
# print(soup.title.name)#获取title的name属性
# print(soup.title.string)#获取title的内容
# print(soup.title.parent.name)#获取title的parent名称,也就是head,上一级.
# print(soup.p)#获取文档中第一个p节点
# print(soup.p['class'])#获取第一个p节点的class内容
# print(soup.a)#获取文档的第一个a节点
# print(soup.find_all('a'))#获取文档中所有的a节点,返回一个list
# soup.find(id='link3')#获取文档中id属性为link3的节点

# import requests
# r = requests.get('https://movie.douban.com/subject/26985127/comments?limit=20&sort=new_score&status=P&start=0')
# soup = BeautifulSoup(r.text, 'html.parser')
# print(soup)
# print("========================")
# print(soup.find(id="comments"))
# r.close()

# soup.select('title')#选择title标签
# soup.select('p nth-of-type(3)')
#
# #通过tag标签逐层查找
# soup.select('body a')#查找body标签下面的a标签
# #找到某个tag标签下的直接子标签：
# soup.select('head>title')
# #通过id来查找：
# soup.select('#link1')
# #通过class来查找：
# soup.select('.sister')
# soup.select('[class~=sister]')
# #通过是否存在某个属性来查找：
# soup.select('a[href]')
# #通过属性的值来查找：
import requests
# soup.select('a[href="http://www.baidu.com"]')
result = requests.get('https://twitter.com/', proxies={'http': '64.15.69.126:8080'})
print(result.status_code)
print(result.text)