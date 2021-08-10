import sys
from collections import deque
n = int(sys.stdin.readline())
arrays = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(low,high):
    queue = deque()

    if low <= arrays[0][0] <= high:
        queue.append((0,0))
        visited[0][0] = True
    else:
        return False

    while queue:
        x,y = queue.popleft()

        if x == n-1 and y == n- 1:
            return True

        for dir in range(4):
            p = x + dx[dir]
            q = y + dy[dir]

            if 0 <= p < n and 0 <= q < n and not visited[p][q] and low <= arrays[p][q] <= high:
                queue.append((p,q))
                visited[p][q] = True


    return False


maxv = -sys.maxsize
minv = sys.maxsize
for i in range(n):
    for j in range(n):
        maxv = max(maxv,arrays[i][j])
        minv = min(minv,arrays[i][j])

ret = sys.maxsize
end = 0
for start in range(0,maxv+1):

    while end <= maxv:
        visited = [[False] * n for _ in range(n)]
        if bfs(start,end):
            if start == 0 and end == 0:
                print(0)
                exit(0)
            ret = min(end - start, ret)
            break
        else:
            end += 1

print(ret)