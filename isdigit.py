s="1sd23fd"
a=[]
for i in s:
    if i.isdigit():
        a.append(int(i))
a.reverse()
print(a)