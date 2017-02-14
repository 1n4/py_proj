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


def f(x):
    return x*x


def format(x):
    return str(x.title())                                              #python中函数后带（)则返回函数值，不带则返回对象，upper全大写，lower全小写，title首字母大写

def f2(x,y):
    return x+y

def f3(x,y):
    return x*y


def odd(x):
    return  x %2 ==1                                                  #仅返回为奇数的数据

def is_not_empty(x):
    if len(x.strip()) >0:
        return x
    # return x and len(x.strip()) >0                                    #结果相同注意此种写法与上面的区别以及和将if写在函数中的异同

print map(f,[1,2,3])
print map((lambda x:x*x),[1,2,3,4])
print map(format,['a','cfdsa'])
print map(lambda x:x.title(),['fdafsd','fdsafd'])
print reduce(f2,[1,2,3,4,7],100)
print reduce(lambda x,y:x+y,[1,2,3,4,5])
print reduce(f2,[1],100)
print reduce(f3,[1,2,3,4,5])
print filter(odd,range(1,32))
print filter(lambda x:x%2==1,range(1,22))
print  filter(is_not_empty,['fdsaf','fdasf','','reqrew'])
print filter(lambda s:len(s.strip())>0,['fdasfda','dfafsd',' '] )
print sorted([32,132,54,4,43,6])                                                          #默认为正序，即从小到大
print sorted([32,132,54,4,43,6],lambda x,y:-cmp(x,y))



