import sys

n = int(sys.stdin.readline())
maps = [list(map(int,list(sys.stdin.readline().rstrip()))) for _ in range(n)]
print(maps)
dx = [-1,1,0,0]
dy = [0,0,-1,1]
visit = [[False for _ in range(n)] for _ in range(n)]

def dfs(cur_x,cur_y):

    if not visit[cur_x][cur_y]:
        visit[cur_x][cur_y] = True
        cnt = 1
        for dir in range(4):
            next_x,next_y = cur_x + dx[dir], cur_y + dy[dir]
            if 0 <= next_x < n and 0 <= next_y < n:
                if maps[next_x][next_y] == 1 and visit[next_x][next_y] == False:
                    cnt += dfs(next_x,next_y)


        return cnt

    else:
        return 0


for i in range(n):
    for j in range(n):
        if not visit[i][j] and maps[i][j] == 1:
            print(dfs(i,j))