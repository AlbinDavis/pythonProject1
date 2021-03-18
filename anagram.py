d = ['listen','tow','silent','lisent','two','abc','no','on']
query = ['two','bca','no','listen']
for i in query:
    s = 0
    for j in d:
        if sorted(j)==sorted(i):
            s+=1
    print(s)



