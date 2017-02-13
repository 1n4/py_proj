# -*- coding:utf-8 -*-
# **FILENAME:
# **AUTHOR:           
# **CREATED TIME:     
# **FUN DESC    :  set中的元素也是无序的，添加时使用add，当添加的元素已经存在时不会报错，但是不能添加进去。删除元素时使用remove
# **MODIFIED BY :     
# **MODIFIED TIME:    
# **MODIFIED CONTENT:
# **REVIEWED BY:      
# **REVIEWED TIME:    
# **INPUT TABLE:  
# **MID TABLE :
# **DIM TABLE :
# **OUTPUT TABLE: 

s = set(['yinandyi','missa','killer'])
if 'yinandyi' in s:
    print 'yes'

def  my_abs(x):
    if x >0:
        return x
    else:
        return  -x
x = int(raw_input("enter a num:"))
print my_abs(x)
