import sys

n = int(sys.stdin.readline())
dp = [[[0 for _ in range(1 << 10)] for _ in range(10)] for _ in range(101)]
mod = 1000000000
def sol():

    for i in range(1,10):
        dp[1][i][1 << i] = 1

    for index in range(2,n+1):
        for number in range(0, 10):
            for bit in range(0, 1 << 10):
                if number == 0:
                    dp[index][0][bit | 1 << 0] += dp[index - 1][0 + 1][bit] % mod
                elif number == 9:
                    dp[index][9][bit | 1 << 9] += dp[index - 1][9 - 1][bit] % mod
                else:
                    dp[index][number][bit | 1 << number] += dp[index-1][number+1][bit] % mod
                    dp[index][number][bit | 1 << number] += dp[index - 1][number - 1][bit] % mod

    return

sol()

ans = 0
for i in range(10):
    ans = (ans +dp[n][i][1023]) % mod
print(ans)