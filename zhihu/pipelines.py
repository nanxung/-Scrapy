# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
class ZhihuPipeline(object):
    def process_item(self, item, spider):
        return item


class MysqlPipeline(object):
    def __init__(self):
        self.conn=pymysql.connect(
            host='localhost',   #本地127.0.0.1
            port=3306,          #默认3306端口
            user='root',        #mysql最高权限用户
            passwd='****',  #root用户密码
            db='zh',       #database name
            charset='utf8'
            )
    def process_item(self,item,spider):
        self._conditional_insert(self.conn.cursor(),item)#调用插入的方法
       # query.addErrback(self._handle_error,item,spider)#调用异常处理方法
        return item

    def _conditional_insert(self,tx,item):

        sql="insert into user(id,url,nick_name,summary,content) values(%s,%s,%s,%s,%s)"
        params=(item["Id"],item["Url"],item['Nick_name'],item['Summary'],item['Content'])
        tx.execute(sql,params)
        print('已经插入一条数据!')
        tx.close()
        self.conn.commit()
      #  self.conn.close()
        
    #错误处理方法
    def _handle_error(self, failue, item, spider):
        print(failue)
