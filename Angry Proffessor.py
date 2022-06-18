def angryProfessor(k, a):
    c = 0
    for i in a:
        if i <= 0:
            c += 1
    print(k,c)
    if c >= k:
        print("NO")
    else:
        print("YES")

t = int(input())
for t_itr in range(t):
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    a = list(map(int, input().rstrip().split()))
    angryProfessor(k, a)