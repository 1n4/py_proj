# -*- coding:utf-8 -*-
# **FILENAME:
# **AUTHOR:           
# **CREATED TIME:     
# **FUN DESC    :y
# **MODIFIED BY :     
# **MODIFIED TIME:    
# **MODIFIED CONTENT:
# **REVIEWED BY:      
# **REVIEWED TIME:  

f= open('1.txt','r+')   #读写方式打开，如果写入内容则文件被清空
f.write("123")
f.close()


f= open('1.txt','w+') #读写方式打开，只要打开就清空
f.write("456")
f.close()

f= open('1.txt','a+') #追加读写方式打开
f.write("\n789")
f.close()
