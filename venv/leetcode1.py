
##########reverse vowels in the string ###########################################################

def reverseVovles(s="hello"):
    v={'a','e','i','o','u','A','E','I','O','U'}
    s=list(s)
    i=0
    j=len(s)-1
    while(i<j):
        if(s[i] not in v):
            i+=1
            continue
        if(s[j] not in v):
            j-=1
            continue
        s[i],s[j]=s[j],s[i]
        i+=1
        j-=1
    return(s)

################### palindrome by whithout using the temp variable ###################################

def palindromeNum(x=121):
    x=121
    if (x < 0 or (x > 0 and x % 10 == 0)):
        return False
    n = 0
    while (n < x):
        n = (n * 10) + x % 10;
        x = x // 10;

    if n == x or x == n // 10:
       return True
    else:
        return False



# n = [ "the", "quick", "brown", "fox",
#      "quick"]
# w2 = "the"
# w1 = "fox"

# n=["geeks", "for", "geeks", "contribute",
#      "practice"]
# w1 = "geeks"
# w2 = "practice"

############### checking shortest distance between two words in a list #####################################
def shortestDistance(n=["axa","ffn", "ty", "bs" ,"oin" ,"bs" ,"axa"], w1="bs", w2="axa"):
    a=n.index(w1)
    b=n.index(w2)
    if a>b:
        a,b=b,a
    m=abs(a-b)
    for i in range(a+1,len(n)):
        if n[i]==n[a]:
            a=i
            m=min(m,abs(a-b))
        if n[i]==n[b]:
            b=i
            m=min(m,abs(a-b))
    return m

#########################String isomorphic checking ###################################
def areIsomorphic( x="pijthbsfy", y="fvladzpbf"):
    d = {}
    s = set()
    if len(x) != len(y):
        return 0

    for i in range(len(x)):
        if x[i] in d:
            if y[i] != d[x[i]]:
                return 0
        else:
            if y[i] in s:
                return 0
            else:
                d[x[i]] = y[i]
                s.add(y[i])

    return 1

######################### String Rotation ###################################
def isRotated(str1="fsbcnuvqhffbsaqxwp",str2= "wpfsbcnuvqhffbsaqx"):
    ac=""
    c=""
    ac+=str1[2:len(str1)]+str1[:2]
    c+=str1[-2:]+str1[:len(str1)-2]
    if((str2==c) or (str2==ac)):
        return 1
    else:
        return 0




def longestSubstrDistinctChars(self, s=""):
    k = set()
    k.add(s[0])
    newString = s[0]
    l = []
    for i in range(1, len(s)):
        if s[i] in k:
            k.clear()
            k.add(s[i])
            l.append(newString)
            newString = s[i]
        else:
            k.add(s[i])
            newString += s[i]
    l.append(newString)
    return (len(max(l, key=len)))







# print(isRotated())
# print(areIsomorphic())
# print(shortestDistance())
# print(palindromeNum())
# print(reverseVovles())
print(longestSubstrDistinctChars())

