import sys
import heapq

n,m = map(int,sys.stdin.readline().rstrip().split())
maps = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
fall = [[i for _ in range(m)] for i in range(n)]
cat_x = None
cat_y = None
exit_x = None
exit_y = None
for i in range(n-1,-1,-1):
    for j in range(m):
        if maps[i][j] == 'C':
            cat_x = i
            cat_y = j
        if maps[i][j] == 'E':
            exit_x = i
            exit_y = j

        if maps[i][j] == 'X':
            fall[i][j] = fall[i+1][j]

distances = [[sys.maxsize for _ in range(m)] for _ in range(n)]
queue = []
heapq.heappush(queue,(0,cat_x,cat_y))
distances[cat_x][cat_y] = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

while queue:
    dist, cur_x, cur_y = heapq.heappop(queue)
    if dist < distances[cur_x][cur_y]:
        continue
    if maps[cur_x][cur_y] == 'E':
        break

    if maps[cur_x][cur_y] == 'D':
        continue

    if maps[cur_x][cur_y] == 'X':
        next_x = fall[cur_x][cur_y]
        next_y = cur_y
        if dist + 10 < distances[next_x][next_y] :
            distances[next_x][next_y] = dist + 10
            heapq.heappush(queue,(distances[next_x][next_y],next_x,next_y))
    else:
        for i in range(2,4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]
            if 0 <= next_x < n and 0 <= next_y < m:
                if dist + 1 < distances[next_x][next_y]:
                    distances[next_x][next_y] = dist + 1
                    heapq.heappush(queue,(distances[next_x][next_y],next_x,next_y))

        #위로 올라가는 사다리
        if maps[cur_x][cur_y] == 'L':
            next_x = cur_x - 1
            next_y = cur_y
            if 0 <= next_x < n:
                if dist + 5 < distances[next_x][next_y]:
                    distances[next_x][next_y] = dist + 5
                    heapq.heappush(queue, (distances[next_x][next_y], next_x, next_y))

        #밑으로 내려가는 사다리
        if 0 <= cur_x + 1 < n:
            if maps[cur_x+1][cur_y] == 'L':
                next_x = cur_x + 1
                next_y = cur_y
                if dist + 5 < distances[next_x][next_y]:
                    distances[next_x][next_y] = dist + 5
                    heapq.heappush(queue, (distances[next_x][next_y], next_x, next_y))







print(distances[exit_x][exit_y] if distances[exit_x][exit_y] != sys.maxsize else "dodo sad")

