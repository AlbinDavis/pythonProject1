n = int(input())
t = int(input())
l = []
for i in range(n):
    li = list(map(int, input().rstrip().split()))
    l.append(li)

c = 0
mark = []
for i in range(len(l)):
    m=l[i][0]
    c = l[i][1]
    for j in range(len(l)):
        if i != j:
            if c+l[j][1] <= t:
                m += l[j][0]
                c += l[j][1]

    mark.append(m)
print(max(mark))


