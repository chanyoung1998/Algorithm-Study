import sys
from itertools import combinations
from collections import deque
import copy
n = int(sys.stdin.readline())
maps = [list(sys.stdin.readline().rstrip().split()) for _ in range(n)]
teachers = []
blanks = []
for i in range(n):
    for j in range(n):
        if maps[i][j] == 'T':
            teachers.append((i,j))
        elif maps[i][j] == 'X':
            blanks.append((i,j))
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def canwehide(map):

    for t_x,t_y in teachers:
        for i in range(4):
            p = t_x + dx[i]
            q = t_y + dy[i]
            while 0 <= p < n and 0 <= q < n:
                if map[p][q] == 'O':
                    break
                if map[p][q] == 'S':
                    return False
                p += dx[i]
                q += dy[i]
    return True




ret = False
for walls in combinations(blanks,3):

    for (x,y) in walls:
        maps[x][y] = 'O'
    ret = canwehide(maps)
    if ret:
        print('YES')
        break

    for (x,y) in walls:
        maps[x][y] = 'X'

if not ret:
    print('NO')