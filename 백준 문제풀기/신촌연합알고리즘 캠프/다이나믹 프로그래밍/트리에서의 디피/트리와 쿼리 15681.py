import sys
sys.setrecursionlimit(10**9)
n,r,q = map(int,sys.stdin.readline().rstrip().split())
adjlist = [[] for _ in range(n+1)]
visit = [False for _ in range(n+1)]
dp = [0 for _ in range(n+1)]
for _ in range(n-1):
    u,v = map(int,sys.stdin.readline().rstrip().split())
    adjlist[u].append(v)
    adjlist[v].append(u)


query = []
for _ in range(q):
    u = int(sys.stdin.readline())
    query.append(u)


def dfs(node):

    dp[node] = 1
    visit[node] = True
    for next in adjlist[node]:
        if not visit[next]:
            dfs(next)
            dp[node] += dp[next]

    return

sol(r)
for que in query:
    print(dp[que])