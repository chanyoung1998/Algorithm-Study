'''
내용:백준 알고리즘 단계별 풀기 dfs와bfs 2178 미로 탐색
날짜:21년3월 13일
사용 언어:파이썬
'''
import sys
from collections import deque
n, m = map(int,sys.stdin.readline().split())
maps = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(x,y):
    queue = deque()
    queue.append([x,y])
    count = 0
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            q = a + dx[i]
            w = b + dy[i]
            if 0 <= q < n and 0 <= w < m and maps[q][w] == 1:
                queue.append([q,w])
                maps[q][w] = maps[a][b] + 1
    print(maps[n-1][m-1])

bfs(0,0)
