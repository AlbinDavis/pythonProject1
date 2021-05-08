class Doctor:
    def __init__(self, docid, docname, deptname, consfee, sundayavl):
        self.docid = docid
        self.docname = docname
        self.deptname = deptname
        self.consfee = consfee
        self.sundayavl = sundayavl

class Hospital:
    def getDoctorList(depname,doclist):
        li=[]
        for i in range(0, len(doclist)):
            if doclist[i].deptname.tolower() ==depname and doclist[i].sundayavl=="available":
                li.append(doclist[i].docid)
                li.append(doclist[i].docname)
        return li

    def selectDoctor(fee,doclist):
        f=0
        l=[]
        n=5
        for i in range(n):
            if doclist[i].sundayavl.tolower() == "not available" and doclist[i].consfee > fee:
                l.append(doclist[i])
                f=1
        if f==1:
            for i in range(len(l)):
                doclist.remove(l[i])
            return True
        else:
            return False

doclist=[]
for i in range(5):
    docid=int(input())
    docname=input()
    deptname=input()
    consfee=int(input())
    sundayavl=input()
    doclist.append(Doctor(docid,docname,deptname,consfee,sundayavl))

depname=input()
fee=int(input())

r=Hospital.getDoctorList(depname,doclist)
if r:
    for i in r:
        print(i)
res=Hospital.selectDoctor(fee,doclist)

if res==True:
    pass
    doclist.sort(key=lambda x: x.consfee)
    for i in doclist:
        print(i.docid)
        print(i.docname)
        print(i.consfee)
else:
    print("Returning the Orginal list")
    for i in doclist:
        print(i.docid)
        print(i.docname)





