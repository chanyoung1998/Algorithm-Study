import sys

n, m = map(int,sys.stdin.readline().rstrip().split())
array = list(map(int,sys.stdin.readline().rstrip().split()))
max = max(array)

def check(a):

    ret = 0
    for i in range(n):
        if array[i] >= a:
            ret += array[i] - a

    return ret


def binarySearch(start,end,target):

    while start + 1 < end:
        mid = (start+end)//2
        if check(mid) >= target:
            start = mid
        else:
            end = mid

    return start

print(binarySearch(0,max+1,m))


