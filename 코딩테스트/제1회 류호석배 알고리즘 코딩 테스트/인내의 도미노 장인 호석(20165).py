
import sys
from collections import deque
n, m, r = map(int,sys.stdin.readline().rstrip().split())
dominoes = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
collasped = [[False for _ in range(m)] for _ in range(n)]
count = 0
for _ in range(r):
    x,y,direction = sys.stdin.readline().rstrip().split()
    x,y = int(x)-1,int(y)-1
    a,b = map(int,sys.stdin.readline().rstrip().split())
    a,b = a-1,b-1
    queue = deque()
    queue.append((x,y))

    if collasped[x][y]:
        continue
    else:
        collasped[x][y] = True
        count += 1

    if direction == 'N':
        #temp = []
        while queue:
            p,q = queue.popleft()
            sizeofdomino = dominoes[p][q]
            if sizeofdomino == 1:
                continue
            for i in range(1,sizeofdomino):
                if p - i >= 0 and not collasped[p-i][q]:
                    queue.append((p-i,q))
                    collasped[p-i][q] = True
                    count += 1
                    #temp.append(p-i)
        if collasped[a][b]:
            collasped[a][b] = False

    elif direction == 'S':
        #temp = []
        while queue:
            p,q = queue.popleft()
            sizeofdomino = dominoes[p][q]
            if sizeofdomino == 1:
                continue
            for i in range(1,sizeofdomino):
                if p + i < n and not collasped[p+i][q]:
                    queue.append((p+i,q))
                    collasped[p+i][q] = True
                    count += 1
                    #temp.append(p+i)
        if collasped[a][b]:
            collasped[a][b] = False

    elif direction == 'E':
        #temp = []
        while queue:
            p,q = queue.popleft()
            sizeofdomino = dominoes[p][q]
            if sizeofdomino == 1:
                continue
            for i in range(1,sizeofdomino):
                if q + i < m and not collasped[p][q+i]:
                    queue.append((p,q+i))
                    collasped[p][q+i] = True
                    count += 1
                    #temp.append(q + i)
        if collasped[a][b]:
            collasped[a][b] = False

    elif direction == 'W':
        #temp = []
        while queue:
            p, q = queue.popleft()
            sizeofdomino = dominoes[p][q]
            if sizeofdomino == 1:
                continue
            for i in range(1, sizeofdomino):
                if q - i >= 0 and not collasped[p][q - i]:
                    queue.append((p, q - i))
                    collasped[p][q - i] = True
                    count += 1
                    #temp.append(q-i)
        if collasped[a][b]:
            collasped[a][b] = False



print(count)
for coll in collasped:
    for i in coll:
        if i:
            print('F',end=' ')
        else:
            print('S',end =' ')
    print()