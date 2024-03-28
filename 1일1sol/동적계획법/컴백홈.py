import sys

r,c, k = map(int,sys.stdin.readline().strip().split(' '))
maps = [list(sys.stdin.readline()) for _ in range(r)]
visit = [[False for _ in range(c)] for _ in range(r)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
ret = 0
def dfs(x,y, count):
    global ret
    if x == 0 and y == c-1:
        if count == k-1:
            ret += 1
            return

    if count > k:
        return

    for i in range(4):
        nx,ny = x + dx[i], y + dy[i]

        if  0<= nx < r and 0 <= ny < c:
            if not visit[nx][ny] and maps[nx][ny] != 'T':
                visit[nx][ny] = True
                dfs(nx,ny,count+1)
                visit[nx][ny] = False

visit[r-1][0] = True
dfs(r-1,0,0)

