lis=list(map(int,input().rstrip().split()))
s1=list(set(lis))
for i in range(len(s1)):
    print("count of %d ="%s1[i],lis.count(s1[i]))
