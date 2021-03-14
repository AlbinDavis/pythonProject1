# import math
# s=input()
# r=math.floor(math.sqrt(len(s)))
# c=math.ceil(math.sqrt(len(s)))
# for i in range(c):
#     print(s[i::c],end=" ")

s="helloworld"
for i in range(len(s)):
    print(s[i::2])
