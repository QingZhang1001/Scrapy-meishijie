# -*- coding: utf-8 -*-
import scrapy
import re
from ..items import ImgItem

class MeishijieSpider(scrapy.Spider):
    name = "meishijie"
    allowed_domains = ["meishij.net"]
    start_urls = ['https://www.meishij.net/china-food/caixi/']


    def parse(self, response):
        cuisine_list=response.xpath('//dl[@class="listnav_dl_style1 w990 clearfix"]//dd/a/@href').extract()
        # extract the link of each cuisine
        #print(len(link_list)) # the amount of the cuicines
        for cuisine_url in cuisine_list:
            #print(cuisine_url)
            yield scrapy.Request(cuisine_url,callback=self.parse_cuisine_img)


    def parse_cuisine_img(self,response):

        item=ImgItem()
        item['image_urls'] = response.xpath('//img[@class="img"]//@src').extract()
        item['image_names'] = response.xpath('//div[@class="c1"]//strong//text()').extract()
        #print(len(item['image_urls']))


        # get the url of the next page
        next_link=response.xpath('//div[@class="listtyle1_page"]//a[@class="next"]//@href').extract()
        split_name=re.split('/',next_link[0])
        cuisine=split_name[-2]  # get the name of each cuisine
        item['cuisine_names']=cuisine
        #print(item['cuisine_names'])
        #print(item['image_names'])
        #print(item['image_urls'])
        #print(item['cuisine_names'])


        yield item




        if next_link:
            next_link = next_link[0]
            #print(next_link)
            yield scrapy.Request(next_link,callback=self.parse_cuisine_img)




















