import sys

n = int(sys.stdin.readline().rstrip())
temperature = [tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
temperature.sort(key=lambda x:(x[0],x[1]))

left = -271
right = 10001
cnt = 1
for l,r in temperature:
    flag = False
    if left <= l <= right:
        left = l
        flag = True

    if left <= r <= right:
        right = r
        flag = True

    if not flag:
        cnt += 1
        left = l
        right = r

print(cnt)