# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.selector import Selector
from Scrapy_VNExpress.items import ScrapyVnexpressItem

class VnexpressSpider(Spider):
    name = 'vnexpress'
    allowed_domains = ['vnexpress.net']
    start_urls = ['https://vnexpress.net/tin-tuc/the-gioi']

    def parse(self, response):
        tintucs = Selector(response).xpath('//section[@class="sidebar_1"]/article[@class="list_news"]')
        
        for tintuc in tintucs:
            item = ScrapyVnexpressItem()
            item['title'] = tintuc.xpath(
                'h3[@class="title_news"]/a[1]/text()').extract()[0]
            item['url'] = tintuc.xpath(
                'h3[@class="title_news"]/a[1]/@href').extract()[0]
            yield item

