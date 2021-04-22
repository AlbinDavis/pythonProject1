class Apparel:
    def __init__(self,appbrand,apptype,price,instock):
        self.appbrand=appbrand
        self.apptype=apptype
        self.price=price
        self.instock=instock
class Store:
    def __init__(self,applist):
        self.applist=applist
    def checkappavl(self,brand,type,appsize,avl):
        for i in range(len(applist)):
            if applist[i].appbrand.tolower()==brand and applist[i].apptype.tolower()==type:
                if appsize.tolower() in applist[i].instock:
                    pass

            print(True)


applist=[]
instock={}
n=int(input())
for i in range(n):
    appbrand=input()
    apptype=input()
    price=int(input())
    c=int(input())
    for j in range(c):
        k=input()
        v=int(input())
        instock[k]=v
    applist.append(Apparel(appbrand,apptype,price,instock))
brand=input()
type=input()
appsize=input()
avl=input()
store=Store(applist)
res=store.checkappavl(brand, type, appsize, avl)



