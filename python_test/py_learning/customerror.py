# -*- coding:utf-8 -*-
# **FILENAME:
# **AUTHOR:           
# **CREATED TIME:     
# **FUN DESC    :        自定义异常测试
# **MODIFIED BY :     
# **MODIFIED TIME:    
# **MODIFIED CONTENT:
# **REVIEWED BY:      
# **REVIEWED TIME:    
# **INPUT TABLE:  
# **MID TABLE :
# **DIM TABLE :
# **OUTPUT TABLE: 

class MyError(Exception):
    def __init__(self,info):
        Exception.__init__(self)
        self.errinfo = info
        print id(self)

    def __str__(self):
        return "MyError:%s" %self.errinfo

try:
    raise MyError('test my error')
except MyError,e:
    print "ErrorInfo:%d-->%s"%(id(e),e)
