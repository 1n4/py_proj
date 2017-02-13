# -*- coding:utf-8 -*-
# **FILENAME:
# **AUTHOR:           
# **CREATED TIME:     
# **FUN DESC    :            类和对象的相关测试，如果一个属性由双下划线开头(__)，该属性就无法被外部访问
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
    addr = 'Earth'
    count =0
    __count =0
    def __init__(self,name,age,**args):
        self.name = name
        self.age = age
        self.args = args

class Person2(object):
    def __init__(self,name,**kwargs):
        self.name=name
        for k,v in kwargs.iteritems():
            setattr(self,k,v)


class Person3(object):
    def __init__(*args, **kw):
        print isinstance(args, tuple)
        args[0].name = args[1]
        args[0].gender = args[2]
        for k, v in kw.iteritems():
            setattr(args[0], k, v)

class Person4(object):
    __score = 60
    def __init__ (self,name,score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score <=100 and self.score>0:
            score = self.score
            if score>=60 and score<80:
                print "及格"
            elif score >=80:
                print "优秀"
            else:
                print "不及格"
        else:
            print "invalid score"





p1 =Person('yin',30)
p5 = Person('and',20)
p2 = Person('andyi',22,bir="1986",gender='male')
p3 = Person2('yin',age=12,gender='male')
p4 = Person3('Bob', 'Male', age=18, course='Python')

p6 =Person4('yinandyi',78)



print  'my name is %s and im %s years old' %(p1.name,p1.age)
print  'my name is %s and im %s years old,my birthday is %s' %(p2.name,p2.age,p2.args.get('bir'))

print p3.name,p3.age,p3.gender

print p4.age
print p4.course

p6.get_grade()

print p1.addr,p1.count
p1.addr='china'                                                                                                      # 因为类属性只有一份，所以，当Person类的address改变时，所有实例访问到的类属性都改变了 ,而当某个实例的属性发生改变时，其它实                                                                                                                                         #例并不改变，即当实例属性和类属性重名时，实例属性优先级高
print p1.addr,p1.count
try:
    print p5.addr,p5.count,p5.__count                                                                    #??????????except的错误类型不对时，不能正确执行后面的打印语句？
except AttributeError:
    print '\nAccess error'






