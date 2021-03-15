'''
내용:백준 알고리즘 단계별 풀기 dfs와bfs 7576 토마토
날짜:21년3월 14일
사용 언어:파이썬
'''

import sys
from collections import deque


def bfs():
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            q = a + dx[i]
            w = b + dy[i]
            if 0 <= q < n and 0 <= w < m and tomatoes[q][w] == 0:
                tomatoes[q][w] = tomatoes[a][b] + 1
                queue.append([q,w])


m, n = map(int,sys.stdin.readline().split())
tomatoes = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
queue = deque()
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 저장될 때부터 모든 토마토가 있어있는 상태인지 확인하기
for i in range(n):
    for j in range(m):
        if tomatoes[i][j] == 1:
            queue.append([i,j])
bfs()

isTrue = False
result = -2
for tomato in tomatoes:
    for j in tomato:
        if j == 0:
            isTrue = True
        result = max(result, j)
if isTrue == True:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result - 1)