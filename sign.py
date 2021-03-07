import numpy as np
arr=[-22,3,4,-56,65,0]
arr2=np.sign(arr)

map(float,arr2)
m=0
p=0
z=0
for i in range(len(arr2)-1):
    if arr2[i]==-1:
        m=m+1
    if arr2[i]==1:
        p+=1
    else:
        z+=1

print("zero:",format((z/len(arr2)),".4f"))
print("pos:",format((p/len(arr2)),".4f"))
print("neg:",format((m/len(arr2)),".4f"))


