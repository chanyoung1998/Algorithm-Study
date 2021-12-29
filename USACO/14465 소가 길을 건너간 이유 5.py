import sys
n,k,b = map(int,sys.stdin.readline().rstrip().split())
lights = [1 for _ in range(n)]
for _ in range(b):
    lights[int(sys.stdin.readline()) - 1] = 0

end = 0
fixed = 0
interval_sum = 0
ret = sys.maxsize
for start in range(n):

    while interval_sum < k and end < n:
        if lights[end] == 0:
            fixed += 1
        interval_sum += 1
        end += 1

    if interval_sum == k:
        ret = min(ret,fixed)

    if lights[start] == 0:
        fixed -= 1
    interval_sum -= 1

print(ret)
