import sys
from itertools import combinations
from collections import deque


def bfs(green,red):
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    time = [[(-1,0) for _ in range(m)] for _ in range(n)]
    queue = deque()
    ret = set()
    for gr in green:
        time[gr[0]][gr[1]] = (0,1)
        queue.append((gr[0],gr[1],1))
    for re in red:
        time[re[0]][re[1]] = (0,2)
        queue.append((re[0],re[1],2))

    while queue:
        x,y,color = queue.popleft()
        if (x,y) in ret:
            continue
        for i in range(4):
            p = x + dx[i]
            q = y + dy[i]

            if 0 <= p < n and 0<= q < m:
                if garden[p][q] == 0:
                    continue

                if time[p][q][0] == -1:
                    time[p][q] = (time[x][y][0]+1, color)
                    queue.append((p,q,color))
                else:
                    if time[p][q][1] == color:
                        continue
                    else:
                        if time[p][q][0] == time[x][y][0] + 1:
                            ret.add((p,q))
    #print(ret)

    return len(ret)


n,m,g,r = map(int,sys.stdin.readline().rstrip().split())
garden = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
possible_soil = []
for i in range(n):
    for j in range(m):
        if garden[i][j] == 2:
            possible_soil.append((i,j))

count = 0
for comb in combinations(possible_soil,(g+r)):
    comb = set(comb)
    for green in combinations(comb,g):
        green = set(green)
        red = comb-green
        count = max(count,bfs(green,red))

print(count)