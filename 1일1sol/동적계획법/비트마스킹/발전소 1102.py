import sys
n = int(sys.stdin.readline().rstrip())
adjlist = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
on_off = list(sys.stdin.readline().rstrip())
p = int(sys.stdin.readline().rstrip())
dp = [-1 for _ in range(1 << n)]

#state인 상태에서 i번째 발전소를 키는데 최소 비용
def min_cost(i,state):
    ret = sys.maxsize
    for j in range(n):
        if state & (1 << j):
            ret = min(ret,adjlist[j][i])

    return ret

def dfs(num,state):

    if num >= p:
        return 0
    if dp[state] != -1:
        return dp[state]

    dp[state] = sys.maxsize
    for i in range(n):
        if state & (1 << i):
            continue
        else:
            dp[state] = min(dp[state], dfs(num+1,state | (1 << i)) + min_cost(i,state))

    return dp[state]

def sol():
    state = 0
    num = 0
    for i in range(len(on_off)):
        if on_off[i] == "Y":
            state = state | (1<<i)
            num += 1

    ret = dfs(num,state)
    if ret == sys.maxsize:
        print(-1)
    else:
        print(ret)
sol()


