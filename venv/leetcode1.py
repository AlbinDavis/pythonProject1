
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




def longestSubstrDistinctChars(s="aewergrththy"):
    k = ""
    l = ""
    for j in range(len(s)):
        if s[j] in k:
            temp=k.index(j) + 1
            k= j
            if len(l) < len(newString):
                l = newString
            newString = s[j]
            j += 1
        else:
            k+=s[j]
            j += 1

    if len(l) < len(newString):
        l = newString
    return len(l)

    # k = {}
    # k[s[0]]=0
    # newString = s[0]
    # l = []
    # j = 1
    # while (j < len(s)):
    #     if s[j] in k:
    #         j=k[s[j]]+1
    #         k.clear()
    #         k[s[j]] = j
    #         l.append(newString)
    #         newString = s[j]
    #         j+=1
    #     else:
    #         k[s[j]]=j
    #         newString += s[j]
    #         j+=1
    #
    # l.append(newString)
    # return (len(max(l, key=len)))



#############Maximum number of characters between any two same character#
def maxChars(self, s):
    d = c(s)
    m = -1
    for i in s:
        if d[i] > 1:
            d[i] = 1
            j = len(s) - 1
            while (s[j] != i):
                j -= 1
            m = max((j - 1) - s.index(i), m)

    return m


# m=-1
# first_index=[-1 for i in range(225)]
# d=c(s)
# for i in range(len(s)):
#     start_index=first_index[ord(s[i])]

#     if start_index ==-1:
#         first_index[ord(s[i])]=i

#     else:
#         m=max(m,i-start_index-1)

# return m


################Run Length Encoding#####################
def encode(a="aasasdasfc"):
    if len(a)==1:
        return a+"1"
    s=""
    c=1
    for i in range(1,len(a)):
        if a[i]!=a[i-1]:
            s+=a[i-1]+str(c)
            c=1
        else:
            c+=1
    s+=a[len(a)-1]+str(c)
    return s



from collections import Counter as c
def isAnagram(a='b',b='d'):
    c1 = c(a)
    c2 = c(b)
    if len(c1)!=len(c2):
        return False
    return c1==c2

def ParenthesisChecker(x="({[]})"):
    s = ('{', '(', '[')
    stack = []
    for i in x:
        if i in s:
            stack.append(i)
        else:
            if not stack:
                return False
            if i == '}':
                if stack.pop() != '{':
                    return False

            if i == ']':
                if stack.pop() != '[':
                    return False
            if i == ')':
                if stack.pop() != '(':
                    return False

    if stack:
        return False
    return True

# print(isRotated())
# print(areIsomorphic())
# print(shortestDistance())
# print(palindromeNum())
# print(reverseVovles())
# print(longestSubstrDistinctChars())
# print(encode())
# print(isAnagram())
# print(ParenthesisChecker())

