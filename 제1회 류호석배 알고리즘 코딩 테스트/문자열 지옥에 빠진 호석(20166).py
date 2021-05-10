import sys
from collections import deque

n,m,k = map(int,sys.stdin.readline().rstrip().split())
map = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
dx = [0,0,1,-1,1,-1,1,-1]
dy = [1,-1,0,0,1,-1,-1,1]
#상,하,좌,우,오위,왼아래,오아래,왼위

def sol(start, i, ret):
    global count

    x = start[0]
    y = start[1]

    if map[x][y] == target[i]:
        ret += map[x][y]

        for j in range(8):
            p = x + dx[j]
            q = y + dy[j]

            if p < 0:
                p = n - 1
            elif p >= n:
                p = 0
            if q < 0:
                q = m - 1
            elif q >= m:
                q = 0

            if i + 1 == length and ret == target:
                count += 1
                break
            else:
                sol((p, q), i + 1, ret)

    return




for _ in range(k):
    target = sys.stdin.readline().rstrip()
    length = len(target)
    count = 0
    ret = ''
    for i in range(n):
        for j in range(m):
            start = (i,j)
            sol(start,0,ret)

    print(count)
