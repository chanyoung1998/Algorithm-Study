'''
2024 02 07
레이저 통신
BFS, 최단 거리
'''
import sys
from collections import deque

W, H = map(int,sys.stdin.readline().split())
MAPS = [list(sys.stdin.readline().strip()) for _ in range(H)]
check = [[[sys.maxsize,sys.maxsize,sys.maxsize,sys.maxsize] for _ in range(W)] for _ in range(H)]
dq = deque()
dirX = [0,-1,0,1]
dirY = [-1,0,1,0]

c = []
for i in range(H):
    for j in range(W):
        if MAPS[i][j] == 'C':
            c.append((i,j))


check[c[0][0]][c[0][1]][0] = 0
check[c[0][0]][c[0][1]][1] = 0
check[c[0][0]][c[0][1]][2] = 0
check[c[0][0]][c[0][1]][3] = 0

dq.append((c[0][0],c[0][1],0,0))
dq.append((c[0][0],c[0][1],0,1))
dq.append((c[0][0],c[0][1],0,2))
dq.append((c[0][0],c[0][1],0,3))

while dq:
    x, y, cost, dir = dq.popleft()

    nx , ny = x + dirX[dir], y + dirY[dir]
    for i in range(4):
        if 0 <= nx < H and 0 <= ny < W and MAPS[nx][ny] != '*':
            if dir == i:
                if check[nx][ny][i] > cost:
                    check[nx][ny][i] = cost
                    dq.append((nx,ny,cost,i))
            elif (dir + 2) % 4 != i:
                if check[nx][ny][i] > cost + 1:
                    check[nx][ny][i] = cost + 1
                    dq.append((nx,ny,cost+1,i))

print(min(check[c[1][0]][c[1][1]]))

