'''
내용:백준 알고리즘 단계별 풀기 dfs와bfs 2667번 단지번호 붙이기
날짜:21년3월 13일
사용 언어:파이썬
'''

import sys

n = int(sys.stdin.readline())
maps = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(n)]


def dfs(x,y):
    global count
    if x <= -1 or x >= n or y <= -1 or y>= n:
        return False

    if maps[x][y] == 1:
        maps[x][y] = 0
        count += 1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True

    return False

ret = []
for i in range(n):
    for j in range(n):
        count = 0
        if dfs(i,j) == True:
            ret.append(count)
            count = 0

ret.sort()
print(len(ret))
for r in ret:
    print(r)






