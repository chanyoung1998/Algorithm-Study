import sys

n = int(sys.stdin.readline())
power = list(map(int,sys.stdin.readline().rstrip().split()))
dp = [1 for _ in range(n)]
power.reverse()

for i in range(1,n):
    for j in range(i):
        if power[i] > power[j]:
            dp[i] = max(dp[i],dp[j] + 1)
print(n - max(dp))