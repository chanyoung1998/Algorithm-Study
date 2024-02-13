import sys
from collections import deque


def check(x, y, time):
    x = x - time
    if x >= 0:
        if maps[x][y] == '#':
            return False

    return True


N = 8
maps = [list(sys.stdin.readline().strip()) for _ in range(N)]
visit = [[0 for _ in range(N)] for _ in range(N)]

dq = deque()
dq.append((N - 1, 0, 0))
dirX = [0, 0, 1, -1, 1, -1, 1, -1, 0]
dirY = [1, -1, 0, 0, -1, -1, 1, 1, 0]
flag = False


while dq:
    curX, curY, time = dq.popleft()
    if curX == 0 and curY == N - 1:
        flag = True
        break
    if check(curX, curY, time):

        for i in range(9):
            nextX, nextY = curX + dirX[i], curY + dirY[i]
            if 0 <= nextX < N and 0 <= nextY < N and (visit[nextX][nextY] < time + 1):
                if check(nextX,nextY,time):
                    visit[nextX][nextY] = time + 1
                    dq.append((nextX, nextY, time + 1))

if flag:
    print(1)
else:
    print(0)