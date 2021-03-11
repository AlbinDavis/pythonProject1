n=int(input())
if n < 1:
    print("incorrect input")
else:
    n1 = n * n
    c=1
    while(n>0):
        if n%10 != n1%10:
            c=0
        n=int(n/10)
        n1=int(n1/10)
    if c == 1:
        print("yes")
    else:
        print("no")