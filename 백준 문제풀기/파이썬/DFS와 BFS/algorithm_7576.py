'''
내용:백준 알고리즘 단계별 풀기 dfs와bfs 7576 토마토
날짜:21년3월 14일
사용 언어:파이썬
'''

import sys
from collections import deque
# 시간 초과 발생
# 애초에 한번 탐색해서 익은 토마토(1)의 인덱스를 초기 큐에 담아 놓고 bfs돌리면 된다.
# 그렇게 하면 50-54번 시행할 필요도 없다.
# bfs도 그냥 간단하짐
def bfs(x, y):
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[x][y] = True
    queue = deque()
    queue.append([x,y])

    while queue:
        a, b = queue.popleft()
        for i in range(4):
            q = a + dx[i]
            w = b + dy[i]
            if 0 <= q < n and 0 <= w < m:
                if tomatoes[q][w] == 0 and not visited[q][w]:
                    tomatoes[q][w] = tomatoes[a][b] + 1
                    visited[q][w] = True
                    queue.append([q, w])
                elif tomatoes[q][w] > 0 and not visited[q][w]:
                    tomatoes[q][w] = min(tomatoes[q][w], tomatoes[a][b] + 1)
                    visited[q][w] = True
                    queue.append([q, w])


m, n = map(int,sys.stdin.readline().split())
tomatoes = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
flag = True
# 저장될 때부터 모든 토마토가 있어있는 상태인지 확인하기
for tomato in tomatoes:
    try:
        tomato.index(0)
    except ValueError:
        pass
    else:
        flag = False
        break

if not flag:
    for i in range(n):
        for j in range(m):
            if tomatoes[i][j] == 1:
                bfs(i,j)

else:
    print(0)








