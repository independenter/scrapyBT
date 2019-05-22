# Author:donghui

from scrapy import cmdline
#scrapy crawl getTuniu --nolog
cmdline.execute("scrapy crawl getTuniu".split())
#cmdline.execute("scrapy crawl getTuniu --nolog".split())