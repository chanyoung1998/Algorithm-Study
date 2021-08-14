import sys



dp = [0 for _ in range(10001)]

for i in range(4,10001):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]


t = int(sys.stdin.readline())
for _ in range(t):
   n = int(sys.stdin.readline().rstrip())
   print(dp[n])







