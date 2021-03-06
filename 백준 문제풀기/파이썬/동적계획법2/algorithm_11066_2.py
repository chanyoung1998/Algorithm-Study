
# 참고: https://suri78.tistory.com/15
import sys

t = int(sys.stdin.readline())

for _ in range(t):
    k = int(sys.stdin.readline())
    costs = list(map(int,sys.stdin.readline().rstrip().split()))
    dp = [[0 for _ in range(k)] for _ in range(k)]

    #dp[i][j]에다가 기본적으로 sum(costs[i:j+1]) 구해 놓는 것
    for i in range(k-1):
        dp[i][i+1] = costs[i] + costs[i+1]
        for j in range(i+2,k):
            dp[i][j] = dp[i][j-1] + costs[j]


    #구하려는 구간의 길이 = d
    for d in range(2,k):
        #구간의 시작 index = i
        for i in range(k-d):
            j = i + d
            minimum = [dp[i][k] + dp[k+1][j] for k in range(i,j)]
            dp[i][j] += min(minimum)

    
    print(dp[0][k-1])


