def pairs(k, arr):
    arr.sort()
    i = 0
    j = 0
    c = 0
    while j < n:
        if abs(arr[j] - arr[i]) == k:
            c += 1
            j += 1
            i += 1
        elif abs(arr[j] - arr[i]) < k:
            j += 1
        else:
            i += 1
    return c


nk = input().split()
n = int(nk[0])
k = int(nk[1])
arr = list(map(int, input().rstrip().split()))
result = pairs(k, arr)
print(result)