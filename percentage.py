# n=int(input())
# li=[]
# for i in range(n):
#     s=[]
#     s=input().split()
#     li.append(s)
# name=input()
# for i in range(n):
#     if(li[i][0]==name):
#         print(format((float(li[i][1]) + float(li[i][2]) + float(li[i][3])) / 3,".2f"))
n = int(input())
dic = {}
mark=[]
for i in range(n):
    name = input().split(" ")
    mark=list(map(float,name[1:]))
    dic[name[0]]=sum(mark) /(len(mark))
print(format(dic[input()], ".2f"))
