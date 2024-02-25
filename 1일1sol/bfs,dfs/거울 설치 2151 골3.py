'''
24 02 25
거울 설치
2151
골3
BFS, 최단 거리
'''

import sys
from collections import deque

n = int(sys.stdin.readline())
maps = [list(sys.stdin.readline().strip()) for _ in range(n)]
door = []
mirror = []
dirX = [0, -1, 0, 1]
dirY = [-1, 0, 1, 0]

check = [[[sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize] for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):

        if maps[i][j] == '#':
            door.append((i, j))
        elif maps[i][j] == '!':
            mirror.append((i, j))
dq = deque()

check[door[0][0]][door[0][1]][0] = 0
check[door[0][0]][door[0][1]][1] = 0
check[door[0][0]][door[0][1]][2] = 0
check[door[0][0]][door[0][1]][3] = 0

dq.append((door[0][0], door[0][1], 0, 0))
dq.append((door[0][0], door[0][1], 0, 1))
dq.append((door[0][0], door[0][1], 0, 2))
dq.append((door[0][0], door[0][1], 0, 3))

while dq:
    x, y, cost, dir = dq.popleft()

    nx, ny = x + dirX[dir], y + dirY[dir]
    for i in range(4):
        if 0 <= nx < n and 0 <= ny < n and maps[nx][ny] != '*':
            if dir == i:
                if check[nx][ny][i] > cost:
                    check[nx][ny][i] = cost
                    dq.append((nx, ny, cost, i))
            elif (dir + 2) % 4 != i and maps[nx][ny] == '!':
                if check[nx][ny][i] > cost + 1:
                    check[nx][ny][i] = cost + 1
                    dq.append((nx, ny, cost + 1, i))

print(min(check[door[1][0]][door[1][1]]))
