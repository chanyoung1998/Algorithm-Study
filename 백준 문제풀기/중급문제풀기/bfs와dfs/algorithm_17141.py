#!/usr/bin/env Python
# coding=utf-8
import sys
import copy
from itertools import combinations
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs(maps, viruses):
    queue = deque()
    time = 0
    for i, j in viruses:
        queue.append((i, j))
        maps[i][j] = 3

    while queue:
        x, y = queue.popleft()
        time = maps[x][y] - 3
        for dir in range(4):
            p = x + dx[dir]
            q = y + dy[dir]

            if (0 <= p < n and 0 <= q < n) and (maps[p][q] == 0 or maps[p][q] == 2):
                maps[p][q] = maps[x][y] + 1
                queue.append((p, q))

    for i in range(n):
        for j in range(n):
            if maps[i][j] == 0:
                return -1

    return time


n,m = map(int,sys.stdin.readline().rstrip().split())
institution = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
can_virus = []

for i in range(n):
    for j in range(n):
        if institution[i][j] == 2:
            can_virus.append((i,j))

min_time = sys.maxsize
for viruses in combinations(can_virus,m):
    temp = copy.deepcopy(institution)
    viruses = list(viruses)
    time = bfs(temp,viruses)

    if time != -1:
        min_time = min(min_time,time)

if min_time == sys.maxsize:
    print(-1)
else:
    print(min_time)

