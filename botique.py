class Boutique:
    def __init__(self,bid,bname,btype,brating,points):
        self.bid=bid
        self.bname=bname
        self.btype=btype
        self.brating=brating
        self.points=points
class Onlineboutique:
    def __init__(self,boutiquedict):
        self.boutiquedict=boutiquedict
    def getboutique(self,low,up,extrapoints,type):
        r=[]
        for i in self.boutiquedict:
            if i.lower()==type.lower():
                for j in self.boutiquedict[i]:
                    if low<=j.brating<=up:
                        j.points+=extrapoints
                        r.append(j)
        if r:
            r.sort(key=lambda x:x.points,reverse=True)
            return r
        else:
            return None

btqdict={}
l=[]
k=[]
n=int(input())
for i in range(n):
    bid=int(input())
    bname=input()
    btype=input()
    brating=float(input())
    points=int(input())
    l.append(Boutique(bid, bname, btype, brating, points))
    k.append(btype)

k=set(k)


for i in k:
    s = []
    for j in l:
        if j.btype==i:
            s.append(j)
    btqdict[i]=s

lower=float(input())
upper=float(input())
extrapoints=int(input())
type=input()

o=Onlineboutique(btqdict)
r=o.getboutique(lower,upper,extrapoints,type)
for i in r:
    print(i.bid,i.bname,i.points)
