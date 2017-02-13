# -*- coding:utf-8 -*-

#sort,append,delete,slice,,join

myList = ['apple','potato','cake']
kind = len(myList)
print 'my shopping list have %n: kinds of food ,they are ' ,myList,
print 'buy some banana,then i have',          #使用，将后面要打印的内容打印在同一行
myList.append('banana')
print myList
print 'after sort my shoplist is',
myList.sort()
print myList
print 'i like banana,buy more,'
myList.append('banana')
print myList
# print 'the first thing i have bought is ',myList[0],'but i have some' ,myList[0] ,'kill it'
print 'the first thing i have bought is %s but i have some %s ,kill it' %(myList[0],myList[0])

myList.__delitem__(0)                   #del myList[0]
print 'so my shooplist is ',myList
delimeter = '***'
print delimeter.join(myList)


if 'banana' in myList:
    print "mylist cantains a banana"


list_a = [x*x for x in range(1,10)]                                    #python的列表生成式
print list_a


list_b = [x*x+1 for x in range (1,20,2)]

list_c = [x for x in range(1,101) if x%2==0]


list_d = [a+b for a in 'abcde' for b in '123123']

