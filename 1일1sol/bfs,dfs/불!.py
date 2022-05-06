import sys
from collections import deque
INF = 987654321
r,c = map(int,sys.stdin.readline().rstrip().split())
maps = [list(sys.stdin.readline().rstrip()) for _ in range(r)]
fire = [[INF for _ in range(c)] for _ in range(r)]
time = [[-1 for _ in range(c)] for _ in range(r)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

fire_queue = deque()
jihoon_queue = deque()
for i in range(r):
    for j in range(c):
        if maps[i][j] == 'F':
            fire_queue.append((i,j))
            fire[i][j] = 0
        elif maps[i][j] == 'J':
            jihoon_queue.append((i,j))
            time[i][j] = 0


while fire_queue:
    x,y = fire_queue.popleft()

    for dir in range(4):
        p,q = x+dx[dir],y+dy[dir]
        if 0 <= p < r and 0 <= q < c and fire[p][q] == INF and maps[p][q] != '#':
            fire[p][q] = fire[x][y] + 1
            fire_queue.append((p,q))

flag = False
# ret = []
while jihoon_queue:

    x,y = jihoon_queue.popleft()
    if x == r-1 or x == 0 or y == c-1 or y == 0:
        print(time[x][y]+1)
        flag = True
        break
    for dir in range(4):
        p, q = x + dx[dir], y + dy[dir]
        if 0 <= p < r and 0 <= q < c and maps[p][q] != '#' and time[x][y] + 1 < fire[p][q]:
            if time[p][q] == -1 or time[x][y] + 1 < time[p][q]:
                time[p][q] = time[x][y] + 1
                jihoon_queue.append((p,q))



# if ret:
#     print(min(ret)+1)
# else:
if not flag:
    print("IMPOSSIBLE")