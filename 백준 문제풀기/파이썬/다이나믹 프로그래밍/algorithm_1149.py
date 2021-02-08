'''
내용:백준 알고리즘 단계별 풀기 다이나믹 프로그래밍  1149 RGB 거리
날짜:21년2월4일
사용 언어:파이썬
'''

n = int(input())
arr = []
dp = []
for i in range(n):
    arr.append(list(map(int, input().split(' '))))

for i in range(n):
    dp.append([0, 0, 0])

dp[0][0] = arr[0][0]
dp[0][1] = arr[0][1]
dp[0][2] = arr[0][2]

# 0부터 n-1번 째 집까지 dp값 구하기
for i in range(1, n):
    for j in range(3):
        dp[i][j] = min(dp[i - 1][(j + 1) % 3], dp[i - 1][(j + 2) % 3]) + arr[i][j]

print(min(dp[n - 1]))