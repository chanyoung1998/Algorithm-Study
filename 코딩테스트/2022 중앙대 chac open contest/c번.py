import sys

n,m = map(int,sys.stdin.readline().rstrip().split())
maps = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
mod = 1000000007
dp = [[0 for _ in range(m)] for _ in range(n)]
for i in range(m):
    dp[n-1][i] = maps[n-1][i]
for i in range(n-2,-1,-1):
    for j in range(m):
        if maps[i][j] == 0:
            continue
        dp[i][j] = dp[i+1][j]
        if j+1 < m:
            dp[i][j] += dp[i+1][j+1]
        if j-1 >= 0:
            dp[i][j] += dp[i+1][j-1]

print(sum(dp[0]) % mod)

