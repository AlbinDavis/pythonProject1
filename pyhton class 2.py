class Compl:
    def __init__(self,r,i):
        self.r=r
        self.i=i
    def s(self,num):
        real=self.r+num.r
        img=self.i+num.i
        print(real,"+i",img,sep="")
c1=Compl(2,3)
c2=Compl(4,5)
c1.s(c2)
#Compl.s(c1,c2)

