import sys
from collections import deque
import copy
n, k = map(int,sys.stdin.readline().rstrip().rsplit())
test_tube = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
s, X, Y = map(int,sys.stdin.readline().rstrip().rsplit())
germ = []

for i in range(n):
    for j in range(n):
        if test_tube[i][j] != 0:
            germ.append((i,j))
germ.sort(key=lambda x: test_tube[x[0]][x[1]])

dx = [1,-1,0,0]
dy = [0,0,1,-1]
queue = deque()
new_queue = deque()
for i,j in germ:
    queue.append((i,j))

time = 0
while time != s:

    if not queue:
        break
    x,y = queue.popleft()
    virus = test_tube[x][y]

    for i in range(4):
        p = x + dx[i]
        q = y + dy[i]

        if 0 <= p < n and 0 <= q < n and test_tube[p][q] == 0:
            test_tube[p][q] = virus
            new_queue.append((p,q))

    if not queue:
        time += 1
        queue = new_queue.copy()
        new_queue = deque()


print(test_tube[X-1][Y-1])
