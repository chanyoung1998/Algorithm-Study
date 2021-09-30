import sys
sys.setrecursionlimit(20000)
n = int(sys.stdin.readline())
population = [0] + list(map(int,sys.stdin.readline().rstrip().split()))
adjlist = [[] for _ in range(n+1)]
visit = [False for _ in range(n+1)]
dp = [[0,0] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    adjlist[a].append(b)
    adjlist[b].append(a)


def sol(node):

    visit[node] = True
    dp[node][1] = population[node]
    for next in adjlist[node]:
        if not visit[next]:
            sol(next)
            dp[node][1] += dp[next][0]
            dp[node][0] += max(dp[next][0],dp[next][1])


sol(1)
print(max(dp[1][0],dp[1][1]))