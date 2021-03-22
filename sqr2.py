n=int(input())
if n < 1:
    print("incorrect input")
else:
    n1 = n * n
    c=0
    while(n>0):
        if n%10 != n1%10:
            c=1
        n=int(n/10)
        n1=int(n1/10)
    if c == 0:
        print("yes")
    else:
        print("no")