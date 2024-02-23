'''
24 02 23
벽 부수고 이동하기 2 14442
골3
그래프, bfs
'''
import sys
from collections import deque

N, M, K = map(int, sys.stdin.readline().split(' '))
MAPS = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(N)]
visited = [[[sys.maxsize for _ in range(K + 1)] for _ in range(M)] for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
dq = deque()
dq.append((0, 0, 0, 1))
visited[0][0][0] = 1

while dq:
    curX, curY, curK, cost = dq.popleft()

    if visited[curX][curY][curK] < cost:
        continue

    for i in range(4):
        nextX, nextY = curX + dx[i], curY + dy[i]
        if 0 <= nextX < N and 0 <= nextY < M:
            if MAPS[nextX][nextY] == 0:
                if visited[nextX][nextY][curK] > cost + 1:
                    visited[nextX][nextY][curK] = cost + 1
                    dq.append((nextX, nextY, curK, cost + 1))
            else:
                if curK + 1 <= K and visited[nextX][nextY][curK + 1] > cost + 1:
                    visited[nextX][nextY][curK + 1] = cost + 1
                    dq.append((nextX, nextY, curK + 1, cost + 1))

print(min(visited[N - 1][M - 1]) if min(visited[N - 1][M - 1]) != sys.maxsize else -1)
