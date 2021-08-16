import sys

n = int(sys.stdin.readline().rstrip())

dp = [0 for _ in range(101)]

dp[1] = 1
dp[2] = 2
dp[3] = 3
dp[4] = 4
dp[5] = 5
A = 1
cnt = 0
for i in range(6,101):
    for j in range(1,i-2):
        dp[i] = max(dp[i],dp[j] * (i-j-1))

print(dp[n])
