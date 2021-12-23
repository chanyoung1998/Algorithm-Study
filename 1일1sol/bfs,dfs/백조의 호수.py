import sys
from collections import deque


# 얼음이 녹는 순서 구하기
def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque(water)

    last_time = 0
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            p = x + dx[i]
            q = y + dy[i]
            if 0 <= p < r and 0 <= q < c:
                if lake[p][q] == 'X':
                    lake[p][q] = lake[x][y] + 1
                    last_time = lake[p][q]
                    queue.append((p,q))

    return last_time


def swan_meet(start,mid,end):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append(start)
    visited = [[False for _ in range(c)] for _ in range(r)]
    visited[start[0]][start[1]] = True
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            p = x + dx[i]
            q = y + dy[i]
            if 0 <= p < r and 0 <= q < c and not visited[p][q]:
                visited[p][q] = True
                if p == end[0] and q == end[1]:
                    return True
                if lake[p][q] <= mid:
                    queue.append((p,q))
    return False


r,c = map(int,sys.stdin.readline().rstrip().split())
lake = [list(sys.stdin.readline().rstrip()) for _ in range(r)]
water = []
swans = []

for i in range(r):
    for j in range(c):
        if lake[i][j] =='.':
            lake[i][j] = 0
            water.append((i,j))
        if lake[i][j] == 'L':
            lake[i][j] = 0
            swans.append((i,j))
            water.append((i,j))


start = -1
end = bfs()

while start+1 < end:
    mid = (start + end) // 2
    if swan_meet(swans[0],mid,swans[1]):
        end = mid
    else:
        start = mid

print(end)

