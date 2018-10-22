# -*- coding: utf-8 -*-
import scrapy
from..items import XiachufangItem
from scrapy.selector import Selector
import re


class FoodSpider(scrapy.Spider):
    name = "food"
    allowed_domains = ["xiachufang.com"]
    start_urls = ['http://xiachufang.com/category']



    def parse(self, response):
        categories_links = response.xpath('//div[@class="cates-list-all clearfix hidden"]//ul[@class=" has-bottom-border"]//li//a//@href').extract()
        for cate_link in categories_links:
            cate_link=response.urljoin(cate_link)
            #print(len(cate_link))
            yield scrapy.Request(cate_link,callback=self.parse_food_info)

    def parse_food_info(self, response):
        next_link = response.xpath('//div[@class="pager"]/a[@class="next"]/@href').extract()
        if next_link:
            next_link = next_link[0]
            next_link=response.urljoin(next_link)
            #print(next_link)
            yield scrapy.Request(next_link,callback=self.parse_food_info)


        recipes = response.xpath("//div[@class='normal-recipe-list']/ul/li").extract()
        for recipe in recipes:
            sel = Selector(text=recipe)
            item =  XiachufangItem()
            #item['dish_name'] = sel.xpath("//p[@class='name']/text()").extract_first
            item['dish_url'] = sel.xpath('//a[1]/@href').extract_first()
            item['dish_id'] = re.compile('/recipe/(.*?)/').findall(item['dish_url'])[0]
            item['img_url'] = sel.xpath('//div[@class="cover pure-u"]/img/@data-src').extract_first()
            score=sel.xpath("//p[@class='stats']/span[@class='score bold green-font']").extract_first()
            item['score'] = sel.xpath("//p[@class='stats']/span[@class='score bold green-font']/text()").extract_first()

            #item['ingredient'] = sel.xpath('//p[@class="ing ellipsis"]/text()').extract_first()
            if item['img_url'] is None or score is None:
                pass
            else:
                yield item





















