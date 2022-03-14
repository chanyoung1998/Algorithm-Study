import sys
from math import ceil,log2
sys.setrecursionlimit(40001)
def dfs(root):


    for next, c in edge[root]:
        if not visit[next]:
            visit[next] = True
            height[next] = height[root] + 1
            parent[next] = root
            dist[next] = c
            dfs(next)

def build():
    for i in range(n):
        ascendent[0][i] = parent[i]
        distance[0][i] = dist[i]

    for j in range(1,x+1):
        for i in range(n):
            ascendent[j][i] = ascendent[j-1][ascendent[j-1][i]]
            distance[j][i] = distance[j-1][ascendent[j-1][i]] + distance[j-1][i]
def lca(a,b):

    dist_a = 0
    dist_b = 0

    if height[b] > height[a]:
        a,b= b,a


    if height[a] > height[b]:
        diff = height[a]- height[b]
        w = ceil(log2(diff))
        while w >= 0:
            if diff >= 2**w:
                diff -= 2**w
                dist_a += distance[w][a]
                a = ascendent[w][a]
                w -= 1
            else:
                w -= 1

    if a == b:
        return dist_a

    else:
        for h in range(x,-1,-1):
            if ascendent[h][a] != ascendent[h][b]:
                dist_a += distance[h][a]
                dist_b += distance[h][b]
                a =ascendent[h][a]
                b=ascendent[h][b]

        dist_a += distance[0][a]
        dist_b += distance[0][b]
        return dist_a + dist_b



n =int(sys.stdin.readline())
edge = [[] for _ in range(n)]
height = [0 for _ in range(n)]
parent = [0 for _ in range(n)]
visit = [0 for _ in range(n)]
dist =[0 for _ in range(n)]

for _ in range(n-1):
    a,b,c = map(int,sys.stdin.readline().rstrip().split())
    edge[a-1].append((b-1,c))
    edge[b-1].append((a-1,c))

visit[0] = True
height[0] = 1
parent[0] = 0
dfs(0)
max_depth = max(height)
x = ceil(log2(max_depth))
ascendent = [[0 for _ in range(n)] for _ in range(x+1)]
distance = [[0 for _ in range(n)] for _ in range(x+1)]

build()


m = int(sys.stdin.readline())
for _ in range(m):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    print(lca(a-1,b-1))