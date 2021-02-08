'''
내용:백준 알고리즘 단계별 풀기 다이나믹 프로그래밍 1932 정수 삼각형
날짜:21년2월6일
사용 언어:파이썬
'''

n = int(input())
arr = []
dp = []
for i in range(n):
    arr.append(list(map(int, input().split(' '))))
for i in range(1, n+1):
    dp.append([0] * i)

dp[0][0] = arr[0][0]
for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = dp[i-1][j] + arr[i][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + arr[i][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + arr[i][j]

print(max(dp[n-1]))