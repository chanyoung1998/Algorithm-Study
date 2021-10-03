import sys
sys.setrecursionlimit(10**7)
n = int(sys.stdin.readline())
adjlist = [[] for _ in range(n+1)]
visit = [False for _ in range(n+1)]
dp = [[0,0] for _ in range(n+1)]
for _ in range(n-1):
    u,v = map(int,sys.stdin.readline().rstrip().split())
    adjlist[u].append(v)
    adjlist[v].append(u)

def dfs(node):

    visit[node] = True
    dp[node][1] = 1
    for next in adjlist[node]:
        if not visit[next]:
            dfs(next)
            dp[node][0] += dp[next][1]
            dp[node][1] += min(dp[next][1],dp[next][0])

dfs(1)
print(min(dp[1][0],dp[1][1]))


