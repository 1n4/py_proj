# -*- coding:utf-8 -*-

class Person:
    def __init__(self,name):
        self.name = name
    def sayHi(self):
        print "hello %s,how are you" %self.name


p = Person("test")
p.sayHi()
