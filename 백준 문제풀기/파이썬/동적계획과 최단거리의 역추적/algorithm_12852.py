'''
내용:백준 알고리즘 단계별 풀기 동적계획과 최단거리의 역추적 12852번 1로 만들기
날짜:21년4월 17일
사용 언어:파이썬
'''

import sys

n = int(sys.stdin.readline())
dp = [[sys.maxsize,-1] for _ in range(n+1)]
dp[1][0] = 0
dp[1][1] = [1]

for i in range(2,n+1):
    dp[i][0] = dp[i-1][0] + 1
    dp[i][1] = dp[i-1][1] + [i]

    if i % 2 == 0 and dp[i//2][0] + 1 < dp[i][0]:
        dp[i][0] = dp[i//2][0] + 1
        dp[i][1] = dp[i//2][1] + [i]

    if i % 3 == 0 and dp[i//3][0] + 1 < dp[i][0]:
        dp[i][0] = dp[i//3][0] + 1
        dp[i][1] = dp[i//3][1] + [i]
print(dp[n][0])
for i in dp[n][1][::-1]:
    print(i,end=' ')


