import sys
from heapq import heappop,heappush

n,m = map(int,sys.stdin.readline().rstrip().split())
solved = [False for _ in range(n+1)]
degree = [0 for _ in range(n+1)]
adjlist = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    degree[b] += 1
    adjlist[a].append(b)

topology = []

for i in range(1,n+1):
    if degree[i] == 0:
        heappush(topology,i)

while topology:
    cur = heappop(topology)
    print(cur,end=' ')

    for next in adjlist[cur]:
        degree[next] -= 1
        if degree[next] == 0:
            heappush(topology,next)


