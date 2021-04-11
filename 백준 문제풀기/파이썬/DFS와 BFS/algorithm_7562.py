'''
내용:백준 알고리즘 단계별 풀기 dfs와bfs 7562번 나이트의 이동
날짜:21년4월 11일
사용 언어:파이썬
'''

import sys
from collections import deque
dx = [-2,-1,2,1,-2,-1,2,1]
dy = [-1,-2,-1,-2,1,2,1,2]
t = int(sys.stdin.readline().rstrip())
for i in range(t):
    l = int(sys.stdin.readline().rstrip())
    p, q = map(int, sys.stdin.readline().rstrip().split())
    d_p, d_q = map(int, sys.stdin.readline().rstrip().split())
    maps = [[0 for _ in range(l)] for _ in range(l)]

    queue = deque()
    queue.append((p,q))

    while queue:
        x, y = queue.popleft()
        if x == d_p and y == d_q:
            print(maps[x][y])
            break
        for i in range(8):
            r = x + dx[i]
            s = y + dy[i]

            if 0 <= r < l and 0 <= s < l and maps[r][s] == 0:
                queue.append((r,s))
                maps[r][s] = maps[x][y] + 1