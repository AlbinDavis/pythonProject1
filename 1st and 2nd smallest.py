n=int(input())
if n > 2:
    m1 = int(input())
    m2=m1
    for i in range(1, n):
        k = int(input())
        if k < m2:9
            if k < m1:
                m2 = m1
                m1 = k
            else:
                m2=k
    if m1==m2:
        print("Equal")
    else:
        print(m1,m2)
