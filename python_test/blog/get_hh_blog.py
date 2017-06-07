# -*- coding:utf-8 -*-
# **FILENAME:
# **AUTHOR:  yjy
# **CREATED TIME:    
# **FUN DESC    :获取韩寒博客全部文章.方法1，根据关键字查找取位置,发现取出的仅按长度匹配的内容不一定正确,使用bs解析.
# **MODIFIED BY :     
# **MODIFIED TIME:    
# **MODIFIED CONTENT:
# **REVIEWED BY:      
# **REVIEWED TIME:  


import urllib
import re
from bs4 import BeautifulSoup as bs
from time import sleep
import sys
import os

import chardet

#可解决往文件中写入中文时出现的错误
reload(sys)
sys.setdefaultencoding('utf-8')

#bs未能获取到正确内容时，可以使用以下方法诊断
# from bs4.diagnose import diagnose
# diagnose(bs_cont)

#版本一，按起始位置的内容长度取，取出内容不一定正确
# #<a title="" target="_blank" href="http://blog.sina.com.cn/s/blog_4701280b0102wrup.html">写给那个茶水妹的《乘风破浪》诞生…</a>
# contents = urllib.urlopen("http://blog.sina.com.cn/s/articlelist_1191258123_0_1.html").read()
# title_start = contents.find(r'title=')
# href_start =  contents.find(r'href=',title_start)
# html_end = contents.find(r'.html">',href_start)
# file_name = contents[-26:]
# # print "contents>>>>>>>>>>\n"+contents
#
# print title_start,href_start,html_end,file_name

# contents=urllib.urlopen("http://blog.sina.com.cn/s/articlelist_1191258123_0_1.html").read()
count=0

#如果文件存在则删除
if os.path.exists(r'blog_contents/blog_title_list.txt'):
    os.remove(r'blog_contents/blog_title_list.txt')

#取所有页面数据
for page in range(1,8):
    url_list = "http://blog.sina.com.cn/s/articlelist_1191258123_0_"+str(page)+".html"
    contents = urllib.urlopen(url_list).read()
    encoding = chardet.detect(contents)
    print encoding

    #使用bs的接收返回内容，使用html.parser解析时未能获取到正确内容，接诊断提示安装html5lib后无效，改为lxml解析
    bs_cont = bs(contents,'lxml')
    # print bs_cont
    href_list = bs_cont.find_all('a',href =re.compile(r'^http://blog.sina.com.cn/s/blog'))
    # print href_list

    count +=len(href_list)

    try:
        for href in href_list:
            # print href.get_text(),href['href']
            url = href['href']
            # file_name = href.get_text().strip().replace(r'\\xa0','_').replace(r' ','_').replace(r'&nbsp;','_').replace('?','_').replace('　','_').replace('&lt','_').replace('&gt','_')
            name = href.get_text()
            # print name
            file_name = name.replace(r'<','').replace(r'>','').replace('？','').replace('?','').replace(r'\xA0','')+".html"
            # file_name = name.replace(r'<','').replace(r'>','').replace('？','').strip()
            print file_name,"-------->",url
            open('blog_contents/blog_title_list.txt','a').write((file_name+"--------------->"+url+'\n'))

            file_contents = urllib.urlopen(href['href']).read()
            open(r'blog_contents/'+file_name, 'w') .write(str(file_contents))
            print "downloading.........."
            sleep(5)
            # print file_contents
    except IOError,e:
        print "file name error !!!!!!!!!!!"+e.message
print "共有%d篇文章"% count