# -*- coding:utf-8 -*-
# **FILENAME:
# **AUTHOR:           
# **CREATED TIME:     
# **FUN DESC    :体质指数计算，list默认不能实现，使用numpy
# **MODIFIED BY :     
# **MODIFIED TIME:    
# **MODIFIED CONTENT:
# **REVIEWED BY:      
# **REVIEWED TIME:    
# **INPUT TABLE:  
# **MID TABLE :
# **DIM TABLE :
# **OUTPUT TABLE:

import numpy as np


height = [1.73,1.66,1.83,1.77]
weight = [56, 73, 66, 51]

np_height = np.array(height)
np_weight = np.array(weight)

bmi = np_weight/np_height**2
bmi = [bmi>20]
print bmi
