# 2024 02 02
# 타일 채우기
# 골4

#  1 -> 0
#  2 -> 3
#  3 -> 0
#  4 -> dp[2] * dp[2] + 2 = 11
#  5 -> 0
#  6 -> dp[2] * 2 + dp[2] * dp[2] * dp[2] + 2 * dp[2] = 6 + 27 + 6 = 39 // dp[4] * dp[2] + dp[2] * 2 = 11 * 3 + 3 * 2 =
#  7 -> 0
#  8 -> dp[6] * dp[2] + dp[4] * 2 + dp[2] * 2 + dp[0] * 2

dp = [0 for _ in range(31)]
dp[0] = 1
dp[2] = 3
dp[4] = 11

for i in range(6,31,2):
    dp[i] = dp[i-2] * dp[2]
    for j in range(i-4,-1,-2):
        dp[i] += dp[j] * 2

n = int(input())

print(dp[n])