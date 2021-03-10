li=input().split(":")
str=li[2]
l=str[2:]
l2=str[:2]
if(l=="PM"):
    if li[0]=="12":
        print(12, li[1], l2, sep=":")
    else:
        print(int(li[0])+12,li[1],l2,sep=":")

elif(l=="AM"):
    if li[0]=="12":
        print("00", li[1], l2, sep=":")
    else:
        print(li[0],li[1],l2,sep=":")

