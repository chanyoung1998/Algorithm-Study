import sys
from collections import deque
n,m = map(int,sys.stdin.readline().rstrip().split())
inputs = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(m)]
indegree = [0 for _ in range(n+1)]
adjlist = [[] for _ in range(n+1)]

for input in inputs:
    if input[0] >= 2:
        for i in range(1,len(input)-1):
            a = input[i]
            b = input[i+1]
            adjlist[a].append(b)
            indegree[b] += 1



queue = deque()
for i in range(1,n+1):
    if indegree[i] == 0:
        queue.append(i)

ret = []
while queue:
    data = queue.popleft()
    ret.append(data)
    for i in adjlist[data]:
        indegree[i] -= 1
        if indegree[i] == 0:
            queue.append(i)


if len(ret) == n:
    for i in range(n):
        print(ret[i])
else:
    print(0)
