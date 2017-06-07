# -*- coding:utf-8 -*-
# **FILENAME:
# **AUTHOR:  yjy         
# **CREATED TIME:    
# **FUN DESC    :测试使用pymysql查询mysql
# **MODIFIED BY :     
# **MODIFIED TIME:    
# **MODIFIED CONTENT:
# **REVIEWED BY:      
# **REVIEWED TIME:  

import pymysql

con=pymysql.connect(
    host='localhost',
    user='root',
    password='678201',
    db='spider',
    charset='utf8'
)

try:
    with con.cursor() as cur:
        sql = 'select  `tittle`,`href` from `wiki_spider` where `id` is not NULL '
        count = cur.execute(sql)

        #获取记录条数
        print count

        # 获取所有内容
        # result = cur.fetchall()
        # print result

        #获取指定条数记录
        result =cur.fetchmany(size=10)
        print result
finally:
    con.close()