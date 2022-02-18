import sys
# 카드 1~34
n = sys.stdin.readline().rstrip()
dp = [0 for _ in range(len(n))]
dp[0] = 1

if len(n) >= 2:
    dp[1] = 2 if 10 < int(n[0:2]) <= 34 else 1
    for i in range(2,len(n)):
        if 1 <= int(n[i]):
            dp[i] = dp[i-1]
        if 10 <= int(n[i-1:i+1]) <= 34:
            dp[i] += dp[i-2]

print(dp[len(n)-1])
