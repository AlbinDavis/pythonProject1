n = int(input())
lis = []
for i in range(n):
    str=input()
    li = []
    li = str.split()
    if li[0]=="append":
        lis.append(int(li[1]))
    elif li[0]=="insert":
        lis.insert(int(li[1]),int(li[2]))
    elif li[0]=="remove":
        lis.remove(int(li[1]))
    elif li[0]=="print":
        print(lis)
    elif li[0]=="sort":
        lis.sort()
    elif li[0]=="reverse":
        lis.reverse()
    elif li[0]=="pop":
        lis.pop()
