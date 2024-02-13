# 2024 02 02
# 4991번 로봇 청소기
# 완전 탐색 , BFS
# 골1
import sys
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

while True:
    W, H = map(int, sys.stdin.readline().strip().split(' '))
    if W == 0 and H == 0:
        break

    MAPS = []
    dirty = []
    curX, curY = None, None
    dq = deque()
    dirty = {}
    check = [[[987654321 for _ in range(1025)] for _ in range(W)] for _ in range(H)]
    for _ in range(H):
        MAPS.append(list(sys.stdin.readline().strip()))

    count = 0
    for i in range(H):
        for j in range(W):
            if MAPS[i][j] == 'o':
                curX, curY = i, j

            if MAPS[i][j] == '*':
                dirty[(i,j)] = count
                count += 1

    dq.append((curX,curY,0,0))
    ret = sys.maxsize

    while dq:
        x, y, cost , visited = dq.popleft()

        if visited == (1 << count) - 1:
            ret = min(ret, cost)

        if check[x][y][visited] < cost:
            continue


        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < H and 0 <= ny < W and MAPS[nx][ny] != 'x':

                if (nx, ny) in dirty:
                    index = dirty[(nx, ny)]
                    nextVisited = visited | (1 << index)
                    if cost + 1 < check[nx][ny][nextVisited]:
                        dq.append((nx,ny,cost+1, nextVisited))
                        check[nx][ny][nextVisited] = cost + 1

                else:
                    if cost + 1 < check[nx][ny][visited]:
                        dq.append((nx, ny, cost + 1, visited))
                        check[nx][ny][visited] = cost + 1

    if ret == sys.maxsize:
        print(-1)
    else:
        print(ret)






