import sys
from collections import deque

n =int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
part = [[0 for _ in range(n)] for _ in range(n)]
indegree = [0 for _ in range(n)]
adjlist = [[] for _ in range(n)]
for _ in range(m):
    x,y,k = map(int,sys.stdin.readline().rstrip().split())
    part[x-1][y-1] = k
    indegree[x-1] += 1
    adjlist[y-1].append(x-1)

basic = []
dq = deque()
for i in range(n):
    if indegree[i] == 0:
        basic.append(i)
        dq.append(i)

while dq:
    x = dq.popleft()
    for next in adjlist[x]:
        indegree[next] -= 1
        for basic_part in basic:
            part[next][basic_part] += part[x][basic_part]*part[next][x]

        if indegree[next] == 0:
            dq.append(next)
# print(part[n-1])

basic.sort()
for basic_part in basic:
    print(basic_part+1,part[n-1][basic_part])