'''
내용:백준 알고리즘 단계별 풀기 다이나믹 프로그래밍  2565 전깃줄
날짜:21년2월8일
사용 언어:파이썬
'''

n = int(input())
A = [0 for _ in range(501)]
dp = [0 for _ in range(501)]
for i in range(n):
    temp = list(map(int,input().split(' ')))
    A[temp[0]] = temp[1]

for i in range(501):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i],dp[j]+1)

print(n-max(dp))