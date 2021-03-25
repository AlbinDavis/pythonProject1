class Table:
    def __init__(self, tableNo, waiterName, status):
        self.tableNo = tableNo
        self.waiterName = waiterName
        self.status = status


def findWaiterWiseTotalNoOfTables(tables):
    d={}
    for i in tables:
        if i.waiterName in d:
            d[i.waiterName] += 1
        else:
            d[i.waiterName] = 1
    return d

# The return statement terminates the function execution.
# A function can have multiple return statements. When any of them is executed, the function terminates.


def findWaiterNameByTableNo(tables,v):
    for i in tables:
        if i.tableNo==v:
            return i.waiterName
    return None


n=int(input())
li=[]
for _ in range(n):
    id=int(input())
    name=input().rstrip()
    status=input()
    li.append(Table(id,name,status))

v = int(input())

d=findWaiterWiseTotalNoOfTables(li)
for key in sorted(d.keys()):
    print(key+"-"+str(d[key]))

name = findWaiterNameByTableNo(li,v)
if name is None:
    print("No waiter found")
else:
    print(name)








