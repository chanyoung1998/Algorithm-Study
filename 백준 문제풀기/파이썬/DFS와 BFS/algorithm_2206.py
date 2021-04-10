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
visited = [[[False, False] for _ in range(m)] for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs():
    queue = deque()
    queue.append([0,0,0])
    visited[0][0][0] = 1
    while queue:
        x, y, w = queue.popleft()
        # w는 x,y가 벽 만남 여부 나타냄 0이면 안만남 1이면 만남.
        if x == n-1 and y == m -1:
            return visited[x][y][w]

        for i in range(4):
            p = x + dx[i]
            q = y + dy[i]

            if 0 <= p < n and 0 <= q < m :
                if maps[p][q] == 0 and visited[p][q][w] == 0:
                    visited[p][q][w] = visited[x][y][w] + 1
                    queue.append([p,q,w])
                elif maps[p][q] == 1 and w == 0:
                    visited[p][q][1] = visited[x][y][0] + 1
                    queue.append([p,q,1])
    return -1

print(bfs())
