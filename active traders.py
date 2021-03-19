n=int(input())
d=dict()
l=[]
for i in range(n):
    l.append(input())
for i in l:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for i in l:
    if (d[i]*100)/n >=5:
        print(i)
