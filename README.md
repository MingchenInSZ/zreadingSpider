# zreadingSpider
  This project uses scrapy to crawl all the aticle information from www.zreading.cn. 
And save all the data into local mongo db.
 
  This project is a eclipse pyDev project. It uses Scrapy(http://scrapy.org),which is an efficient spider, to extract
all the article information from www.zreading.cn,including article title,link,post_date,subcategory,tags ang even the
reads information. And all the detail data are saved to local mongo database.
  
  User can change the extract target in spider file(such as shipu/spider/shipuSpider.py), and change the fields in items
accordingly.
  During crawling, all the extracted item are pipedlined into local database(here refer to mongo), and all the db information
are set in setting file:

    MONGO_SERVER = "localhost" #set the mongodb_url,here use localhost
    MONGO_PORT = port_number #the default port of mongodb is 27017
    MONGO_DB = db_name # set the db to use
    MONGO_COLLECTION="zreading"  #set the collection name
    
  Scrapy uses cmdline mode to run the spider:
  
      scrapy crawl zreading.cn 
    
  Or:
       
      scrapy.cmdline.execute("scrapy crawl zreading.cn".split())
  
  from python file.
     
     
  Enjoy your journey!
                                                                                      Author: minghchen
                                                                                      contact: mingchen0710@126.com
     
  

