'''
내용:백준 알고리즘 단계별 풀기 다이나믹 프로그래밍  11053 가장 긴 부분 수열
날짜:21년2월3일
사용 언어:파이썬
'''

n = int(input())
A = list(map(int,input().split()))
dp = [0 for _ in range(1001)]
def LIS(n):
    if n == 1:
        dp[0] = 1
        return

    dp[0] = 1
    #dp[i]값 결정하기
    for i in range(1,n):
        temp = [0]
        for j in range(i):
            if A[i] > A[j]:
                temp.append(dp[j])
        dp[i] = max(temp) + 1
    #print(dp[n-1])
    return

LIS(n)
print(max(dp))

''' 다른 풀이
import sys

n = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))
length = [0 for _ in range(n)]


for i in range(n):
    length[i] = 1
    for j in range(i):
        if sequence[j] < sequence[i] and length[i] < length[j] + 1:
            length[i] = length[j] + 1

print(max(length))

'''