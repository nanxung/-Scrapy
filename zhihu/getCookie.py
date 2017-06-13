# encoding=utf-8
import requests
import re
import sys
#设置请求头
headers={
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch, br',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Connection':'keep-alive',
    'Host':'www.zhihu.com',
    'Origin':'https://www.zhihu.com',
    'Referer':'https://www.zhihu.com/',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'x-hd-token':'hello',
}

user=[
    'Kirio','sw2016','2051750893'
]
b=open('user','a')
#下面写入账号密码

post_data={
    '_xsrf':'***',
    'password':'chenbo01',
    'captcha':'***',
    'phone_num':'18079954801',
}

req=requests.Session()

def login():
    page=req.get(url="https://www.zhihu.com/#signin",headers=headers)
    parser=re.compile(u'<input type="hidden" name="_xsrf" value="(.*?)"/>',re.S)
    xsrf=re.findall(parser,page.text)[0]
    headers['X-Xsrftoken']=xsrf
    post_data['_xsrf']=xsrf
    #下载验证码
    with open("../code.jpg",'wb') as w:
        p=req.get(url="https://www.zhihu.com/captcha.gif?r=1495546872530&type=login",headers=headers)
        w.write(p.content)

    code=input("请输入验证码:")
    if not code:
        sys.exit(1)
    post_data['captcha']=code
    res=req.post(url='https://www.zhihu.com/login/phone_num',data=post_data,headers=headers)
    print(res.text)
    return req

cookie=login().cookies.get_dict()
    