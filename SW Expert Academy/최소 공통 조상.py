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


def build_height(root,level):

    height[root] = level
    size[root] = 1

    for next in adjlist[root]:
        size[root] += build_height(next,level+1)

    return size[root]


def build_ascendent():

    for x in range(X+1):
        for i in range(1,V+1):
            if x == 0:
                ascendent[i][x] = parent[i]
            else:
                ascendent[i][x] = ascendent[ascendent[i][x-1]][x-1]

T = int(input())
for t in range(1,T+1):
    # n = int(input())
    V,E,A,B = map(int,input().rstrip().split())
    edges = list(map(int,input().rstrip().split()))
    adjlist = [[] for _ in range(V+1)]
    height = [0 for _ in range(V+1)]
    parent = [0 for _ in range(V+1)]
    size = [0 for _ in range(V+1)]
    for i in range(0,len(edges)-1,2):
        adjlist[edges[i]].append(edges[i+1])
        parent[edges[i+1]] = edges[i]

    build_height(1,1)
    X = ceil(log2(max(height)))
    ascendent = [[0 for _ in range(X+1)] for _ in range(V+1)]
    build_ascendent()
    ret = lca(A,B)
    print('#{} {} {}'.format(t,ret,size[ret]))


