'''
2024 02 11
벽 부수고 이동하기 4
16946
골2
'''

import sys
from collections import deque

def bfs(i,j,key):
    dq = deque()
    dq.append((i,j))
    visited[i][j] = key
    ret = 1

    while dq:
        x,y = dq.popleft()
        for i in range(4):
            nx,ny = x + dirx[i], y + diry[i],
            if 0 <= nx < N and 0 <= ny < M:
                if MAPS[nx][ny] == 0 and visited[nx][ny] == -1:
                    visited[nx][ny] = key
                    ret += 1
                    dq.append((nx,ny))

    return ret



N,M = map(int,sys.stdin.readline().split(' '))
MAPS = [list(map(int,list(sys.stdin.readline().strip()))) for _ in range(N)]
check = {}
visited = [[-1 for _ in range(M)] for _ in range(N)]
dirx = [0,0,1,-1]
diry = [1,-1,0,0]

for i in range(N):
    for j in range(M):
        key = i * M + j
        if MAPS[i][j] == 0 and visited[i][j] == -1:
            ret = bfs(i,j,key)
            check[key] = ret

for i in range(N):
    for j in range(M):
        if MAPS[i][j] == 0:
            print(0,end='')
        else:
            ret = 1
            tmp = set()
            for _ in range(4):
                ni,nj = i + dirx[_] , j +diry[_]
                if 0 <= ni < N and 0 <= nj < M:
                    key = ni * M + nj
                    if visited[ni][nj] != -1  and visited[ni][nj] not in tmp :
                        ret += check[visited[ni][nj]]
                        tmp.add(visited[ni][nj])

            print(ret % 10,end='')

    print()



