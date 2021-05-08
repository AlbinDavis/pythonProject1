li=[1,-2,5,3,-6,7,-4,2]
r=0
m=0
for i in range(len(li)):
    s=li[i]
    m=s
    for j in range(i+1,len(li)):
        s+=li[j]
        if s>m:
            m=s
    if m>r:
        r=m
print(r)
