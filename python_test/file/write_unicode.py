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

import  codecs  as cd


f = open('4.txt','w+')
t_str = unicode.encode(u'测试写入中文\n','utf-8')
f.write(t_str)
f.flush()
print f.read()
f.close()

f1 = cd.open('4.txt','a','utf-8')
f1.write(u"中文测试")
f1.close()