# -*- coding:utf-8 -*-
# **FILENAME:
# **AUTHOR:           
# **CREATED TIME:     
# **FUN DESC    :           带参数的的装饰器
# **MODIFIED BY :     
# **MODIFIED TIME:    
# **MODIFIED CONTENT:
# **REVIEWED BY:      
# **REVIEWED TIME:    
# **INPUT TABLE:  
# **MID TABLE :
# **DIM TABLE :
# **OUTPUT TABLE: 

def log(prefix):
    print "step1"
    def log_decorator(f):
        print '[%s]call %s....' %(prefix,f.__name__)
        return f
    return  log_decorator

@log('DEBUG')
def test() :
    print "over"

@log('[INFO]')
def test2():
    pass

# print test()
# print test2()
