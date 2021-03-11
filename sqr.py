n=int(input())
if n < 1:
    print("incorrect input")
else:
    n1=n*n
    s1=str(n)
    s2=str(n1)
    i=1
    c=1
    while(i<=len(s1)):
        if s1[len(s1)-i] != s2[len(s2)-i]:
            c=0
        i+=1
    if c==1:
        print("yes")
    else:
        print("no")

