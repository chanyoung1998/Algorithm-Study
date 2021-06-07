import sys
from collections import deque
import copy
n, l, r = map(int,sys.stdin.readline().rstrip().split())
maps = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

def make_union_and_move(map):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    open = [[False for _ in range(n)] for _ in range(n)]
    flag = False
    for x in range(n):
        for y in range(n):
            if not open[x][y]:
                union = []
                union.append((x,y))
                sum = map[x][y]
                open[x][y] = True
                queue = deque()
                queue.append((x,y))

                while queue:
                    a,b = queue.popleft()
                    for i in range(4):
                        p = a + dx[i]
                        q = b + dy[i]
                        if 0 <= p < n and 0 <= q < n and not open[p][q] and l <= abs(map[a][b]-map[p][q]) <= r :
                            queue.append((p,q))
                            sum += map[p][q]
                            open[p][q] = True
                            union.append((p, q))

                for i,j in union:
                    map[i][j] = sum//len(union)

                if sum != map[x][y]:
                    flag = True

    return flag
count = 0
while True:
    ret = make_union_and_move(maps)
    if ret:
        count += 1
    else:
        print(count)
        break
