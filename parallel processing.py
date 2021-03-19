n = int(input())
li = []
for i in range(n):
    li.append(int(input()))
c = int(input())
l = int(input())
if c < 2:
    print(sum(li))
else:
    li.sort()
    c1=1
    s=0
    for i in range(len(li)-1,0,-1):
        if li[i]%c==0 and c1<=l:
            c1+=1
            s+=li[i]//c
            li.remove(li[i])
    print(sum(li)+s)



