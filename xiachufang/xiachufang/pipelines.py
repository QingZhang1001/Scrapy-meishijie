# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
import json
import codecs
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
import pymongo

client = pymongo.MongoClient('localhost',27017)
xiachufang= client['xiachufang']
dishes = xiachufang['dishes']

class JsonWithEncodingPipeline(object):

    def __init__(self):
        self.file=codecs.open('food.json','w',encoding='utf-8')

    def process_item(self,item,spider):
        line = json.dumps(dict(item),ensure_ascii=False) + '\n'
        self.file.write(line)
        return item

    def spider_closed(self,spider):
        self.file.close()



class XiachufangPipeline(object):
    def process_item(self, item, spider):

        #conn = pymysql.connect(host='127.0.0.1',user='root',passwd='7714066',db='xiachufang')


        #dish_name = item['dish_name']
        dish_url = item['dish_url']
        dish_id = item['dish_id']
        img_url = item['img_url']
        score = item['score']
        #ingredient = item['ingredient']

        dishes.insert_one({"dish_url":dish_url,
                           "dish_id":dish_id,
                           "img_url":img_url,
                           "score":score})
        return item



