import sys

n,m =map(int,sys.stdin.readline().rstrip().split())
weights = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(i,j,count,sum):
    global ret

    if count == 4:
        print(sum)
        ret = max(ret,sum)
        return

    sum += weights[i][j]
    visited[i][j] = True
    for dir in range(4):
        p = i + dx[dir]
        q = j + dy[dir]

        if 0 <= p < n and 0 <= q < m and not visited[p][q]:
            dfs(p,q,count+1,sum)
    visited[i][j] = False

max_value = 0
for i in range(n):
    for j in range(m):
        ret = 0
        dfs(i,j,0,0)
        max_value = max(max_value,ret)
print(max_value)

