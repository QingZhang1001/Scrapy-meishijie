# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XiachufangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #dish_name = scrapy.Field()
    dish_url = scrapy.Field()
    dish_id = scrapy.Field()
    img_url = scrapy.Field()
    score = scrapy.Field()
    #ingredient = scrapy.Field()


