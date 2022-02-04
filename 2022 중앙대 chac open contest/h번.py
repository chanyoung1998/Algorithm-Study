import sys
from heapq import heappush,heappop
from collections import deque

# https://www.geeksforgeeks.org/shortest-path-in-a-complement-graph/
n,m = map(int,sys.stdin.readline().rstrip().split())
adjlist = [set() for _ in range(n+1)]
dist = [sys.maxsize for _ in range(n+1)]
visit = set(range(1,n+1))

for _ in range(m):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    adjlist[a].add(b)
    adjlist[b].add(a)

# print(adjlist)
# pq = []
# dist[1] = 0
# heappush(pq,(dist[1],1))

pq = deque()
dist[1] = 0
pq.append(1)
while pq:
    # cur_dist, cur = heappop(pq)
    cur = pq.popleft()
    visit -= {cur}
    removed = set()
    for next in visit:
        if next not in adjlist[cur]:
            dist[next] = dist[cur] + 1
            removed.add(next)
            pq.append(next)
    visit -= removed

for i in range(1,n+1):
    if dist[i] != sys.maxsize:
        print(dist[i])
    else:
        print(-1)
