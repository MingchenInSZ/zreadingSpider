# -*- coding: UTF-8 -*-
'''
This is the spider
'''

from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector,Selector
from pyquery import PyQuery as pq
from shipu.items import ZreadingItem
import re

class shipuSpider(CrawlSpider):
    name = "zreading.cn"
    allowed_domains = ["zreading.cn"]
    start_urls = ["http://www.zreading.cn/"]
    rules = [
#              Rule(LinkExtractor(allow=[r'/archives/\d+\.html$']),follow=False,callback='parse_content'),
             Rule(LinkExtractor(allow=[r'/page/\d+$']),follow=True,callback='parse_category')

             ]

    def parse_content(self,response):
        sel = Selector(response)
        print repr(response)

    def parse_category(self,response):
        sel = Selector(response)#/html/body/div[1]/div[3]/div[1]/article[3]/header/h2/a
        header = sel.xpath("//div[@id='content']/article/header/h2/a").extract()
        titles = [pq(head).attr("title") for head in header]
        hrefs = [pq(head).attr("href") for head in header]
        desc = sel.xpath("//div[@id='content']/article/address/span").extract()
        dates = [pq(desc[3*i])("span").text() for i in range(len(desc)/3)]
        posts = [pq(desc[3*i+1])("span").text() for i in range(len(desc)/3)]
        reads = [pq(desc[3*i+2])("span").text() for i in range(len(desc)/3)]
        reads = [re.findall(r"\d+",read.replace(",",""))[0] for read in reads]
        #/html/body/div[1]/div[3]/div[1]/article[10]/address/a[2]
        others = sel.xpath("//div[@id='content']/article/address/a").extract()
        subcates,tags ,st,insert= [],[],"",False
        for o in others:
            query = pq(o).attr("href")
            if "tag" not in query:
                if not insert:
                    subcates.append(pq(o)("a").text())
                else:
                    subcates.append(",".join([subcates.pop(),pq(o)("a").text()]))
                insert = True
                if st!="":
                    tags.append(st)
                st = ""
            else:
                st += "+"+pq(o)("a").text()
                insert = False
        tags.append(st)
        #/html/body/div[1]/div[3]/div[1]/article[1]/div
        contents = sel.xpath("//div[@id='content']/article/div").extract()
        contents = [pq(content)("div").text() for content in contents]
#         print len(titles),len(hrefs),len(dates),len(reads),len(posts),len(tags),len(subcates),len(contents)
    
        for i in range(len(titles)):
            return self.processItem(titles, contents, hrefs, posts, subcates, tags, reads, dates,i)
#         return self.processItem(titles, contents, hrefs, posts, subcates, tags, reads, dates,0)
    
    def processItem(self,titles,abstracts,links,posts,subcates,tags,reads,dates,i):
        item = ZreadingItem()
        item["title"] = titles[i]
        item["abstract"] = abstracts[i]
        item["link"] = links[i]
        item["post"] = posts[i]
        item["subcate"] = subcates[i]
        item["tags"] = tags[i]
        item["reads"] = reads[i]
        item["date"] = dates[i]
        return item
            
            
            
            
            
            
            