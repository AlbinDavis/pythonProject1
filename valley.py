step=int(input())
path=input()
s = 0
v = 0
for i in path:
    if s == 0 and i == "D":
        v += 1
    if i == "U":
        s += 1
    else:
        s -= 1
print(v)
