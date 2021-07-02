import sys

n = int(sys.stdin.readline().rstrip())
costs = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

dp = [[[0 for _ in range(1 << n)] for _ in range(n)] for _ in range(n)]

def sol():
    full = (1 << n) - 1

    for i in range(n):
        dp[0][i][1<<i] = costs[0][i]

    for person in range(1,n):
        for job in range(n):
            for bit in range(1<<n):
                if bit & 1 << job == 1:
                    continue
                dp[person][job][bit| 1 << job] = min(dp[person][job][bit| 1 << job], )