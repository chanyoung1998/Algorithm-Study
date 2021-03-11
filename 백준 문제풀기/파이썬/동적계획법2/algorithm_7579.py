'''
내용:백준 알고리즘 단계별 풀기 동적 계획법 7579 앱
날짜:21년3월11일
사용 언어:파이썬
'''

import sys

N,M = map(int,sys.stdin.readline().split())
memories = list(map(int,sys.stdin.readline().split()))
costs = list(map(int,sys.stdin.readline().split()))
dp = [[0 for _ in range(sum(costs) + 1)] for _ in range(N)]

for i in range(costs[0],sum(costs) + 1):
    dp[0][i] = memories[0]

for i in range(1,N):
    for j in range(sum(costs) + 1):
        if costs[i] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(memories[i] + dp[i-1][j-costs[i]], dp[i-1][j])


for _ in range(sum(costs) + 1):
    if dp[N-1][_] >= M:
        print(_)
        break



