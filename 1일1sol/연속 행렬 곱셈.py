import sys

n = int(sys.stdin.readline())
matrix = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
dp = [[0]*(n+1) for _ in range(n+1)]

def top_down(s,e):
    if s == e:
        return 0

    if dp[s][e] != 0:
        return dp[s][e]

    else:
        dp[s][e] = sys.maxsize
        for i in range(s,e):
            dp[s][e] = min(dp[s][e],top_down(s,i)+top_down(i+1,e)+matrix[s][0]*matrix[i][1]*matrix[e][1])
        return dp[s][e]


print(top_down(0,n-1))

