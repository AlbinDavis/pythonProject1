
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

def longestSubstrDistinctChars2(s="aewergrththy"):
    k = {}
    k[s[0]]=0
    newString = s[0]
    l = []
    j = 1
    while (j < len(s)):
        if s[j] in k:
            j=k[s[j]]+1
            k.clear()
            k[s[j]] = j
            l.append(newString)
            newString = s[j]
            j+=1
        else:
            k[s[j]]=j
            newString += s[j]
            j+=1

    l.append(newString)
    return (len(max(l, key=len)))



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

def ParenthesisChecker(a="((((("):

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

# Input:
# N = 4, arr[] = [1 3 2 4]
# Output:
# 3 4 4 -1
# Explanation:
# In the array, the next larger element
# to 1 is 3 , 3 is 4 , 2 is 4 and for 4 ?
# since it doesn't exist, it is -1.
def nextLargerElement(self, arr, n):
    stack = []
    result = []
    stack.append(arr[len(arr) - 1])
    result.append(-1)
    for i in range(len(arr) - 2, -1, -1):
        while (len(stack) > 0 and arr[i] > stack[-1]):
            stack.pop()
        if stack:
            result.append(stack[-1])
            stack.append(arr[i])
        else:
            result.append(-1)
            stack.append(arr[i])
    return result[::-1]

# Input:
# N = 7, price[] = [100 80 60 70 60 75 85]
# Output:
# 1 1 1 2 1 4 6
# Explanation:
# Traversing the given input span for 100
# will be 1, 80 is smaller than 100 so the
# span is 1, 60 is smaller than 80 so the
# span is 1, 70 is greater than 60 so the
# span is 2 and so on. Hence the output will
# be 1 1 1 2 1 4 6.
def calculateSpan(a=[100, 80, 60, 70, 60, 75 ,85]):
    stack = []
    stack.append(0)
    l = []
    l.append(1)
    for i in range(1,len(a)):
        while (len(stack) > 0) and (a[stack[-1]] <= a[i]):
            stack.pop()
        if not stack:
            l.append(i + 1)
            stack.append(i)
        else:
            l.append(i - stack[-1])
            stack.append(i)
    return l

# Given two arrays A and B of equal size N, the task is to find if given arrays are equal or not. Two arrays are said to be equal if both of them contain same set of elements, arrangements (or permutation) of elements may be different though.
# Note : If there are repetitions, then counts of repeated elements must also be same for two array to be equal.
def check(A=[1,2,5,4,0],B=[2,4,5,0,1]):
    c1=c(A)
    c2=c(B)
    for i in c1:
        if i in c2 and c2[i]==c1[i]:
            continue
        else:
            return 0
    return 1

def kthElement(arr1=[1,2], arr2=[3,4,5,6], k=5):
    i = 0
    j = 0
    l = []
    c = 0
    while (i < len(arr1) and j < len(arr2)):



        if (arr1[i] < arr2[j]):
            l.append(arr1[i])
            i += 1
        else:
            l.append(arr2[j])
            j += 1
    if i == len(arr1):
        l += arr2[j:]
        return l[k - 1]
    if j == len(arr2):
        l += arr1[i:]
        return l[k - 1]
    return l[k - 1]
# print(isRotated())
# print(areIsomorphic())
# print(shortestDistance())
# print(palindromeNum())
# print(reverseVovles())
# print(longestSubstrDistinctChars())
# print(encode())
# print(isAnagram())
# print(ParenthesisChecker())
# print(calculateSpan())
# print(check())
# print(kthElement())



