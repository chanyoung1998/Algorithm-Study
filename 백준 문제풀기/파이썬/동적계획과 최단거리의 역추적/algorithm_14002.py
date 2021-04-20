'''
내용:백준 알고리즘 단계별 풀기 동적계획과 최단거리의 역추적 14002 가장 긴 증가하는 부분 수열4
날짜:21년4월 17일
사용 언어:파이썬
'''

import sys

n = int(sys.stdin.readline().rstrip())
numbers = list(map(int,sys.stdin.readline().rstrip().split()))
dp = [1 for _ in range(n)]
array = [[x] for x in numbers]
for i in range(n):
    for j in range(i):
        if numbers[i] > numbers[j]:
            if dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                array[i] = array[j] + [numbers[i]]
length = 0
flag = 0
for i in range(n):
    if length < dp[i]:
        flag = i
        length = dp[i]
print(length)
print(*array[flag])