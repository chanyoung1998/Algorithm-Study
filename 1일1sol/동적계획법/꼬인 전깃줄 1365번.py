import sys

n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
LIS = [arr[0]]


for i in range(1,n):

    if LIS[-1] < arr[i]:
        LIS.append(arr[i])
    else:
        lo = -1
        hi = len(LIS) -1
        target = arr[i]
        while lo + 1 < hi:
            mid = (lo +hi) //2

            if LIS[mid] >= target:
                hi = mid
            else:
                lo = mid

        LIS[hi] = target

print(n-len(LIS))