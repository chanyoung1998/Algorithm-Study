import sys

n,m =map(int,sys.stdin.readline().rstrip().split())
weights = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]


def dfs(i,j,count,sum):
    global ret

    if count == 4:
        #print(sum)
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


ex = [[0,0,0,1],[0,1,2,1],[0,0,0,-1],[0,-1,0,1]]
ey = [[0,1,2,1],[0,0,0,1],[0,1,2,1],[0,1,1,1]]


def check_fuck_shape(i,j):
    global ret
    for x in range(4):
        isOut = False
        sum_value = 0

        for y in range(4):
            p = i + ex[x][y]
            q = j + ey[x][y]

            if p < 0 or p >= n or q < 0 or q >= m:
                isOut = True
                break
            else:
                sum_value += weights[p][q]

        if not isOut:
            ret = max(ret,sum_value)
    return


max_value = 0
for i in range(n):
    for j in range(m):
        ret = 0
        dfs(i,j,0,0)
        check_fuck_shape(i,j)
        max_value = max(max_value,ret)
print(max_value)

