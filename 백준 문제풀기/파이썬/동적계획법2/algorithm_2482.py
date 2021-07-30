import sys
sys.setrecursionlimit(10000000)
mod = 1000000003
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

def sol(number,i):

    if number/i == 2:
        return 2

    if i == 1:
        return number

    if dp[number][i] == 0:
        dp[number][i] = (sol(number-2,i-1) + sol(number-1,i)) % mod
        return dp[number][i]
    else:
        return dp[number][i]

if n/2 < k:
    print(0)
else:
    print(sol(n,k))
