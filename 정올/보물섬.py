import sys
from collections import deque
n,m = map(int,sys.stdin.readline().rstrip().split())
maps = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
land = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for i in range(n):
    for j in range(m):
        if maps[i][j] == 'L':
            land.append((i,j))

ret = 0
for start_x,start_y in land:
    q = deque()
    q.append((start_x,start_y,0))
    visit = [[-1 for _ in range(m)] for _ in range(n)]
    visit[start_x][start_y] = 0
    while q:
        x,y,path = q.popleft()

        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            if 0 <= a < n and 0<= b <m and maps[a][b] =='L':
                if visit[a][b] == -1:
                    ret = max(ret,path+1)
                    visit[a][b] = path+1
                    q.append((a,b,path+1))

    # print(visit)
print(ret)