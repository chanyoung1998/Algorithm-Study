'''
내용:백준 알고리즘 단계별 풀기 dfs와bfs 2206번 벽 부수고 이동하기
날짜:21년4월 10일
사용 언어:파이썬
'''
'''
8 8
01000100
01010100
01010100
01010100
01010100
01010100
01010100
00010100
'''
import sys
from collections import deque
n, m = map(int,sys.stdin.readline().split())
maps = [list(map(int,list(sys.stdin.readline().rstrip()))) for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]
dp = [[False for _ in range(m)] for _ in range(n)]
distance = [[0 for _ in range(m)] for _ in range(n)]

def bfs():
    queue = deque()
    queue.append((0,0))
    distance[0][0] = 1

    while queue:

        x, y = queue.popleft()
        isbroken = dp[x][y]

        if x == n-1 and y == m -1:
            break

        for i in range(4):
            p = x + dx[i]
            q = y + dy[i]

            if (0 <= p < n and 0 <= q < m and distance[p][q] == 0) or (0 <= p < n and 0 <= q < m and distance[p][q] >= distance[x][y] + 1 and isbroken):
                if isbroken:
                    if maps[p][q] == 0:
                        queue.append((p,q))
                        dp[p][q] = True
                        distance[p][q] = distance[x][y] + 1
                else:
                    if maps[p][q] == 0:
                        queue.append((p,q))
                        dp[p][q] = False
                        distance[p][q] = distance[x][y] + 1
                    else:
                        queue.append((p,q))
                        dp[p][q] = True
                        distance[p][q] = distance[x][y] + 1


    if distance[n-1][m-1] == 0:
        print(-1)
    else:
        print(distance[n-1][m-1])

    return

bfs()
