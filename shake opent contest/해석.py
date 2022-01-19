import sys

inputs = list(map(int,sys.stdin.readline().rstrip()))
length = len(inputs)
dp = [[0 for _ in range(length)] for _ in range(length)]
mod = 10**9 + 7
#print(inputs)

for i in range(length-1):
    if inputs[i] != inputs[i+1]:
        dp[i][i+1] = 1
for i in range(length):
    for j in range(length):
        if i > j:
            dp[i][j] = 1

for interval in range(2,length):
    for start in range(length-interval):
        end = start + interval
        for i in range(start,end+1):
            if i == end and inputs[start] != inputs[i]:
                dp[start][end] = (dp[start][end] + dp[start + 1][i - 1]) % mod
            elif inputs[start] != inputs[i]:
                dp[start][end] = (dp[start][end] + dp[start+1][i-1]*dp[i+1][end]) % mod


print(dp)
print(dp[0][length-1])