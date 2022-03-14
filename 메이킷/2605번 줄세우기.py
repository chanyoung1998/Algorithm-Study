import sys

n = int(sys.stdin.readline())
inputs = list(map(int,sys.stdin.readline().rstrip().split()))
ret = []
i = 1
for x in inputs:
    if not ret:
        ret.append(i)
    else:
        ret.insert(i-x-1,i)

    i += 1
print(*ret)