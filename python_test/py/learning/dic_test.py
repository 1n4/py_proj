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

score_dict = {
    'yinandyi':88,
    'killer':78,
    'missa':90
}
print score_dict
print len(score_dict)
print score_dict['yinandyi']    #打印的顺序不一定是我们创建时的顺序，而且，不同的机器打印的顺序都可能不同，这说明dict内部是无序的，不能用dict存储有序的集合。
print "missa's score is:",score_dict.get('missa')
for x in score_dict:
    if score_dict.get(x)>80:
      print "they are good stu," ,x ,score_dict.get(x)

score_dict['yinandyi'] = 99
print score_dict
name = raw_input("enter a name:")
if name  in score_dict:
    print "i'm here"
elif name =="q":
    quit()
else:
    print "no %s" %name


d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }
sum =sum(d.itervalues())
print sum/len(d)

