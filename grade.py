n = int(input())
for i in range(n):
    n1 = int(input().rstrip())
    n2 = n1
    if n2 < 38:
        print(n2)
    else:
        while (n2 % 5 != 0):
            n2 += 1
        if (n2 - n1 < 3):
            print(n2)
        else:
            print(n1)

# if grade >= 38:
#     if grade % 5 == 3:
#         grade += 2
#     elif grade % 5 == 4:
#         grade += 1
# print(grade)

