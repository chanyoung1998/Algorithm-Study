import sys

INF = sys.maxsize
n = int(sys.stdin.readline())
costs = [[0,0,0]]
for _ in range(n):
    costs.append(list(map(int,sys.stdin.readline().rstrip().split())))

dp = [[INF]*3 for _ in range(n+1)]
ans = INF
for first in range(3):
    for k in range(3):
        if first == k:
            dp[1][k] = costs[1][k]
        else:
            dp[1][k] = INF

    for i in range(2,n+1):
        for j in range(3):
            if j == 0:
                dp[i][j] = costs[i][j] + min(dp[i-1][1],dp[i-1][2])
            elif j == 1:
                dp[i][j] = costs[i][j] + min(dp[i - 1][0], dp[i - 1][2])
            elif j == 2:
                dp[i][j] = costs[i][j] + min(dp[i - 1][0], dp[i - 1][1])

    for k in range(3):
        if k == first:
            continue
        ans = min(ans,dp[n][k])
print(ans)

