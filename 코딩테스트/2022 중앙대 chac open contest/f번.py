import sys

n,m = map(int,sys.stdin.readline().rstrip().split())
arrays = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(m)]
dp = [[[-1 for _ in range(51)] for _ in range(51)] for _ in range(m+1)]

dp[0][0][0] = 0
for k in range(m):
    for i in range(51):
        for j in range(51):
            if dp[k][i][j] == -1:
                continue

            dp[k+1][i][j] = max(dp[k+1][i][j],dp[k][i][j])

            if i + arrays[k][0] > 50 or j + arrays[k][1] > 50:
                continue

            dp[k+1][i+arrays[k][0]][j+arrays[k][1]] = max(dp[k+1][i+arrays[k][0]][j+arrays[k][1]],dp[k][i][j] + arrays[k][2])
ret = []
for x in range(n):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    if dp[m][a][b] == -1:
        dp[m][a][b] = 0
    ret.append((x+1,dp[m][a][b]))
    # print(dp[m][a][b])
ret.sort(key=lambda x:x[1])
for x,y in ret:
    print(x,y)