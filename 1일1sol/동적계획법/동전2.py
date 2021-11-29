import sys
n,k = map(int,sys.stdin.readline().rstrip().split())
coins = [int(sys.stdin.readline()) for _ in range(n)]
dp = [sys.maxsize for _ in range(k+1)]
dp[0] = 0
for i in range(n):
    for j in range(coins[i],k+1):
        if j - coins[i] >= 0:
            dp[j] = min(dp[j-coins[i]]+1,dp[j])

print(dp[k] if dp[k] != sys.maxsize else -1)