def hurdleRace(k, height):
    if max(height) - k <= 0:
        print(0)
    else:
        print(max(height) - k)


nk = input().split()

n = int(nk[0])

k = int(nk[1])

height = list(map(int, input().rstrip().split()))

hurdleRace(k, height)
