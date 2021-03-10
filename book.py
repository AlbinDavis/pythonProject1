n = int(input())
p = int(input())
if n%2==0:
    n += 1
print(min(p//2, (n-p)//2))
# if (n % 2 == 0) and (p == 1 or p == n):
#     print(0)
# elif (n % 2 != 0) and (p == 1 or p == n or p == n - 1):
#     print(0)
# else:
#     i = 2
#     j = 1
#     c = 0
#     c1 = 0
#     while i < n:
#         if i != n - 1:
#             if p == i or p == i + 1:
#                 c = j
#         j += 1
#         i += 2
#     if n%2 ==0:
#         i = n-1
#         j = 1
#         while i > 1:
#             if i != 2:
#                 if p == i or p == i - 1:
#                     c1 = j
#             j += 1
#             i -= 2
#     else:
#         i = n - 2
#         j = 1
#         while i > 1:
#             if i != 2:
#                 if p == i or p == i - 1:
#                     c1 = j
#             j += 1
#             i -= 2
#     print(min(c, c1))
