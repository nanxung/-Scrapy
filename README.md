#zhihu
<h4>设置连接数据库</h4>
pymysql.connect(<br>
            host='localhost',   #本地127.0.0.1<br>
            port=3306,          #默认3306端口<br>
            user='root',        #mysql最高权限用户<br>
            passwd='****',  #root用户密码<br>
            db='zh',       #database name<br>
            charset='utf8'<br>
            )<br>
数据库名zh,表名user(id,url,nick_name,summary,content)<br>
<h2>如何运行</h2>
配置完成后<br>
进入项目根目录执行scrapy crawl zh即可<br>
