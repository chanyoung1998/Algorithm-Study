import sys

n = int(sys.stdin.readline())
adjmatrix = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

ans = sys.maxsize
def dfs(cur,costs,visit):
    global ans

    if visit == (1 << n) - 2:
        if adjmatrix[cur][0] != 0:
            ans = min(ans, costs + adjmatrix[cur][0])
        return



    for i in range(1,n):
        if not (visit & 1 << i) and adjmatrix[cur][i] != 0 and costs + adjmatrix[cur][i] <= ans:
            dfs(i,costs+adjmatrix[cur][i], visit | 1 << i)



dfs(0,0,0)
print(ans)

