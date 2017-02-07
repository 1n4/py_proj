# -*- coding:utf-8 -*-
# 学习for循环,break,global变量声明
# 测试，如果列表中的元素包含元组，则打印元组中的每一个元素

for x in [1,2,"test",(1,2)]:
    print(x)
else :
    print "for loop over"
    # while len(x) > 0:
    #     length = len(x)
    #     i=0
    #     while i < length:
    #         i += 1
    #         print(x(i))

while 1:
    s = raw_input("enter a string:")
    if s == "quit":
        break
    print "the length of s is ",len(s)
print "you enter a quit order,bye"




