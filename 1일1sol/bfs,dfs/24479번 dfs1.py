import sys
sys.setrecursionlimit(100000)

n,m,r = map(int,sys.stdin.readline().rstrip().split())
adjlist =[[] for _ in range(n+1)]
visit = [0 for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    adjlist[a].append(b)
    adjlist[b].append(a)

for i in range(n+1):
    adjlist[i].sort()

def dfs(node):
    global cnt
    if visit[node] == 0:
        visit[node] = cnt
        cnt += 1
        for next in adjlist[node]:
            if visit[next] == 0:
                dfs(next)



cnt = 1
dfs(r)
# print(*visit[1:])
for i in (visit[1:]):
    print(i)


