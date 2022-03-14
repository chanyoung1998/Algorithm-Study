import sys

n = int(sys.stdin.readline().rstrip())
maps = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
dp = [[[0,0,0] for _ in range(n)] for _ in range(n)]

#0:가로,1:세로:2:대각선
dp[0][1][0] = 1

for i in range(n):
    for j in range(n):
        for k in range(3):
            if k == 0 and maps[i][j] != 1:
                dp[i][j][k] += dp[i][j-1][0] + dp[i][j-1][2] if j -1 >= 0 else 0
            elif k == 1 and maps[i][j] != 1:
                dp[i][j][k] += dp[i-1][j][1] + dp[i-1][j][2] if i -1 >= 0 else 0
            elif k == 2 and maps[i][j] != 1 and maps[i][j-1] != 1 and maps[i-1][j] != 1:
                dp[i][j][k] += dp[i-1][j-1][0]+dp[i-1][j-1][1] + dp[i-1][j-1][2] if i-1 >= 0 and j-1>= 0 else 0

print(sum(dp[n-1][n-1]))