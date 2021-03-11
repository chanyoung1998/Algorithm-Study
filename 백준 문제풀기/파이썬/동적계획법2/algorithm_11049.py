'''
내용:백준 알고리즘 단계별 풀기 동적 계획법 11049 행렬 곱셈 순서
날짜:21년3월4일
사용 언어:파이썬
'''

import sys

n = int(sys.stdin.readline())
matrix = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

for i in range(n-1):
    dp[i][i+1] = matrix[i][0] * matrix[i][1] * matrix[i+1][1]


# 주의:a,b,c,d 행렬이 있을 때 가능 조합 : (a + b,c,d) (a,b + c,d) (a,b,c + d)이다
for d in range(2,n):
    for i in range(n-d):
        j = i + d
        minimum = [dp[i][k] + dp[k+1][j] + matrix[i][0] * matrix[k][1] * matrix[j][1] for k in range(i,j)]
        dp[i][j] = min(minimum)


print(dp[0][n-1])
