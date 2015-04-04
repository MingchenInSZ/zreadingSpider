# -*- coding: utf-8 -*-

# Scrapy settings for shipu project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'shipu'


ITEM_PIPELINES = ['shipu.pipelines.MongoPipeline']

MONGO_SERVER = "localhost" #set the mongodb_url
MONGO_PORT = 27017 #the default port of mongodb
MONGO_DB = "foobar" # set the db to use
MONGO_COLLECTION="zreading"  #set the collection name
SPIDER_MODULES = ['shipu.spiders']
NEWSPIDER_MODULE = 'shipu.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'shipu (+http://www.yourdomain.com)'
