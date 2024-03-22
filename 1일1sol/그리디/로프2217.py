import sys

n = int(sys.stdin.readline())
ropes = [int(sys.stdin.readline()) for _ in range(n)]

ropes.sort(reverse=True)

ret = 0
cnt = 1
for r in ropes:

    if ret < r * cnt:
        ret = r * cnt

    cnt += 1

print(ret)
