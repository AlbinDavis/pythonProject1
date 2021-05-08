li=[12, 1, 12, 3, 12, 1, 1, 2, 3, 2, 2, 3, 7]
l=[0]*(max(li)+1)
for i in range(len(li)):
    l[li[i]]+=1
for i in range(len(l)):
    if l[i]==1:
        print(i)