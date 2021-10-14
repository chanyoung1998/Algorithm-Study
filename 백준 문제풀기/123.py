import sys

n,m = map(int,sys.stdin.readline().rstrip().split())
k = int(sys.stdin.readline())
hole = [tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(k)]
dp = [[0 for _ in range(m)] for _ in range(n)]
mod = 10**9 + 7
for i, j in hole:
    dp[i-1][j-1] = -1

flag = False
for i in range(m):
    for j in range(n):

        if i % 2 == 1:

            if dp[j][i] == -1:
                continue


            if j-1 >= 0:
                dp[j][i] += dp[j-1][i] if dp[j-1][i] != -1 else 0
                dp[j][i] %= mod
            if i-1 >= 0:
                dp[j][i] += dp[j][i-1] if dp[j][i-1] != -1 else 0
                dp[j][i] %= mod
            if j+1 < n and i - 1 >= 0:
                dp[j][i] += dp[j+1][i-1] if dp[j+1][i-1] != -1 else 0
                dp[j][i] %= mod
        else:

            if i == 0:
                if dp[j][i] == -1:
                    flag = True
                    continue

                if flag:
                    dp[j][i] = 0
                else:
                    dp[j][i] = 1

                continue

            if dp[j][i] == -1:
                continue

            if j - 1 >= 0:
                dp[j][i] += dp[j - 1][i] if dp[j - 1][i] != -1 else 0
                dp[j][i] %= mod
            if i - 1 >= 0:
                dp[j][i] += dp[j][i - 1] if dp[j][i - 1] != -1 else 0
                dp[j][i] %= mod

            if j-1 >= 0 and i -1 >= 0:
                dp[j][i] += dp[j-1][i-1] if dp[j-1][i-1] != -1 else 0
                dp[j][i] %= mod

'''for _ in dp:
    print(_)
'''
print(dp[n-1][m-1])