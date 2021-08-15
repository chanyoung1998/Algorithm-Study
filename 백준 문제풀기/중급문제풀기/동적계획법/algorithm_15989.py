import sys
dp = [0 for _ in range(10001)]

'''
def sol(count_1, count_2, count_3):
    if count_1 * 1 + count_2 * 2 + count_3 * 3 > n:
        return
    elif count_1 * 1 + count_2 * 2 + count_3 * 3 == n:
        if (count_1, count_2, count_3) in check:
            return
        else:
            check.add((count_1, count_2, count_3))
    else:
        sol(count_1 + 1, count_2, count_3)
        sol(count_1, count_2 + 1, count_3)
        sol(count_1, count_2, count_3 + 1)
'''



dp = [[0]*3 for _ in range(10001)]
dp[1][0] = 1
dp[2][0] = 1
dp[2][1] = 1
dp[3][0] = 1
dp[3][1] = 1
dp[3][2] = 1

for i in range(4,10001):
    for j in range(3):
        if j == 0:
            dp[i][j] = dp[i-1][0]
        elif j == 1:
            dp[i][j] = dp[i-2][0] + dp[i-2][1]
        else:
            dp[i][j] = dp[i-3][0] + dp[i-3][1] + dp[i-3][2]


t = int(sys.stdin.readline())
for _ in range(t):
   n = int(sys.stdin.readline().rstrip())
   print(sum(dp[n]))






