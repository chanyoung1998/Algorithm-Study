'''
내용:백준 알고리즘 단계별 풀기 다이나믹 프로그래밍  10844 쉬운 계단 수
날짜:21년2월5일
사용 언어:파이썬
'''


n = int(input())
dp = [[0 for i in range(10)] for k in range(101)]

for i in range(1,10):
    dp[1][i] = 1

for j in range(2,n+1):
    for i in range(0,10):
        if i == 0:
            dp[j][0] = dp[j - 1][1]
        elif i == 9:
            dp[j][9] = dp[j - 1][8]
        else:
            dp[j][i] = (dp[j - 1][i - 1]+dp[j - 1][i + 1]) % 1000000000

sum = 0
for i in range(0,10):
    sum += dp[n][i]
print(sum%1000000000)