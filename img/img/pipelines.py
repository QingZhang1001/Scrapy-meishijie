# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import re
import os
import urllib
import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request
import json
import codecs

from img import settings

class JsonWithEncodingPipeline(object):

    def __init__(self):
        self.file=codecs.open('meishijie.json','w',encoding='utf-8')

    def process_item(self,item,spider):
        line = json.dumps(dict(item),ensure_ascii=False) + '\n'
        self.file.write(line)
        return item

    def spider_closed(self,spider):
        self.file.close()


class ImgPipeline(ImagesPipeline):
    def get_media_request(self,item,info):
        for img_url in item['image_urls']:
            yield Request(img_url,meta={'item':item,'index':item['image_urls'].index(img_url)})


    def file_path(self, request, response=None, info=None):
        item = request.meta['item']  # 通过上面的meta传递过来item
        index = request.meta['index']  # 通过上面的index传递过来列表中当前下载图片的下标

        folder_name=item['cuisine_names']
        image_guid = item['image_names'][index] +'.'+request.url.split('/')[-1].split('.')[-1]

        filename = u'full/{0}/{1}'.format(folder_name,image_guid)
        return filename

'''
    def item_completed(self,results,item,info):


        image_paths = [x['path'] for ok,x in results if ok]
        if not image_paths:
            raise DropItem('Item contains no images')
        #item['image_paths'] = image_paths
        return item
'''






