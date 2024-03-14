'''
24 03 13
그리디
그래프
골2
'''

import sys

r,c = map(int,sys.stdin.readline().strip().split(' '))
maps = [list(sys.stdin.readline().strip()) for _ in range(r)]

# 탐색 순서 중요 최대한 위로 붙어서 가야함
dx = [-1,0,1]
dy =[1,1,1]


def dfs(x,y):
    # 한 곳에는 하나의 파이프만 설치 가능
    maps[x][y] = '-'
    if y == c-1:
        return True

    for i in range(3):
        nextX,nextY = x + dx[i] , y + dy[i]
        if 0 <= nextX < r and 0 <= nextY < c and maps[nextX][nextY] == '.':
            if dfs(nextX,nextY):
                return True

    return False

ret = 0
for i in range(r):
    if dfs(i,0):
        ret += 1

print(ret)