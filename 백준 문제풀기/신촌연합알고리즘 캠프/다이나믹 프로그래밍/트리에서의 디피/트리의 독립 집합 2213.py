import sys
sys.setrecursionlimit(20000)
n = int(sys.stdin.readline())
weight = [0]+list(map(int,sys.stdin.readline().rstrip().split()))
adjlist = [[] for _ in range(n+1)]
visit = [False for _ in range(n+1)]
dp = [[0,0] for _ in range(n+1)]
route = [[[],[]] for _ in range(n+1)]
for _ in range(n-1):
    u,v = map(int,sys.stdin.readline().rstrip().split())
    adjlist[u].append(v)
    adjlist[v].append(u)


def dfs(node):

    visit[node] = True
    dp[node][1] = weight[node]
    route[node][1] = [node]
    for next in adjlist[node]:
        if not visit[next]:
            dfs(next)
            dp[node][1] += dp[next][0]
            route[node][1] += route[next][0]
            if dp[next][0] > dp[next][1]:
                dp[node][0] += dp[next][0]
                route[node][0] += route[next][0]
            else:
                dp[node][0] += dp[next][1]
                route[node][0] += route[next][1]

    return

dfs(1)
if dp[1][0] > dp[1][1]:
    print(dp[1][0])
    print(*sorted(route[1][0]))
else:
    print(dp[1][1])
    print(*sorted(route[1][1]))
