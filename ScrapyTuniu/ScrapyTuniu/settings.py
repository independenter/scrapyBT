# -*- coding: utf-8 -*-

# Scrapy settings for ScrapyTuniu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'ScrapyTuniu'

SPIDER_MODULES = ['ScrapyTuniu.spiders']
NEWSPIDER_MODULE = 'ScrapyTuniu.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ScrapyTuniu (+http://www.yourdomain.com)'

# Obey robots.txt rules
#ROBOTSTXT_OBEY = True

HTTPERROR_ALLOWED_CODES = [404]


# 配置mongoDB
MONGO_HOST = "127.0.0.1"  # 主机IP
MONGO_PORT = 27017  # 端口号
MONGO_DB = "tuniu"  # 库名
MONGO_COLL = "taiguo"  # collection

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1  #下载间隔
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED是注释的时候scrapy默认没有开启cookie
#当COOKIES_ENABLED没有注释设置为False的时候scrapy默认使用了settings里面的cookie
#当COOKIES_ENABLED设置为True的时候scrapy就会把settings的cookie关掉，使用自定义cookie
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept':'*/*',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.9',
               'Connection': 'keep-alive',
               'Cookie': 'Hm_lvt_19f9e31a97c820b0081af5bccd6bb217=1540695217,1540695273,1540695273,1540695273',
               'Host': '45.126.123.80:118',
               'Referer': "http://s.tuniu.com/search_complex/whole-nj-0-%E6%B3%B0%E5%9B%BD/20",
               'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
               }


# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'ScrapyTuniu.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'ScrapyTuniu.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
DOWNLOADER_MIDDLEWARES = {
   #'tutorial.middlewares.MyCustomDownloaderMiddleware': 543,
    #关闭IP代理，豆瓣会进行封号
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware':123,
    'ScrapyTuniu.middlewares.IPPOOlS' : 3,
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': 2,
    'ScrapyTuniu.uamid.Uamid': 1
}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   #'tutorial.pipelines.SomePipeline': 300,
   # 预留MongoDB存储类
    'ScrapyTuniu.pipelines.GetDoubanMongo': 300,
   #'ScrapyTuniu.pipelines.JsonWritePipline': 300
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
IPPOOL = [{'http': '180.175.150.228:8060'}, {'http': '138.186.72.151:53281'}]
# 设置用户代理池
UPPOOL = [
"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"
]