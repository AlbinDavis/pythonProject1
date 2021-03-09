nk=int(input().split())
k=nk[1]
bill=int(input().split())
b=int(input())

anna_bill=int((sum(bill)-bill[k])/2)
if b-anna_bill == 0:
    print("Bon Appetit")
else:
    print(b-anna_bill)
