import sys

n,m = map(int,sys.stdin.readline().rstrip().split())

graph = []
for _ in range(n):
    graph.append(list(map(int,list(sys.stdin.readline().rstrip()))))

def dfs(x,y):

    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        dfs(x+1,y)
        return True

    return False

ret = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j):
            ret += 1
print(ret)
