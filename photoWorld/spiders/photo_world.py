# -*- coding: utf-8 -*-
import scrapy
from photoWorld.items import PhotoworldItem
from photoWorld.utils.get_base_html import get_base_page


class PhotoWorldSpider(scrapy.Spider):
    name = 'photo-world'
    allowed_domains = ['photoworld.com.cn/']
    start_urls = [get_base_page()]

    def parse(self, response):
        #items = []
        # with open('photo.html', "w")as f:
        #     f.write(response.text)
        for each in response.xpath("//div[@id='home-main']/article"):
            #print(each)
            item = PhotoworldItem()
            url = each.xpath("h3/a/@href").get()
            title = each.xpath("h3/a/@title").get()
            label = each.xpath("p/a/text()").get()
            images = []
            for image_items in each.xpath("div[1]/a"):
                image = image_items.xpath("img/@src").get()
                images.append(image)
            author = each.xpath("aside/span[2]/a/text()").get()
            description = each.xpath("div/div[2]/p[2]/text()").get()
            item["url"] = url
            item['title'] = title
            item['label'] = label
            item['images'] = images
            item['author'] = author
            item['description'] = description
            #items.append(item)
            yield  item
        for i in range(2):
            get_base_page(i+2)
            yield scrapy.Request(get_base_page(i+2),callback=self.parse)





            



