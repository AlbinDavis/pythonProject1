n= int(input())
# for i in range(n):
#         for j in range(n-i-1):
#             print(" ",end=""),
#             k=j
#         while(i+1):
#             print("#",end="")
#             i-=1
#         print("\r")

for i in range(1,n+1):
    print(str('#'*i).ljust(n))
