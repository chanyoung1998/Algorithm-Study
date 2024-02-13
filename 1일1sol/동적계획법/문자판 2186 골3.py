import sys

N, M, K = map(int, sys.stdin.readline().strip().split(' '))
MAPS = [list(sys.stdin.readline().strip()) for _ in range(N)]
TARGET = list(sys.stdin.readline().strip())

dp = [[[-1 for _ in range(len(TARGET))] for _ in range(M)] for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, depth):

    if dp[x][y][depth] != -1:
        return dp[x][y][depth]

    dp[x][y][depth] = 0
    if MAPS[x][y] == TARGET[depth]:
        if depth == len(TARGET) - 1:
            dp[x][y][depth] = 1
            return 1
        else:
            for k in range(1, K + 1):
                for i in range(4):
                    nx, ny = x + dx[i]*k, y + dy[i]*k
                    if 0 <= nx < N and 0 <= ny < M:
                        dp[x][y][depth] += dfs(nx, ny, depth + 1)

    return dp[x][y][depth]


ret = 0
for i in range(N):
    for j in range(M):
        ret += dfs(i, j, 0)
print(ret)