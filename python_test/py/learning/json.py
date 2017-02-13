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

f =open(r'D:\desktop\test.txt','r')
print f.readline()
f.close()

class PTest(object):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return 'PTest:%s'%self.name

t =PTest("test")
print t
print t.name

