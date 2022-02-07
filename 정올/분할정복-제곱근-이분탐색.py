import sys

n = int(sys.stdin.readline())

start = 0
end = n+1

while start + 1 < end:
    mid = (start+end)//2

    if mid ** 2 > n:
        end = mid
    else:
        start = mid
print(start)