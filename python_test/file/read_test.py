# -*- coding:utf-8 -*-
# **FILENAME:
# **AUTHOR:           
# **CREATED TIME:     
# **FUN DESC    :使用迭代方式读取文件
# **MODIFIED BY :     
# **MODIFIED TIME:    
# **MODIFIED CONTENT:
# **REVIEWED BY:      
# **REVIEWED TIME:  

f = open('2.txt','r')

# list_rd = f.readline(2)                                                           #当设置的size<len(line)时，读取指定的size长度，光标停在读取完的位置，否则，读取整行
# f.seek(1,1)                                                                          #seek移动光标位置
# list_rds = f.readlines()                                           #readlines默认从光标当前位置起读取系统指定的io.DEFALUT_BUFFER_SIZE长度的文件内容
# print list_rd
# print list_rds

iter_f = iter(f)
lines = 0
for line in iter_f:
    lines +=1

print lines
f.close()


