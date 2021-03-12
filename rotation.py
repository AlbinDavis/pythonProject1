# Python3 implementation of right rotation
# of an array K number of times

# Function to rightRotate array
def RightRotate(a, n, k):
    # If rotation is greater
    # than size of array
    k = k % n;

    for i in range(0, n):

        if (i < k):

            # Printing rightmost
            # kth elements
            print(a[n + i - k], end=" ")

        else:

            # Prints array after
            # 'k' elements
            print(a[i - k], end=" ")

    print("\n")


Array = [1, 2, 3, 4, 5]
N = len(Array)
K = 2

RightRotate(Array, N, K)

# i=0
# j=0
# k = int(input())
# arr = list(map(int, input().rstrip().split()))
# while(i!=k):
#     j = arr[len(arr) - 1]
#     for m in reversed(range(len(arr))):
#         arr[m]=arr[m-1]
#     arr[0]=j
#     i+=1
#
#
# for i in arr:
#     print(arr[i])


# using list slicing

# x=1
# l=[1,2,3]
#
# print(l[-x:] + l[:-x]) to right
# print(l[x:] + l[:x]) to left

# Using collection Module

# arr=deque(arr)
#from collections import deque
# arr.rotate(k)


