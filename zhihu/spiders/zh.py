# -*- coding: utf-8 -*-
import scrapy
from zhihu.items import *
import re
class ZhSpider(scrapy.Spider):
    name = 'zh'
    allowed_domains = ['zhihu.com']
    start_urls = ['http://zhihu.com/']
    url='http://www.zhihu.com/'
    start_urls=['ruan-fu-zhong-tong-zhi','mu-huan-98']
    task_set=set(start_urls)
    tasked_set=set()


    def start_requests(self):
        while len(self.task_set)>0:
            id=self.task_set.pop()
            if id in self.task_set:
                raise CloseSpider(reason="已经存在的数据 %s" %(id))
            self.tasked_set.add(id)

            userinfo_url='https://www.zhihu.com/people/{}/answers'.format(id)
            user_item=UserItem()
            user_item['Id']=id
            user_item['Url']=userinfo_url
            yield scrapy.Request(
                userinfo_url,
                meta={"item":user_item},callback=self.User_parse,dont_filter=True
            )
            yield scrapy.Request(
                'https://www.zhihu.com/people/{}/followers'.format(id),
                callback=self.Add_user,dont_filter=True
            )
    
    def Add_user(self,response):
        sel=scrapy.selector.Selector(response)
       #<a class="UserLink-link" target="_blank" href="/people/12321-89">12321</a>
        #//*[@id="Profile-following"]/div[2]/div[2]/div/div/div[2]/h2/div/span/div/div/a/@href
        #//*[@id="Popover-24089-95956-toggle"]
        #//*[@id="Popover-24089-95956-toggle"]/a
        co=sel.xpath('//*[@id="root"]/div/main/div/div/div[2]').extract_first()
        pattern=re.compile(u'<a class="UserLink-link" target="_blank" href="/people/(.*?)">.*?</a>',re.S)
        l=re.findall(pattern,co)
        #l=sel.xpath('//*[@id="Profile-following"]/div[2]/div[2]/div/div/div[2]/h2/div/span/div/div/a/@href')
        for i in l:
            if i not in self.tasked_set:
                self.task_set.add(i)

    def User_parse(self, response):
        item=response.meta["item"]
        sel=scrapy.selector.Selector(response)
        nick_name=sel.xpath('//*[@id="ProfileHeader"]/div/div[2]/div/div[2]/div[1]/h1/span[1]/text()').extract_first()
        print(nick_name)
        summary=sel.xpath('//*[@id="ProfileHeader"]/div/div[2]/div/div[2]/div[1]/h1/span[2]/text()').extract_first()
        print(summary)
        item['Nick_name']=nick_name
        print(sel.xpath( '//span[@class="location item"]/@title').extract_first())
        co=sel.xpath('//*[@id="ProfileHeader"]/div/div[2]/div/div[2]/div[2]').extract_first()
        print("**********************")
        print(co)
        print('**********************')
        patten=re.compile(u'.*?</div>(.*?)<div.*?>',re.S)
        l=re.findall(patten,co)
        print(str(l))
        #print(sel.xpath('//*[@id="ProfileHeader"]/div/div[2]/div/div[2]/div[2]/span/div/div[2]/div').extract_first())
        #print(sel.xpath('//*[@id="ProfileHeader"]/div/div[2]/div/div[2]/div[2]/span/div/div[3]/div').extract_first())
        #print(sel.xpath('//*[@id="ProfileHeader"]/div/div[2]/div/div[2]/div[2]/span/div/div[4]/div/div').extract_first())
        #print(sel.xpath('//*[@id="ProfileHeader"]/div/div[2]/div/div[2]/div[2]/span/div/div[5]/div/a/span[2]').extract_first())




