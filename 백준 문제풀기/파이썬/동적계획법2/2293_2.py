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

for i,v in enumerate(value):
    for j in range(1,k+1):

        if i > 0:
            count = 0
            temp = j
            while temp > 0 :
                count += 1
                temp -= v
            dp[j] += count

        if j % v == 0:
            dp[j] += 1

print(dp[k])