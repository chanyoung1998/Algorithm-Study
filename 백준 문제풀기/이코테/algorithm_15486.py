import sys


n = int(sys.stdin.readline().rstrip())
consult = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
dp = [0 for _ in range(n+1)]
max_value = 0

for i in range(n-1,-1,-1):
    time = consult[i][0] + i
    if time <= n:
        dp[i] = max(consult[i][1] + dp[time], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value

print(max_value)