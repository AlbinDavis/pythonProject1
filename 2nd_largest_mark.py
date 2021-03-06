li = []
marks = []
mar=[]
n = int(input())
for i in range(n):
    name = input()
    mark = float(input())
    marks.append(mark)
    li.append([name, mark])
marks.sort()
s = set(marks)
marks =list(s)
marks.sort()
li.sort()
for i in range(n):
    if li[i][1] ==marks[1]:
        print(li[i][0])
