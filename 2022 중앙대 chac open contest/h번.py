import sys
from heapq import heappush,heappop
n,m = map(int,sys.stdin.readline().rstrip().split())
adjlist = [set() for _ in range(n+1)]
dist = [sys.maxsize for _ in range(n+1)]
visit = [False for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    adjlist[a].add(b)
    adjlist[b].add(a)

print(adjlist)
pq = []
dist[1] = 0
heappush(pq,(dist[1],1))

while pq:
    cur_dist, cur = heappop(pq)
    if dist[cur] < cur_dist:
        continue
    visit[cur] = True




for i in range(1,n+1):
    if dist[i] != sys.maxsize:
        print(dist[i])
