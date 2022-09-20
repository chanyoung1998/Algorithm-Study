n,m,k = map(int,input().split())

dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(n+1):
    for j in range(m+1):
        if i == 0 and j == 0:
            dp[i][j] = 0
        elif i == 0 or j == 0:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

if k > dp[n][m]:
    print(-1)
else:
    lo = 0
    hi = dp[n][m]
    pi = n
    pj = m

    ret = ''

    while not (pi == 0 or pj == 0):

        if lo+dp[pi-1][pj] < k <= hi:
            lo = lo + dp[pi-1][pj]
            pj -= 1
            ret += 'z'
        else:
            hi = hi - dp[pi][pj-1]
            pi -= 1
            ret += 'a'

    # print(ret)

    if pi == 0:
        ret += 'z' * ((n+m)-len(ret))
    else:
        ret += 'a' * ((n+m)-len(ret))

    print(ret)
