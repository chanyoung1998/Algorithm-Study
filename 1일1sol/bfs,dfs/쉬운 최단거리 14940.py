import sys
from collections import deque

m, n = map(int, sys.stdin.readline().strip().split(' '))
maps = [list(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(m)]
check = [[-1 for _ in range(n)] for _ in range(m)]

dq = deque()
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
for i in range(m):
    for j in range(n):
        if maps[i][j] == 2:
            dq.append((i, j, 0))
            check[i][j] = 0
            break

while dq:
    curX, curY, cost = dq.popleft()

    for i in range(4):
        nextX, nextY = curX + dx[i], curY + dy[i]

        if 0 <= nextX < m and 0 <= nextY < n and maps[nextX][nextY] != 0:

            if check[nextX][nextY] == -1:
                check[nextX][nextY] = cost + 1
                dq.append((nextX, nextY, cost + 1))


for i in range(m):
    for j in range(n):

        if maps[i][j] == 1 and check[i][j] == -1:
            print(-1,end=' ')
        elif maps[i][j] == 0:
            print(0,end=' ')
        else:
            print(check[i][j],end=' ')

    print()