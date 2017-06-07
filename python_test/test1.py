import math

print filter(lambda x:int(math.sqrt(x))*int(math.sqrt(x))==x, range(1, 101))