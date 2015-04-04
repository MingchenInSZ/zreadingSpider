# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings
class MongoPipeline(object):
    '''
    Initialize all the connection parameters, including 
       server:MONGO_SERVER
       port:MONGO_PORT
       db:MONGO_DB
       collection:MONGO_COLLECTION
    '''
    def __init__(self):
        self.mongo_server = settings["MONGO_SERVER"]
        self.mongo_db = settings["MONGO_DB"]
        self.mongo_port = settings["MONGO_PORT"]
        self.collection = settings["MONGO_COLLECTION"]
        
        
    '''
    Insert the item to mongodb specified by server:port,db and collection name
    '''    
    def process_item(self, item, spider):
        self.db[self.collection].insert(dict(item))
        return item
    
    '''
    when the spider opens, these codes runs
    '''
    def open_spider(self,spider):
        self.client = pymongo.Connection(self.mongo_server,self.mongo_port)
        self.db = self.client[self.mongo_db]
    '''
    Close the connection
    '''
    def close_spider(self,spider):
        self.client.close()
   