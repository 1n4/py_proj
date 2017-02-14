# -*- coding:utf-8 -*-
# **FILENAME:
# **AUTHOR:           
# **CREATED TIME:     
# **FUN DESC    :         动态的导入模块测试
# **MODIFIED BY :     
# **MODIFIED TIME:    
# **MODIFIED CONTENT:
# **REVIEWED BY:      
# **REVIEWED TIME:    
# **INPUT TABLE:  
# **MID TABLE :
# **DIM TABLE :
# **OUTPUT TABLE: 

try:
    from cStringIO import StringIO
    print     'from cStringIO import StringIO'
except ImportError:
    from StringIO import  StringIO
    print "from StringIO import  StringIO"

