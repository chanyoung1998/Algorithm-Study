import sys

n = int(sys.stdin.readline().rstrip())
costs = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
INF = sys.maxsize
dp = [[-1 for _ in range(1 << n)] for _ in range(n)]

def sol(x,visited):

    if visited == (1 << n) - 1:
        return 0

    if dp[x][visited] != -1:
        print(x,visited)
        return dp[x][visited]

    dp[x][visited] = INF
    for i in range(n):
        if visited & (1 << i):
            continue

        dp[x][visited] = min(dp[x][visited],sol(x+1,visited | 1 << i) + costs[x][i])

    return dp[x][visited]

print(sol(0,0))
