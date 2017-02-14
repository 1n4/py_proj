#coding：utf-8
#错误写法如下，需要注意求和与if的位置，如果先求和，则比较的逻辑并未生效。
# sum = 0
# for x in L:
#     if x>100:
#         continue
#     sum = sum+x
# print sum

L =  [75, 98, 59, 81, 66, 431,5645,43, 69, 85]
sum = 0
for x in L:
    if x>100:
        continue
    sum = sum+x
print sum
