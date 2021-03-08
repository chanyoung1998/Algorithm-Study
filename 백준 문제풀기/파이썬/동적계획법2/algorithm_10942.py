'''
내용:백준 알고리즘 단계별 풀기 동적 계획법 10942 팰린드롬
날짜:21년3월8일
사용 언어:파이썬
'''

import sys

n = int(sys.stdin.readline())
array = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
dp = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    dp[i][i] = 1
    if i < n-1 and array[i] == array[i+1]:
        dp[i][i+1] = 1

#d구간의 길이
for d in range(2, n):
    # 구간의 시작 index = i
    for i in range(n - d):
        j = i + d
        if array[i] == array[j] and dp[i+1][j-1] == 1:
            dp[i][j] = 1

for _ in range(m):
    s, e = map(int,sys.stdin.readline().split())
    print(dp[s-1][e-1])