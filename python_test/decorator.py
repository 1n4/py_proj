# -*- coding:utf-8 -*-
# **FILENAME:
# **AUTHOR:           
# **CREATED TIME:     
# **FUN DESC    : 
# **MODIFIED BY :     
# **MODIFIED TIME:    
# **MODIFIED CONTENT:
# **REVIEWED BY:      
# **REVIEWED TIME:    
# **INPUT TABLE:  
# **MID TABLE :
# **DIM TABLE :
# **OUTPUT TABLE:

import time
def log(f):                                                                                                           #定义装饰器函数，参数是需要被装饰的原函数
    print "step1"
    def fn(x):                                                                                                          #加入五毛钱特效-->print
         print 'step2'
         print "now call "+f.__name__+"(%s)" %x
         return f(x)                                                                                                   #返回原来的代码，即factorial(6)
    return fn                                                                                                          #返回加特效后的代码

def performance(f):
    def fn(x):
        print  "call " +f.__name__+  "(%s)" %x  +"\r" +time.ctime()
        return f(x)
    return fn

@log
def factorial(n):
    return reduce(lambda x,y:x*y,range(1,n+1))


@performance
def factorial2(n):
    return reduce(lambda x,y:x*y,range(1,n+1))

print  `factorial(5)`+'\n@log'
print "@performance"+`factorial2(6)`
