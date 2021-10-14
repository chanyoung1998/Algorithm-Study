import sys

n,m = map(int,sys.stdin.readline().rstrip().split())
dp = [[-1 for _ in range(1 << m)] for _ in range(n*m)]


def sol(i,state):


    if state == 0 and i == n * m:
        return 1
    elif state != 0 and i == n *m:
        return 0

    if dp[i][state] != -1:
        return dp[i][state]

    dp[i][state] = 0

    if state & 1:
        dp[i][state] = sol(i+1, state >> 1) % 9901

    if not (state & 1):
        dp[i][state] += sol(i+1,(state >> 1) | (1 << m-1)) % 9901

    if i % m != m-1 and not (state & 3):
        dp[i][state] += sol(i+1,(state >> 1) | 1) % 9901

    return dp[i][state] % 9901


print(sol(0,0))