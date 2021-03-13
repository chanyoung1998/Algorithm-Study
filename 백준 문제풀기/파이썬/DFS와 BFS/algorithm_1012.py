'''
내용:백준 알고리즘 단계별 풀기 dfs와bfs 1012번 유기농 배추
날짜:21년3월 13일
사용 언어:파이썬
'''

import sys
sys.setrecursionlimit(2505)

def dfs(x,y):
    if x <= -1 or x >= m or y <= -1 or y >= n:
        return False

    if maps[x][y] == 1:
        maps[x][y] = 0
        dfs(x,y-1)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x+1,y)
        return True

    return False


t = int(sys.stdin.readline())
for _ in range(t):
    m,n,k = map(int,sys.stdin.readline().split())
    maps = [[0 for _ in range(n)] for _ in range(m)]
    for _ in range(k):
        x, y = map(int,sys.stdin.readline().split())
        maps[x][y] = 1
    count = 0
    for i in range(m):
        for j in range(n):
            if dfs(i,j) == True:
                count += 1
    print(count)



