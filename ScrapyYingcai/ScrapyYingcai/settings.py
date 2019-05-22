# -*- coding: utf-8 -*-

# Scrapy settings for ScrapyYingcai project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'ScrapyYingcai'

SPIDER_MODULES = ['ScrapyYingcai.spiders']
NEWSPIDER_MODULE = 'ScrapyYingcai.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ScrapyYingcai (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

HTTPERROR_ALLOWED_CODES = [404]


# 配置mongoDB
MONGO_HOST = "127.0.0.1"  # 主机IP
MONGO_PORT = 27017  # 端口号
MONGO_DB = "yingcai"  # 库名
MONGO_COLL = "python"  # collection

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.25  #下载间隔
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED是注释的时候scrapy默认没有开启cookie
#当COOKIES_ENABLED没有注释设置为False的时候scrapy默认使用了settings里面的cookie
#当COOKIES_ENABLED设置为True的时候scrapy就会把settings的cookie关掉，使用自定义cookie
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#                'Accept-Encoding': 'gzip, deflate, br',
#                'Accept-Language': 'zh-CN,zh;q=0.9',
#                'Connection': 'keep-alive',
#                'Cookie': 'bid=2g-CWSYSi-0; douban-fav-remind=1; __yadk_uid=785kNB1yjnf9bvU81sPYXQv7t4KkdMVE; ps=y; push_noty_num=0; push_doumail_num=0; __utmz=30149280.1540695006.5.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ll="118371"; ue="dh2531@foxmail.com"; _vwo_uuid_v2=DE4D18E5F668BE348D47B8B20A38232CE|3d6afdcc96b66b75470d540589f1b16c; __utmc=30149280; ap_v=0,6.0; __utma=30149280.24434663.1538293737.1540702888.1540711835.7; __utmt=1; dbcl2="186463708:f2cdGKsdfMU"; ck=kdGH; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1540712248%2C%22https%3A%2F%2Faccounts.douban.com%2Flogin%3Fredir%3Dhttps%3A%2F%2Faccounts.douban.com%2Fsafety%2Funlock_sms%2Fcaptcha%3Fconfirmation%3Dd2b4fe429ed680d2%26alias%3Ddh2531%2540foxmail.com%26source%3DNone%26login_type%3Dsms%22%5D; _pk_id.100001.8cb4=a69bc73b07a036fc.1538293736.4.1540712248.1540695029.; _pk_ses.100001.8cb4=*; __utmv=30149280.18646; __utmb=30149280.3.10.1540711835',
#                'Host': 'movie.douban.com',
#                'Referer': "https://movie.douban.com/subject/26985127/comments?start=240&limit=20&sort=new_score&status=P",
#                'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
#                'X-Requested-With': 'XMLHttpRequest'
#                }


# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'ScrapyYingcai.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'ScrapyYingcai.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
DOWNLOADER_MIDDLEWARES = {
   #'tutorial.middlewares.MyCustomDownloaderMiddleware': 543,
    #关闭IP代理，豆瓣会进行封号
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware':123,
    'ScrapyYingcai.middlewares.IPPOOlS' : 3,
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': 2,
    'ScrapyYingcai.uamid.Uamid': 1
}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   #'tutorial.pipelines.SomePipeline': 300,
   # 预留MongoDB存储类
    'ScrapyYingcai.pipelines.GetDoubanMongo': 300,
   #'ScrapyYingcai.pipelines.JsonWritePipline': 300
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

#0 从配置文件拿 1 从代理json文件拿
IPPoolMode=0

