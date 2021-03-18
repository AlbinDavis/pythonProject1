n=int(input())
li=[]
for i in range(1,(n//2)+1):
    if n%i==0:
        li.append(i)
print(li)


