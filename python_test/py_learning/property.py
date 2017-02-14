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
class Student(object):
    __slots__=('name,score,gender,score')                                                                 #__slots__类允许添加的属性列表
    def __init__(self, name, score):
        self.name = name
        self.__score = score
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, score):
        if score < 0 or score > 100:
            raise ValueError('invalid score')
        self.__score = score


s = Student('yinandyi','78')
try:
    s.score = int(raw_input("enter a num:"))
except ValueError('invalid score'):
    s.score = int(raw_input("enter a num:"))
print s.score
