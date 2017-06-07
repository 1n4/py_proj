# -*- coding:utf-8 -*-
# **FILENAME:
# **AUTHOR:  yjy         
# **CREATED TIME:    
# **FUN DESC    :
# **MODIFIED BY :     
# **MODIFIED TIME:    
# **MODIFIED CONTENT:
# **REVIEWED BY:      
# **REVIEWED TIME:  

import configparser

cfg = configparser.ConfigParser()
cfg.read('gitconfig.ini','utf-8')
print cfg.sections()
for se in cfg.sections():
    print se
    # print cfg.items(se)
