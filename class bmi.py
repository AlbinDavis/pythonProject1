class Person:
    def __init__(self,name,height,weight):
        self.name=name
        self.height=height
        self.weight=weight
        self.bmi=0
        self.bmists=""

    def calculatebmi(self):
        self.bmi=self.weight//(self.height*self.height)

class Society:
    def __init__(self,personlist,d):
        self.personlist=personlist
        self.d=d

    def calculatebmiandstatusbyname(self,pname):
        t = False
        for i in self.personlist:
            if i.name.lower()==pname.lower():
                i.calculatebmi()
                for j in self.d:
                    s=self.d[j]
                    if s[0] <= i.bmi <= s[1]:
                        i.bmists = j
                        t=True
        return t
    def removeinvalidpersons(self,number):
        l=[]
        li=[]
        pass
            # if i.bmi < number and i.bmi!=0:
            #     print(i.name,i.bmi)

n=int(input())
personlist=[]
for i in range(n):
    name=input()
    height=int(input())
    weight=int(input())
    personlist.append(Person(name,height,weight))

m=int(input())
d={}
for i in range(m):
    bmistatus=input()
    lower=int(input())
    upper=int(input())
    d[bmistatus]=(lower,upper)
pname=input()
number=int(input())
s=Society(personlist,d)
if s.calculatebmiandstatusbyname(pname):
    for i in personlist:
        print(i.bmi)
#     for i in personlist:
#         if i.bmi !=0:
#             print(i.bmi,i.bmists,sep=" ")
# else:
#     "No Person Exists"
k=s.removeinvalidpersons(number)



