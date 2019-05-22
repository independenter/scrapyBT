# -*- coding: utf-8 -*-

# Scrapy settings for Scrapy58Userinfo project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Scrapy58Userinfo'

SPIDER_MODULES = ['Scrapy58Userinfo.spiders']
NEWSPIDER_MODULE = 'Scrapy58Userinfo.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Scrapy58Userinfo (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# 配置mongoDB
MONGO_HOST = "127.0.0.1"  # 主机IP
MONGO_PORT = 27017  # 端口号
MONGO_DB = "samecity58"  # 库名
MONGO_COLL = "haikou"  # collection

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'Scrapy58Userinfo.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'Scrapy58Userinfo.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
DOWNLOADER_MIDDLEWARES = {
   #'tutorial.middlewares.MyCustomDownloaderMiddleware': 543,
    #'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware':123,
    'Scrapy58Userinfo.middlewares.IPPOOlS' : 3,
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': 2,
    'Scrapy58Userinfo.uamid.Uamid': 1
}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   #'tutorial.pipelines.SomePipeline': 300,
    'Scrapy58Userinfo.pipelines.Get58Mongo': 300,
    'Scrapy58Userinfo.pipelines.JsonWritePipline': 300
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
IPPOOL = [{"http": "103.233.123.209:60080"},{"http": "103.106.148.207:40590"},{"http": "103.90.200.10:58124"},{"http": "103.194.88.57:38327"},{"http": "103.194.88.57:38327"},{"http": "103.90.200.29:59125"},{"http": "103.231.33.180:42297"},{"http": "103.79.228.238:50825"},{"http": "185.61.94.65:45215"},{"http": "112.247.176.5:8060"},{"http": "39.137.141.11:8080"},{"http": "39.137.141.14:80"},{"http": "39.137.140.83:80"},{"http": "39.137.140.14:80"},{"http": "39.137.140.87:80"},{"http": "39.137.139.21:80"},{"http": "39.137.139.28:80"},{"http": "39.137.140.18:80"},{"http": "39.137.141.12:8080"},{"http": "39.137.140.16:80"},{"http": "39.137.140.20:80"},{"http": "39.137.140.81:80"},{"http": "39.137.140.19:80"},{"http": "39.137.140.25:80"},{"http": "39.137.140.143:80"},{"http": "104.248.174.177:80"},{"http": "39.137.140.23:80"},{"http": "39.137.140.148:80"},{"http": "39.137.141.17:8080"},{"http": "39.137.139.24:80"},{"http": "39.137.139.26:80"},{"http": "39.137.140.22:80"},{"http": "60.217.139.209:8060"},{"http": "60.217.156.204:8060"},{"http": "183.230.177.116:8060"},{"http": "221.223.91.178:8060"},{"http": "169.239.123.69:44801"},{"http": "170.82.48.55:45505"},{"http": "183.230.162.20:8060"},{"http": "180.167.29.116:80"},{"http": "183.230.204.30:8060"},{"http": "155.93.112.118:34873"},{"http": "36.106.209.1:9999"},{"http": "60.190.137.194:46194"},{"http": "60.190.137.194:46194"},{"http": "41.215.246.168:37902"},{"http": "221.223.85.91:8060"},{"http": "49.76.65.62:8060"},{"http": "222.182.188.34:8060"},{"http": "197.231.255.207:60587"},{"http": "183.230.175.93:8060"},{"http": "27.208.225.195:8060"},{"http": "119.180.132.3:8060"},{"http": "60.217.159.166:8060"},{"http": "115.206.195.47:8060"},{"http": "119.180.172.92:8060"},{"http": "114.95.164.62:8060"},{"http": "114.55.43.83:9999"},{"http": "103.49.59.209:50598"},{"http": "115.206.110.31:8060"},{"http": "111.200.239.46:8080"},{"http": "103.206.103.221:23500"},{"http": "103.78.143.186:47085"},{"http": "115.223.232.38:8060"},{"http": "222.162.247.99:80"},{"http": "183.230.177.121:8060"},{"http": "111.165.99.58:8060"},{"http": "114.234.69.201:8060"},{"http": "103.193.254.194:51725"},{"http": "103.58.72.176:80"},{"http": "218.58.193.37:8060"},{"http": "222.173.90.162:8060"},{"http": "114.245.180.26:8060"},{"http": "119.179.141.82:8060"},{"http": "114.244.84.19:8060"},{"http": "183.230.179.164:8060"},{"http": "115.153.146.79:8060"},{"http": "116.238.176.204:8060"},{"http": "119.190.196.203:8060"},{"http": "60.217.154.190:8060"},{"http": "218.56.124.137:8060"},{"http": "111.200.239.40:8080"},{"http": "119.190.189.8:8060"},{"http": "119.180.143.128:8060"},{"http": "119.180.142.223:8060"},{"http": "119.180.175.147:8060"},{"http": "60.217.156.0:8060"},{"http": "112.247.205.208:8060"},{"http": "112.247.204.224:8060"},{"http": "60.217.140.86:8060"},{"http": "119.180.128.249:8060"},{"http": "60.217.143.20:8060"},{"http": "119.190.196.136:8060"},{"http": "27.208.225.176:8060"},{"http": "60.212.181.175:8060"},{"http": "60.217.156.66:8060"},{"http": "60.217.154.119:8060"},{"http": "119.180.130.226:8060"},{"http": "119.179.176.161:8060"},{"http": "119.180.136.243:8060"}]
# 设置用户代理池
UPPOOL = [
"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"
]