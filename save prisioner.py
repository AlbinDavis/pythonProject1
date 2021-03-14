def saveThePrisoner(n, m, s):
    m %= n
    res = (m + s - 1) % n
    if res == 0:
        res = n
    print(res)
#     if m==n==s:
#         print(n-1)
# 
#     else:
#         m = m % n
#         if s == 1 and m< n and m != 0:
#             print(m)
#         elif s==1 and m==0:
#             print(n)
#         elif s + m - 1 <= n:
#             print(s + m - 1)
#         else:
#             print((s + m) % n - 1)
# 
# 
t = int(input())
for t_itr in range(t):
    nms = input().split()

    n = int(nms[0])

    m = int(nms[1])

    s = int(nms[2])

    saveThePrisoner(n, m, s)
