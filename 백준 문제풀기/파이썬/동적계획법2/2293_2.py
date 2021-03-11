'''
내용:백준 알고리즘 단계별 풀기 동적 계획법 2293 동전1
날짜:21년3월 8일
사용 언어:파이썬
'''
# 사용한 동전의 구성이 같은데, 순서만 다른 것은 같은 경우이다.
import sys

n, k = map(int,sys.stdin.readline().split())
value = [int(sys.stdin.readline()) for _ in range(n)]

dp = [0 for _ in range(k+1)]
dp[0] = 1

# v일 때 dp[i] += dp[i-v]
for v in value:
    for i in range(1,k+1):
        if i - v >= 0:
            dp[i] += dp[i-v]

print(dp[k])