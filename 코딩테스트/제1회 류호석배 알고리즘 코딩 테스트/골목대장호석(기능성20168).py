import sys
from collections import deque
sys.setrecursionlimit(10**5 + 1)
n,m,a,b,c = map(int,sys.stdin.readline().rstrip().split())
adjlist = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int,sys.stdin.readline().rstrip().split())
    adjlist[u].append((v,w))
    adjlist[v].append((u,w))

start = a
end = b
visited = [False for _ in range(n+1)]
humiliation = -1
ret = []
def sol(node,cost,humiliation):

    visited[node] = True

    if node == end:
        visited[node] = False
        if cost <= c:
            ret.append(humiliation)
        return

    for next,weight in adjlist[node]:
        if not visited[next]:
            sol(next,cost+weight,max(humiliation,weight))

    visited[node] = False
    return

sol(start,0,0)
if ret != []:
    print(min(ret))
else:
    print(-1)