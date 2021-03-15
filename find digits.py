
def findDigits(n):
    li=str(n)
    c=0
    for i in li:
        if int(i)!=0 and n%int(i)==0:
            c+=1
    return c

t = int(input())

for t_itr in range(t):
    n = int(input())

    result = findDigits(n)
