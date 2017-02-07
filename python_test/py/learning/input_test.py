# -*- coding:utf-8 -*-
#猜数游戏，如果输入小于既定值，则需要继续输入
#学习while循环和键盘输入，以及方法调用

a = 10

def  getInput():
     x = int(raw_input("please enter a num:"))
     return x

def compare():
    c = 0
    while c < a:
        c = getInput()
    else:
        print "you win!"

compare ()




