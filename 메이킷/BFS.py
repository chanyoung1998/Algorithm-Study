import sys
from collections import deque
# 1 1 0 0 0 1 0 0
# 1 1 1 0 0 1 0 0
# 0 1 0 0 0 1 0 0
# 0 0 0 0 0 0 0 0
board = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(4)]
visit = [[False for _ in range(8)] for _ in range(4)]

queue = deque()

queue.append((0,0))
# 시작 지점 방문 처리
visit[0][0] = True
cnt = 1

dx = [-1,1,0,0]
dy = [0,0,-1,1]

while queue:
    cur_x,cur_y = queue.popleft()

    for dir in range(4):
        next_x = cur_x + dx[dir]
        next_y = cur_y + dy[dir]
        #다음 좌표가 범위에 맞는지 먼저 검사
        if 0 <= next_x < 4 and 0 <= next_y < 8:
            if not visit[next_x][next_y] and board[next_x][next_y] == 1:
                cnt += 1
                #큐에 넣을 때 방문 처리
                visit[next_x][next_y] = True
                queue.append((next_x,next_y))

print(cnt)