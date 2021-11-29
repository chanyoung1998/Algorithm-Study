import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    stickers = []
    for _ in range(2):
        stickers.append(list(map(int,sys.stdin.readline().rstrip().split())))

    dp = [[[0,0] for _ in range(n)] for _ in range(2)]
    dp[0][0][1] = stickers[0][0]
    dp[1][0][1] = stickers[1][0]
    for i in range(1,n):
        for j in range(2):
            dp[j][i][0] = max(max(dp[0][i-1]),max(dp[1][i-1]))
            dp[j][i][1] = stickers[j][i] + (max(dp[0][i-1]) if j == 1 else max(dp[1][i-1]))

    print(max(max(dp[0][n-1]),max(dp[1][n-1])))