# 设置IP池
IPPOOL = [{"http": "197.231.253.87:54840"},{"http": "213.163.104.65:46841"},{"http": "221.223.85.208:8060"},{"http": "103.92.153.219:60401"},{"http": "114.94.10.232:43376"},{"http": "123.117.169.112:8060"},{"http": "131.108.63.5:42128"},{"http": "116.196.99.217:9999"},{"http": "113.107.173.92:44045"},{"http": "103.106.101.17:40969"},{"http": "223.167.15.119:8060"},{"http": "223.100.166.3:36945"},{"http": "38.99.117.103:61064"},{"http": "128.201.92.25:53281"},{"http": "116.196.99.216:9999"},{"http": "115.46.103.130:8123"},{"http": "119.190.201.161:8060"},{"http": "118.250.1.222:8060"},{"http": "123.115.128.226:8060"},{"http": "122.115.78.240:41250"},{"http": "129.205.194.170:52866"},{"http": "164.160.127.110:41906"},{"http": "103.255.234.161:39847"},{"http": "175.9.179.159:8060"},{"http": "124.89.162.134:8060"},{"http": "119.180.157.146:8060"},{"http": "38.99.117.43:47894"},{"http": "105.235.203.182:61271"},{"http": "170.79.91.227:40968"},{"http": "102.164.248.31:59400"},{"http": "213.32.252.132:51615"},{"http": "123.123.255.8:8060"},{"http": "45.236.107.226:36400"},{"http": "138.185.166.112:23500"},{"http": "123.115.130.249:8060"},{"http": "157.119.225.79:60068"},{"http": "114.95.165.75:8060"},{"http": "183.230.180.45:8060"},{"http": "36.7.128.146:44473"},{"http": "114.217.3.178:808"},{"http": "119.179.130.38:8060"},{"http": "185.255.88.41:48418"},{"http": "123.123.253.61:8090"},{"http": "168.197.114.6:38962"},{"http": "113.121.243.43:49327"},{"http": "101.26.114.142:8060"},{"http": "169.255.10.174:57917"},{"http": "124.225.144.224:8060"},{"http": "143.202.72.5:47471"},{"http": "119.180.153.35:8060"},{"http": "119.180.141.188:8060"},{"http": "169.255.10.126:30310"},{"http": "111.72.141.87:8060"},{"http": "144.0.79.94:8060"},{"http": "185.52.1.89:3128"},{"http": "119.190.190.180:8060"},{"http": "115.223.72.228:8060"},{"http": "137.59.3.6:41409"},{"http": "222.91.126.166:8060"},{"http": "103.87.169.217:53159"},{"http": "118.143.37.170:35886"},{"http": "123.123.7.194:8060"},{"http": "103.215.157.125:49121"},{"http": "138.204.233.120:57754"},{"http": "58.214.186.30:8060"},{"http": "122.112.229.214:1080"},{"http": "103.102.236.161:53281"},{"http": "103.102.236.129:53281"},{"http": "103.106.101.24:40969"},{"http": "124.89.161.28:8060"},{"http": "164.163.250.22:42213"},{"http": "124.127.69.60:8060"},{"http": "116.196.70.122:9999"},{"http": "103.197.32.198:33554"},{"http": "183.45.88.109:56851"},{"http": "123.115.80.225:8060"},{"http": "103.92.213.17:59404"},{"http": "103.92.213.17:59404"},{"http": "129.205.195.49:52866"},{"http": "103.80.118.166:44234"},{"http": "103.217.154.197:23500"},{"http": "103.108.96.187:51112"},{"http": "222.208.208.110:8060"},{"http": "38.99.117.236:35179"},{"http": "112.246.233.86:8060"},{"http": "138.185.166.212:23500"},{"http": "119.180.128.5:8060"},{"http": "112.247.200.196:8060"},{"http": "27.208.191.95:8060"},{"http": "119.179.136.70:8060"},{"http": "103.43.16.179:808"},{"http": "122.116.222.171:54486"},{"http": "183.196.97.125:41397"},{"http": "114.248.87.82:8060"},{"http": "143.202.73.186:47290"},{"http": "138.97.145.157:38797"},{"http": "180.97.192.16:8888"},{"http": "171.37.152.239:8123"},{"http": "171.38.39.21:8123"},{"http": "123.117.177.180:8060"}]
# 设置用户代理池
UPPOOL = [
"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"
]