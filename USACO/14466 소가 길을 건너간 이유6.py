import sys
from collections import deque

def bfs(cow_x,cow_y):
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    queue = deque()
    queue.append((cow_x,cow_y))
    visit[cow_x][cow_y] = 1

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            p = x + dx[i]
            q = y + dy[i]

            if 0 <= p < n and 0 <= q < n and visit[p][q] == 0:
                if (p,q) in path[x][y]:
                    continue
                else:
                    queue.append((p,q))
                    visit[p][q] = 1


n,k,r = map(int,sys.stdin.readline().rstrip().split())
path = [[[] for _ in range(n)] for _ in range(n)]
cows = []
for _ in range(r):
    a,b,c,d = map(int,sys.stdin.readline().rstrip().split())
    path[a-1][b-1].append((c-1, d-1))
    path[c-1][d-1].append((a-1, b-1))

# for _ in path:
#     print(_)

for _ in range(k):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    cows.append((a-1,b-1))

count = 0
for i in range(k):
    visit = [[0 for _ in range(n)] for _ in range(n)]
    bfs(cows[i][0],cows[i][1])

    for j in range(i+1,k):
        if visit[cows[j][0]][cows[j][1]] == 0:
            count += 1

print(count)