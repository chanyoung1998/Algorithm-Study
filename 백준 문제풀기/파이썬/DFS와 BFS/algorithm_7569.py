'''
내용:백준 알고리즘 단계별 풀기 dfs와bfs 7579 토마토
날짜:21년3월 14일
사용 언어:파이썬
'''
import sys
from collections import deque
m, n, h = map(int,sys.stdin.readline().split())
tomatoes = [[list(map(int,sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]
queue = deque()
for z in range(h):
    for x in range(n):
        for y in range(m):
            if tomatoes[z][x][y] == 1:
                queue.append([z,x,y])
dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]


def bfs():
    while queue:
        z,x,y = queue.popleft()
        for i in range(6):
            r = z + dz[i]
            q = x + dx[i]
            w = y + dy[i]
            if 0 <= q < n and 0 <= w < m and 0 <= r <h and tomatoes[r][q][w] == 0:
                tomatoes[r][q][w] = tomatoes[z][x][y] + 1
                queue.append([r,q,w])

bfs()
isTrue = False
result = -2
for tomato in tomatoes:
    for toma in tomato:
        for j in toma:
            if j == 0:
                isTrue = True
            result = max(result, j)

if isTrue == True:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result - 1)