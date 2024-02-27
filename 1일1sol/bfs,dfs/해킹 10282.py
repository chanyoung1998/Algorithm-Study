'''
24 02 27
해킹
10282
골4
그래프
'''

import sys
from collections import deque

t = int(sys.stdin.readline())
for _ in range(t):
    n, d, c = map(int, sys.stdin.readline().strip().split(' '))
    adjlist = [[] for _ in range(n + 1)]
    for _ in range(d):
        a, b, s = map(int, sys.stdin.readline().strip().split(' '))
        adjlist[b].append((a, s))

    visit = [sys.maxsize for _ in range(n+1)]
    dq = deque()
    dq.append((c,0))
    visit[c] = 0
    while dq:
        cur, curTime = dq.popleft()

        for nextCom,cost in adjlist[cur]:
            if visit[nextCom] > curTime + cost:
                visit[nextCom] = curTime + cost
                dq.append((nextCom,visit[nextCom]))

    ret = 0
    retTime = 0
    for v in visit:
        if v != sys.maxsize:
            ret += 1
            retTime = max(retTime,v)

    print(ret,retTime)

