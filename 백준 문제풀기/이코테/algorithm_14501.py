import sys


n = int(sys.stdin.readline().rstrip())
consult = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
dp = [0 for _ in range(n)]

for i in range(n):
    temp = 0
    if consult[i][0] + i <= n:
        dp[i] += consult[i][1]

    for j in range(i):
        if consult[j][0] + j <= i:
            temp = max(temp,dp[j])
    dp[i] += temp

print(max(dp))


