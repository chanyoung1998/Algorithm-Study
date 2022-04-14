import sys
from collections import deque
sys.setrecursionlimit(10001)
n,m = map(int,sys.stdin.readline().rstrip().split())
maps = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
cheese_cnt = 0
for _ in maps:
    cheese_cnt += sum(_)




dx = [-1,1,0,0]
dy = [0,0,-1,1]
def backtracking(i,j):
    global cheese_cnt


    if maps[i][j] == 1:
        cheese_cnt -= 1
        maps[i][j] = 0
        visit[i][j] = True
        return

    else:
        if not visit[i][j]:
            visit[i][j] = True
            for dir in range(4):
                p = i + dx[dir]
                q = j + dy[dir]
                if 0 <= p < n and 0 <= q < m:
                    backtracking(p,q)



last_cheese = 0
time = 0
while cheese_cnt != 0:
    visit = [[False for _ in range(m)] for _ in range(n)]
    last_cheese = cheese_cnt
    backtracking(0,0)
    time += 1

print(last_cheese,time,sep='\n')