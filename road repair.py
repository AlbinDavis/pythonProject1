n1=int(input())
l=[]
li=[]
for i in range(n1):
    l.append(int(input()))
n2=int(input())
for i in range(n2):
    li.append(int(input()))
print(sum(li)-sum(l))
# l.sort()
# li.sort()
# s=0
# for i in range(n1):
#     s+=abs(li[i]-l[i])
# print(s)