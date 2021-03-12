arr = [1, 2, 3, 4, 5]
n = len(arr)
k = 2

k = k % n

# Prints the rotated array from start position
for i in range(n):
    print(arr[(k + i) % n])




#

