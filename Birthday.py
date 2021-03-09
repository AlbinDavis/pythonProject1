d=3
s=[1,2,1,3,2]
list(map(int,s))
m=2

c1 = 0
for i in range(len(s)-m+1):
    c = 0
    r = 0
    j = i
    for j in range(m):
        r+=s[i+j]
        c+=1
        if r == d:
            c1 += 1
print(c1)

# c = 0
# for i in range(len(s)-m+1):
#
#         r = 0
#         if sum(s[i:i+m])==d:
#                 c+=1
# print(c)
