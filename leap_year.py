#gregorian calender
y=int(input())
if y % 4==0 and y % 100 != 0:
    print("ly")
elif y % 4==0 and y%100 == 0 and y%400==0:
    print("ly")
else:
    print("not")
#julian calender
if y % 4 == 0:
    print("leap")
else:
    print("not leap")