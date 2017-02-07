# -*- coding:utf-8 -*-

z = 200
def func(x):
        global z
        print "x = ",x
        print "z = ",z
        x = 10                      #   局部变量
        z = 100                    #   z已经被声明为全局变量

print z
func(30)
print "z=" ,z


#默认参数
def say(words,times=1):
    print(words*times)

say("hello world")
say("hello",5)

#关键参数

def keyParTest(a,b=10,c=5):
    print(a,b,c)

keyParTest(20)
keyParTest(30,4)
keyParTest(3,9,20)


#return
def max(x, y):
    if x > y:
        return x
    else:
        return y

print max(2, 3)                    #直接打印函数结果


