# -*- coding:utf-8 -*-
# **FILENAME:
# **AUTHOR:  yjy         
# **CREATED TIME:    
# **FUN DESC    :
# **MODIFIED BY :     
# **MODIFIED TIME:    
# **MODIFIED CONTENT:
# **REVIEWED BY:      
# **REVIEWED TIME:

#导入需要用到的库
from urllib import urlopen
from bs4 import BeautifulSoup as bs
import re
import pymysql.connections



#获取文件内容
contents = urlopen('https://en.wikipedia.org/wiki/Main_Page').read()

#使用bs来解析
bs_contents = bs(contents,'html.parser')


#获取以a标签中以wiki开头的href属性
urls_list = bs_contents.find_all('a',href=re.compile('^/wiki/'))


#逐条取数
for url in urls_list:
    con=pymysql.connect(
        host='localhost',
        user='root',
        password='678201',
        db='spider',
        charset='utf8'
    )

    #过滤图片
    if  not re.search('(\.jpg|JPG)$',url['href']):
        print url.get_text()+'--------------->'+'https://en.wikipedia.org'+url['href']

        try:
            with con.cursor() as cur:
                sql = 'insert into `wiki_spider` (`tittle`,`href`)values (%s,%s)'
                cur.execute(sql,(url.get_text(),'https://en.wikipedia.org'+url['href']))
                con.commit()

        finally:
            con.close()