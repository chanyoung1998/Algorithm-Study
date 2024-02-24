'''
24 02 24
미네랄
2933
골1
그래프,
'''
import sys
from collections import deque


def check(curX, curY):
    for i in range(4):
        nextX, nextY = curX + dx[i], curY + dy[i]
        if 0 <= nextX < r and 0 <= nextY < c:
            if maps[nextX][nextY] == 'x':
                if not bfs(nextX, nextY):  # 떨어지는 클러스터는 1개 밖에 없기 때문에 return fasle면 다른 경우는 고려하지 않아도 됨.
                    break


def bfs(x, y):
   
    visit = [[False for _ in range(c)] for _ in range(r)]
    visit[x][y] = True
   
    dq = deque()
    dq.append((x, y))
   
    cluster = set()
    cluster.add((x, y))
   
    flag = False # 클러스터가 땅에 닿아 있는지 체크하기 위한 flag

   # bfs하면서 인접한 미네랄들을 클러스터에 추가
    while dq:
        curX, curY = dq.popleft()
        if curX == r - 1:
            flag = True

        for i in range(4):
            nextX, nextY = curX + dx[i], curY + dy[i]
            if 0 <= nextX < r and 0 <= nextY < c:
                if maps[nextX][nextY] == 'x' and not visit[nextX][nextY]:
                    visit[nextX][nextY] = True
                    cluster.add((nextX, nextY))
                    dq.append((nextX, nextY))

    # 땅에 닿아 있지 않은 클러스터는 떨어짐
    if not flag:
        diff = sys.maxsize # 클러스터가 얼마나 떨어 질지 계산
        for cX, cY in cluster:
            tmp = 0
            flag2 = False
            for i in range(cX + 1, r):
                if ((i, cY) not in cluster) and maps[i][cY] == '.':
                    tmp += 1
                elif ((i, cY) in cluster):
                    flag2 = True
                    break
                else:
                    break

            if not flag2:
                diff = min(diff, tmp)

        # 클러스터 diff만큼 떨어 뜨리기
        for cX, cY in cluster:
            maps[cX][cY] = '.'
        for cX, cY in cluster:
            maps[cX + diff][cY] = 'x'

    return flag


r, c = map(int, sys.stdin.readline().strip().split(' '))
maps = [list(sys.stdin.readline().strip()) for _ in range(r)]
n = int(sys.stdin.readline())
rows = list(map(int, sys.stdin.readline().strip().split(' ')))
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    row = r - rows[i]
    if i % 2 == 0:
        # 왼 -> 오
        for j in range(c):
            if maps[row][j] == 'x':
                maps[row][j] = '.'
                check(row, j)
                break
    else:
        # 오 -> 왼
        for j in range(c - 1, -1, -1):
            if maps[row][j] == 'x':
                maps[row][j] = '.'
                check(row, j)
                break

for map in maps:
    for m in map:
        print(m, end='')
    print()
