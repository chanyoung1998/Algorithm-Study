import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
fixed = [int(sys.stdin.readline()) for _ in range(m)]
seats_fixed = [0 for _ in range(n+1)]
dp = [[0,0] for _ in range(n+1)]

for fix in fixed:
    seats_fixed[fix] = 1


dp[1][0] = 1
dp[1][1] = 0
dp[2][0] = 1
dp[2][1] = 1 if seats_fixed[1] != 1 and seats_fixed[2] != 1 else 0

for i in range(3,n+1):
    dp[i][0] = dp[i-1][0]
    if seats_fixed[i-1] != 1:
        dp[i][0] += dp[i-1][1]

    if seats_fixed[i] != 1 and seats_fixed[i-1] != 1:
        dp[i][1] = dp[i-2][0] + dp[i-2][1]

print(sum(dp[n]))