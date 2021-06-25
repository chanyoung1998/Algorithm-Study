import sys
import heapq
from collections import deque

n = int(sys.stdin.readline().rstrip())
map = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

shark_size = 2

fish_list = [[] for _ in range(7)]
cur_x = 0
cur_y = 0
for i in range(n):
    for j in range(n):
        if 1 <= map[i][j] <= 6:
            fish_list[map[i][j]].append((i,j))
        if map[i][j] == 9:
            cur_x = i
            cur_y = j

map[cur_x][cur_y] = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def bfs(cur_x,cur_y):
    queue = deque()
    queue.append((cur_x,cur_y))
    temp = [[-1 for _ in range(n)] for _ in range(n)]
    temp[cur_x][cur_y] = 0
    while queue:
        p,q = queue.popleft()

        for i in range(4):
            new_p = dx[i] + p
            new_q = dy[i] + q

            if 0<= new_p < n and 0 <= new_q < n and map[new_p][new_q] <= shark_size and temp[new_p][new_q] == -1:
                temp[new_p][new_q] = temp[p][q] + 1
                queue.append((new_p,new_q))

    return temp

def bfs2(cur_x,cur_y,x,y):
    queue = deque()
    queue.append((cur_x,cur_y))
    temp = [[-1 for _ in range(n)] for _ in range(n)]
    temp[cur_x][cur_y] = 0
    while queue:
        p,q = queue.popleft()
        if p == x and q ==y:
            break
        for i in range(4):
            new_p = dx[i] + p
            new_q = dy[i] + q

            if 0 <= new_p < n and 0 <= new_q < n and map[new_p][new_q] <= shark_size and temp[new_p][new_q] == -1:
                temp[new_p][new_q] = temp[p][q] + 1
                queue.append((new_p,new_q))

    return temp[x][y]


ret = 0
eaten = 0
while True:

    distances = []
    dist_map = bfs(cur_x, cur_y)

    for i in range(1,shark_size):
        if i >= 7:
            break
        for (x,y) in fish_list[i]:
            if dist_map[x][y] == -1:
                continue
            distances.append((x,y,dist_map[x][y],i))

    if len(distances) != 0:
        distances.sort(key=lambda x:(x[2],x[0],x[1]))

        ret += distances[0][2]
        fish_list[distances[0][3]].remove((distances[0][0],distances[0][1]))
        cur_x = distances[0][0]
        cur_y = distances[0][1]

        eaten += 1
        if eaten == shark_size:
            shark_size += 1
            eaten = 0
    else:
        break

print(ret)