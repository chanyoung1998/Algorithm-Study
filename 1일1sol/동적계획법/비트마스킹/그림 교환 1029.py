import sys

n = int(sys.stdin.readline().rstrip())
cost = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(n)]
dp = [[[-1 for _ in range(1<<n)] for _ in range(10)] for _ in range(n)]



def dfs(pre_cost,cur,state):

    if state == (1<<n) - 1:
        dp[cur][pre_cost][state] = 1
        return 1
    if dp[cur][pre_cost][state] != -1:
        return dp[cur][pre_cost][state]

    dp[cur][pre_cost][state] = 1

    for i in range(n):
        if state & (1<<i):
            continue
        else:
            if cost[cur][i] >= pre_cost:
                dp[cur][pre_cost][state] = max(dp[cur][pre_cost][state],dfs(cost[cur][i],i,state | (1 << i) ) + 1)

    return dp[cur][pre_cost][state]



ret = dfs(0,0,1)
print(ret)