import sys
from collections import deque

INF = 10000
def bfs(x):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    dq = deque()
    start = nodes[x]
    dq.append((start,0))
    visit[start[0]][start[1]] = 0

    while dq:
        cur,dis = dq.popleft()

        for i in range(4):
            p = cur[0] + dx[i]
            q = cur[1] + dy[i]

            if 0 <= p < n and 0 <= q < n and maps[p][q] != '1' and visit[p][q] == -1:
                visit[p][q] = dis + 1
                dq.append(((p,q),dis+1))

def find(x):
    if parent[x] == -1:
        return x

    parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)

    if x> y:
        parent[x] = y
    else:
        parent[y] = x





n,m = map(int,sys.stdin.readline().rstrip().split())
maps = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
edge = []
nodes = []
for i in range(n):
    for j in range(n):
        if maps[i][j] == 'K' or maps[i][j] == 'S':
            nodes.append(tuple((i,j)))

for i in range(m+1):
    visit = [[-1 for _ in range(n)] for _ in range(n)]
    bfs(i)
    for j in range(i+1,m+1):
        if visit[nodes[j][0]][nodes[j][1]] == -1:
            continue
        edge.append((i,j,visit[nodes[j][0]][nodes[j][1]]))

edge.sort(key=lambda x:x[2])
parent =[-1 for _ in range(m+1)]

ret = 0
cnt = 0
for a,b,c in edge:

    if cnt == m:
        break

    if find(a) != find(b):
        union(a,b)
        ret += c
        cnt += 1

if cnt != m:
    print(-1)
else:
    print(ret)