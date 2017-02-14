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
#1,1,2,3,5,8
def fibo(num):

    a = 1
    b = 1
    i = 0

    while i < num:
        a,b = a+b,a                       #需注意写在一行和分开写的区别，写在一行时可以理解为是一个运算，而写在两行则先执行上一行再下一行
        i += 1
        print b



def get_res(num):
    if num ==0:
        res =0
    elif num == 1:
        res =1
    else :
        res = get_res(num-1) + get_res(num-2)
    return res

def fibo2( num2 ):
    i = 0
    while i <= num2:
        print get_res(i)
        i += 1

def fibo3(num3):
    numList=[1,1]
    for x in range(0,num3):
        numList.append(numList[-1+numList[-2]])
    return numList

fibo(9)
fibo2(9)
fibo3(9)
