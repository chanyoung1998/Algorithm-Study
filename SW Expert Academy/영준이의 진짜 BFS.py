from collections import deque
from math import ceil,log2


def lca(a,b):

    cnt = 0
    if height[b] > height[a]:
        a, b= b, a
    if height[a] > height[b]:
        for x in range(X,-1,-1):
            if height[ascendent[a][x]] >= height[b]:
                a = ascendent[a][x]

    if a == b:
        return a
    else:
        for x in range(X,-1,-1):
            if ascendent[a][x] != ascendent[b][x]:
                a = ascendent[a][x]
                b = ascendent[b][x]
        return parent[a]









T = int(input())
for t in range(T):

    n = int(input())
    parent = [0,0] + list(map(int,input().rstrip().split()))
    height = [0 for _ in range(n+1)]
    adjlist = [[] for _ in range(n+1)]


    for i in range(1,n+1):
        height[i] = height[parent[i]] + 1
        adjlist[parent[i]].append(i)

    X = ceil(log2(max(height)))
    ascendent = [[0 for _ in range(X+1)] for _ in range(n + 1)]

    for x in range(X+1):
        for j in range(1,n+1):
            if x == 0:
                ascendent[j][x] = parent[j]
            else:
                ascendent[j][x] = ascendent[ascendent[j][x-1]][x-1]


    for i in range(1,n+1):
        adjlist[i].sort()



    visit = [False for _ in range(n+1)]
    dq = deque()
    dq.append(1)
    visit[1] = True
    pos = 1
    cnt = 1
    ret = 0
    while dq:
        if cnt == n:
            break
        cur = dq.popleft()

        if not adjlist[cur]:
            continue
        LCA = lca(pos, cur)
        ret += abs(height[pos]-height[LCA]) + abs(height[cur]-height[LCA])
        pos = cur

        for next in adjlist[cur]:
            if not visit[next]:
                LCA = lca(pos,next)
                ret += abs(height[pos] - height[LCA]) + abs(height[next] - height[LCA])
                visit[next] = True
                pos = next
                cnt += 1
                dq.append(next)

    print('#{} {}'.format(t+1,ret))

