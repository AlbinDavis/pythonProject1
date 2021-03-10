bnk = list(map(int, input().rstrip().split()))
k = list(map(int, input().rstrip().split()))
m = list(map(int, input().rstrip().split()))
b = bnk[0]
p = []
for i in range(len(k)):
    for j in range(len(m)):
        if k[i] + m[j] <= b:
            p.append(k[i] + m[j])
if p:
    print(max(p))
else:
    print("-1")

