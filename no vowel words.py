s=[]
li=[]
for i in range(148):
    s.append(input().lower())
for i in s:
    if 'a' not in i and 'e' not in i and 'i' not in i and 'o' not in i and 'u' not in i :
        li.append(i)
print(*li,sep="\n")
