# -*- coding:utf-8 -*-
# **FILENAME:
# **AUTHOR:           
# **CREATED TIME:     
# **FUN DESC    :           汉诺塔游戏，有a，b，c三个柱子，将a上的n个盘子移动到c上，要保证圆盘还是从上到下为从小到大摆放
# **MODIFIED BY :     
# **MODIFIED TIME:    
# **MODIFIED CONTENT:
# **REVIEWED BY:      
# **REVIEWED TIME:    
# **INPUT TABLE:  
# **MID TABLE :
# **DIM TABLE :
# **OUTPUT TABLE:

def move(n,a,b,c):

    if n == 1:
        print a,"-->",c
        return

    move(n-1,a,c,b)                                        #将a上面的n-1个圆盘先移动到b上，注意参数位置的变化
    move(1,a,b,c)                                            #将a上的底盘移动到c上
    move(n-1,b,a,c)                                         #将b上的圆盘依次移动到c上，因为从a上是按小到大的顺序移动到b上，所以b上当前的排列上，大在上小在下，可直接移动到c上

    
n = int(raw_input("请输入圆盘个数："))

move(n,"1号柱","2号柱","3号柱")
