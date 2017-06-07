# -*- coding:utf-8 -*-
# **FILENAME:
# **AUTHOR:           
# **CREATED TIME:     
# **FUN DESC    :测试读写文件的光标操作
# **MODIFIED BY :     
# **MODIFIED TIME:    
# **MODIFIED CONTENT:
# **REVIEWED BY:      
# **REVIEWED TIME:  
import os

f = open('3.txt','r')
print f.tell()
print f.read(2)
print f.tell()
print f.read(3)
f.seek(0,os.SEEK_SET)
print f.read(3)
print f.tell()

f.seek(4,os.SEEK_SET) #移动光标位置，绝对位置
print f.read(3)
print f.tell()


f.seek(4,os.SEEK_SET) #移动光标位置，指定光标的位置，相对于当前文件的起始位置
print f.read(3)
print f.tell()

f.seek(4,os.SEEK_CUR) #移动光标位置，相对于光票当前的位置
print f.read(3)
print f.tell()

f.seek(0,os.SEEK_SET)
cont = f.readline()
print len(cont),cont
f.seek(0,os.SEEK_SET)
f.seek(-4,os.SEEK_END) #移动光标位置，相对于文件结尾的位置
print f.read(5)
print f.tell()
