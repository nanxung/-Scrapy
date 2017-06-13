# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field

class ZhihuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class UserItem(scrapy.Item):
    """
    知乎用户的用户名，居住地，所在行业，职业经历，教育经历，个人简介
    """
    Id=Field()
    Url=Field()
    Nick_name=Field()
    Home_Position=Field()
    Compmany=Field()
    Edu=Field()
    Content=Field()