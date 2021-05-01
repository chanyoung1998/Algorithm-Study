'''
내용:백준 알고리즘 단계별 풀기 최소 신장 트리 17472 다리만들기2
날짜:21년5월1일
사용 언어:파이썬
'''

import sys
from collections import deque

def find_island(i, j, count):

    if map[i][j] != 1:
        return False

    queue = deque()
    queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        map[x][y] = count
        for i in range(4):
            p = x + dx[i]
            q = y + dy[i]

            if 0 <= p < n and 0 <= q < m and map[p][q] == 1:
                queue.append((p, q))

    return True

def make_bridges_horizontal(map_horizontal):
    start_island = -1
    end_island = -1
    start_index = -1
    end_index = -1
    flag = 0

    for i in range(len(map_horizontal)):
        if map_horizontal[i] != 0 and flag == 0:
            start_index = i
            start_island = map_horizontal[i]
            flag = 1

        if map_horizontal[i] == start_island:
            start_index = i

        if map_horizontal[i] != 0 and map_horizontal[i] != start_island and flag == 1:
            end_index = i
            end_island = map_horizontal[i]
            if end_index - start_index  >= 3:
                bridges.append((start_island-2,end_island-2,end_index-start_index-1))
            start_island = end_island
            end_island = -1
            start_index = end_index
            end_index = -1
            flag = 1

def make_bridges_vertical(map_vertical):
    start_island = -1
    end_island = -1
    start_index = -1
    end_index = -1
    flag = 0

    for i in range(len(map_vertical)):
        if map_vertical[i] != 0 and flag == 0:
            start_index = i
            start_island = map_vertical[i]
            flag = 1

        if map_vertical[i] == start_island:
            start_index = i

        if map_vertical[i] != 0 and map_vertical[i] != start_island and flag == 1:
            end_index = i
            end_island = map_vertical[i]
            if end_index - start_index >= 3:
                bridges.append((start_island-2, end_island-2, end_index - start_index - 1))
            start_island = end_island
            end_island = -1
            start_index = end_index
            end_index = -1
            flag = 1

def find(a):
    if parent[a] == a:
        return a

    parent[a] = find(parent[a])
    return parent[a]

def union(a,b):

    a = find(a)
    b = find(b)

    if a == b:
        return

    if b > a:
        parent[b] = a
    else:
        parent[a] = b

    return

def isSameParent(a,b):

    a = find(a)
    b = find(b)

    if a == b:
        return True
    else:
        return False

n, m = map(int,sys.stdin.readline().rstrip().split())
map = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]
count = 2
for i in range(n):
    for j in range(m):
        if find_island(i,j,count):
            count += 1

bridges = []
for i in range(n):
    make_bridges_horizontal(map[i])


for i in range(m):
    map_vertical = []
    for j in range(n):
        map_vertical.append(map[j][i])
    make_bridges_vertical(map_vertical)

parent = [i for i in range(count-2)]
bridges.sort(key=lambda x: x[2])
count = 0
mst = 0
'''for _ in map:
    print(*_)
print(bridges)
'''
for a,b,c in bridges:
    if count == len(parent)-1:
        break
    if isSameParent(a,b):
        continue
    else:
        union(a,b)
        count += 1
        mst += c

if count != len(parent) - 1:
    print(-1)
else:
    print(mst)
