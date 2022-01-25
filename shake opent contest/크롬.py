import sys

n,m,k = map(int,sys.stdin.readline().rstrip().split())
tabs = [ ]
#print(len(tabs))
dp = [[[-1 for _ in range(501)] for _ in range(m+1)] for _ in range(n+1)]
ret = sys.maxsize
for _ in range(n):
    #cpu,memory,priority
    tabs.append(tuple(map(int,sys.stdin.readline().rstrip().split())))

dp[0][0][0] = 0

for i in range(n):
    for j in range(m+1):
        for p in range(501):

            if dp[i][j][p] == -1:
                continue
            cpu,mem,pri = tabs[i]
            #i번 째 선택 안 했을 경우
            dp[i+1][j][p] = max(dp[i][j][p],dp[i+1][j][p])
            cpu = min(cpu+j,m)
            #i번 째 선택 했을 경우
            dp[i+1][cpu][p+pri] = max(dp[i+1][cpu][p+pri],dp[i][j][p] + mem)


ret = 1000

for p in range(501):
    if dp[n][m][p] >= k:
        ret = min(ret,p)


if ret == 1000:
    print(-1)
else:
    print(ret)