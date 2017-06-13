# -*- coding: utf-8 -*-
import scrapy


class ZhSpider(scrapy.Spider):
    name = 'zh'
    allowed_domains = ['zhihu.com']
    start_urls = ['http://zhihu.com/']

    def parse(self, response):
        pass
