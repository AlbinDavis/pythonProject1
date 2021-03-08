label=["good","bad","good","bad","good"]
cost=[2,5,3,11,1]
d=2
c=0
li=[]
s=0
for i in range(len(label)):
    if label[i]=="good":
        s+=cost[i]
        c+=1;
    else:
        s+=cost[i]

    if c==2:
        li.append(int(s))
        c=0
        s=0
if len(li)==0:
    print(0)
else:
    print(li)
