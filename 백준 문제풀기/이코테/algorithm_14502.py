import sys
import copy
from collections import deque
from itertools import combinations

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def safe_area_count(map):
    queue = deque()
    for i,j in germ:
        queue.append((i,j))

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            p = x + dx[i]
            q = y + dy[i]

            if 0 <= p < n and 0 <= q < m and map[p][q] == 0:
                map[p][q] = 2
                queue.append((p,q))
    sum = 0
    for map_ in map:
        sum += map_.count(0)
    return sum

n, m = map(int,sys.stdin.readline().rstrip().rsplit())
map = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
blank = []
germ = []
for i in range(n):
    for j in range(m):
        if map[i][j] == 0:
            blank.append((i, j))
        elif map[i][j] == 2:
            germ.append((i,j))

safe_area = 0
for walls in combinations(blank,3):
    map_copy = copy.deepcopy(map)
    for i,j in walls:
        map_copy[i][j] = 1

    safe_area = max(safe_area,safe_area_count(map_copy))

print(safe_area)