import sys
from collections import deque

n,m,k = map(int,sys.stdin.readline().rstrip().split())
bf = [(-1,-1)]
deleted = []

for _ in range(m):
    u,v = map(int,sys.stdin.readline().rstrip().split())
    bf.append((u,v))
for _ in range(k):
    r = int(sys.stdin.readline())
    deleted.append(r)

color = []
def sol(number):
    isdeleted = [False for _ in range(m + 1)]
    adjlist = [[] for _ in range(n + 1)]
    global color
    color = [-1 for _ in range(n + 1)]
    for i in range(number):
        isdeleted[deleted[i]] = True

    for i in range(1, len(bf)):
        u, v = bf[i]
        if isdeleted[i]:
            continue
        else:
            adjlist[u].append(v)
            adjlist[v].append(u)


    queue = deque()
    queue.append(1)
    color[1] = 0

    while queue:
        cur = queue.popleft()
        for next in adjlist[cur]:
            if color[next] == -1:
                if color[cur] == 0:
                    color[next] = 1
                elif color[cur] == 1:
                    color[next] = 0
                queue.append(next)
            elif color[next] == color[cur]:
                return False



    return True


low = -1
high = k
check = False
while low + 1 < high:
    mid = (low+high) // 2
    if sol(mid):
        high = mid
        check = True
    else:
        low = mid

if sol(high):

    a = 0
    b = 0
    for i in range(1,n+1):
        if color[i] == 0:
            a += 1
        elif color[i] == 1:
            b += 1
    if a > b:
        a,b = b,a

    print(high)
    print(a,b)
else:
    print(-1)


