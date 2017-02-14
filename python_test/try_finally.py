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

try:
    f = open(r'./test.txt')
    num = int(f.read(2))
    print num
except IOError,e:
    print 'catch IOError',e

except ValueError,e:
    print 'catch ValueError',e
else:
    print "file exist,open sucess"
finally:
    print 'close file'
    f.close()

