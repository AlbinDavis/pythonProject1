def find(arr, x, y):
    c1 = arr.count(x)
    c2 = arr.count(y)
    s = 0
    if (c1 == 0 and c2 == 0) or (c1 == 0 and c2 != 0) or (c1 != 0 and c2 == 0):
        print(-1)
    elif c1 - c2 > 0:
        for i in range(len(arr)):
            if arr[i] == x:
                s += 1
            if s > c2:
                print(i - 1)
                break
    elif c1 - c2 < 0:
        for i in range(len(arr)):
            if arr[i] == y:
                s += 1
            if s > c1:
                print(i - 1)
                break
    else:
        print(len(arr) - 1)


n = int(input())
for i in range(n):
    nxy = list(map(int, input().rstrip().split()))
    arr = list(map(int, input().rstrip().split()))
    x = nxy[1]
    y = nxy[2]
    find(arr, x, y)
