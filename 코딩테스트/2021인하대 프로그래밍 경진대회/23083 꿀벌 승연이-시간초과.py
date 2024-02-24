import sys

sys.setrecursionlimit(10**6)
n,m = map(int,sys.stdin.readline().rstrip().split())
k = int(sys.stdin.readline().rstrip())
hole = [tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(k)]
visit = [[0 for _ in range(m)] for _ in range(n)]

for i,j in hole:
    visit[i-1][j-1] = -1

dx1 = [0,1,1]
dy1 = [1,0,1]

dx2 = [0,1,-1]
dy2 = [1,0,1]

ret = 0

def dfs(x,y):
    global ret
    if x == n - 1 and y == m-1:

        ret += 1
        return


    visit[x][y] = 1
    if y % 2 == 1:
        for dist in range(3):
            u = x + dx1[dist]
            w = y + dy1[dist]
            if 0 <= u < n and 0 <= w < m and visit[u][w] == 0:
                dfs(u,w)

    else:
        for dist in range(3):
            u = x + dx2[dist]
            w = y + dy2[dist]
            if 0 <= u < n and 0 <= w < m and visit[u][w] == 0:
                dfs(u,w)

    visit[x][y] = 0
    return

dfs(0,0)
print(ret % (10**9 + 7))