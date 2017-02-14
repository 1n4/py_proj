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


#一个猜数字游戏，测试try ...except

import random

x = random.randint(1,100)

while True:
   try:
        guess = int(raw_input("enter a num,between 1,100:"))
   except ValueError,e:
        print "you should enter a num between 1,100"
        continue
   if guess >x:
       print   'bigger'
   elif guess <x:
       print "smaller"
   else:
       print "right ,game over"
       break
       



