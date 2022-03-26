import sys

INF = sys.maxsize
n = int(sys.stdin.readline())
m= int(sys.stdin.readline())
dist = [[INF for _ in range(n)] for _ in range(n)]
adjlist = [[] for _ in range(n)]
for _ in range(m):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    dist[a-1][b-1] = 1
    dist[b-1][a-1] = 1
    adjlist[a-1].append(b-1)
    adjlist[b-1].append(a-1)

for i in range(n):
    dist[i][i] = 0



for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

dist_max = [0 for _ in range(n)]
for i in range(n):
    for j in range(n):
        if dist[i][j] != INF:
            dist_max[i] = max(dist_max[i],dist[i][j])



visit = [False for _ in range(n)]

def dfs(x):



    visit[x] = True
    index = x
    ret = x
    for next in adjlist[x]:
        if not visit[next]:
            index = dfs(next)
            if dist_max[ret] > dist_max[index]:
                ret = index


    if dist_max[ret] > dist_max[index]:
        ret = index

    return ret
# print(dist_max)
a = []
for i in range(n):
    if not visit[i]:
        a.append(dfs(i)+1)
        # print(visit)

a.sort()
print(len(a))
for i in range(len(a)):
    print(a[i])