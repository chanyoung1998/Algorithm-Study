import sys
from collections import deque


def BFS():
    global count
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    visit = [[False for _ in range(n)] for _ in range(n)]
    queue = deque()
    queue.append((0,0))
    visit[0][0] = True
    flag = False
    while queue:
        x,y = queue.popleft()
        for l,s in inputs[x][y]:
            if not light[l][s]:
                flag = True

                #print(l,s)
                light[l][s] = True
                count += 1

        for i in range(4):
            p = x + dx[i]
            q = y + dy[i]

            if 0 <= p < n and 0 <= q < n and light[p][q] and not visit[p][q]:
                queue.append((p,q))
                visit[p][q] = True
    return flag


n,m = map(int,sys.stdin.readline().rstrip().split())
inputs = [[[] for _ in range(n)] for _ in range(n)]
light = [[False for _ in range(n)] for _ in range(n)]
light[0][0] = True
count = 1
for _ in range(m):
    x,y,a,b = map(int,sys.stdin.readline().rstrip().split())
    inputs[x-1][y-1].append((a-1,b-1))

while True:
    if not BFS():
        print(count)
        break





