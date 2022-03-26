import sys
from heapq import heappop,heappush
INF = 987654321
m,n = map(int,sys.stdin.readline().rstrip().split())
miro = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(n)]
dist = [[INF for _ in range(m)] for _ in range(n)]
dist[0][0] = 0
pq =[]
heappush(pq,(0,0,0)) # w,x,y
dx = [-1,1,0,0]
dy = [0,0,-1,1]

while pq:
    w,x,y = heappop(pq)

    if dist[x][y] < w:
        continue

    for dir in range(4):
        p = x +dx[dir]
        q = y + dy[dir]
        if 0 <= p < n and 0 <= q < m:
            if dist[p][q] > w + miro[p][q]:
                dist[p][q] = w + miro[p][q]
                heappush(pq,(w + miro[p][q],p,q))

print(dist[n-1][m-1])

