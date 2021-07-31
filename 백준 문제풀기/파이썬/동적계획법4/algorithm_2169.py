import sys

n,m = map(int,sys.stdin.readline().rstrip().split())
costs = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
minf = -sys.maxsize
dp = [[minf] * m for _ in range(n)]

dp[0][0] = costs[0][0]
for i in range(1,m):
    dp[0][i] = dp[0][i-1] + costs[0][i]

for j in range(1,n):

    # 밑에서 바로 내려 오는 경우
    for i in range(m):
        dp[j][i] = dp[j-1][i] + costs[j][i]

    L = [minf] * m
    R = [minf] * m
    L[m-1] = dp[j-1][m-1] + costs[j][m-1]
    R[0] = dp[j-1][0] + costs[j][0]

    # 오른쪽으로 가는 경우
    for i in range(1,m):
        R[i] = max(R[i-1],dp[j-1][i]) + costs[j][i]

    # 왼족으로 가는 경우
    for i in range(m-2,-1,-1):
        L[i] = max(L[i+1],dp[j-1][i]) + costs[j][i]

    for i in range(m):
        dp[j][i] = max(L[i],R[i])

print(dp[n-1][m-1])



