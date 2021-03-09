arr=[1,3,2,4,5,4,3,2,1,3,4]
li=list(set(arr))
print(li)
max=0
l=0

for i in range(len(li)):
        c=arr.count(li[i])
        print("count of %d =" % li[i], arr.count(li[i]))
        if c>max :
            max=c
            l=li[i]
print("count=",l)

