import sys
sys.setrecursionlimit(10001)
n,m = map(int,sys.stdin.readline().rstrip().split())
r,c,s,k = map(int,sys.stdin.readline().rstrip().split())
INF = 999999
visit = [[INF for _ in range(m)] for _ in range(n)]
dy = [2,2,1,-1,-2,-2,-1,1]
dx = [-1,1,2,2,1,-1,-2,-2]

ret = 999999
def dfs(x,y,cnt):

    global ret

    if x == s and y == k:
        ret = min(ret,cnt)
        return

    if cnt >= ret:
        return

    for i in range(8):
        p = x + dx[i]
        q = y + dy[i]
        if 0 <= p < n and 0 <= q < m and cnt + 1 < visit[p][q]:
            visit[p][q] = cnt + 1
            dfs(p,q,cnt+1)
    return

dfs(r,c,0)
print(ret)
