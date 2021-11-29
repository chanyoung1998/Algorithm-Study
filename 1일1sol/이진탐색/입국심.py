import sys

n,m = map(int,sys.stdin.readline().rstrip().split())
time = []
for _ in range(n):
    time.append(int(sys.stdin.readline()))

def pepleOnTime(t):

    count = 0
    for i in range(n):
        count += t // time[i]

    return count

def binarySearch(start,end,target):

    lo = start
    hi = end
    while lo + 1 < hi:

        mid = (lo+hi) // 2

        if pepleOnTime(mid) >= target:
            hi = mid
        else:
            lo = mid

    return hi


print(binarySearch(-1,sys.maxsize ,m))