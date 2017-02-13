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

class Person(object):
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
    def whoAmI(self):
        return 'im a person,my name is %s' %self.name


class Student(Person):
    def __init__(self,name,gender,school):
        super(Student,self).__init__(name,gender)
        self.school = school


class Teacher(Person):
    def __init__(self,name,gender,course):
        super(Teacher,self).__init__(name,gender)
        self.course = course

p=Person('killer','male')
s = Student("yin",'male','whlg')
t = Teacher('zbd','male','java')

print s.name,s.whoAmI()
print p.name,p.whoAmI()
print t.course,t.whoAmI()
print isinstance(s,Student)


class A(object):
    def __init__(self, a):
        print 'init A...'
        self.a = a

class B(A):
    def __init__(self, a):
        super(B, self).__init__(a)
        print 'init B...'

class C(A):
    def __init__(self, a):
        super(C, self).__init__(a)
        print 'init C...'

class D(B, C):
    def __init__(self, a):
        super(D, self).__init__(a)
        print 'init D...'

d=D('test')

