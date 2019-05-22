# Author:donghui

from scrapy import cmdline
#scrapy crawl getDouban --nolog
cmdline.execute("scrapy crawl getDouban".split())
#cmdline.execute("scrapy crawl getDouban --nolog".split())