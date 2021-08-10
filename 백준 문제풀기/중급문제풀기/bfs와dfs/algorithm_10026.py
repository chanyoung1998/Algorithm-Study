import sys
from collections import deque
n = int(sys.stdin.readline())
grid = [list(sys.stdin.readline().rstrip()) for _ in range(n)]


dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True

    while queue:

        i,j = queue.popleft()


        for dis in range(4):
            p = i + dx[dis]
            q = j + dy[dis]

            if 0<= p < n and 0 <= q < n and not visited[p][q] and grid[i][j] == grid[p][q]:
                queue.append((p,q))
                visited[p][q] = True

    return 1

def red_green_weakness_bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] =True

    color = grid[x][y]
    allowed_color = []

    if color == 'B':
        allowed_color = ['B']
    else:
        allowed_color = ['R','G']

    while queue:

        i,j = queue.popleft()


        for dis in range(4):
            p = i + dx[dis]
            q = j + dy[dis]

            if 0 <= p < n and 0 <= q < n and not visited[p][q] and grid[p][q] in allowed_color:
                queue.append((p,q))
                visited[p][q] = True
    return 1


visited = [[False] * n for _ in range(n)]
count = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            count += bfs(i,j)
print(count,end=' ')

count = 0
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            count += red_green_weakness_bfs(i,j)

print(count)