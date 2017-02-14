# -*- coding:utf-8 -*-
# **FILENAME:
# **AUTHOR:           
# **CREATED TIME:     
# **FUN DESC    :         将list中的字符串转换成大写
# **MODIFIED BY :     
# **MODIFIED TIME:    
# **MODIFIED CONTENT:
# **REVIEWED BY:      
# **REVIEWED TIME:    
# **INPUT TABLE:  
# **MID TABLE :
# **DIM TABLE :
# **OUTPUT TABLE: 


L1 = ['oiuoi',121,'fafsd']
L2 = [x.upper() for x in L1 if isinstance(x,str)]
print L2
