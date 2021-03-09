n = int(input())
ar = list(map(int, input().rstrip().split()))
li = list(set(ar))
r = 0
for i in range(len(li)):
    c = ar.count(li[i])
    if c > 1:
        if c % 2 == 0:
            r += int(c / 2)
            print(li[i],r)
        else:
            r += int((c - 1) / 2)
            print(li[i], r)
print(r)


