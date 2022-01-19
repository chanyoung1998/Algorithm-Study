import sys

n,m,k = map(int,sys.stdin.readline().rstrip().split())
tabs = []
dp = [[[-sys.maxsize for _ in range(500)] for _ in range(m+1)] for _ in range(n)]
ret = sys.maxsize
for _ in range(n):
    tabs.append(tuple(map(int,sys.stdin.readline().rstrip().split())))

'''for j in range(m):
    for p in range(500):
        if tabs[0][0] <= j and tabs[0][2] <= p:
            dp[0][j][p] = tabs[0][1]
'''
for i in range(n):
    for j in range(m+1):
        for p in range(500):
            if j - tabs[i][0] >= 0 and p-tabs[i][2] >= 0:
                dp[i][j][p] = max(dp[i-1][j][p],dp[i-1][j-tabs[i][0]][p-tabs[i][2]] + tabs[i][1])
            else:
                if i -1 >= 0:
                    dp[i][j][p] = max(dp[i-1][j][p],0)
            if j >= m and dp[i][j][p] >= k:
                ret = min(ret, p)
                # print(dp[i][j][p])
                # print(i,j,p)


if ret == sys.maxsize:
    print(-1)
else:
    print(ret)