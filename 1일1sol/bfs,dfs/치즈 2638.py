import sys
from collections import deque

n, m = map(int, sys.stdin.readline().strip().split(' '))
maps = [list(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(n)]

cnt = 0
for i in range(n):
    for j in range(m):
        if maps[i][j] == 1:
            cnt += 1
            maps[i][j] = 3

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

ret = 0
while cnt:
    visit = [[False for _ in range(m)] for _ in range(n)]
    visit[0][0] = True
    dq = deque()
    dq.append((0, 0))
    while dq:

        x, y = dq.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] > 1:
                maps[nx][ny] -= 1


        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<= nx < n and 0 <= ny < m and not visit[nx][ny] and maps[nx][ny] == 0:
                dq.append((nx,ny))
                visit[nx][ny] = True

    for i in range(n):
        for j in range(m):
            if maps[i][j] == 1:
                maps[i][j] = 0
                cnt -= 1
            elif maps[i][j] > 1:
                maps[i][j] = 3


    ret += 1

print(ret)
