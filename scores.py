scores=[10,5,20,20,4,5,2,25,1]
c1 = 0
c=0
min= scores[0]
max= scores[0]
for i in range(len(scores)):
    if scores[i] > max:
        max = scores[i]
        c += 1
    elif scores[i] < min:
        min = scores[i]
        c1 += 1
print(c,c1)

